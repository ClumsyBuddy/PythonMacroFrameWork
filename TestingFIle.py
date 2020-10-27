import keyboard
import mouse
import time


def MainLoop():
	Counter = 0
	while keyboard.is_pressed("i") == False:
		Counter+=1
		if keyboard.is_pressed("e"):
			print("Clicked E")
		if Counter == 100000:
			break
		time.sleep(0.10)
		print("Looping")
	print("Exited Loop")




def main():
	print("Hello World")
	MainLoop()
    


if __name__ == '__main__':
    main()