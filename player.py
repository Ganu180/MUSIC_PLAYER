import pygame


class MusicPlayer:

    def __init__(self):
        pygame.mixer.init()
        self.paused = False

    def play(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def resume(self):
        pygame.mixer.music.unpause()
        self.paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)