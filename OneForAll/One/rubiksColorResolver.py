
from argparse import ArgumentParser
from json import dumps as json_dumps
from json import loads as json_loads
from math import sqrt
from rubikscolorresolver import RubiksColorSolverGeneric
import logging
import os

if os.path.exists("scramble.txt"):
  os.remove("scramble.txt")
else:
	pass

def color(filename):

	try:
		if filename:
			file_as_string = []
			with open(filename, 'r') as fh:
				rgb = ''.join(fh.readlines())

		scan_data_str_keys = json_loads(rgb)
		scan_data = {}

		for (key, value) in scan_data_str_keys.items():
			scan_data[int(key)] = value

		square_count = len(scan_data.keys())
		square_count_per_side = int(square_count/6)
		width = int(sqrt(square_count_per_side))

		cube = RubiksColorSolverGeneric(width)
		cube.enter_scan_data(scan_data)
		cube.crunch_colors()

		print(''.join(cube.cube_for_kociemba_strict()))
		with open('scramble.txt', 'w') as f:
			print >> f, ''.join(cube.cube_for_kociemba_strict())

	except Exception as e:
		pass