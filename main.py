import numpy as np
import sys
import argparse

def readFile(data_dir):
	Data = []
	f=open(data_dir, 'r')
	counter = 0
	for line in f:
		if counter > 0:
			elements = line.split(',')
			# print(elements)
			if (elements[-1] == '\n'):
				elements = elements[:-1]
			# print(elements)
			Data.append(list(map(float, elements)))
		counter+= 1
	f.close()

	Data = np.array(Data) # list can not read by index while arr can be
	Data = np.squeeze(Data)
	print(Data.shape)
	return Data

def exportMatrix(matrix, dir):
	f = open(dir, "w")
	for x in range(matrix.shape[0]):
		line = ""
		frame = matrix[x]
		for i in range(len(frame)-1):
			line += str(frame[i]) + ", "
		line += str(frame[-1])
		line += "\n"
		f.write(line)
	print(f.close())	


if __name__ == '__main__':

	# Data = readFile("exampleData")
	# Data = Data.astype(float)
	# exportMatrix(Data, "exampleData.txt")

	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--DataDir', required=True, type=str, help='path to data sample')
	args = parser.parse_args()
	print (args)

	dataDir = args.DataDir

	Data = readFile(dataDir)
	Data = Data.astype(float)
	exportMatrix(Data, "Data.txt")