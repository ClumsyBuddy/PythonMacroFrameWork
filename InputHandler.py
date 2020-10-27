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
	global ClickPosX, ClickPosY
	if key.char == 'e':
		_mouse.WinDragTo(300, 200, 600, 200, 4)
	if key.char == 'm':
		PosX, PosY = _mouse.ImageSearchEntireScreen("Temp.PNG", True, 0.80)
		print(PosX, PosX)
	if key.char == 'i':
		Pos =  _mouse.LocateImageReturnCenter("Temp.PNG", True, (0,0), (75,75), 0.80)
		print(Pos)
	if key.char == 'o':
		_mouse.ScreenShotRegion("Test.PNG", (0,0), (75,75))

def HandleNonCharInput(key):
	if key == keyboard.Key.esc:
		print("Stopping Input")
		return False
