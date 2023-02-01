from meter import Meter
from skill import Skill
from timer import Timer
from tkinter import Frame
from settings import Debug


class SkillSlot:
    
    """ 
    Used by the timer class, 
    to reperesent a frame of skill, 
    its meter and the timer associated with it 
    """
    
    def __init__(self, root, skill_name: str, duration_seconds: int, key_binding) -> None:
        self.name = skill_name
        self.root = root
        self.frame = Frame(root, bg='white')
        self.binding = key_binding
        
        # SubClasses
        
        self.skill = Skill(self.frame, skill_name)
        self.meter = Meter(self.frame)
        self.timer = Timer(duration_seconds)

        # Pack  
        
        self.skill.label.pack()
        self.meter.label.pack()
        
    
    def update(self):
        """ Updates the element if it is started """
        
        if self.timer.started == True:
            index = self.timer.frame_index
            self.meter.set_frame(index)
            self.meter.label.configure('image', self.meter.frame)
        else:
            if self.timer.ended == True and Debug == False:
                self.meter.label.configure('fg', 'white')
                self.skill.label.configure('fg','white')
    
    def reset(self):
        """ resets the element if it is reset """
        
        self.timer.running=False
        self.timer.thread_timer.join()
        self.timer.start()
