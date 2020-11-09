import pyautogui as auto
import win32api, win32con, win32gui
import time
from Utility import UtilityFunctions as utility


#Needs to be redone
def SendClickToWindow(x, y, Window = None, Speed = 0.05):
	try:
		hWnd = win32gui.FindWindowEx(0, 0, None, Window)
	except:
		print("Couldn't Find the window")
	else:
		print("Window: " + str(hWnd))
		print("Before ScreenToClient: " + str(x), str(y))
		(x,y) = win32gui.ScreenToClient(hWnd, (x,y))
		print("Before AfterScreenToClient: " + str(x), str(y))
		lParama = win32api.MAKELONG(x,y)
		print("Before After MakeLong: " + str(lParama))
		win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, lParama)
		win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParama)
		time.sleep(Speed)
		win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParama)

		print("Clicked " + str(x), str(y))



#Clamp the speed so it wont be udner 0.05 because any lower and clicks might not register
#Set the cursor position to the desired location and then Mouse down and then mouse up aka Click
def WinClick(x,y, Speed = 0.05):
	Speed = Utility.ClampMin(Speed, 0.05)
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(Speed)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Clamp the position then get the current cursor position. Then perform winclick and return to previous position
#Otherwise this is a wrapper for WinClick
def WinClickAndReturn(x,y, Speed = 0.05):
	Speed = Utility.ClampMin(Speed, 0.05)
	OldPosX, OldPosY = win32api.GetCursorPos()
	WinClick(x,y,Speed)
	win32api.SetCursorPos((OldPosX,OldPosY))


#This was annoying to make
#Set the cursor to the target position, then perform mouse down
#Get the distance between the Start position of the click the the end position
#Create checks to see if it has reached the end position of the X or Y Axis
#if it has reach the endpos then stop moving that axis
#inside the while loop we are checking if it is forwards or backwards aka going -1 or 1
#it will constantly move the cursor until it has reached or gone past the Endpos
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

#Use pyautogui to Move the mouse and return to old position
def MoveReturn(PosX, PosY):
	OldPosX, OldPosY = auto.position()
	auto.click(PosX, PosY)
	auto.moveTo(OldPosX, OldPosY)
#use pyautogui to Click a position on screen
def MoveandClick(PosX, PosY):
	auto.click(PosX, PosY)
#use pyautogui to Drag the mouse form where ever your mouse currently is
def DragMouse(PosX, PosY, Speed = 2, _button = 'left'):
	auto.dragTo(PosX, PosY, Speed, button=_button)
#use pyautogui to drag mouse from a point to another point
def DragMouseToFrom(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 2, _button = 'left'):
	auto.moveTo(StartPosX, StartPosY)
	auto.dragTo(EndPosX, EndPosY, Speed, button=_button)
#Get the cursor position
def ReturnCursorPosition():
	CursorPos = win32api.GetCursorPos()
	return CursorPos