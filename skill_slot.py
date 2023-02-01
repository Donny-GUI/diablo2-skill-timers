from meter import Meter
from skill import Skill
from timer import Timer
from tkinter import Frame
from settings import Debug


class SkillSlot:
    def __init__(self, root, skill_name: str, duration_seconds: int, key_binding) -> None:
        self.name = skill_name
        self.root = root
        self.frame = Frame(root, bg='white')
        self.binding = key_binding
        
        self.skill = Skill(self.frame, skill_name)
        self.meter = Meter(self.frame)
        self.timer = Timer(duration_seconds)

        self.skill.label.pack()
        self.meter.label.pack()
        
    
    def update(self):
        if self.timer.started == True:
            index = self.timer.frame_index
            self.meter.set_frame(index)
            self.meter.label.configure('image', self.meter.frame)
        else:
            if self.timer.ended == True and Debug == False:
                self.meter.label.configure('fg', 'white')
                self.skill.label.configure('fg','white')
    
    def reset(self):
        self.timer.running=False
        self.timer.thread_timer.join()
        self.timer.start()
