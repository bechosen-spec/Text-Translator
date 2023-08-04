import sys
import streamlit as st
from googletrans import Translator
from gtts import gTTS
from gtts.lang import tts_langs
from IPython.display import display, Audio

# Initialize the Translator object
translator = Translator()

# Function to perform translation
def detect_text(text): #TODO: Detected language should be USER SYSTEM LANGUAGE (OR COULD BE LEFT)
    source_lang = translator.detect(text).lang
    return source_lang

# Function to read text out loud
def text_to_speech(text, target_lang, output_file):
    tts = gTTS(text=text, lang=target_lang, slow=False)
    tts.save(output_file)
    audio = Audio(output_file)
    display(audio)

def main():
    st.title("Text Translator and Text-to-Speech")

    # Input text from the user
    text = st.text_area("Enter text to translate and read aloud:", value="")

    with st.form(key='translate_form'):
        if st.form_submit_button(label="Translate and Read Aloud"):
            if text.strip():
                detected_lang = detect_text(text)  # Use langdetect.detect for language detection

                # Check if the detected language is supported by gTTS
                supported_languages = tts_langs()  # Add other supported language codes as needed
                if detected_lang not in supported_languages:
                    st.error(f"The detected language ({detected_lang}) is not supported for text-to-speech.")
                else:
                    st.write("Detected Language:", detected_lang)

                    # Read the translated text aloud
                    output_filename = "text_audio.mp3"
                    text_to_speech(text, detected_lang, output_filename)
                    st.audio(output_filename) #TODO: SHOULD BE ACTIVATED wHEN READ BUTTON IS PRESSED
            else:
                st.warning("Please enter some text to translate and read aloud.")

if __name__ == "__main__":
    main()