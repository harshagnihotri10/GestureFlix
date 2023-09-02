#     In this video_player.py module:
# We create a VideoPlayer class that encapsulates video playback control using OMXPlayer.
# The __init__ method takes the video_path as an argument, which should be the path to the video file you want to play.
# The play method launches OMXPlayer with the specified video file and sets the volume. If a video is already playing, it checks if the previous process has ended before starting a new one.
# The pause method sends a pause command to OMXPlayer to pause the video playback.
# The set_volume method allows you to set the volume of OMXPlayer. It ensures the volume is within the valid range (0.0 to 1.0).
# The increase_volume and decrease_volume methods adjust the volume by a fixed increment (e.g., 0.1).
# The get_volume method returns the current volume level.

import subprocess

class VideoPlayer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.player_process = None
        self.volume = 0.5  # Initial volume (0.0 to 1.0)

    def play(self):
        if self.player_process is None or self.player_process.poll() is not None:
            self.player_process = subprocess.Popen(["omxplayer", "-b", self.video_path], stdin=subprocess.PIPE)
            self.set_volume(self.volume)

    def pause(self):
        if self.player_process is not None and self.player_process.poll() is None:
            self.player_process.stdin.write(b' ')

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        if self.player_process is not None and self.player_process.poll() is None:
            self.player_process.stdin.write(f'--vol {int(self.volume * 1000)}\n'.encode())

    def increase_volume(self):
        self.set_volume(self.volume + 0.1)

    def decrease_volume(self):
        self.set_volume(self.volume - 0.1)

    def get_volume(self):
        return self.volume
    


