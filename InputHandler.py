from pynput import keyboard, mouse
import MouseController as _mouse

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
	if key.char == 'e':
		_mouse.MoveReturn(100,100)
	if key.char == 'm':
		_mouse.WinClickAndReturn(100,100)
def HandleNonCharInput(key):
	if key == keyboard.Key.esc:
		print("Stopping Input")
		return False