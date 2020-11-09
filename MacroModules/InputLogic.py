from .InputHandling.InputHandler import Input_Handler




class Input_Logic(Input_Handler):
	def __init__(self, CharKeys, HeldKeys):
		super().__init__(CharKeys, HeldKeys)
		#self._Input = Input_Handler
		self.MousePos = []
		self.ScreenSize = ()

		self.InitInput()

	def InitInputLogic(self):
		pass

	def UpdateInputHandler(self):
		self.HandleInput()
		self.KeyToggleLogic()
		return self.ContinueInput()

	def UpdateInputLogic(self):
		pass

	def PostKeyPress(self, CurrentKey, t):
		if CurrentKey == 'e':
			#self.KeyToggles[t] = not self.KeyToggles[t]
			self.MousePos.append(_mouse.ReturnCursorPosition())
			print(self.MousePos)
		if CurrentKey == 'i':
			self.KeyToggles[t] = not self.KeyToggles[t]


	def KeyToggleLogic(self):
		#print("KeyToggleFunction")
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					pass
				if self.CharKeys[Key] == 'i':
					pass
					
					#_mouse.WinClickAndReturn(Pos[0], Pos[1])

