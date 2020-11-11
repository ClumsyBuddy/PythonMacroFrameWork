from MacroModules.InputLogic import Input_Logic
from MacroModules.InputHandling.InputKeyBoard import KeyBoardController as _keyboard
from MacroModules.InputHandling.InputMouse import MouseController as _mouse
from MacroModules.InputHandling.Utility import UtilityFunctions as _utility
#from MacroModules import InputHandling
import time

class MinerScript(Input_Logic):
	def __init__(self, CharKeys, HeldKeys):
		super().__init__(CharKeys, HeldKeys)


	def KeyHeldDown(self, CurrentKey):
		if CurrentKey == 'esc':
			#self.StopInput = True
			pass
		if CurrentKey == 'o':
			_keyboard.KeyboardInput('w')
			print("Should be moving")



	def PostKeyRelease(self, Key, t):
		if Key == 'e':
			self.KeyToggles[t] = not self.KeyToggles[t]
			print("Toggle Key")
			print(self.KeyToggles[t])
			pass
		if Key == 'i':
			self.StopInput = True
		if Key == 'j':
			self.KeyToggles[t] = not self.KeyToggles[t]

	def MouseHeldDown(self):
		_mouse.MoveMouse(None, 50)
		print("Moved Mouse Down")


	def KeyToggleLogic(self):
		for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					self.HandleMoueInput()
				if self.CharKeys[Key] == 'i':
					pass
				if self.CharKeys[Key] == 'j':
					_keyboard.KeyboardInput('w')



def main():
	Script = MinerScript(['e', 'i', 'j'], ['o'])
	ExitLoop = False

	while ExitLoop == False:
		Script.UpdateInputHandler(True, 0)
		ExitLoop = Script.ContinueInput()
	print("Exiting App")






if __name__ == '__main__':
	main()