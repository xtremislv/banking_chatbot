from speech2text import *
import tkinter as tk

from tkinter import filedialog
import pygame
import os
import glob

device=0

root = tk.Tk()
button_rec = tk.Button(root, text='Start', command=start)
button_rec.pack()
button_stop = tk.Button(root, text='Stop', command=stop)
button_stop.pack()

pygame.mixer.init()

class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        self.label = tk.Label(self.frame, text="play the audio file:")
        self.label.grid(row=0, column=0, columnspan=2)

        self.play_button = tk.Button(self.frame, text="Play", command=self.play_latest_audio)
        self.play_button.grid(row=1, column=0, pady=10)

        self.predefined_directory = "Path to the Directory"

    def play_latest_audio(self):
        audio_files = glob.glob(os.path.join(self.predefined_directory, "*.mp3")) + glob.glob(os.path.join(self.predefined_directory, "*.wav"))

        if not audio_files:
            tk.messagebox.showerror("Error", "No audio files found in the predefined directory.")
            return

        latest_audio_file = max(audio_files, key=os.path.getmtime)

        pygame.mixer.music.load(latest_audio_file)
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayerApp(root)
    root.mainloop()
