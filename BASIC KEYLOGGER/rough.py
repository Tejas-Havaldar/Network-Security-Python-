# with open("log.txt","a") as f:
#     f.write("Hello World\n")


# with Pynput we can do following
# Controlling your mouse
# Controlling your keyboard
# Listening to your mouse
# Listening to your keyboard

from pynput.mouse import Controller
from pynput.keyboard import Controller

def control_mouse():
    mouse = Controller()
    mouse.position = (100,200)

# control_mouse()

def control_keyboard():
    keyboard = Controller()
    keyboard.type("I amawesome")

control_keyboard()