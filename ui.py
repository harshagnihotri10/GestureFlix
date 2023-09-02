# In this ui.py module:
# We create a UI class that takes a VideoPlayer instance as an argument to interact with the video playback.
# The create_layout method defines the layout of the PySimpleGUI window, including buttons for play, pause, and a volume slider. It also displays the currently recognized gesture and the volume level.
# The run method initializes the PySimpleGUI window, handles button events (play, pause, volume), updates the gesture label, and sets the volume when the slider is adjusted.


import PySimpleGUI as sg
import threading

class UI:
    def __init__(self, video_player):
        self.video_player = video_player
        self.layout = self.create_layout()
        self.window = sg.Window('Gesture-Controlled Video Player', self.layout)
        self.gesture_label = self.window['-GESTURE-']
        self.volume_label = self.window['-VOLUME-']

    def create_layout(self):
        layout = [
            [sg.Text('Gesture Detected:', font=('Helvetica', 14))],
            [sg.Text('', key='-GESTURE-', size=(20, 1), font=('Helvetica', 14))],
            [sg.Button('Play', size=(10, 1), font=('Helvetica', 14))],
            [sg.Button('Pause', size=(10, 1), font=('Helvetica', 14))],
            [sg.Text('Volume:', font=('Helvetica', 14))],
            [sg.Slider(range=(0, 100), orientation='h', default_value=50, size=(20, 15), key='-VOLUME-', font=('Helvetica', 14))],
        ]
        return layout

    def run(self):
        while True:
            event, values = self.window.read(timeout=100)
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'Play':
                self.video_player.play()
            elif event == 'Pause':
                self.video_player.pause()

            if event == '-VOLUME-':
                volume = values['-VOLUME-'] / 100
                self.video_player.set_volume(volume)
                self.volume_label.update(f'Volume: {int(volume * 100)}%')

            self.gesture_label.update(f'Gesture Detected: {self.video_player.get_last_gesture()}')

        self.window.close()

