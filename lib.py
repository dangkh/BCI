import numpy as np
import matplotlib.pyplot as plt

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
	Data = Data.T
	print("Reading Data Finished with shape:", Data.shape)
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


def visualFile(matrix):
	matrix = matrix.T
	print(matrix.shape)
	numberChanels = matrix.shape[0]
	lengSignal = matrix.shape[1]
	for ch in range(numberChanels):
		ox = [x for x in range(lengSignal)]

		fig = plt.figure()
		plt.plot( ox, matrix[ch], color='blue', linewidth=1, label="channel" + str(ch))
		plt.ylabel(' Signal Value', fontsize=20)
		plt.xlabel(' Time Frame ', fontsize=20)
		plt.title('Channel_' + str(ch), fontsize=30)
		plt.legend(fontsize = 20)
		plt.savefig('./images/Channel_' + str(ch) +'.png')
		plt.clf()