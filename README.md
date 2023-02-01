






     


![title](https://user-images.githubusercontent.com/108424001/216174222-ae49187b-abbc-4e90-a5ac-f95d7cf1fde6.png)  
![battlecommand](https://user-images.githubusercontent.com/108424001/216168754-72349527-1a5e-4bd0-94a6-1cd9e979358a.png)![bloodmeter](https://user-images.githubusercontent.com/108424001/216168730-6612c211-4785-4de2-91ad-6dc8a7769316.gif)

---



Working on a Diablo 2 resurrected skill timer with authentic skill buff timers.


So far the intro screen is complete (ill show a gif in a bit). 

![ezgif com-gif-maker](https://user-images.githubusercontent.com/108424001/216184167-91fea314-f1c2-49f5-9158-0b1d1093c36c.gif)


The timers are creatable with 
different skills and speeds. Working on binding right now. 



![todo](https://user-images.githubusercontent.com/108424001/216178650-0aee3ec3-a495-4a2d-a157-f4a6d1e405fd.png)



1. create a way to pipe saved files from main_menu to load into DiabloSkillTimers Class
2. Bind all the durations to the skill timers
3. Bind all the keys to the skill timers programmatically
4. Make the main menu not look like dog water script



example: 

![battlecommand](https://user-images.githubusercontent.com/108424001/216168754-72349527-1a5e-4bd0-94a6-1cd9e979358a.png)![bloodmeter](https://user-images.githubusercontent.com/108424001/216168730-6612c211-4785-4de2-91ad-6dc8a7769316.gif)



## Primary Tools
---

1. Python3 3.11
2. Tkinter/PySimpleGUI
3. GIMP
4. EZGif

---
![description](https://user-images.githubusercontent.com/108424001/216174868-9ddb983f-0e54-46e5-80de-f94ef3681f2a.png)


```
datafile.py
```

datafile.py is the datafile class whereas, the opening gui can save the data from the choices made to a json file 
so that... the timers gui can use it for reference when binding skills, setting durations, using images

```
diablo_skill_timers.py
```

diablo_skill_timers is a class that represents the timer gui, it takes in the datafile to create the elements of the 
timer. It shows the bloodmeter gif...


## Blood Meter

![bloodmeter](https://user-images.githubusercontent.com/108424001/216168411-f0e19346-eae9-4d75-b6ee-6e384061f0d1.gif)


this is a custom gif i made myself. original content... 

..from the original diablo 2 health meter. I have a mana version one also. There were harrrd to create, so please dont steal them without giving credit where its due.

---

![usage](https://user-images.githubusercontent.com/108424001/216174208-dff9f652-6beb-40da-a616-77ca4c43faff.png)


```Powershell
git clone https://github.com/Donny-GUI/diablo2-timers.git
cd diablo2-timers
```
