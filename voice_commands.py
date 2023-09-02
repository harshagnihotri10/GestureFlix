# In this voice_commands.py module:
# We create a VoiceCommandRecognizer class that takes instances of VideoPlayer and UI as arguments to interact with video playback and display feedback on the UI.
# The listen_for_voice_commands method listens for voice commands using the microphone. It adjusts for ambient noise, listens for voice input, recognizes the command using Google's speech recognition, and handles the recognized command.
# The handle_command method interprets recognized voice commands and triggers corresponding actions such as play, pause, volume control, or exiting the UI.
# The start_listening method starts the voice recognition process in a separate thread, allowing it to run in the background while the main application continues to operate.
# In the if __name__ == '__main__': block at the end, we provide an example of how to use the VoiceCommandRecognizer class for testing voice commands separately. In your main main.py script, you would import the VoiceCommandRecognizer class and use it as part of your application.


import speech_recognition as sr
import threading

class VoiceCommandRecognizer:
    def __init__(self, video_player, ui):
        self.video_player = video_player
        self.ui = ui
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.voice_thread = threading.Thread(target=self.listen_for_voice_commands)
        self.voice_thread.daemon = True

    def listen_for_voice_commands(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                with self.microphone as source:
                    audio = self.recognizer.listen(source, timeout=5)

                command = self.recognizer.recognize_google(audio).lower()
                self.handle_command(command)
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except Exception as e:
                print(f"Error: {str(e)}")

    def handle_command(self, command):
        if "play" in command:
            self.video_player.play()
        elif "pause" in command:
            self.video_player.pause()
        elif "volume up" in command:
            self.video_player.increase_volume()
        elif "volume down" in command:
            self.video_player.decrease_volume()
        elif "exit" in command:
            self.ui.window.close()

    def start_listening(self):
        self.voice_thread.start()

if __name__ == '__main__':
    # Example usage for testing voice commands separately
    from video_player import VideoPlayer
    from ui import UI
    video_player = VideoPlayer("your_video.mp4")  # Replace with your video file path
    ui = UI(video_player)
    voice_recognizer = VoiceCommandRecognizer(video_player, ui)
    voice_recognizer.start_listening()
    ui.run()

