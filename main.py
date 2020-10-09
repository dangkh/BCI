import numpy as np
import sys
import argparse	
from lib import *

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--DataDir', required=True, type=str, help='path to data sample')
	args = parser.parse_args()
	print (args)

	dataDir = args.DataDir

	Data = readFile(dataDir)
	Data = Data.astype(float)
	Data = Data[3:17,:].T
	# exportMatrix(Data, "Data.txt")
	visualFile(Data, fixAxes = False, name = "orignal")
	rescontr = testPCA(Data)
	visualFile(rescontr, fixAxes = False, name = "refined")