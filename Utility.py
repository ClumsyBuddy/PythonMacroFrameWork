import numpy as np


def ClampMin(Val, Min):
	if Val < Min:
		Val = Min
		return Val
	else:
		return Val

def ClampMax(Val, Max):
	if Val > Max:
		Val = Max
		return Val
	else:
		return Val