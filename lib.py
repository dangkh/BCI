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


def visualFile(matrix, fixAxes = False, name = None):
	matrix = matrix.T
	print(matrix.shape)
	numberChanels = matrix.shape[0]
	lengSignal = matrix.shape[1]
	if name == None:
		nameImg = 'Channel_'
	else:
		nameImg = name + '_'
	for ch in range(numberChanels):
		ox = [x for x in range(lengSignal)]

		fig = plt.figure()
		plt.plot( ox, matrix[ch], color='blue', linewidth=1, label="channel" + str(ch))
		if fixAxes:
			plt.ylim(3500, 4500)
		plt.ylabel(' Signal Value', fontsize=20)
		plt.xlabel(' Time Frame ', fontsize=20)
		plt.title('Channel_' + str(ch), fontsize=30)
		# plt.legend(fontsize = 20)
		plt.savefig('./images/'+nameImg + str(ch) +'.png')
		plt.clf()

def testPCA(Data):
	originalData = np.copy(Data)
	newD = Data[0:4000]
	
	maxNum = np.max(newD[:,12])
	minNum = np.min(newD[:,12])
	tmpData = np.copy(Data)

	for x in range(Data.shape[0]):
		if (tmpData[x,12] > maxNum) or (tmpData[x,12] < minNum):
			tmpData[x,12] = 0

	combine_matrix = tmpData
	[frames, columns] = combine_matrix.shape
	columnindex = np.where(combine_matrix == 0)[1]
	frameindex = np.where(combine_matrix == 0)[0]
	columnwithgap = np.unique(columnindex)
	framewithgap = np.unique(frameindex)
	Data_without_gap = np.delete(combine_matrix, columnwithgap, 1)
	mean_data_withoutgap_vec = np.mean(Data_without_gap, 1).reshape(Data_without_gap.shape[0], 1)
	columnWithoutGap = Data_without_gap.shape[1]

	x_index = [x for x in range(0, columnWithoutGap, 1)]
	mean_data_withoutgap_vecX = np.mean(Data_without_gap[:,x_index], 1).reshape(frames, 1)

	joint_meanXYZ = mean_data_withoutgap_vecX
	MeanMat = np.tile(joint_meanXYZ, combine_matrix.shape[1])
	Data = np.copy(combine_matrix - MeanMat)
	Data[np.where(combine_matrix == 0)] = 0

	newD = Data[0:4000]
	_, Sg , UN = np.linalg.svd(newD/np.sqrt(newD.shape[0]-1), full_matrices = False)
	k = 9
	UN = UN.T
	UN = UN[:, :k]

	newD0 = np.copy(newD)
	newD0[:,12] = 0
	_, Sg0 , UN0 = np.linalg.svd(newD0/np.sqrt(newD0.shape[0]-1), full_matrices = False)
	UN0 = UN0.T
	UN0 = UN0[:, :k]

	T_matrix = np.matmul(UN0.T , UN)

	newTmp = np.matmul(np.matmul(np.matmul(Data, UN0), T_matrix), UN.T)
	newTmp = newTmp + MeanMat

	originalData[np.where(Data == 0)] = newTmp[np.where(Data == 0)]
	return originalData