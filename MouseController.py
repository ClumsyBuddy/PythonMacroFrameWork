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

def WinDragTo(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 1):
	win32api.SetCursorPos((StartPosX, StartPosY))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	DistX, DistY = (EndPosX - StartPosX), (EndPosY - StartPosY)
	Counter = 0
	XCheck, YCheck = False, False
	PosX, PosY = win32api.GetCursorPos()
	while (PosX, PosY) != (EndPosX, EndPosY):
		Counter += 1
		PosX, PosY = win32api.GetCursorPos()
		XMov, YMov = 0, 0
		if DistX != 0:
			if DistX < 0:
				XMov = Speed * -1
				if PosX <= EndPosX:
					XCheck = True
			else:
				XMov = Speed
				if PosX >= EndPosX:
					XCheck = True
		if DistY != 0:
			if DistY < 0:
				YMov = Speed * -1
				if PosY <= EndPosY:
					YCheck = True
			else:
				YMov = Speed
				if PosY >= EndPosY:
					YCheck = True
		if XCheck == True & YCheck == True:
			break
		if XCheck == True:
			XMov = 0
		if YCheck == True:
			YMov = 0
		SetX = PosX + XMov
		SetY = PosY + YMov
		win32api.SetCursorPos((SetX, SetY))
		time.sleep(0.01)
		if Counter == 3000:
			break
	time.sleep(0.05)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def MoveReturn(PosX, PosY):
	OldPosX, OldPosY = auto.position()
	auto.click(PosX, PosY)
	auto.moveTo(OldPosX, OldPosY)

def MoveandClick(PosX, PosY):
	auto.click(PosX, PosY)

def ScreenShotRegion(Name = 'ScreenShot', Pos = (0,0), Rect = (0,0)):
	auto.screenshot(Name, region=(Pos[0], Pos[1], Rect[0], Rect[1]))


def LocateImageReturnCenter(PathToImage, GScale = False, Pos = (0,0), Rect = (0,0), Acc = 1):
	try:
		Pos = auto.locateOnScreen(PathToImage, region=(Pos[0], Pos[1], Rect[0], Rect[1]), grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return -1, -1, -1, -1
	else:
		return Pos

def ImageSearchEntireScreen(PathToImage, GScale = False, Acc = 1):
	try:
		PosX, PosY = auto.locateCenterOnScreen(PathToImage,  grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return -1, -1
	else:
		return PosX, PosY

def AdjustLocateImageReturnCenter(PathToImage, GScale = False, Acc = 1):
	None #Wip Function, Locate Image and slowly zoom in to find a small region



def DragMouse(PosX, PosY, Speed = 2, _button = 'left'):
	auto.dragTo(PosX, PosY, Speed, button=_button)

def DragMouseToFrom(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 2, _button = 'left'):
	auto.moveTo(StartPosX, StartPosY)
	auto.dragTo(EndPosX, EndPosY, Speed, button=_button)


def ReturnCursorPosition():
	CursorPos = win32api.GetCursorPos()
	return CursorPos