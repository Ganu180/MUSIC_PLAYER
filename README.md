# 🎵 Personal Music Player — Python Desktop Application

### 🐍 Python • 🖥️ Tkinter • 🎶 Pygame • OOP

A feature-rich desktop **Music Player built with Python**, designed with a modular architecture and an interactive graphical interface.

The application supports music playback, playlists, favourites, search, shuffle, repeat, progress tracking, volume control, and dark theme functionality.

This project demonstrates practical implementation of **Python, Object-Oriented Programming (OOP), GUI development, audio handling, file management, and event-driven programming**.

---

## ✨ Features

### 🎵 Music Playback

- ▶️ Play songs
- ⏸️ Pause & Resume
- ⏹️ Stop playback
- ⏮️ Previous song
- ⏭️ Next song
- 🔊 Volume control
- ⏱️ Song progress tracking

### 📂 Music Management

- 🎶 Load songs from the music library
- 📜 Playlist management
- ❤️ Favourite songs
- 🔎 Search functionality
- 🔀 Shuffle mode
- 🔁 Repeat mode
- 🖱️ Select and play songs from the interface

### 🎨 User Interface

- 🌙 Dark Theme
- 🎵 Currently playing song display
- 📊 Progress bar
- 🎛️ Interactive playback controls
- 🖥️ Desktop GUI

---

# 🛠️ Technologies Used

| Area | Technology |
|---|---|
| Programming | Python |
| GUI | Tkinter |
| Audio Playback | Pygame |
| Data Storage | JSON / File Handling |
| Architecture | Modular Python |
| Development | VS Code |
| Version Control | Git & GitHub |

---

# 🧩 Project Architecture

The application is divided into separate Python modules to keep the code organized and maintainable.

### `main.py`
Application entry point responsible for launching the music player.

### `ui.py`
Handles the graphical user interface and user interactions.

### `player.py`
Manages audio playback and player functionality.

### `metadata.py`
Handles music-related metadata.

### `storage.py`
Handles saved application data and persistent settings.

### `settings.json`
Stores application configuration and settings.

This modular structure separates the **UI, playback logic, metadata handling, and storage logic**.

---

# 📁 Project Structure

```text
MUSIC_PLAYER/
│
├── assets/
├── music/
│
├── main.py
├── metadata.py
├── player.py
├── storage.py
├── ui.py
├── settings.json
├── .gitignore
└── README.md
```

---

# 🔄 Application Workflow

```text
Launch Application
       ↓
Load Settings
       ↓
Load Music Library
       ↓
Display User Interface
       ↓
Search / Select Song
       ↓
Play Music
       ↓
Playback Controls
       ↓
Playlist / Favourite Management
       ↓
Save User Settings
```

---

# ▶️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ganu180/MUSIC_PLAYER.git
```

## 2️⃣ Navigate to the Project

```bash
cd MUSIC_PLAYER
```

## 3️⃣ Install Pygame

```bash
pip install pygame
```

## 4️⃣ Add Music

Add supported audio files to the:

```text
music/
```

folder.

## 5️⃣ Run the Application

```bash
python main.py
```

---

# 💡 What I Learned

Through this project, I gained hands-on experience with:

- Python application development
- Object-Oriented Programming
- Tkinter GUI development
- Audio playback using Pygame
- Event-driven programming
- File and directory handling
- JSON-based settings management
- Modular application architecture
- Application state management
- Git & GitHub version control

---

# 🚀 Future Improvements

Potential future enhancements include:

- 🖼️ Album artwork display
- 🎤 Enhanced song metadata display
- 💾 Database integration
- 🎨 Additional UI customization
- 📦 Create a standalone executable
- 🎧 Extended audio format support

---

# 👨‍💻 Author

## Ganesh Gokhale

**Data Analyst | Aspiring Data Scientist | Python Developer**

💼 **LinkedIn:** [Ganesh Gokhale](https://www.linkedin.com/in/ganesh-gokhale-g18/)

📧 **Email:** [iamganeshgokhale180@gmail.com](mailto:iamganeshgokhale180@gmail.com)

🐙 **GitHub:** [Ganu180](https://github.com/Ganu180)

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐.

**Thanks for visiting! 🎵**
