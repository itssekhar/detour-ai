# iOS Voice Assistant

A Python-based voice assistant that can:
1. Record voice input
2. Convert speech to text
3. Process with OpenAI to extract location information
4. Open Google Maps with the extracted location

## Setup Instructions

1. Install Pythonista on your iOS device from the App Store

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Run the script:
   ```bash
   python ios_voice_assistant.py
   ```

2. Speak when prompted. For example:
   - "Take me to Central Park"
   - "How do I get to Times Square?"
   - "Directions to the nearest coffee shop"

3. The assistant will:
   - Convert your speech to text
   - Extract the location using OpenAI
   - Open Google Maps with the location

## Requirements

- iOS device with Pythonista installed
- Internet connection
- OpenAI API key
- Microphone access

## Note

This app requires microphone permissions and internet access to function properly. 