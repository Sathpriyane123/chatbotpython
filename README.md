Voice-Assisted Chatbot using Python
======================

Overview
--------
This is a voice-assisted chatbot that integrates Gemini API and Weather API to provide real-time information 
and assistance. The chatbot supports voice commands, text input, and customizable API responses.

Features
--------
1. **Voice Assistance**:
   - Interact with the chatbot via voice commands.
   - Converts speech-to-text and text-to-speech seamlessly.

2. **Gemini API Integration**:
   - Fetches real-time data using the Gemini API for custom queries.
   - Secure API key management.

3. **Weather API Integration**:
   - Retrieves current weather updates for any city using OpenWeatherMap API.

4. **Customizable Responses**:
   - Easily extendable to include additional APIs or functionality.

Technologies Used
-----------------
- **Programming Language**: Python
- **APIs**:
  - Gemini API
  - OpenWeatherMap API
- **Libraries**:
  - `python-dotenv` for environment variable management
  - `requests` for API requests
  - `speech_recognition` for voice input
  - `pyttsx3` for text-to-speech processing
- **Environment**:
  - Virtual environment (`myenv`)

Setup and Installation
----------------------
1. **Clone the Repository**



2. **Create and Activate Virtual Environment**
- On Windows:
  ```
  .\myenv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source myenv/bin/activate
  ```

3. **Install Dependencies**

4. **Configure Environment Variables**
- Create a `.env` file in the project root:
  ```
  GEMINI_API_KEY=your_gemini_api_key
  WEATHER_API_KEY=your_weather_api_key
  ```

5. **Run the Chatbot**

Usage Instructions
------------------
1. Launch the `chatbot.py` script.
2. Speak into the microphone or type your queries.
3. Examples of queries:
- "What's the weather in New York?"
- "Provide data from Gemini API."
- "Convert text-to-speech for me."

File Structure
--------------

Future Enhancements
-------------------
- Add support for more APIs (e.g., stock market, news, etc.).
- Integrate with AI frameworks for improved conversational abilities.
- Enhance voice recognition for better accuracy.

Author
------
- **Name**: [Your Name]
- **Role**: Junior Software Developer
- **Company**: Doctosmart Enterprises
- **Contact**: [Your Email]

