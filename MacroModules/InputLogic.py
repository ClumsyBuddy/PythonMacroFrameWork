from .InputHandling.InputHandler import Input_Handler
import time



class Input_Logic(Input_Handler):
	def __init__(self, CharKeys, HeldKeys):
		super().__init__(CharKeys, HeldKeys)
		self.MousePos = []
		self.ScreenSize = ()

		self.InitInput()

	def InitInputLogic(self):
		pass

	def UpdateInputHandler(self, k = True, t = 0):
		self.UpdateInput(k)
		self.KeyToggleLogic()
		time.sleep(t)
		return self.ContinueInput()

	def UpdateInputLogic(self):
		pass

	def PostKeyPress(self, CurrentKey, t):
		if CurrentKey == 'e':
			pass
			print(self.MousePos)
		if CurrentKey == 'i':
			pass


	def KeyToggleLogic(self):
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					pass
				if self.CharKeys[Key] == 'i':
					pass

