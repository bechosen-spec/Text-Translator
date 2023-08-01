import streamlit as st
from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Function to perform translation
def translate_text(text, target_lang):
    """
    Translates the input text to the specified target language.

    Parameters:
        text (str): The text to be translated.
        target_lang (str): The target language code (e.g., 'yo' for Yoruba, 'ha' for Hausa, 'ig' for Igbo).

    Returns:
        str: The translated text in the target language.
    """
    # Detect the source language of the input text
    source_lang = translator.detect(text).lang

    # Perform translation
    translated_text = translator.translate(text, src=source_lang, dest=target_lang).text

    return translated_text

def main():
    st.title("Text Translator")
    st.write("Enter text to translate and select the target language from the dropdown.")

    # Input text from the user
    text = st.text_area("Enter text to translate:", value="")

    # Target language selection
    target_lang = st.selectbox(
        "Select the target language:",
        options=['en', 'yo', 'ha', 'ig'],
        index=0
    )

    if st.button("Translate"):
        if text.strip():
            translated_text = translate_text(text, target_lang)
            st.write("Translated Text:", translated_text)
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()
