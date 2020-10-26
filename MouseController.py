import pyautogui as auto




def MoveReturn(PosX, PosY):
	OldPosX, OldPosY = auto.position()
	auto.click(PosX, PosY)
	auto.moveTo(OldPosX, OldPosY)

def MoveandClick(PosX, PosY):
	auto.click(PosX, PosY)

def LocateImageReturnCenter(PathToImage, GScale, Rect, Acc):
	PosX, PosY = auto.locateCenterOnScreen(PathToImage, region=Rect, greyscale=GScale, confidence=Acc)
	return PosX, PosY

def ImageSearchEntireScreen(PathToImage, GScale, Acc):
	PosX, PosY = auto.locateCenterOnScreen(PathToImage, grayscale=True, confidence=Acc)
	return PosX, PosY

def AdjustLocateImageReturnCenter(PathToImage, GScale, Left, Top, Width, Height, Acc):
	PosX, PosY = -1, -1
	Counter = 0
	while PosX == -1 & PosY == -1:
		Counter += 1
		if Counter > 10:
			break
		try:
			PosX, PosY = auto.locateCenterOnScreen(PathToImage, region=(Left, Top, Width, Height), greyscale=GScale, confidence=Acc)
		except:
			print("Couldn't find the Image")
			if GScale == False:
				GScale = True
			if Acc > 0.60:
				Acc -= 0.05
			Left += 20
			Top += 20
			Width += 20
			Height += 20
		else:
			return PosX, PosY
		return PosX, PosY


def DragMouse(PosX, PosY, Speed = 2, _button = 'left'):
	auto.dragTo(PosX, PosY, Speed, button=_button)

def DragMouseToFrom(StartPosX, StartPosY, EndPosX, EndPosY, Speed = 2, _button = 'left'):
	auto.moveTo(StartPosX, StartPosY)
	auto.dragTo(EndPosX, EndPosY, Speed, button=_button)