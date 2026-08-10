# Voice Assistant

A simple desktop voice assistant written in Python using Tkinter for the GUI. It listens to the microphone (via SpeechRecognition + Google), speaks responses using pyttsx3, performs basic actions (open websites, play a local music file, tell the time, check weather using OpenWeatherMap), and collects simple usage data for local visualizations with matplotlib.

## Features
- Microphone input using Google Speech Recognition (SpeechRecognition library)
- Text-to-speech with pyttsx3
- Weather lookup via OpenWeatherMap
- Open YouTube / Google in the browser
- Play a local music file (Windows: os.startfile)
- Collects query metadata and shows matplotlib visualizations when the assistant session ends

## Stack
- Language: Python (desktop)
- GUI: Tkinter
- Major libraries: pyttsx3, SpeechRecognition, requests, matplotlib

## Quick start
These steps assume you have Python 3.8+ installed.

1. Clone the repository:

```bash
git clone https://github.com/KrishShalgar/Voice_Assisstant.git
cd Voice_Assisstant
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set required environment variables (recommended):
- OPENWEATHER_API_KEY — your OpenWeatherMap API key (the project currently contains a placeholder in main.py; it is safer to set your own key as an environment variable and update the code to read it).
- MUSIC_FILE_PATH — path to a local audio file to use for the "play music" command (or update the hardcoded path in main.py).

On macOS / Linux example:

```bash
export OPENWEATHER_API_KEY=your_key_here
export MUSIC_FILE_PATH=/path/to/song.mp3
```

On Windows (PowerShell):

```powershell
$env:OPENWEATHER_API_KEY = "your_key_here"
$env:MUSIC_FILE_PATH = "C:\path\to\song.mp3"
```

5. Run the app:

```bash
python main.py
```

## Notes & platform compatibility
- The code currently initializes pyttsx3 with the `sapi5` driver and uses `os.startfile()` to play music, which are Windows-specific. To run on macOS/Linux you may need to change the TTS driver or playback method.
- SpeechRecognition commonly requires PyAudio for direct microphone access. Installing PyAudio can require system packages (portaudio) — see PyAudio installation instructions for your platform.
- The repository currently contains an OpenWeatherMap API key placeholder in main.py and a hardcoded music filepath; for security and portability these should be replaced with environment variables or a configuration file.

## Suggested next improvements (optional)
- Move configuration (API keys, music path) to environment variables or a config file.
- Replace blocking, monolithic main loop with a thread-safe event-driven approach so the GUI remains responsive while listening.
- Fix runtime errors in analytics functions (undefined variables like `query_texts`) and change string histograms to bar plots using collections.Counter.
- Add a populated requirements.txt and a CONTRIBUTING / INSTALLATION section (this file covers the basics).

## Troubleshooting
- If the microphone isn't detected: verify system microphone permissions and that PyAudio is installed.
- If speech recognition returns "None" often: check network connection (recognize_google uses the internet) and microphone sensitivity.

## License / Author
- Author: Krish
- LICENSE: none provided in this repository — add one if you want to specify reuse terms.
