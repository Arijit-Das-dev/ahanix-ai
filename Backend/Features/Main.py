import time as t
from Backend.Services.modelLlama import j
from Backend.Core.Features.greetFunc import greet
from Frontend.F_Main import style3_MAIN, animation
from DB.wake_db import insert_wake

style3_MAIN()
animation()

if __name__ == "__main__":
    
    greet()

    while True:
        # Listen only for wake word
        wake_word = j.listen_wake_word()

        if wake_word:
            # Insert wake word in DB (if needed)
            insert_wake(wake_word)

            
            j.speak("Yes sir")

            # Run main Jarvis conversation
            query = j.take_command()

            if query != "none":
                result = j.JarvisRun(query)

                if result == "exit":
            # After finishing, loop continues to listen again
                    break

        t.sleep(0.2)