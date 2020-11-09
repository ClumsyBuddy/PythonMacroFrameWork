import keyboard
import win32gui, win32api, win32con
import time
import pyautogui as auto


#Take a char key and translate it to a windows keycode
def char2key(c):
   vk_key = win32api.VkKeyScan(c)
   return hex(vk_key) 

#Send a key to a window via windows apli
def SendKeyToWindow(Key, Speed):
	pass

def KeyboardInput(Key):
	auto.press(Key)
	

#Send a key to a window using pyautogui or something similair
def SendCharKeyToWindow(Key, Speed):
	pass