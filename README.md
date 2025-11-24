# Sophia - Voice Assistant

sophia is a simple Python-based voice assistant that can play songs, tell the time, fetch Wikipedia summaries, tell jokes, and more using voice commands. It uses speech recognition and text-to-speech to interact with the user.

## Features

- Play songs on YouTube
- Tell the current time
- Answer "who is" questions using Wikipedia
- Tell jokes
- Respond to fun questions (e.g., "Are you single?")
- Simple conversational responses

## Requirements

- Python 3.6+
- Microphone and speakers

## Dependencies

Install the required Python packages using pip:

```sh
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
```

You may also need to install additional dependencies for `pyaudio` (used by `SpeechRecognition`):

- On Windows:  
  Download and install the appropriate `.whl` from [PyAudio downloads](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio), then run:
  ```sh
  pip install path_to_downloaded_whl
  ```
- On Linux:
  ```sh
  sudo apt-get install portaudio19-dev python3-pyaudio
  ```

## Usage

1. Make sure your microphone is connected.
2. Run the script:

   ```sh
   python Sophia.py
   ```

3. Say "sophia" followed by your command.  
   Example commands:
   - "sophia play Shape of You"
   - "sophia what is the time"
   - "sophia who is Albert Einstein"
   - "sophia tell me a joke"

## Notes

- The assistant listens for the keyword "sophia" before processing commands.
- Internet connection is required for some features (e.g., playing songs, Wikipedia search).
- You can change the wake word or voice in the script as needed.

## License

This project is for educational purposes.
