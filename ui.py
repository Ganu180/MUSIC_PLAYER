import os
import tkinter as tk
from tkinter import ttk, messagebox

from player import MusicPlayer


class MusicPlayerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Music Player")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.player = MusicPlayer()
        self.music_folder = "music"
        self.song_paths = {}

        self.create_widgets()
        self.load_songs()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="🎵 PERSONAL MUSIC PLAYER",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        tk.Label(
            self.root,
            text="Playlist",
            font=("Arial", 14, "bold")
        ).pack()

        self.song_list = tk.Listbox(
            self.root,
            width=60,
            height=10,
            font=("Arial", 12)
        )
        self.song_list.pack(pady=10)

        self.now_playing = tk.Label(
            self.root,
            text="Now Playing: None",
            font=("Arial", 12)
        )
        self.now_playing.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="▶ Play",
            width=12,
            command=self.play_song
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="⏹ Stop",
            width=12,
            command=self.stop_song
        ).grid(row=0, column=1, padx=5)

        tk.Label(self.root, text="Volume").pack()

        self.volume = ttk.Scale(
            self.root,
            from_=0,
            to=100,
            orient="horizontal",
            length=250
        )
        self.volume.set(70)
        self.volume.pack()

        self.status = tk.Label(
            self.root,
            text="Status: Ready",
            fg="green"
        )
        self.status.pack(pady=10)

    def load_songs(self):
        if not os.path.exists(self.music_folder):
            os.makedirs(self.music_folder)

        songs = os.listdir(self.music_folder)

        for song in songs:
            if song.lower().endswith(".mp3"):
                path = os.path.join(self.music_folder, song)
                self.song_paths[song] = path
                self.song_list.insert(tk.END, song)

    def play_song(self):
        selected = self.song_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a song."
            )
            return

        song = self.song_list.get(selected[0])

        self.player.play(self.song_paths[song])

        self.now_playing.config(
            text=f"Now Playing: {song}"
        )

        self.status.config(
            text="Status: Playing",
            fg="green"
        )

    def stop_song(self):
        self.player.stop()

        self.status.config(
            text="Status: Stopped",
            fg="red"
        )

    def run(self):
        self.root.mainloop()