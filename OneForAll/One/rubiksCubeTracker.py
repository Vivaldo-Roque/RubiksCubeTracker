
from rubikscubetracker import RubiksVideo, RubiksImage, merge_two_dicts
from math import sqrt
import argparse
import json
import logging
import os
import sys
import subprocess

if os.path.exists("out.txt"):
  os.remove("out.txt")
else:
	pass

def tracker(directory):

	def convert_keys_to_int(dict_to_convert):
		result = {}

		for (key, value) in dict_to_convert.items():
			result[int(key)] = value

		return result

	data = {}

	cube_size = None
	cube_size = None

	for (side_index, side_name) in enumerate(('U', 'L', 'F', 'R', 'B', 'D')):
		filename = os.path.join(directory, "rubiks-side-%s.png" % side_name)

		if os.path.exists(filename):
				#log.info("filename %s, side_index %s, side_name %s" % (filename, side_index, side_name))

				#log.info("filename %s, side_index %s, side_name %s" % (filename, side_index, side_name))
			rimg = RubiksImage(side_index, side_name)
			rimg.analyze_file(filename, cube_size)

			if cube_size is None:
				side_square_count = len(rimg.data.keys())
				cube_size = int(sqrt(side_square_count))

			data = merge_two_dicts(data, rimg.data)
				# log.info("cube_size %d" % cube_size)

		else:
			print "ERROR: %s does not exist" % filename
			sys.exit(1)

	print(json.dumps(data, sort_keys=True))
	with open('out.txt', 'w') as f:
		print >> f, json.dumps(data, sort_keys=True)