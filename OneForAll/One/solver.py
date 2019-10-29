from kociemba import solve
from rubiksColorResolver import color
from rubiksCubeTracker import tracker

def Solve():

	tracker("fotos/")

	color("out.txt")


	data=""

	with open('scramble.txt', 'r') as myfile:
		data=myfile.read().replace('\n', '')
		
	data=solve(data)

	return  data