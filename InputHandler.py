from pynput import keyboard, mouse
import MouseController as _mouse
import Utility as utility
import time


def InitInput():
	listener = keyboard.Listener(on_press=on_press)
	listener.start()
	return listener


def on_press(key):
	if hasattr(key, 'char'):
		HandleCharInput(key)
	else:
		if HandleNonCharInput(key) == False:
			return False


def HandleCharInput(key):
	global ClickPosX, ClickPosY
	if key.char == 'e':
		None
	if key.char == 'm':
		None
	if key.char == 'i':
		None
	if key.char == 'o':
		None

def HandleNonCharInput(key):
	if key == keyboard.Key.esc:
		print("Stopping Input")
		return False
