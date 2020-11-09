# PythonMacroFrameWork
Frame work for making macros in python, including Image based recognition, Mouse, keyboard listeners and Controllers



To Start with the framework simply:
from MacroModules.InputLogic import Input_Logic


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
