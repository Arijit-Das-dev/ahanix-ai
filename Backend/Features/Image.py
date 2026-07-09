import streamlit as st
import Frontend.F_Image as ui
import requests
from PIL import Image
from io import BytesIO
import uuid
from DB.mongo_db.image_db import insert_into_user

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id

st.set_page_config(

    page_title="ImageLab",
    layout="centered"
    )

ui.inject_css()

if "img_started" not in st.session_state:
    st.session_state.img_started = False

if not st.session_state.img_started:
    start = ui.landing_section()
    if start:
        st.session_state.img_started = True
        st.rerun()
else:
    prompt, generate = ui.prompt_section()
    
    if generate:

        if prompt:

            insert_into_user(user_id=user_id, prompt=prompt)

            with st.spinner("Generating image, Please wait..."):
                try:
                    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1024&height=1024&nologo=true&model=flux"
                    response = requests.get(url, timeout=30)
                    
                    # Validate response
                    if response.status_code != 200:
                        st.error(f"API error: HTTP {response.status_code}")
                    elif "image" not in response.headers.get("Content-Type", ""):
                        st.error(f"Unexpected response type: {response.headers.get('Content-Type')}")
                        st.code(response.text[:300])  # Show what came back (for debugging)
                    else:
                        img = Image.open(BytesIO(response.content))
                        
                        st.image(img, caption=f"Generated: {prompt}", use_container_width=True)
                        
                        buf = BytesIO()
                        img.save(buf, format="PNG")
                        buf.seek(0)  # ← also add this; missing seek can cause empty downloads
                        st.download_button(
                            label="Download Image",
                            data=buf.getvalue(),
                            file_name="generated_image.png",
                            mime="image/png"
                        )
                except requests.exceptions.Timeout:
                    st.error("Request timed out. Pollinations may be slow — try again.")
                except Exception as e:
                    st.error(f"Error generating image: {e}")       