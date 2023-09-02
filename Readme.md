# GestureFlix
## Gesture-Controlled Video Player for Raspberry Pi

This project demonstrates a gesture-controlled video player for the Raspberry Pi. Users can control video playback, including play, pause, and volume adjustments, using hand gestures and voice commands. It utilizes MediaPipe for gesture recognition, OMXPlayer for video playback, PySimpleGUI for the user interface, and the SpeechRecognition library for voice commands.

### Project Overview

- **gesture_recognition.py:** Implements gesture recognition using MediaPipe.
- **video_player.py:** Manages video playback using OMXPlayer.
- **ui.py:** Implements the graphical user interface (GUI) with PySimpleGUI.
- **voice_commands.py:** Sets up voice recognition for controlling the video player.

### Hardware Requirements

- Raspberry Pi (e.g., Raspberry Pi 4)
- Raspberry Pi Camera Module or USB Webcam
- HDMI Display
- Speaker or headphones (for audio output)

### Software Requirements

- Raspbian OS installed on your Raspberry Pi
- Python (Preferably Python 3)
- MediaPipe Python package
- OpenCV (for image processing)
- PySimpleGUI (for the user interface)
- SpeechRecognition (for voice commands)
- OMXPlayer (for video playback)

### Installation

1. Clone this repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/harshagnihotri10/gestureflix.git
   cd gesture-controlled-video-player
   ```

2. Install the required Python libraries:

   ```bash
   pip install mediapipe opencv-python PySimpleGUI SpeechRecognition omxplayer-wrapper
   ```

### Usage

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

### Customization and Expansion

- You can customize the gesture recognition logic and gestures in `gesture_recognition.py`.
- Extend the project by adding more gestures or voice commands for additional functionalities.
- Implement error handling, gesture calibration, or security measures as needed.


### Acknowledgments

- [MediaPipe](https://mediapipe.dev/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OMXPlayer](https://github.com/popcornmix/omxplayer)

```