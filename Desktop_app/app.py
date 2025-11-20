import tkinter as tk
import pygame
import os

class SoundsPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))


    def abs_path(self, file):
        return os.path.join(self.base_dir, file)
    
    def play(self, file):
        pygame.mixer.music.load(self.abs_path(file))
        pygame.mixer.music.play()

class AnimalApp:
    def __init__(self):
        self.player = SoundsPlayer()

        self.root = tk.Tk()
        self.root.title("Animal Sounds")
        self.root.geometry('300x250')
        self.root.resizable(False, False)

        self.create_widgets()
    
    def create_widgets(self):
        tk.Button(
            self.root, text='Мышка', font=("Arial", 14),
            command=lambda: self.player.play("mouse.mp3")
        ).pack(pady=10)

        tk.Button(
            self.root, text='Кошка', font=("Arial", 14),
            command=lambda: self.player.play("cat.mp3")
        ).pack(pady=10)
        
        tk.Button(
            self.root, text='Собака', font=("Arial", 14),
            command=lambda: self.player.play("dog.mp3")
        ).pack(pady=10)
    
    def run(self):
        self.root.mainloop()