<div align="center">


<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-0.2-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-1.5-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/MongoDB-7.0-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/LLaMA-3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cohere-Command_R-39C5BB?style=flat-square"/>
  <img src="https://img.shields.io/badge/Mistral-AI-FF6B00?style=flat-square"/>
  <img src="https://img.shields.io/badge/Groq-LPU-F55036?style=flat-square"/>
  <img src="https://img.shields.io/badge/OpenRouter-GPT-412991?style=flat-square"/>
</p>

<br/>

> **JARVIS AI** is a modular, multi-model intelligent assistant platform that unifies six LLM providers, a full RAG pipeline, persistent MongoDB memory, voice interaction, resume intelligence, code assistance, and image generation — all inside a single Streamlit interface.

<br/>

[**Live Demo**](#) · [**Report Bug**](../../issues) · [**Request Feature**](../../issues) · [**Research Paper**](#research)

</div>

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the App](#running-the-app)
- [🧩 Modules](#-modules)
  - [🤖 Main Assistant](#-main-assistant)
  - [📚 Scholar (RAG)](#-scholar-rag--document-intelligence)
  - [🎙️ Voice Engine](#️-voice-engine)
  - [💻 Code Editor & Co-Pilot](#-code-editor--co-pilot)
  - [📝 Resume Builder](#-resume-builder)
  - [🔬 Prompt Engineering Lab](#-prompt-engineering-lab)
  - [🖼️ ImageLab](#️-imagelab)
  - [👤 Account & Settings](#-account--settings)
- [🗄️ Database Design](#️-database-design)
- [🔁 RAG Pipeline](#-rag-pipeline)
- [🔀 Multi-LLM Routing](#-multi-llm-routing)
- [🧪 Tests](#-tests)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📖 Research](#-research)
- [👨‍💻 Author](#-author)

---

## ✨ Features

| Category | Capability |
|---|---|
| 🧠 **Multi-LLM** | Gemini 2.5 Flash · LLaMA 3.3 70B (Groq) · Cohere Command-R · Mistral · OpenRouter GPT |
| 📚 **RAG Pipeline** | PDF ingestion → semantic chunking → HuggingFace embeddings → ChromaDB similarity search |
| 🗃️ **Persistent Memory** | MongoDB-backed session history across all modules |
| 🎙️ **Voice Interaction** | Wake-word detection ("Jarvis") · Edge-TTS synthesis · ElevenLabs premium voice |
| 📝 **Resume Intelligence** | JD-driven resume builder · ATS scoring · Skills gap analysis · PDF export |
| 💻 **Code Assistance** | Code generation · Review · Refactoring · Debugging via Mistral |
| 🔬 **Prompt Engineering** | Live prompt workspace · Iteration history · YAML-based templates |
| 🖼️ **Image Generation** | Text-to-image via Pollinations.ai · One-click PNG download |
| 🌦️ **Real-time Weather** | Live weather via Open-Meteo API (temperature, windspeed, humidity) |
| 🗒️ **Smart Notes** | Scholar module generates downloadable PDF study notes from documents |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER LAYER                           │
│           Streamlit Web UI  (Browser / Desktop)             │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    APPLICATION LAYER                        │
│   app.py navigation · Page routing · Session state mgmt    │
└──────────┬──────────────────────────────────────┬──────────-┘
           │                                      │
┌──────────▼──────────┐              ┌────────────▼────────────┐
│   PROCESSING LAYER  │              │   RETRIEVAL LAYER       │
│  Query pre-proc     │              │  PDF Ingestion          │
│  Intent routing     │              │  Recursive Chunking     │
│  Prompt assembly    │              │  HuggingFace Embeddings │
│  Context building   │              │  ChromaDB Vector Store  │
└──────────┬──────────┘              └────────────┬────────────┘
           │                                      │
┌──────────▼──────────────────────────────────────▼──────────-┐
│                     MULTI-LLM LAYER                         │
│                                                             │
│  ┌──────────┐ ┌─────────┐ ┌────────┐ ┌────────┐ ┌───────┐  │
│  │  Gemini  │ │  LLaMA  │ │ Cohere │ │Mistral │ │  GPT  │  │
│  │2.5 Flash │ │3.3-70B  │ │Cmd-R   │ │8B/Sm   │ │ OR    │  │
│  └──────────┘ └─────────┘ └────────┘ └────────┘ └───────┘  │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│                      MEMORY LAYER                           │
│     Session manager · Context reconstruction · History      │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│                     DATABASE LAYER                          │
│  MongoDB (conversations · prompts · code · images)          │
│  ChromaDB (vector embeddings)                               │
│  MySQL    (weather logs · wake events)                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
jarvis-ai/
│
├── 📂 Assets/
│   └── pdf/                        # Uploaded PDFs for RAG ingestion
│
├── 📂 Backend/
│   ├── 📂 Config/
│   │   ├── models.yaml             # ← All LLM & embedding model names (single source of truth)
│   │   └── settings.py             # ← API keys & DB URIs loaded from .env
│   │
│   ├── 📂 Core/Features/
│   │   ├── 📂 LLmModelCore/
│   │   │   ├── 📂 TTS_ENGINE/
│   │   │   │   └── elevenlabs_client.py   # ElevenLabs premium TTS
│   │   │   ├── greet_Func.py              # Time-aware greeting + weather on launch
│   │   │   ├── llm_Service.py             # Central model name registry
│   │   │   └── voice_Engine.py            # Edge-TTS + wake word + command listener
│   │   │
│   │   ├── 📂 PdfGenerator/
│   │   │   └── generate_pdf.py            # Generates downloadable PDF notes
│   │   │
│   │   ├── 📂 RagPipeLine/
│   │   │   ├── Ingestion_PipeLine.py      # PDF load → clean → chunk → embed → ChromaDB
│   │   │   └── Retrieval_PipeLine.py      # Query embed → similarity search → filter → Cohere
│   │   │
│   │   └── 📂 ResumeBuilder/
│   │       ├── pdf_parser.py              # Extracts text from uploaded resume PDF
│   │       └── resume_builder.py          # JD-driven resume generation logic
│   │
│   ├── 📂 Features/                       # Streamlit page controllers (backend logic)
│   │   ├── Account.py
│   │   ├── app.py                         # ← ENTRY POINT (streamlit run this)
│   │   ├── code_editor.py
│   │   ├── home.py
│   │   ├── Image.py
│   │   ├── Main.py
│   │   ├── prompt_eng.py
│   │   ├── Resume.py
│   │   ├── Scholar.py
│   │   └── 📂 settings/
│   │       └── settings_materials.py
│   │
│   ├── 📂 Services/                       # Individual LLM provider adapters
│   │   ├── cohere_client_1.py             # Cohere RAG answering (command-r)
│   │   ├── cohere_client_2.py             # Cohere notes generation (command-a)
│   │   ├── gemini_client.py               # Google Gemini 2.5 Flash
│   │   ├── llama_client.py                # LLaMA 3.3 70B via Groq (also Jarvis voice runner)
│   │   ├── mistral_client.py              # Mistral code assistance (2 model variants)
│   │   └── 📂 openrouter_client/
│   │       └── resume_analysis/
│   │           └── openai_client.py       # GPT via OpenRouter for resume analysis
│   │
│   ├── 📂 Utils/
│   │   └── mongo_doc_builder.py           # MongoDB document schema factory
│   │
│   └── 📂 models/
│       └── resume_essentials/
│           └── essentials.py              # Resume data models / Pydantic schemas
│
├── 📂 DB/
│   ├── 📂 MySQL/
│   │   ├── wake_db.py                     # Logs voice wake-word events
│   │   └── weather_db.py                  # Persists weather query data
│   │
│   └── 📂 mongo_db/
│       ├── editor_db.py                   # Code editor history
│       ├── image_db.py                    # Image generation prompts
│       ├── main_db.py                     # Core assistant conversation store
│       └── prompt_eng_db.py               # Prompt lab history
│
├── 📂 Frontend/                           # UI layer (Streamlit components & CSS)
│   ├── F_Account.py
│   ├── F_DocMind.py                       # Scholar UI + document uploader
│   ├── F_Editor.py                        # Code editor UI
│   ├── F_Home.py                          # Landing / about page
│   ├── F_Image.py                         # ImageLab UI
│   ├── F_Main.py                          # Main assistant UI
│   ├── F_MergePages.py                    # Shared global CSS injector
│   ├── F_PromptEng.py                     # Prompt engineering UI
│   └── F_Resume.py                        # Resume builder UI
│
├── 📂 Prompt/                             # System prompt templates (plain text)
│   ├── mainPrompt.txt                     # Core assistant personality & rules
│   ├── codePrompt1.txt                    # Mistral code generation prompt
│   ├── codePrompt2.txt                    # Mistral code review prompt
│   ├── coherePrompt.txt                   # Cohere RAG answering prompt
│   ├── coherePrompt2.txt                  # Cohere notes generation prompt
│   ├── gptPrompt.txt                      # OpenRouter GPT prompt
│   └── PromptEng.txt                      # Prompt Engineering Lab system prompt
│
├── 📂 Tests/
│   ├── audio_Test.py
│   ├── docmind_test.py
│   ├── home_page_test.py
│   ├── ingestion_pipeline_test.py
│   └── retrieval_pipeline_test.py
│
├── .gitignore
├── LICENSE                                # MIT — © 2026 Arijit Das
├── README.md
└── requirements.txt
```

---

## ⚙️ Tech Stack

### AI & Language Models

| Provider | Model | Used For |
|---|---|---|
| **Groq** | `llama-3.3-70b-versatile` | Main assistant, voice commands, weather |
| **Google** | `gemini-2.5-flash-lite` | Conversational assistant |
| **Cohere** | `command-r-08-2024` | RAG answer generation |
| **Cohere** | `command-a-03-2025` | Scholar notes generation |
| **Mistral** | `ministral-8b-latest` | Code generation |
| **Mistral** | `mistral-small-latest` | Code review / refactoring |
| **OpenRouter** | `openai/gpt-oss-120b:free` | Resume analysis |
| **HuggingFace** | `all-MiniLM-L6-v2` | Document embeddings (local) |

### Core Infrastructure

| Technology | Version | Role |
|---|---|---|
| Python | 3.11 | Core language |
| Streamlit | 1.32+ | Web UI framework |
| LangChain | 0.2 | LLM orchestration, document loaders, text splitters |
| ChromaDB | 1.5.8 | Local vector database (cosine similarity) |
| MongoDB | 7.0 | Persistent conversation & output storage |
| MySQL | 8.0 | Weather & wake-word event logging |

### Voice & Media

| Library | Purpose |
|---|---|
| `edge-tts 7.2.8` | Free neural TTS — `en-US-GuyNeural` voice |
| `elevenlabs 2.49.0` | Premium TTS — `eleven_multilingual_v2` |
| `speechrecognition` | Google ASR for command capture |
| `pyaudio` | Microphone input stream |
| `pollinations.ai` | Free text-to-image API |

### Document Processing

| Library | Purpose |
|---|---|
| `langchain-community` · `PyPDFLoader` | PDF text extraction |
| `RecursiveCharacterTextSplitter` | Chunk size 800 · overlap 150 |
| `fpdf2` | PDF note generation & export |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.11+**
- MongoDB instance (local or [Atlas](https://www.mongodb.com/atlas))
- MySQL instance (local or cloud)
- API keys for at least one LLM provider (see below)
- A microphone (optional — for voice features)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

**2. Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> ⚠️ The first run will automatically download the `all-MiniLM-L6-v2` model (~90 MB) from HuggingFace. Ensure you have an internet connection.

---

### Environment Variables

Create a **`.env`** file in the root directory:

```env
# ─── LLM PROVIDERS ────────────────────────────────────────────
GROQ_API_KEY=your_groq_api_key_here          # LLaMA 3.3 70B
GEMINI_API_KEY=your_gemini_api_key_here       # Gemini 2.5 Flash
COHERE_API_KEY=your_cohere_api_key_here       # Command-R / Command-A
MISTRAL_API_KEY=your_mistral_api_key_here     # Ministral / Mistral Small
GPT_API_KEY=your_openrouter_api_key_here      # OpenRouter GPT

# ─── VOICE (OPTIONAL) ─────────────────────────────────────────
ELEVENLABS_API_KEY=your_elevenlabs_key_here   # Premium TTS (optional)

# ─── DATABASES ────────────────────────────────────────────────
MONGODB_URL=mongodb://localhost:27017          # or Atlas URI
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_JARVIS_WAKE=jarvis_wake_db
MYSQL_JARVIS_WEATHER=jarvis_weather_db
```

> 💡 **Minimum setup:** You only need `GROQ_API_KEY` + `MONGODB_URL` to get the core assistant running. All other keys unlock additional modules.

**Where to get API keys:**

| Key | Link |
|---|---|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) — Free tier available |
| `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) — Free tier available |
| `COHERE_API_KEY` | [dashboard.cohere.com](https://dashboard.cohere.com) — Free trial |
| `MISTRAL_API_KEY` | [console.mistral.ai](https://console.mistral.ai) — Free trial |
| `GPT_API_KEY` | [openrouter.ai](https://openrouter.ai) — Free models available |
| `ELEVENLABS_API_KEY` | [elevenlabs.io](https://elevenlabs.io) — Free tier (10k chars/mo) |

---

### Running the App

```bash
cd Backend/Features
streamlit run app.py
```

The app will open at **`http://localhost:8501`** 🎉

> **Note:** Run from `Backend/Features/` directory so that relative prompt file paths resolve correctly.

---

## 🧩 Modules

### 🤖 Main Assistant

> **Page:** `Assistant` | **Models:** LLaMA 3.3 70B (Groq) · Gemini 2.5 Flash

The core conversational interface. Supports multi-turn dialogue with a wake-word activated voice mode. On launch, JARVIS greets you with a time-aware message (Good Morning / Afternoon / Evening) and current weather conditions.

**Voice Commands:**
- Say **"Jarvis"** → activates command listening mode
- Ask anything → LLaMA 3.3 responds via voice + text
- Say **"weather"** → fetches live weather from Open-Meteo API
- Say **"exit"** → JARVIS returns to passive wake-word listening

```python
# Voice flow (simplified)
j.listen_wake_word()   # Passive loop: waits for "jarvis"
command = j.take_command()  # Active: captures full user command
reply = j.ask_llama(command)
j.speak(reply)         # Edge-TTS audio playback via Streamlit
```

---

### 📚 Scholar (RAG & Document Intelligence)

> **Page:** `Scholar` | **Models:** Cohere Command-R (RAG) · Cohere Command-A (notes)

Upload any PDF document and ask questions grounded in its content. The Scholar module also generates structured, downloadable study notes.

**Workflow:**

```
PDF Upload
    ↓
DirectoryLoader (PyPDFLoader) — page-by-page extraction
    ↓
Text cleaning: Unicode normalisation · hyphen-break fix · whitespace normalisation
    ↓
RecursiveCharacterTextSplitter — chunk_size=800, overlap=150
    ↓
HuggingFace Embeddings (all-MiniLM-L6-v2) — 384-dim vectors
    ↓
ChromaDB Vector Store — cosine similarity space
    ↓
Query → similarity_search_with_score(k=10)
    ↓
Filtering: score ≤ 1.0 · length ≥ 80 chars · deduplication
    ↓
Top-3 chunks → Cohere Command-R → Grounded Answer
```

**Notes Generation:**
Enter text notes or a topic → Cohere Command-A generates structured notes → Download as PDF via `fpdf2`.

---

### 🎙️ Voice Engine

> **Backend:** `Backend/Core/Features/LLmModelCore/voice_Engine.py`

Two-stage voice architecture:

| Stage | Library | Details |
|---|---|---|
| **TTS (Standard)** | `edge-tts` | `en-US-GuyNeural` · rate `+3%` · pitch `+5Hz` · streams MP3 via Streamlit HTML |
| **TTS (Premium)** | `ElevenLabs` | `eleven_multilingual_v2` · Voice ID configurable in `models.yaml` · MP3 44100Hz 128kbps |
| **Wake Word** | `speech_recognition` | Listens for: `["jarvis", "jarves", "jar vis", "javis"]` |
| **Command ASR** | `speech_recognition` (Google) | `en-in` language · 30s timeout · 25s phrase limit |

**Mic lock mechanism:** `is_speaking` flag prevents microphone capture while audio is playing, eliminating echo feedback.

---

### 💻 Code Editor & Co-Pilot

> **Page:** `Code/Debug` | **Models:** Mistral Ministral-8B · Mistral Small

A dual-panel coding workspace:

| Panel | Function | Model |
|---|---|---|
| **Code Editor** | Write, run, and save code with syntax highlighting | — |
| **Code Generator** | Natural language → code generation | `ministral-8b-latest` (prompt: `codePrompt1.txt`) |
| **Code Reviewer** | Paste code → get review, bugs, suggestions | `mistral-small-latest` (prompt: `codePrompt2.txt`) |

All code queries and outputs are persisted to MongoDB `Jarvis_Code_Db` collections (`code_editor`, `co_pilot`).

---

### 📝 Resume Builder

> **Page:** `Resume` | **Models:** OpenRouter GPT-OSS 120B · Cohere

End-to-end resume intelligence:

1. **Upload** existing resume PDF → text extracted via `pdf_parser.py`
2. **Paste** target job description
3. **Analyse** → ATS keyword match score · skills gap identification
4. **Generate** → tailored resume sections addressing the gaps
5. **Export** → download polished PDF resume

---

### 🔬 Prompt Engineering Lab

> **Page:** `PromptLab` | **Model:** Gemini 2.5 Flash

An interactive workspace for designing, testing, and iterating on LLM prompts. Features:

- Real-time prompt testing against Gemini
- Session-persisted prompt history (MongoDB `prompt_eng_db`)
- Side-by-side output comparison across iterations

---

### 🖼️ ImageLab

> **Page:** `ImageLab` | **API:** Pollinations.ai

Text-to-image generation without any API key requirement:

```python
url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
```

- Enter any descriptive prompt
- Image renders directly in the UI
- One-click **Download as PNG**
- All prompts stored in MongoDB `image_db`

---

### 👤 Account & Settings

- **Account page:** User profile management and session overview
- **Settings page:** Configure preferences, toggle features
- **About/Home:** Project overview and navigation guide

---

## 🗄️ Database Design

### MongoDB Collections

```
┌─────────────────────── Jarvis_main_db ───────────────────────┐
│                                                              │
│  User_Query            │  Assistant_Answer                  │
│  ─────────────         │  ──────────────────                │
│  user_id: string       │  user_id: string                   │
│  user_query: string    │  ai_answer: string                 │
│  date: datetime        │  date: datetime                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌─────────────────────── Jarvis_Code_Db ───────────────────────┐
│                                                              │
│  code_editor           │  co_pilot                          │
│  ────────────          │  ─────────                         │
│  user_id: string       │  user_id: string                   │
│  user_code: string     │  user_query: string                │
│  date: datetime        │  date: datetime                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────── image_db ──┐   ┌────────── prompt_eng_db ───────┐
│                        │   │                                │
│  user_id: string       │   │  user_id: string               │
│  user_prompt: string   │   │  user_query / ai_response      │
│  date: datetime        │   │  date: datetime                │
│                        │   │                                │
└────────────────────────┘   └────────────────────────────────┘
```

### MySQL Tables

| Database | Table | Stores |
|---|---|---|
| `MYSQL_JARVIS_WEATHER` | weather | temperature, windspeed, winddirection, weathercode, humidity, pressure, cloud_cover |
| `MYSQL_JARVIS_WAKE` | wake_events | Wake-word detection timestamps and session info |

### ChromaDB

```
DB/ChromaDB/                  ← Persistent local vector store
└── collection: default
    ├── documents             ← Raw chunk text (800 char chunks)
    ├── embeddings            ← 384-dim float32 vectors (all-MiniLM-L6-v2)
    └── metadata
        ├── source            ← Original PDF file path
        ├── file_name         ← PDF filename
        ├── page              ← PDF page number
        ├── chunk_id          ← "{source}_chunk_{n}"
        └── length            ← Character length of chunk
```

---

## 🔁 RAG Pipeline

```
Step 1: INGESTION
─────────────────
PDF file(s) in Assets/pdf/
        │
        ▼
DirectoryLoader (glob="*.pdf", PyPDFLoader)
        │   ← page-by-page Document objects
        ▼
Text Cleaning
  • unicodedata.normalize('NFKC')
  • Re-join hyphenated line breaks
  • Collapse whitespace
        │
        ▼
RecursiveCharacterTextSplitter
  chunk_size=800, overlap=150
  separators: ["\n\n", "\n", ".", " "]
        │   ← LangChain Document chunks
        ▼
HuggingFace Embeddings (all-MiniLM-L6-v2)
        │   ← 384-dim float32 vectors
        ▼
Chroma.from_documents(persist_directory="DB/ChromaDB",
                      hnsw:space="cosine")


Step 2: RETRIEVAL
─────────────────
User Query
        │
        ▼
Embed query (same all-MiniLM-L6-v2 model)
        │
        ▼
ChromaDB.similarity_search_with_score(k=10)
        │
        ▼
Filter pipeline:
  ① score > 1.0           → discard
  ② len(content) < 80     → discard
  ③ duplicate content     → discard
  ④ sort ascending by score
  ⑤ TOP_K = 3             → keep best 3
        │
        ▼
context = "\n\n".join(top_3_chunk_texts)
        │
        ▼
Cohere Command-R (system_prompt + context + user_query)
        │
        ▼
Grounded Answer → Streamlit Chat UI
```

---

## 🔀 Multi-LLM Routing

Each LLM provider is wrapped as an independent adapter class with a consistent `ask*()` interface. The routing is **task-based** and user-selectable:

```
User Request
      │
      ├─ Main Chat          → Jarvis (LLaMA 3.3 via Groq) or Gemini
      ├─ RAG / Scholar      → Cohere Command-R
      ├─ Notes Generation   → Cohere Command-A
      ├─ Code Generation    → Mistral Ministral-8B
      ├─ Code Review        → Mistral Small
      ├─ Resume Analysis    → OpenRouter GPT-OSS 120B
      └─ Prompt Lab         → Gemini 2.5 Flash

Each adapter maintains its own:
  • In-memory chat history (MEMORY list)
  • System prompt (loaded from Prompt/*.txt)
  • Session-scoped state
```

---

## 🧪 Tests

Run individual test scripts from the project root:

```bash
# Test RAG ingestion pipeline
python -m Tests.ingestion_pipeline_test

# Test RAG retrieval pipeline
python -m Tests.retrieval_pipeline_test

# Test audio (TTS output)
python -m Tests.audio_Test

# Test Scholar (DocMind) page
python -m Tests.docmind_test

# Test home page rendering
python -m Tests.home_page_test
```

**Sample retrieval test query:**
```python
rp = RETRIEVAL_PIPELINE_MODEL()
output = rp.final_answer(user_query="what is the code of conduct")
```

---

## 🗺️ Roadmap

- [ ] **Agentic Mode** — LangGraph-based multi-step planning and tool use
- [ ] **Multi-user Support** — Role-based access control and session isolation
- [ ] **Fine-tuning Interface** — LoRA fine-tuning UI for open-weight models
- [ ] **Vision Input** — Image understanding via Gemini Vision
- [ ] **Adaptive RAG** — Reinforcement-learning-based chunk scoring from user feedback
- [ ] **Plugin API** — Standardised interface for third-party module contributions
- [ ] **Mobile App** — React Native frontend consuming the Python backend
- [ ] **Docker Compose** — One-command containerised deployment
- [ ] **Streaming Responses** — Token-by-token streaming in chat UI
- [ ] **Multi-language Voice** — Full voice support in languages beyond English

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get involved:

1. **Fork** the repository
2. **Create** your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Contribution Guidelines

- Follow the existing module pattern — each new feature should have a `Backend/Services/` adapter, a `Backend/Features/` controller, and a `Frontend/` UI component
- Add your new LLM model name to `Backend/Config/models.yaml` only — never hard-code model strings
- Store secrets exclusively through `Backend/Config/settings.py` — never commit API keys
- Add a test in `Tests/` for any new pipeline component
- Update this README with any new module documentation

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License
Copyright (c) 2026 Arijit Das
```

---

## 📖 Research

This project is documented in a full IEEE-style research paper:

> **"JARVIS AI: A Multi-Model Intelligent Assistant with Retrieval-Augmented Generation, Conversational Memory, and Productivity Automation"**
> — Covers system architecture, RAG pipeline design, MongoDB memory schema, multi-LLM routing algorithms, experimental evaluation, and comparative analysis against ChatGPT, Perplexity AI, Open WebUI, and AnythingLLM.

The paper includes evaluation metrics: **Precision@5: 0.91**, **Hallucination reduction: 18.7% → 4.2%**, **User Satisfaction: 4.2/5.0**.

---

## 👨‍💻 Author

<div align="center">

**Arijit Das**

[![GitHub](https://img.shields.io/badge/GitHub-ArijitDas-181717?style=for-the-badge&logo=github)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-profile)

*Built with ❤️ and a lot of ☕*

</div>

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/jarvis-ai&type=Date)](https://star-history.com/#your-username/jarvis-ai&Date)

</div>