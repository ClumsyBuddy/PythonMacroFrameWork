import keyboard as _keyboard

##This class Handles all of the input. WIP I want to add more functionality
class Input_Handler():
	def __init__(self, CharKeys, HeldKeys):
		self.StopInput = False
		self.CharKeys = CharKeys
		self.HeldKeys = HeldKeys
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

	def UpdateInputHandler(self):
		self.HandleInput()

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
		pass

	def PostKeyRelease(self, CurrentKey, t): #t allows the toggle of the current key to turn on some logic
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

	def KeyToggleLogic(self):
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					pass
				if self.CharKeys[Key] == 'i':
					pass
