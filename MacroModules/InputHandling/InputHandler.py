from .InputKeyBoard import KeyBoardController as _KeyboardController
from .InputMouse import MouseController as _mouse
from .Utility import UtilityFunctions as utility

import time
import keyboard as _keyboard
import random

##This class Handles all of the input. WIP I want to add more functionality
class Input_Handler():
	def __init__(self):
		self.StopInput = False
		self.CharKeys = ['e', 'i', 'y']
		self.HeldKeys = ['esc', 'o']
		self.KeyBool = []
		self.KeyToggles = []
		self.InitInput()
		self.MousePos = []
		self.TempCounter = 0
#Initialize the Keybool with the amount of keys int he Key Char list
	def InitInput(self):
		for Key in range(len(self.CharKeys)):
			self.KeyBool.append(False)
		for Key in range(len(self.CharKeys)):
			self.KeyToggles.append(False)
		#For each key type Check if the key has already been pressed
		#if it hasnt been pressed recently then perform a PostKeyPress action with the key
		#if the key has been pressed and then released perform a PostKeyRelease Action with the key
		#if the key is Esc thats used for closing input
	def HandleInput(self):
		#If the key is a key to be held down then send it to the KeyHeldDown Function
		for Held in range(len(self.HeldKeys)):
			if self.CheckForKeyPress(self.HeldKeys[Held]):
				self.KeyHeldDown(self.HeldKeys[Held])

		#the Keybool is to make sure a key doesnt get clicked repeatedly
		for Key in range(len(self.CharKeys)):
			if self.KeyBool[Key] == False:
				if self.CheckForKeyPress(self.CharKeys[Key]):
					self.PostKeyPress(self.CharKeys[Key], Key)
					self.KeyBool[Key] = True
			if self.KeyBool[Key] == True:
				if self.CheckForKeyRelease(self.CharKeys[Key]):
					self.PostKeyRelease(self.CharKeys[Key], Key)
					self.KeyBool[Key] = False

	#Function to handle keys that are excepted to be held down
	def KeyHeldDown(self, CurrentKey):
		if CurrentKey == 'esc':
			self.StopInput = True
		if CurrentKey == 'o':
			print("Holding " + CurrentKey)

	#Logic after knowning which key has been pressed
	def PostKeyPress(self, CurrentKey, t): #t allows the toggle of the current key to turn on some logic
		if CurrentKey == 'e':
			#self.KeyToggles[t] = not self.KeyToggles[t]
			self.MousePos.append(_mouse.ReturnCursorPosition())
			print(self.MousePos)
		if CurrentKey == 'i':
			self.KeyToggles[t] = not self.KeyToggles[t]
			#self.MousePos = list(_mouse.ReturnCursorPosition())
			#print(self.MousePos)

	def PostKeyRelease(self, CurrentKey, t): #t allows the toggle of the current key to turn on some logic
		if CurrentKey == 'e':
			pass
		if CurrentKey == 'i':
			#self.TakeAScreenShot()
			pass


#Simple functino that checks if the key has been pressed
	def CheckForKeyPress(self, Key):
		if _keyboard.is_pressed(Key):
			return True
		else:
			return False

	#Simple function that check if a key is being pressed but is used to return if its not pressed This function isnt actially needed
	def CheckForKeyRelease(self, Key):
		if _keyboard.is_pressed(Key):
			return False
		else:
			return True
		return self.CharKeys
	#Simeple get function for StopInput to let the Logicthread know if its time to break for input loop
	def ContinueInput(self):
		return self.StopInput
	#Temp function to handle Toggle Logic
	def KeyToggleLogic(self):
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					#print("Looping E Key")
					print(_KeyboardController.char2key('e'))
				if self.CharKeys[Key] == 'i':
					time.sleep(.50)
					Pos = utility.LocateAmountOfImageOnScreen('CopperOre.PNG')
					if len(Pos) == 27:
						pass
					else:
						rand = random
					#_mouse.WinClickAndReturn(Pos[0], Pos[1])

class InputLogic():
	def __init__():
		self.MousePosition = 0,0
		self.MouseRect = 0,0

#Not being used but a InputTimer, basic counter used to check how long a key was pressed. Might delete
class InputTimer():
	def __init__(self, MaxTime = 0, MinTime = 0):
		self.Time = 0
		self.StartTimer = False
		self.MaxTime = MaxTime
		self.MinTime = MinTime
	def Start_Timer(self):
		self.StartTimer = True
	def Update_Timer(self):
		if self.Time == self.MaxTime:
			self.Time = self.MinTime
		self.Time += 1

#Just used to debug my key presses
def PrintCurrentKey(Key, Pressed):
	if Pressed == True:
		print(Key + " Pressed")
	else:
		print(Key + " Released")