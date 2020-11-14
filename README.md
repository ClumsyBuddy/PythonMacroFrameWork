# PythonMacroFrameWork
Frame work for making macros in python, including Image based recognition, Mouse, keyboard listeners and Controllers



To Start with the framework simply:
```
from MacroModules.InputLogic import Input_Logic
from MacroModules.InputHandling.InputKeyBoard import KeyBoardController as _keyboard
from MacroModules.InputHandling.InputMouse import MouseController as _mouse
from MacroModules.InputHandling.Utility import UtilityFunctions as _utility
```

1. Create a class that inherits from Input_Logic
2. Override main key handling functions

```
class Example(Input_Logic):
		def __init__():
			super().__init__()
		def PostKeyPress(self, Key, t):
			if Key == 'e':
				self.KeyToggles[t] = not KeyToggles[t]
		def KeyToggleLogic(self):
			for Key in range(len(self.KeyToggles)):
			if self.KeyToggles[Key]:
				if self.CharKeys[Key] == 'e':
					pass
				if self.CharKeys[Key] == 'i':
					pass
		def PostKeyRelease(self, Key, t):
			pass
```
There are more Functions you can override but these are the mains one
Use functions from SendMouse or SendKeyboard to send Input to the screen

This framework is WIP, I will be fleshing out the classes so that it's more user-friendly. 
Possible rewrite of the input handler to allow more combinations of how input can be handled.
