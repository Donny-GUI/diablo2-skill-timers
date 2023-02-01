from util import Files
from PIL import Image, ImageTk, ImageSequence
from tkinter import Label


class Meter:
    def __init__(self, frame) -> None:
        
        self.file = Files.bloodmeter
        self.image = Image.open(self.file)
        self.frames = [ImageTk.PhotoImage(self.image.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.image)]
        self.max_frame = len(self.frames)
        self.index = -1
        self.frame = self.frames[self.index]
        self.label = Label(frame, image=self.frame, bg='white')
        
    def set_frame(self, index: int):
        if index < 91:
            self.index+=1
            self.frame = self.frames[index]