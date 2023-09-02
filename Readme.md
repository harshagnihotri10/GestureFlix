<h1 align="center">GestureFlix</h1>
<p align="center">Turn your Raspberry Pi into a Gesture-Controlled Video Player with Voice Commands</p>

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization and Expansion](#customization-and-expansion)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)


## Introduction
The Gesture-Controlled Video Player is a fun and interactive project that turns your Raspberry Pi into a video player controlled by hand gestures and voice commands. It uses the power of MediaPipe for gesture recognition, OMXPlayer for video playback, PySimpleGUI for the user interface, and SpeechRecognition for voice control.

## Features
- Gesture recognition for play, pause, volume control
- Voice commands for video playback
- Intuitive user interface with play, pause, volume buttons
- Customizable gestures and voice commands
- Responsive and efficient design for Raspberry Pi

## Hardware Requirements

- Raspberry Pi (e.g., Raspberry Pi 4)
- Raspberry Pi Camera Module or USB Webcam
- HDMI Display
- Speaker or headphones (for audio output)

## Software Requirements

- Raspbian OS installed on your Raspberry Pi
- Python (Preferably Python 3)
- MediaPipe Python package
- OpenCV (for image processing)
- PySimpleGUI (for the user interface)
- SpeechRecognition (for voice commands)
- OMXPlayer (for video playback)


## Installation

1. Clone this repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/harshagnihotri10/gestureflix.git
   cd gesture-controlled-video-player
   ```

2. Install the required Python libraries:

   ```bash
   pip install mediapipe opencv-python PySimpleGUI SpeechRecognition omxplayer-wrapper
   ```
## Usage

1. Ensure you have connected the camera module or a USB webcam to your Raspberry Pi.

2. Navigate to the project directory and run the main script:

   ```bash
   python main.py
   ```

3. Use hand gestures in front of the camera to control video playback. For example:
   - Show a "play" gesture to start playing the video.
   - Show a "pause" gesture to pause the video.
   - Adjust the volume by showing the corresponding gestures.

4. Issue voice commands to control the video player. For example:
   - Say "Play" to start playing the video.
   - Say "Pause" to pause the video.
   - Say "Volume up" or "Volume down" to adjust the volume.

5. The user interface will display the recognized gesture and volume level.


## Project Structure
- `main.py`: Entry point of the project.
- `gesture_recognition.py:` Implements gesture recognition using MediaPipe.
- `video_player.py:` Manages video playback using OMXPlayer.
- `ui.py:` Implements the graphical user interface (GUI) with PySimpleGUI.
- `voice_commands.py:` Sets up voice recognition for controlling the video player.
- `video.mp4`: Sample video file (replace with your own).

## Customization and Expansion

- You can customize the gesture recognition logic and gestures in `gesture_recognition.py`.
- Extend the project by adding more gestures or voice commands for additional functionalities.
- Implement error handling, gesture calibration, or security measures as needed.

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OMXPlayer](https://github.com/popcornmix/omxplayer)

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

