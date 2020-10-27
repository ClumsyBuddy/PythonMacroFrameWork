import pyautogui as auto
import win32api, win32con
import time
import Utility

def WinClick(x,y, Speed = 0.05):
	Speed = Utility.ClampMin(Speed, 0.05)
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(Speed)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def WinClickAndReturn(x,y, Speed = 0.05):
	Speed = Utility.ClampMin(Speed, 0.05)
	OldPosX, OldPosY = win32api.GetCursorPos()
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(Speed)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	win32api.SetCursorPos((OldPosX,OldPosY))



def MoveReturn(PosX, PosY):
	OldPosX, OldPosY = auto.position()
	auto.click(PosX, PosY)
	auto.moveTo(OldPosX, OldPosY)

def MoveandClick(PosX, PosY):
	auto.click(PosX, PosY)

def LocateImageReturnCenter(PathToImage, GScale, Pos, Rect, Acc):
	try:
		PosX, PosY = auto.locateCenterOnScreen(PathToImage, region=(Pos.x, Pos.y, Rect.Width, Rect.Height), greyscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return -1, -1
	else:
		return PosX, PosY

def ImageSearchEntireScreen(PathToImage, GScale, Acc):
	try:
		PosX, PosY = auto.locateCenterOnScreen(PathToImage,  grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return -1, -1
	else:
		return PosX, PosY

def AdjustLocateImageReturnCenter(PathToImage, GScale, Acc):
	ScreenX, ScreenY = auto.size()
	_quadX = (ScreenX/2)
	_quadY = (ScreenY/2)
	Quad1 = ([0, _quadX, 0, _quadX],[ 0, 0, _quadY, _quadY])
	Quad2 = [(ScreenX/2), (ScreenY/2)]
	print(Quad1)
	ExitLoop = False
	while ExitLoop == False:
		for i in range(0, 4, 1):
			Location = auto.locateCenterOnScreen(PathToImage, region=(0, 0, ScreenX, ScreenY), greyscale=GScale, confidence=Acc)
			if Location == auto.ImageNotFoundException:
				ScreenX = ScreenX / 2
				ScreenY = ScreenY / 2
		if i == 4:
			ExitLoop = True



def DragMouse(PosX, PosY, Speed = 2, _button = 'left'):
	auto.dragTo(PosX, PosY, Speed, button=_button)

def DragMouseToFrom(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 2, _button = 'left'):
	auto.moveTo(StartPosX, StartPosY)
	auto.dragTo(EndPosX, EndPosY, Speed, button=_button)