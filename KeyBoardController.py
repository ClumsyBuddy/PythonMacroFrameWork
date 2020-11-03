import keyboard
import win32gui, win32api, win32con
import time
from ctypes import windll



#Take a char key and translate it to a windows keycode
def char2key(c):
    # https://msdn.microsoft.com/en-us/library/windows/desktop/ms646329(v=vs.85).aspx
    result = windll.User32.VkKeyScanW(ord(unicode(c)))
    shift_state = (result & 0xFF00) >> 8
    vk_key = result & 0xFF

    return vk_key



def WindowKeyCodesFromKeys(Key):
	pass


#Send a key to a window via windows apli
def SendKeyToWindow(Key, Speed):
	pass
	

#Send a key to a window using pyautogui or something similair
def SendCharKeyToWindow(Key, Speed):
	pass