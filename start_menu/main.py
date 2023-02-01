import tkinter as tk
from tkinter import PhotoImage
from PIL import Image
import pyautogui
import asyncio
import subprocess


####################################################################
#       Classes
####################################################################


class Directory:
    """ A collection of directories used in this script """

    current = "\\".join(__file__.split("\\")[:-1]) 
    background_image = f"{current}\\background_good.png"
    X_image = f"{current}\\X.png"
    settings_image = f'{current}\\settings.png'
    background = f'{current}\\background.png'


class UserImages:
    background = f"{Directory.current}\\frame1.png"
    X          = f"{Directory.current}\\X.png"
    start      = f"{Directory.current}\\start.gif"
    settings   = f"{Directory.current}\\settings.gif"
    title      = f"{Directory.current}\\d1.gif"
    exit_      = f'{Directory.current}\\exit.gif'
    spacebar   = f'{Directory.current}\\meter_full.gif'
    book        = f'{Directory.current}\\background.png'


####################################################################
#       Functions
####################################################################



def get_image_dims(filename: str) -> tuple[int, int]:
    """ Returns the filepath image dimensions as a tuple of int (width) int (height) """

    image: Image = Image.open(filename)
    return image.size


async def execute_start_menu() -> None:
    """ start an async execution of the start menu, awaits the subprocess, outputs stderr, stdin to console """
    
    process = await asyncio.create_subprocess_exec(
        "python", 'path//to/script',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    await process.wait()


def start_menu() -> None:

    asyncio.run(execute_start_menu())


def close_window() -> None:
    
    root.destroy()


####################################################################
#       Declare
####################################################################

###################
# Dimensions
###################

XWIDTH, XHEIGHT   = get_image_dims(UserImages.X)
BWIDTH, BHEIGHT   = get_image_dims(UserImages.start)
SWIDTH, SHEIGHT   = get_image_dims(UserImages.settings)
TWIDTH, THEIGHT   = get_image_dims(UserImages.title)
EXWIDTH, EXHEIGHT = get_image_dims(UserImages.exit_)
WIDTH, HEIGHT     = get_image_dims(UserImages.title)
CENTERX           = WIDTH/2
CENTERY           = HEIGHT/2
SCREEN_SIZE: tuple[int, int] = pyautogui.size()
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE
START_BUTTON_PLACE = 150
START_BUTTON_END = START_BUTTON_PLACE + SHEIGHT
SETTINGS_BUTTON_PLACE = START_BUTTON_END + 30
SETTINGS_BUTTON_END = SETTINGS_BUTTON_PLACE + SHEIGHT
EXIT_BUTTON_PLACE = SETTINGS_BUTTON_END + 30


###################
# Root Window
###################

root              = tk.Tk(screenName="D2R Timer")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry(f"{WIDTH}x{HEIGHT}+{SCREEN_WIDTH-WIDTH}+{SCREEN_HEIGHT-HEIGHT-40}")

###################
# Image Loads
###################

BACKGROUND_IMAGE  = PhotoImage(file = UserImages.background)
X_IMAGE           = PhotoImage(file = UserImages.X)
START_BUTTON      = PhotoImage(file = UserImages.start)
SETTINGS_BUTTON   = PhotoImage(file = UserImages.settings)
EXIT_BUTTON       = PhotoImage(file = UserImages.exit_)
BOOK_BACKGROUND   = PhotoImage(file = UserImages.book)
###################
# Frame Stuff
###################

i=0
si = 0
st = 0
TITLE_FRAMES_TOTAL = 68
TITLE_FRAMES_ALLOWED = 67
SPACE_FRAMES_TOTAL = 64
SPACE_FRAMES_ALLOWED = 63
START_FRAME       = PhotoImage(file=UserImages.start, format= 'gif -index %i' %(st))
start_frames      = [PhotoImage(file=UserImages.start, format='gif -index %i' %(i)) for i in range(SPACE_FRAMES_TOTAL)]
SETTINGS_FRAME    = PhotoImage(file=UserImages.settings, format= 'gif -index %i' %(st))
settings_frames   = [PhotoImage(file=UserImages.settings, format='gif -index %i' %(i)) for i in range(SPACE_FRAMES_TOTAL)]
TITLE_FRAME       = PhotoImage(file= UserImages.title, format = 'gif -index %i' %(i))
frames            = [PhotoImage(file=UserImages.title, format = 'gif -index %i' %(i)) for i in range(TITLE_FRAMES_TOTAL)]
EXIT_FRAME        = PhotoImage(file=UserImages.exit_, format = 'gif -index %i' %(st))
exit_frames       = [PhotoImage(file=UserImages.exit_, format='gif -index %i' %(i)) for i in range(SPACE_FRAMES_TOTAL)] 


###########################################################################
#       Layout
###########################################################################

###################
# Background
###################

background_label = tk.Label(
        root, 
        image=BOOK_BACKGROUND
    )

background_label.place(
        x=0, 
        y=0, 
        width=WIDTH, 
        height=HEIGHT,
    )


gif_label = tk.Label(
        root, 
        padx=-1, 
        pady=-1, 
        borderwidth=-1
    )

gif_label.place(
        x=WIDTH,
        y=0
    )

###################
#   Close Button
###################

close_button = tk.Button(
        root, 
        text="",
        image=X_IMAGE, 
        font='AvQest', 
        command=close_window,
        width=XWIDTH,
        height=XHEIGHT,
        padx=-1,
        pady=-1,
        borderwidth=-1,
        background=None
    )

close_button.place(
        x=WIDTH-XWIDTH,
        y=0,
        width=XWIDTH,
        height=XHEIGHT,
        bordermode=None,
    )


###################
#  Start Button
###################

def start_setup() -> None:
    pass 

start_button = tk.Button(
        root,
        foreground='white',
        image=start_frames[0],
        background=None,
        width=BWIDTH,
        height=BHEIGHT,
        padx=0,
        pady=0,
        borderwidth=-1,
        activebackground=None,
        activeforeground=None, 
        command=start_setup
    )

start_button.place(
        x=10,
        y=START_BUTTON_PLACE,
        width=BWIDTH,
        height=BHEIGHT,
        bordermode=None,
    )

###################
# Settings Button
###################

def settings_menu() -> None:
    pass

settings_button = tk.Button(
        root,
        text='',
        image=settings_frames[0],
        background=None,
        width=SWIDTH,
        height=SHEIGHT,
        padx=0,
        pady=0,
        borderwidth=-1,
        activebackground=None,
        activeforeground=None, 
        command=settings_menu
    )

settings_button.place( 
        x=10,
        y=SETTINGS_BUTTON_PLACE,
        width=SWIDTH,
        height=SHEIGHT,
        bordermode=None,
    )

###################
#  Exit Button
###################

exit_button = tk.Button(
        root,
        text='',
        image=exit_frames[0],
        background=None,
        width=EXWIDTH,
        height=EXHEIGHT,
        padx=0,
        pady=0,
        borderwidth=-1,
        activebackground=None,
        activeforeground=None, 
        command=close_window
    )

exit_button.place(
        x=10,
        y=EXIT_BUTTON_PLACE,
        width=EXWIDTH,
        height=EXHEIGHT,
        bordermode=None,
    )


#######################
# Animation Functions
#######################


def update_diablo_gif(index: int) -> None:
    """ Update the image of the gif to the index specified """

    frame: PhotoImage = frames[index]
    index += 1

    if index>TITLE_FRAMES_ALLOWED: #With this condition it will play gif infinitely
        index: int = 0

    back_label: tuple[str, str, str, any, any] = background_label.configure(image=frame)
    
    root.after(60, update_diablo_gif, index)



def update_start_gif(index: int) -> None:
    """ Update the image of the gif to the index specified """

    sframe: PhotoImage = start_frames[index]
    index += 1

    if index>SPACE_FRAMES_ALLOWED:
        index: int = 0

    back_label: tuple[str, str, str, any, any] = start_button.configure(image=sframe)

    root.after(60, update_start_gif, index)

def update_settings_gif(index: int) -> None:
    """ Update the image of the gif to the index specified """

    sframe: PhotoImage = settings_frames[index]
    index += 1

    if index>SPACE_FRAMES_ALLOWED:
        index: int = 0

    back_label: tuple[str, str, str, any, any] = settings_button.configure(image=sframe)

    root.after(60, update_settings_gif, index)

def update_exit_gif(index: int) -> None:
    """ Update the image of the gif to the index specified """

    sframe: PhotoImage = exit_frames[index]
    index += 1

    if index>SPACE_FRAMES_ALLOWED:
        index: int = 0

    back_label: tuple[str, str, str, any, any] = exit_button.configure(image=sframe)

    root.after(60, update_exit_gif, index)

###################
# Main Loop
###################

root.after(0, update_start_gif, 0)
root.after(0, update_settings_gif, 0)
root.after(0, update_diablo_gif, 0)
root.after(0, update_exit_gif, 0)
root.mainloop()