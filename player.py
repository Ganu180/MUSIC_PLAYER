import pygame


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()