import numpy as np
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui as auto

def ClampMin(Val, Min):
	if Val < Min:
		Val = Min
		return Val
	else:
		return Val

def ClampMax(Val, Max):
	if Val > Max:
		Val = Max
		return Val
	else:
		return Val

def IsWindowFocused(Name = ""):
	if GetWindowText(GetForegroundWindow()) == Name:
		return True
	else:
		return False

def ScreenShotRegion(Name = 'ScreenShot', Pos = (0,0), Rect = (auto.size())):
	auto.screenshot(Name, region=(Pos[0], Pos[1], Rect[0], Rect[1]))


def LocateImageReturnCenter(PathToImage, GScale = False, Pos = (0,0), Rect = (0,0), Acc = 1):
	try:
		Pos = auto.locateCenterOnScreen(PathToImage, region=(Pos[0], Pos[1], Rect[0], Rect[1]), grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return -1, -1, -1, -1
	else:
		return Pos

def ImageSearchEntireScreen(PathToImage, GScale = False, Acc = 1):
	try:
		Pos = auto.locateCenterOnScreen(PathToImage,  grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return None
	else:
		return Pos

def AdjustLocateImageReturnCenter(PathToImage, GScale = False, Acc = 1):
	None #Wip Function, Locate Image and slowly zoom in to find a small region


def ReturnScreenSize():
	return auto.size()