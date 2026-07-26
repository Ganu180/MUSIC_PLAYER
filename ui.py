import os
import tkinter as tk
from tkinter import ttk, messagebox

from player import MusicPlayer

from metadata import get_song_duration, format_time

from storage import load_data, save_data

from tkinter import filedialog

class MusicPlayerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Music Player")
        self.root.geometry("800x700")
        self.root.resizable(True, True)

        self.current_index = -1

        self.player = MusicPlayer()
        self.music_folder = "music"
        self.song_paths = {}

        self.data = load_data()

        self.shuffle = False
        self.repeat = False

        self.create_widgets()
        self.load_songs()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="🎵 PERSONAL MUSIC PLAYER",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Search").pack(side=tk.LEFT)

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(
            label="Open Music Folder",
            command=self.open_folder
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.root.quit
        )

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        self.root.config(menu=menu_bar)

        tk.Button(
            search_frame,
            text="Search",
            command=self.search_song
        ).pack(side=tk.LEFT)

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

        self.song_list.bind("<Double-Button-1>", lambda event: self.play_song())

        self.now_playing = tk.Label(
            self.root,
            text="Now Playing: None",
            font=("Arial", 12)
        )
        self.now_playing.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        self.progress = ttk.Progressbar(
            self.root,
            length=500,
            mode="determinate"
        )

        self.progress.pack(pady=10)

        self.time_label = tk.Label(
            self.root,
            text="00:00 / 00:00",
            font=("Arial", 11)
        )

        self.time_label.pack()

        tk.Button(
            button_frame,
            text="▶ Play",
            width=12,
            command=self.play_song
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="⏸ Pause",
            width=12,
            command=self.pause_song
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="▶ Resume",
            width=12,
            command=self.resume_song
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="⏹ Stop",
            width=12,
            command=self.stop_song
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="⏮ Previous",
            width=12,
            command=self.previous_song
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="⏭ Next",
            width=12,
            command=self.next_song
        ).grid(row=0,column=5,padx=5)

        tk.Button(
            button_frame,
            text="❤ Favorite",
            width=12,
            command=self.add_favorite
        ).grid(row=0,column=6,padx=5)

        tk.Button(
            button_frame,
            text="🔀 Shuffle",
            width=12,
            command=self.toggle_shuffle
        ).grid(row=0,column=7,padx=5)

        tk.Button(
            button_frame,
            text="🔁 Repeat",
            width=12,
            command=self.toggle_repeat
        ).grid(row=0,column=8,padx=5)

        tk.Label(self.root, text="Volume").pack()

        self.volume = ttk.Scale(
            self.root,
            from_=0,
            to=100,
            orient="horizontal",
            length=250,
            command=self.change_volume
        )

        self.volume.set(70)
        self.volume.pack()

        self.status = tk.Label(
            self.root,
            text="Status: Ready",
            fg="green"
        )
        self.status.pack(pady=10)

        self.root.configure(bg="#2B2B2B")

        self.status.configure(
            bg="#2B2B2B",
            fg="white"
        )

        self.now_playing.configure(
            bg="#2B2B2B",
            fg="white"
        )

    def load_songs(self):

        if not os.path.exists(self.music_folder):
            os.makedirs(self.music_folder)

        songs = os.listdir(self.music_folder)

        songs.sort()

        for song in songs:
            if song.endswith(".mp3"):
                path = os.path.join(self.music_folder, song)

                self.song_paths[song] = path

                self.song_list.insert(tk.END, song)
                
    def play_song(self):
        selected = self.song_list.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Select a song first.")
            return

        self.current_index = selected[0]
        song = self.song_list.get(self.current_index)

        # Update recent songs
        if song in self.data["recent"]:
            self.data["recent"].remove(song)

        self.data["recent"].insert(0, song)
        self.data["recent"] = self.data["recent"][:10]
        save_data(self.data)

        # Play song
        self.player.play(self.song_paths[song])

        self.song_duration = get_song_duration(self.song_paths[song])

        self.progress["maximum"] = self.song_duration
        self.progress["value"] = 0

        self.update_progress()

        self.now_playing.config(text=f"🎵 {song}")
        self.status.config(text="Status: Playing", fg="green")

    def stop_song(self):
        self.player.stop()

        self.status.config(
            text="Status: Stopped",
            fg="red"
        )

    def pause_song(self):

        self.player.pause()

        self.status.config(
            text="Status: Paused",
            fg="orange"
        )


    def resume_song(self):

        self.player.resume()

        self.status.config(
            text="Status: Playing",
            fg="green"
        )


    def next_song(self):

        if self.song_list.size() == 0:
            return

        self.current_index += 1

        if self.current_index >= self.song_list.size():
            self.current_index = 0

        self.song_list.selection_clear(0, tk.END)
        self.song_list.selection_set(self.current_index)

        self.play_song()


    def previous_song(self):

        if self.song_list.size() == 0:
            return

        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = self.song_list.size() - 1

        self.song_list.selection_clear(0, tk.END)
        self.song_list.selection_set(self.current_index)

        self.play_song()

    def change_volume(self, value):

        self.player.set_volume(float(value))

    def update_progress(self):

        if self.player.paused:
            self.root.after(1000, self.update_progress)
            return

        current = self.progress["value"]

        if current < self.song_duration:

            current += 1

            self.progress["value"] = current

            self.time_label.config(
                text=f"{format_time(int(current))} / {format_time(self.song_duration)}"
            )

            self.root.after(1000, self.update_progress)

        else:
            if self.repeat:
                self.play_song()
            else:
                self.next_song()

    def search_song(self):

        keyword = self.search_entry.get().lower()

        self.song_list.selection_clear(0, tk.END)

        for index in range(self.song_list.size()):

            song = self.song_list.get(index).lower()

            if keyword in song:

                self.song_list.selection_set(index)

                self.song_list.see(index)

                break

    def open_folder(self):

        folder = filedialog.askdirectory()

        if not folder:
            return

        self.music_folder = folder

        self.song_list.delete(0, tk.END)

        self.song_paths.clear()

        self.load_songs()

    def add_favorite(self):

        selected = self.song_list.curselection()

        if not selected:
            return

        song = self.song_list.get(selected[0])

        if song not in self.data["favorites"]:
            self.data["favorites"].append(song)
            save_data(self.data)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle

        if self.shuffle:
            self.status.config(text="Shuffle ON")
        else:
            self.status.config(text="Shuffle OFF")

    def toggle_repeat(self):
        self.repeat = not self.repeat

        if self.repeat:
            self.status.config(text="Repeat ON")
        else:
            self.status.config(text="Repeat OFF")

    def run(self):
        self.root.mainloop()