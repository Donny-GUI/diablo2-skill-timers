import tkinter as tk
from tkinter import Frame
from skill_slot import SkillSlot
from util import SkillTimer
from timer import Timer
from data import DataFiles, Data

from settings import (
    SCREEN_WIDTH,
    SKILL_HEIGHT,
    BAR_WIDTH
)


class DiabloSkillTimers:
    
    def __init__(self) -> None:
        self.loader = DataFiles()
        self.datafile = Data()
        self.data = {}
        self.names = None
        
        self.root = tk.Tk()
        self.root.title("d2 timer")
        self.root.overrideredirect(True)
        self.root.geometry(f'{BAR_WIDTH}x{SKILL_HEIGHT*len(SkillTimer.names)}+{SCREEN_WIDTH-100}+0')
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.root.attributes("-transparentcolor", "white")
        self.root.attributes('-alpha',0.5)
        
        self.root.slots:   dict[str:dict]  = {}
        self.root.frames:  dict[str:dict]  = {}
        self.root.binders: dict[str:dict]  = {}
        self.root.meters:  dict[str:dict]  = {}
        self.root.skills:  dict[str:dict]  = {}
        self.root.timers:  dict[str:dict]  = {}
    
    def load_data(self, filename: str):
        data = self.loader.get_data(filename)
        self.datafile.set(data)
        self.datafile.set_filename(filename)
        self.datafile.save_file(filename)
        self.datafile.loaded = True
        self.data = self.datafile.get()
        self.names = list(self.data.keys())
        
    def start(self):
        
        for name in self.names:
            slot = self.root.slots[name] = SkillSlot(root = self.root, skill_name=name, duration_seconds=self.data[name]['duration'], key_binding=self.data[name]['bind'])
            self.root.frames[name]       = slot.frame
            self.root.binders[name]      = slot.binding
            self.root.meters[name]       = slot.meter
            self.root.skills[name]       = slot.skill
            self.root.timers[name]       = slot.timer
        self.root.mainloop()




def diablo_skill_timers(names: list[str], durations: list[int], key_bindings: list[str]):
    
    root = tk.Tk()
    root.title("d2 timer")
    root.overrideredirect(True)
    root.geometry(f'{BAR_WIDTH}x{SKILL_HEIGHT*len(SkillTimer.names)}+{SCREEN_WIDTH-100}+0')
    #root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")
    root.attributes("-transparentcolor", "white")
    root.attributes('-alpha',0.5)
    
    root.slots: list[SkillSlot] = [
        SkillSlot(
                root=root, 
                skill_name=x, 
                duration_seconds=durations[index], 
                key_binding=key_bindings[index]
        ) for index, x in enumerate(names)
    ]
    #root.slots: list[SkillSlot] = [SkillSlot(root=root, skill_name=x, duration_seconds=randint(1,15), key_binding=randint(1,15)) for x in SkillTimer.names]
    # get frames
    root.frames: list[Frame]    = [x.frame for x in root.slots]
    # pack frames
    root.packed                 = [x.pack() for x in root.frames]
    
    root.timers: list[Timer]    = [x.timer for x in root.slots]
    
    root.binders: list          = [x.bind(key_bindings[index], x.timer.start) for index, x in enumerate(root.slots)]

    root.mainloop()
    
diablo_skill_timers()

    