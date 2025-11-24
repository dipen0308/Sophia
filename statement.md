# Project Statement — Sophia (Voice Assistant)

Overview
This project implements a small voice-controlled assistant in Python that listens for a wake word ("alexa") and can play music, report the time, fetch short Wikipedia summaries, tell jokes, and respond to a few conversational prompts.

Objectives
- Demonstrate basic speech recognition and text-to-speech integration.
- Provide a simple, extendable assistant for learning and experimentation.
- Keep implementation readable and easy to modify.

Scope
- Input: microphone audio.
- Output: spoken responses via the system audio and console prints.
- Intended for local, single-user desktop use with internet required for some features (YouTube, Wikipedia).

Key Features
- Wake-word detection ("sophia") before command processing.
- Play songs on YouTube using pywhatkit.
- Fetch brief Wikipedia summaries.
- Tell jokes using pyjokes.
- Announce current time and respond to simple conversational queries.

Dependencies & Requirements
- Python 3.6+
- Packages: SpeechRecognition, pyttsx3, pywhatkit, wikipedia, pyjokes
- Platform: Windows (microphone and audio output required)
- Additional: PyAudio (may require platform-specific installation)

Limitations & Risks
- Reliant on internet for some features and Google speech recognition.
- No authentication, logging, or safeguards against malicious commands.
- Accuracy depends on microphone quality and ambient noise.
- Not intended for critical or sensitive tasks.

Maintenance & Future Work
- Improve wake-word handling and add configurable wake word.
- Add command confirmation, error handling, and unit tests.
- Implement offline speech recognition model and command parsing.

License
Use for educational and personal experimentation. No warranty; modify and extend as needed.
