import numpy as np
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui as auto
from enum import Enum


#Clamp to keep something from going under the min Val
def ClampMin(Val, Min):
	if Val < Min:
		Val = Min
		return Val
	else:
		return Val
#A Clamp to keep something from going over the Max Value
def ClampMax(Val, Max):
	if Val > Max:
		Val = Max
		return Val
	else:
		return Val

#Check if a window given is in focus or not
def IsWindowFocused(Name = ""):
	if GetWindowText(GetForegroundWindow()) == Name:
		return True
	else:
		return False

def ReturnXY(List):
	return List[0], List[1]





#Take a screenshot of the Region and give it a default name or name provided
def ScreenShotRegion(Name = 'ScreenShot', Pos = (0,0, 0,0)):
	auto.screenshot(Name, region=(Pos[0], Pos[1], Pos[2], Pos[3]))


#Search the region for the image given, Basically ImageSearchFunction but in a region
def LocateImageReturnCenter(PathToImage, GScale = False, Pos = (0,0), Rect = (0,0), Acc = 1):
	try:
		Pos = auto.locateCenterOnScreen(PathToImage, region=(Pos[0], Pos[1], Rect[0], Rect[1]), grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return None
	else:
		return Pos

#Search the entire screen for the Image given and return the Center position of it
#if found otherwise return None
def ImageSearchEntireScreen(PathToImage, GScale = False, Acc = 1):
	try:
		Pos = auto.locateCenterOnScreen(PathToImage,  grayscale=GScale, confidence=Acc)
	except:
		print("Couldn't find Image")
		return None
	else:
		return Pos

#Still have to figure the logicistics of this one. Not sure how I am goig to approach it
def AdjustLocateImageReturnCenter(PathToImage, GScale = False, Acc = 1):
	None #Wip Function, Locate Image and slowly zoom in to find a small region

#Function to return Screen size, Keep code clean and not have alot of lines in main files
def ReturnScreenSize():
	return auto.size()
