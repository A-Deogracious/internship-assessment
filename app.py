import streamlit as st
import requests
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()
SUNBIRD_API_TOKEN = os.getenv("SUNBIRD_API_TOKEN")

# API endpoints
STT_URL = "https://api.sunbird.ai/tasks/stt"
SUMMARISE_URL = "https://api.sunbird.ai/tasks/summarise"
SUNFLOWER_URL = "https://api.sunbird.ai/tasks/sunflower_simple"
TTS_URL = "https://api.sunbird.ai/tasks/tts"

# Available languages
LANGUAGES = {
    "Luganda": "Luganda",
    "Runyankole": "Runyankole",
    "Ateso": "Ateso",
    "Lugbara": "Lugbara",
    "Acholi": "Acholi"
}

LANG_CODES = {
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}

st.set_page_config(page_title="Sunbird AI Translation App", page_icon="🦜")

st.title("🦜 Sunbird AI Translation & Speech App")
st.write("Transform text or audio through transcription, summarization, translation, and speech synthesis.")

# Input type selection
input_type = st.radio("Choose input type:", ["Text", "Audio"])

text_input = ""
audio_file = None

if input_type == "Text":
    text_input = st.text_area("Enter your text:", height=150, placeholder="Type or paste your text here...")
else:
    audio_file = st.file_uploader("Upload audio file (WAV, MP3):", type=["wav", "mp3"])
    
    if audio_file:
        file_size_mb = audio_file.size / (1024 * 1024)
        if file_size_mb > 10:
            st.error("⚠️ Audio file is too large. Please upload a file shorter than 5 minutes.")
            audio_file = None

# Language selection
target_language = st.selectbox("Select target language for translation:", list(LANGUAGES.keys()))

# Process button
if st.button("🚀 Process", type="primary"):
    if input_type == "Text" and not text_input.strip():
        st.error("Please enter some text!")
    elif input_type == "Audio" and not audio_file:
        st.error("Please upload an audio file!")
    else:
        with st.spinner("Processing..."):
            try:
                original_text = text_input
                
                # Step 1: Transcribe audio if needed
                if input_type == "Audio":
                    st.info("🎤 Transcribing audio...")
                    
                    files = {
                        'audio': (audio_file.name, audio_file.getvalue(), 'audio/wav')
                    }
                    headers = {
                        'Authorization': f'Bearer {SUNBIRD_API_TOKEN}'
                    }
                    
                    response = requests.post(STT_URL, files=files, headers=headers, timeout=120)
                    
                    if response.status_code == 200:
                        result = response.json()
                        original_text = result.get('text', '')
                        st.success("✅ Transcription complete!")
                        st.subheader("📝 Transcribed Text")
                        st.write(original_text)
                    else:
                        st.error(f"Transcription failed: {response.status_code} - {response.text}")
                        st.stop()
                else:
                    # Show original text for text input
                    st.subheader("📝 Original Text")
                    st.write(original_text)
                
                # Step 2: Summarize
                st.info("📋 Summarizing text...")
                
                summary = original_text  # Default to original text
                
                # Try summarization, but don't fail if it doesn't work
                try:
                    headers = {
                        'Authorization': f'Bearer {SUNBIRD_API_TOKEN}',
                        'Content-Type': 'application/json'
                    }
                    
                    summary_payload = {
                        "text": original_text
                    }
                    
                    response = requests.post(SUMMARISE_URL, json=summary_payload, headers=headers, timeout=60)
                    
                    if response.status_code == 200:
                        result = response.json()
                        summary = result.get('summarized_text', result.get('summary', original_text))
                        st.success("✅ Summary complete!")
                    else:
                        st.info("Using original text (summarization unavailable)")
                except:
                    st.info("Using original text")
                
                st.subheader("📋 Summary")
                st.write(summary)
                
                # Step 3: Translate using Sunflower
                st.info(f"🌍 Translating to {target_language}...")
                
                translate_prompt = f"Translate this English text to {target_language}: {summary}"
                
                translate_data = {
                    "instruction": translate_prompt
                }
                
                try:
                    response = requests.post(
                        SUNFLOWER_URL,
                        data=translate_data,  # Use data= for form-encoded
                        headers={'Authorization': f'Bearer {SUNBIRD_API_TOKEN}'},
                        timeout=120
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        translated_text = result.get('response', result.get('output', summary))
                        st.success(f"✅ Translation to {target_language} complete!")
                        st.subheader(f"🌍 Translated Summary ({target_language})")
                        st.write(translated_text)
                    else:
                        st.error(f"Translation failed: {response.status_code} - {response.text}")
                        st.stop()
                except Exception as e:
                    st.error(f"Translation error: {str(e)}")
                    st.stop()
                
                # Step 4: Text-to-Speech
                st.info("🔊 Generating speech...")
                
                lang_code = LANG_CODES[target_language]
                
                tts_payload = {
                    "text": translated_text,
                    "language": lang_code
                }
                
                try:
                    headers_json = {
                        'Authorization': f'Bearer {SUNBIRD_API_TOKEN}',
                        'Content-Type': 'application/json'
                    }
                    
                    response = requests.post(TTS_URL, json=tts_payload, headers=headers_json, timeout=120)
                    
                    if response.status_code == 200:
                        result = response.json()
                        audio_base64 = result.get('audio', '')
                        
                        if audio_base64:
                            audio_bytes = base64.b64decode(audio_base64)
                            
                            st.success("✅ Speech synthesis complete!")
                            st.subheader("🔊 Generated Audio")
                            st.audio(audio_bytes, format='audio/wav')
                        else:
                            st.warning("No audio generated.")
                    else:
                        st.error(f"TTS failed: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"TTS error: {str(e)}")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.divider()
st.caption("Powered by Sunbird AI 🦜")