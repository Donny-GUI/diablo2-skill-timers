from util import Files
from PIL import Image, ImageTk
from tkinter import Label


class Skill:
    def __init__(self, frame,  skill_name):
        self.name = skill_name
        self.file = Files.map[skill_name]
        self.image = Image.open(self.file)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.tkimage, bg='white')