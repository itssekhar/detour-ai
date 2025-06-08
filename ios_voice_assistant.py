import speech_recognition as sr
import webbrowser
import json
import os
from datetime import datetime

class VoiceAssistant:
    def __init__(self):
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Common location keywords and their variations
        self.location_keywords = {
            'restaurant': ['restaurant', 'restaurants', 'dining', 'food', 'eat', 'cafe', 'café'],
            'shopping': ['shopping', 'mall', 'store', 'shop', 'market', 'supermarket'],
            'park': ['park', 'parks', 'garden', 'playground'],
            'hospital': ['hospital', 'clinic', 'medical', 'doctor'],
            'school': ['school', 'university', 'college', 'education'],
            'station': ['station', 'bus stop', 'train', 'subway', 'metro'],
            'airport': ['airport', 'airfield', 'aerodrome'],
            'hotel': ['hotel', 'motel', 'inn', 'lodging'],
            'gym': ['gym', 'fitness', 'workout', 'exercise'],
            'library': ['library', 'libraries', 'bookstore'],
            'museum': ['museum', 'gallery', 'exhibition'],
            'theater': ['theater', 'theatre', 'cinema', 'movie']
        }
        
    def record_audio(self):
        """Record audio from microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            return audio
    
    def speech_to_text(self, audio):
        """Convert speech to text using Google's speech recognition"""
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return None
    
    def extract_location(self, text):
        """Extract location information from text using keyword matching"""
        text_lower = text.lower()
        
        # Check for "nearest" or similar words
        location_indicators = ['nearest', 'closest', 'nearby', 'near me', 'around me']
        has_location_indicator = any(indicator in text_lower for indicator in location_indicators)
        
        # Find matching location type
        for location_type, keywords in self.location_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                if has_location_indicator:
                    return f"nearest {location_type}"
                return location_type
        
        return None
    
    def open_google_maps(self, location):
        """Open Google Maps with the specified location"""
        try:
            # Format the location for Google Maps URL
            formatted_location = location.replace(" ", "+")
            maps_url = f"https://www.google.com/maps/search/?api=1&query={formatted_location}"
            webbrowser.open(maps_url)
            print(f"Opening Google Maps for: {location}")
        except Exception as e:
            print(f"Error opening Google Maps: {e}")
    
    def run(self):
        """Main loop for the voice assistant"""
        print("Voice Assistant Started. Press Ctrl+C to exit.")
        print("You can ask for locations like 'nearest restaurant', 'closest shopping mall', etc.")
        try:
            while True:
                # Record audio
                audio = self.record_audio()
                
                # Convert speech to text
                text = self.speech_to_text(audio)
                if not text:
                    continue
                
                # Extract location
                location = self.extract_location(text)
                if not location:
                    print("Could not identify a location in your request. Try asking for a specific type of place.")
                    continue
                
                # Open Google Maps
                self.open_google_maps(location)
                
        except KeyboardInterrupt:
            print("\nVoice Assistant Stopped.")

if __name__ == "__main__":
    # Create and run the voice assistant
    assistant = VoiceAssistant()
    assistant.run() 