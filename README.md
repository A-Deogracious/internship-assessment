text
# Sunbird AI Translation & Speech Application

A Generative AI web application that processes text or audio through a complete pipeline of transcription, summarization, translation to Ugandan local languages, and speech synthesis - all powered by Sunbird AI's APIs.

## Project Description

This application demonstrates the integration of multiple AI capabilities using Sunbird AI's API. Users can input text directly or upload audio files, which are then processed through an automated pipeline that transcribes (if audio), summarizes, translates to local Ugandan languages, and generates speech output.

## Features

- **Dual Input Support**: Accept both text input and audio file uploads
- **Speech-to-Text**: Transcribe uploaded audio files to text
- **Text Summarization**: Generate concise summaries of input text
- **Translation**: Translate summaries into 5 Ugandan languages (Luganda, Runyankole, Ateso, Lugbara, Acholi)
- **Text-to-Speech**: Convert translated text into audio
- **User-friendly Interface**: Clean Streamlit interface with real-time progress indicators

## Architecture Overview

### Pipeline Flow
INPUT
├─ Text Input → Skip to Step 2
└─ Audio Upload → Step 1: Speech-to-Text (Sunbird STT API)
↓
Step 2: Summarization (Sunbird Summarise API)
↓
Step 3: Translation (Sunbird Sunflower Simple API)
↓
Step 4: Text-to-Speech (Sunbird TTS API)
↓
OUTPUT (Display all intermediate results + audio player)

text

### API Endpoints Used

| Step | Endpoint | Purpose |
|------|----------|---------|
| 1 | `/tasks/stt` | Speech-to-Text transcription |
| 2 | `/tasks/summarise` | Text summarization |
| 3 | `/tasks/sunflower_simple` | AI-powered translation |
| 4 | `/tasks/tts` | Text-to-Speech synthesis |

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.x
- **AI Provider**: Sunbird AI (all AI capabilities)
- **Key Libraries**: 
  - `streamlit` - Web interface
  - `requests` - API calls
  - `python-dotenv` - Environment variable management
  - `base64` - Audio decoding

## Local Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Sunbird AI API token (get one at [https://api.sunbird.ai/](https://api.sunbird.ai/))

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<A-Deogracious>/internship-assessment.git
   cd internship-assessment
   ```

2. **Create and activate virtual environment**
   
   **Windows:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```bash
   # Windows
   New-Item .env
   
   # Mac/Linux
   touch .env
   ```
   
   Add your Sunbird AI API token to `.env`:
SUNBIRD_API_TOKEN=your_api_token_here

text

See `.env.example` for reference.

5. **Run the application**
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SUNBIRD_API_TOKEN` | Your Sunbird AI API authentication token | Yes |

**Note**: Never commit your `.env` file to version control. It's already in `.gitignore`.

## Usage

### Text Input

1. Select **"Text"** as input type
2. Enter or paste your text in the text area
3. Select target language for translation (Luganda, Runyankole, Ateso, Lugbara, or Acholi)
4. Click **"🚀 Process"**
5. View results:
- Original text
- Summary
- Translated summary
- Audio player with speech output

### Audio Input

1. Select **"Audio"** as input type
2. Upload a WAV or MP3 file (must be under 5 minutes)
3. Select target language
4. Click **"🚀 Process"**
5. View results:
- Transcribed text
- Summary
- Translated summary
- Audio player with speech output

### Example

**Input Text:**
Uganda is a beautiful country located in East Africa. It is known for its diverse wildlife,
including mountain gorillas. The capital city is Kampala.

text

**Summary:**
Uganda is an East African country known for wildlife like mountain gorillas, with Kampala as its capital.

text

**Translation (Luganda):**
Uganda nsi nnungi mu East Africa ekimanyiddwa olw'ebisolo eby'enjawulo ng'enkima z'ensozi,
ekibuga ekikulu kye Kampala.

text

**Output:** Audio player with Luganda speech

## Deployed Application

**Live Demo**: [Your Hugging Face Space URL will go here]

Try the application online without any local setup!

## Project Structure
internship-assessment/
├── app.py # Main Streamlit application
├── exercises/
│ └── basics.py # Part 1: Programming exercises
├── tests/
│ └── test_basics.py # Unit tests for Part 1
├── constants.py # Test constants
├── requirements.txt # Python dependencies
├── .env # Environment variables (not in repo)
├── .env.example # Environment variables template
├── .gitignore # Git ignore rules
└── README.md # This file

text

## Known Limitations

1. **Audio File Size**: Maximum file size is 10MB (approximately 5 minutes of audio) to prevent timeouts
2. **Text-to-Speech Timeout**: The TTS API may timeout for very long texts or during high server load. The application handles this gracefully with error messages.
3. **Supported Languages**: Translation is available only for the 5 supported Ugandan languages
4. **Audio Formats**: Only WAV and MP3 formats are supported for audio input
5. **API Rate Limits**: Subject to Sunbird AI API rate limits based on your account type

## Development

### Running Tests

The project includes unit tests for the programming exercises:

```bash
pytest
```

All tests should pass before submission.

### Code Structure

- **`app.py`**: Main application with Streamlit UI and API integration
- **`exercises/basics.py`**: Implementation of Collatz sequence and distinct numbers algorithms
- **Error Handling**: Comprehensive try-catch blocks with user-friendly error messages and timeout handling

## Troubleshooting

**Issue**: "Translation failed: 422"
- **Solution**: Ensure your API token is valid and properly set in `.env`

**Issue**: "TTS timed out"
- **Solution**: This is a server-side issue. Try with shorter text or try again later.

**Issue**: "Audio file too large"
- **Solution**: Trim your audio to under 5 minutes or compress the file.

**Issue**: Streamlit won't start
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## Credits

- **APIs**: [Sunbird AI](https://sunbird.ai/)
- **Framework**: [Streamlit](https://streamlit.io/)
- **Developer**: Arinda Deogracious
- **Internship Program**: Sunbird AI Internship Assessment 2026

## License

This project is part of the Sunbird AI internship assessment.

---

**Powered by Sunbird AI 🦜**