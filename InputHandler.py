import MouseController as _mouse
import Utility as utility
import time
import keyboard as _keyboard

#This class Handles all of the input. WIP I want to add more functionality
class Input_Handler():
	def __init__(self):
		self.StopInput = False
		self.CharKeys = ['e', 'i', 'y']
		self.HeldKeys = ['esc', 'o']
		self.KeyBool = []
		self.KeyToggles = []
		self.InitInput()

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
		if self.CheckForKeyPress(CurrentKey) and CurrentKey == 'esc':
			self.StopInput = True

	#Logic after knowning which key has been pressed
	def PostKeyPress(self, CurrentKey, t): #t allows the toggle of the current key to turn on some logic
		if CurrentKey == 'e':
			self.KeyToggles[t] = not self.KeyToggles[t]
		if CurrentKey == 'i':
			PrintCurrentKey(CurrentKey, True)

	def PostKeyRelease(self, CurrentKey, t): #t allows the toggle of the current key to turn on some logic
		if CurrentKey == 'e':
			PrintCurrentKey(CurrentKey, False)
		if CurrentKey == 'i':
			PrintCurrentKey(CurrentKey, False)

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

	#Simeple get function for StopInput to let the Logicthread know if its time to break for input loop
	def ContinueInput(self):
		return self.StopInput

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