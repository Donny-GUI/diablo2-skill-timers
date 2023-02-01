import os
import dataclasses
from PIL import Image



@dataclasses.dataclass(slots=True)
class Files:
    black           = f'{os.getcwd()}\\black.png'
    bloodmeter      = f'{os.getcwd()}\\bloodmeter.gif'
    battleorders    = f'{os.getcwd()}\\skills\\battleorders.png'
    battlecommand   = f'{os.getcwd()}\\skills\\battlecommand.png'
    burstofspeed    = f'{os.getcwd()}\\skills\\burstofspeed.png'
    chillingarmor   = f'{os.getcwd()}\\skills\\chillingarmor.png'
    cloakofshadows  = f'{os.getcwd()}\\skills\\clockofshadows.png'
    cyclonearmor    = f'{os.getcwd()}\\skills\\cyclonearmor.png'
    energyshield    = f'{os.getcwd()}\\skills\\energyshield.png'
    fade            = f'{os.getcwd()}\\skills\\fade.png'
    frozenarmor     = f'{os.getcwd()}\\skills\\frozenarmor.png'
    holyshield      = f'{os.getcwd()}\\skills\\holyshield.png'
    hurricane       = f'{os.getcwd()}\\skills\\hurricane.png'
    shiverarmor     = f'{os.getcwd()}\\skills\\shiverarmor.png'
    shout           = f'{os.getcwd()}\\skills\\shout.png'
    map= {  
        'bloodmeter':       bloodmeter,
        'battleorders':     battleorders,
        'battlecommand':    battlecommand,
        'burstofspeed':     burstofspeed,
        'chillingarmor':    chillingarmor,
        'cloakofshadows':   cloakofshadows,
        'cyclonearmor':     cyclonearmor,
        'energyshield':     energyshield,
        'fade':             fade,
        'frozenarmor':      frozenarmor,
        'holyshield':       holyshield,
        'hurricane':        hurricane,
        'shiverarmor':      shiverarmor,
        'shout':            shout
        }


@dataclasses.dataclass(slots=True)
class SkillTimer:
    names           = [
        "battleorders", "battlecommand", "burstofspeed", 
        "chillingarmor", "cyclonearmor", 'cloakofshadows',
        'energyshield','fade','frozenarmor','holyshield',
        'hurricane','shiverarmor','shout'
        ]
    
    battleorders    = [Image.open(Files.battleorders),       Image.open(Files.bloodmeter)]
    battlecommand   = [Image.open(Files.battlecommand   ),   Image.open(Files.bloodmeter)]
    burstofspeed    = [Image.open(Files.burstofspeed    ),   Image.open(Files.bloodmeter)]
    chillingarmor   = [Image.open(Files.chillingarmor   ),   Image.open(Files.bloodmeter)]
    cyclonearmmor   = [Image.open(Files.cyclonearmor    ),   Image.open(Files.bloodmeter)]
    cloakofshadows  = [Image.open(Files.cloakofshadows  ),   Image.open(Files.bloodmeter)]
    energyshield    = [Image.open(Files.energyshield    ),   Image.open(Files.bloodmeter)]
    fade            = [Image.open(Files.fade        ),       Image.open(Files.bloodmeter)]
    frozenarmor     = [Image.open(Files.frozenarmor ),       Image.open(Files.bloodmeter)]
    holyshield      = [Image.open(Files.holyshield  ),       Image.open(Files.bloodmeter)]
    hurricane       = [Image.open(Files.hurricane   ),       Image.open(Files.bloodmeter)]
    shiverarmor     = [Image.open(Files.shiverarmor ),       Image.open(Files.bloodmeter)]
    shout           = [Image.open(Files.shout       ),       Image.open(Files.bloodmeter)]
    map = {
        "battleorders":battleorders, 
        "battlecommand":battlecommand, 
        "burstofspeed":burstofspeed, 
        "chillingarmor":chillingarmor, 
        "cyclonearmor":cyclonearmmor, 
        'cloakofshadows':cloakofshadows,
        'energyshield':energyshield, 
        'fade':fade,
        'frozenarmor':frozenarmor,
        'holyshield':holyshield,
        'hurricane':hurricane,
        'shiverarmor':shiverarmor,
        'shout':shout
    }

def get_random_name():
    from random import randint
    names = ['Barb', 'Sorc', 'Paly', 'Sin', 'Druid', 'Necro', 'Necromancer', 'Barbarian', 'Paladin', 'Assassin', 'Sorceress', 'Moo_Cow']
    rand1 = randint(0, len(names)-1); randname = names[rand1]
    subclasses = ['Lite', 'Fire', 'Cold', 'Melee', 'Poison', 'Bone', 'Holy', 'Aura', 'Summon', 'Zeal', 'Bow', 'Jav', 'Trap', 'Windy', 'Pet', 'MagicFind'] 
    rand2 = randint(0, len(subclasses)-1); randclass = subclasses[rand2]
    char_type = ["Ladder", "Normal", 'Nightmare', "Hell", "Hardcore", "Offline", "Season"]
    rand3 = randint(0, len(char_type)-1); randtype = char_type[rand3]
    if (rand1, rand2, rand3) == (6, 6, 6):return "Jeffery_Epstein_Necromancer"
    elif (rand1, rand2, rand3) == (1, 2, 3):return "Jeffery_Epstein_Assassin"
    elif (rand1, rand2, rand3) == (4, 2, 0):return "Smoking_Fat_Doinks"
    else:
        switch = randint(0, 1)
        if switch%2: name = f'{randtype}_{randname}_{randclass}'
        else: name= f'{randtype}_{randclass}_{randname}'
        return name