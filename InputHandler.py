from pynput import keyboard, mouse
import MouseController as _mouse
import Utility as utility
import time
import keyboard as _keyboard


def TempInput():
	if _keyboard.is_pressed('i') == True:
		return True
	else:
		return False

class Input_Handler():
	def __init__(self):
		super().__init__(self)
		self.MousePos = 0
		self.ClickPosX = 0
		self.Toggle = False
	def InitInput(self):
		None
	def HandleInput(self):
		if CheckForKeyPress('esc'):
			return True
		if CheckForKeyPress('i'):
			print(_mouse.ReturnCursorPosition())
		if CheckForKeyPress('e'):
			None
		return False


	def CheckForKeyPress(self, Key):
		if _keyboard.is_pressed(Key):
			return True
		else:
			return False

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

MousePos = None
def HandleCharInput(key):
	global ClickPosX, ClickPosY
	global MousePos
	Rect = (125,125)
	if key.char == 'e':
		None
	if key.char == 'm':
		None
	if key.char == 'i':
		None
	if key.char == '-':
		None
	if key.char == ';':
		None

def HandleNonCharInput(key):
	if key == keyboard.Key.esc:
		print("Stopping Input")
		return False
