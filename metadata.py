from mutagen.mp3 import MP3


def get_song_duration(song_path):
    audio = MP3(song_path)
    return int(audio.info.length)


def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"