from MacroModules.InputLogic import Input_Logic
#from MacroModules.InputHandling import InputKeyBoard
#from MacroModules.InputHandling import InputMouse
#from MacroModules.InputHandling import Utility
from MacroModules import InputHandling


class MinerScript(Input_Logic):
	def __init__(self, CharKeys, HeldKeys):
		super().__init__(CharKeys, HeldKeys)





	def PostKeyPress(self, Key, t):
		if Key == 'e':
			self.KeyToggles[t] = not self.KeyToggles[t]


	def KeyToggleLogic(self):
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					print("hello")
				if self.CharKeys[Key] == 'i':
					pass



def main():
	Script = MinerScript(['e', 'i'], ['esc'])
	ExitLoop = False
	
	while ExitLoop == False:
		Script.UpdateInputHandler()
		ExitLoop = Script.ContinueInput()






if __name__ == '__main__':
	main()