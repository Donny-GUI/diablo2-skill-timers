import tkinter as tk
from tkinter.ttk import Combobox, Label, Entry, Frame, Button
from util import SkillTimer
import dataclasses
from data import DataFiles, Data
from util import get_random_name
from settings import BINDS




class Values:
    names: list       = SkillTimer.names
    durations: list   = list(range(0,500))
    binds: list       = BINDS

class FrameData:
    def __init__(self, slot) -> None:
        self.slot       = slot
        self.name       = None
        self.duration   = None
        self.binder     = None
    
    def update(self, name, duration, binder):
        self.name = name
        self.duration = duration 
        self.binder = binder
    
    def get(self):
        data = {}
        data['name'] = self.name
        data['duration'] = self.duration
        data['bind'] = self.binder
        return data


 


class DiabloMainMenu:
    def __init__(self) -> None:
        self.num_columns = 5
        self.num_rows = 5
        self.root = tk.Tk(screenName='Diablo Skill Timer')
        self.side_bar               = Frame(self.root,
                                            borderwidth=5,
                                            border=3,  
                                            relief='ridge',
                                            height=1)
        self.profile_name_label     = Label(self.root,
                                            text='Diablo Skill Timer', 
                                            font='AvQest 30',
                                            relief='ridge',
                                            border=5,
                                            borderwidth=5, 
                                            background='black', 
                                            foreground='yellow')
        self.profile_label          = Label(self.side_bar,
                                            text='Profile Name:', 
                                            font='AvQest 20',
                                            relief='ridge',
                                            border=5,
                                            borderwidth=5, 
                                            background='black', 
                                            foreground='yellow')
        self.profile_name           = Entry(self.side_bar, 
                                            font='AvQest', 
                                            background='black',
                                            foreground='red', width=25)
        
        self.profile_name.insert(0, get_random_name())
        self.side_bar.grid(column=3,row=1)
        self.profile_name_label.grid(column=3, row=0)
        self.profile_name.grid(column=1, row=1)
        self.profile_label.grid(column=0, row=1)
        
        self.main_menu = MainMenu(self.root)
        self.bottom = BottomFrame(self.side_bar, self)
        
        self.__data = {}
        
        self.datafiles = DataFiles()
        self.data = Data()
        
        self.root.mainloop()
    
    def save(self):
        pass
        
    
    def collect(self):
        self.__data =  self.main_menu.collect()
        self.data.set(self.__data)
        


class SkillOptionFrame(DiabloMainMenu):
    
    def __init__(self, root, slot_number) -> None:
        
        # Layout
        self.super_frame = Frame(root, relief='ridge', border=5, padding=5)
        
        self.frame                      = Frame(self.super_frame)
        self.data                       = FrameData(slot_number)
        self.label                      = Label(text = 
                                                f'Skill', 
                                                width=20, 
                                                master=self.frame, 
                                                font='AvQest 15'
                                                )
        self.duration_label             = Label(self.frame,
                                                width=20,
                                                text='Skill Duration: ', 
                                                font='AvQest 15')
        self.name_combo                 = Combobox(self.frame,
                                                  width=20,
                                                  values=list(SkillTimer.names), 
                                                  font='AvQest 15')
        self.durations_entry            = Entry(self.frame,
                                                width=20, 
                                                font='AvQest 15')
        self.binder_combo               = Combobox(self.frame,
                                                   width=20, 
                                                   values=Values.binds, 
                                                   font='AvQest 15')
        # Grid And Pack
        self.label.grid(column=0, row=0)
        self.name_combo.grid(column=1, row=0)
        self.duration_label.grid(column=0, row=1)
        self.durations_entry.grid(column=1, row=1)
        self.binder_combo.grid(column=1, row=2)
        self.frame.pack()
        self.super_frame.pack()
        self.update()
        self.used = False
        
    def get_name(self):
        self.data.name = self.name_combo.get()
        return self.data.name
    
    def update(self):
        self.data.update(
            self.name_combo.get(), 
            self.durations_entry.get(), 
            self.binder_combo.get()
            )
        if self.data.name != None or self.data.binder or None and self.data.duration or None:
            self.used = True
        else:
            self.used = False
        
    def get_data(self):
        self.update()
        return self.data.get()
        
        

class MainMenu(DiabloMainMenu):
    
    def __init__(self, root) -> None:
        self.root = root
        self.slots = {}
        self.datums = {}
        self.row_length = 4
        self.durations = {}
        self.names = []
        self.binds = {}
        self.slot_names = [str(x) for x in range(0, len(SkillTimer.names))]
        self.data = {}
        self.left_slots = Frame(root, borderwidth=5)
        self.left_slots.grid(column=0, row=1, rowspan=50)
        self.right_slots = Frame(root, borderwidth=5)
        self.right_slots.grid(column=1, row=1, rowspan=50)

        for index, name in enumerate(self.slot_names):
            if index%2:
                slot = self.slots[name] = SkillOptionFrame(self.left_slots, name)
            else:
                slot = self.slots[name] = SkillOptionFrame(self.right_slots, name)
    
    def collect(self):
        self.data = {}
        for name in self.slot_names:
            slot: SkillOptionFrame = self.slots[name]
            slot.update()
            if slot.used:
                name = slot.get_name()
                xdata = slot.get_data()
                self.data[name] = xdata
        return self.data


class BottomFrame(DiabloMainMenu):
    def __init__(self, root, object: DiabloMainMenu) -> None:
        self.frame = Frame(root, relief='sunken', border =5, height=100)
        self._save =  Button(self.frame, text="Save", width=30,command=object.save)
        self.update = Button(self.frame, text="Update", width=30, command=object.collect)
        self.load =   Button(self.frame, text="Load", width=30, )
        self._save.pack()
        self.update.pack()
        self.load.pack()
        self.frame.grid(column=1, row=3)
        

    
mainmenu = DiabloMainMenu()
        
                
                
            

            