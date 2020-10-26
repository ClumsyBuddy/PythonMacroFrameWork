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

def LocateImageReturnCenter(PathToImage, GScale, Rect, Acc):
	PosX, PosY = auto.locateCenterOnScreen(PathToImage, region=Rect, greyscale=GScale, confidence=Acc)
	return PosX, PosY

def ImageSearchEntireScreen(PathToImage, GScale, Acc):
	PosX, PosY = auto.locateCenterOnScreen(PathToImage, grayscale=True, confidence=Acc)
	return PosX, PosY

def AdjustLocateImageReturnCenter(PathToImage, GScale, Left, Top, Width, Height, Acc):
	ScreenX, ScreenY = auto.size()
	PosX, PosY = auto.locateCenterOnScreen(PathToImage, region=(Left, Top, Width, Height), greyscale=GScale, confidence=Acc)


def DragMouse(PosX, PosY, Speed = 2, _button = 'left'):
	auto.dragTo(PosX, PosY, Speed, button=_button)

def DragMouseToFrom(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 2, _button = 'left'):
	auto.moveTo(StartPosX, StartPosY)
	auto.dragTo(EndPosX, EndPosY, Speed, button=_button)