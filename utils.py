import numpy as np
from PIL import Image
import os

def load_data(source):
	inputA = []
	inputB = [] 
	y = []
	with open(source) as file:
		data = file.readlines()

	for line in data:
		temp = line.split()
		if len(temp)==3:
			y.append(1)
			path = os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[0])
			
			filename = 'ext'+temp[0]+'_'
			if len(temp[1])==1:
				filename+='000'+temp[1]+'.jpg'
			elif len(temp[1])==2:
				filename+='00'+temp[1]+'.jpg'
			else:
				filename+='0'+temp[1]+'.jpg'
			path1 = os.path.join(path, filename)
			image = Image.open(path1)
			x = np.array(image)
			inputA.append(x)
			
			filename = 'ext'+temp[0]+'_'
			if len(temp[2])==1:
				filename+='000'+temp[2]+'.jpg'
			elif len(temp[2])==2:
				filename+='00'+temp[2]+'.jpg'
			else:
				filename+='0'+temp[2]+'.jpg'
			path2 = os.path.join(path, filename)
			image = Image.open(path2)
			x = np.array(image)
			inputB.append(x)
		
		else:
			y.append(0)
			
			path = 	os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[0])
			filename = 'ext'+temp[0]+'_'
			if len(temp[1])==1:
				filename+='000'+temp[1]+'.jpg'
			elif len(temp[1])==2:
				filename+='00'+temp[1]+'.jpg'
			else:
				filename+='0'+temp[1]+'.jpg'	
			path1 = os.path.join(path, filename)
			image = Image.open(path1)
			x = np.array(image)
			inputA.append(x)
			
			path = 	os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[2])
			filename = 'ext'+temp[2]+'_'
			if len(temp[3])==1:
				filename+='000'+temp[3]+'.jpg'
			elif len(temp[3])==2:
				filename+='00'+temp[3]+'.jpg'
			else:
				filename+='0'+temp[3]+'.jpg'	
			path2 = os.path.join(path, filename)
			image = Image.open(path2)
			x = np.array(image)
			inputB.append(x)

	inputA = np.array(inputA)
	inputB = np.array(inputB)
	length = len(y)
	y = np.array(y)
	y = np.reshape(y, (length,1))		
	return inputA, inputB, y		

if __name__ == '__main__':
	inputA, inputB, y = load_data(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\pairsDevTrain.txt')
	print(inputA.shape)
	print(inputB.shape)
	print(y.shape)

