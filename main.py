# In this main.py:
# We import the GestureRecognize, VideoPlayer, UI, and VoiceCommandRecognizer classes from their respective modules.
# We create instances of these classes, including gesture_recognizer, video_player, ui, and voice_recognizer.
# The main loop, captures frames from the camera, recognizing gestures, and updating the UI based on gestures detected.
# We integrate voice command recognition by creating a separate thread (voice_thread) to handle voice commands using the VoiceCommandRecognizer class.
# The ui.update_gesture_label and ui.update_volume_label methods are used to update the gesture and volume labels on the user interface.
# We release resources for the camera and close the UI window when the main loop exits.

import cv2
import PySimpleGUI as sg
import threading
import subprocess
import speech_recognition as sr
from gesture_recognition import GestureRecognizer
from video_player import VideoPlayer
from ui import UI
from voice_commands import VoiceCommandRecognizer

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create instances of GestureRecognizer and VideoPlayer
gesture_recognizer = GestureRecognizer()
video_player = VideoPlayer("video/video1")  # video file path

# Initialize the SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Create the user interface
ui = UI(video_player)

# Create the voice command recognizer
voice_recognizer = VoiceCommandRecognizer(video_player, ui)
voice_thread = threading.Thread(target=voice_recognizer.start_listening)
voice_thread.daemon = True

# Start the voice command thread
voice_thread.start()

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read a frame from the camera.")
        break

    # Recognize gestures
    gesture_action = gesture_recognizer.recognize_gesture(frame)

    # Perform actions based on detected gestures
    if gesture_action == "play_pause":
        video_player.toggle_play_pause()
    elif gesture_action == "volume_up":
        video_player.increase_volume()
    elif gesture_action == "volume_down":
        video_player.decrease_volume()

    # Update the UI window
    ui.update_gesture_label(gesture_action)
    ui.update_volume_label(video_player.get_volume())

    # Display the processed frame
    cv2.imshow("Gesture Controlled Video Player", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
ui.window.close()
