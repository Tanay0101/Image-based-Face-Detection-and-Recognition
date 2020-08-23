import numpy as np
from PIL import Image
import os
import cv2
from mtcnn import MTCNN
from tqdm import tqdm


def ext_face(path, impath, filename):
	detector = MTCNN()
	src = cv2.imread(impath)
	image = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
	result = detector.detect_faces(image)
	os.chdir(path)
	if(len(result)==1):            
		x1, y1, width, height = result[0]['box']
		x2, y2 = x1 + width, y1 + height
		face_boundary = image[y1:y2, x1:x2]
		face_image = cv2.resize(face_boundary, (224,224))    
		cv2.imwrite("ext"+filename, cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR))
	else:
		image = cv2.resize(image, (224,224))                
		cv2.imwrite("ext"+filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))     

def extract_data(source):

	with open(source) as file:
		data = file.readlines()

	for line in tqdm(data):
        
		temp = line.split()
		if len(temp)==3:
			path = os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[0])
			
			filename = temp[0]+'_'
			if len(temp[1])==1:
				filename+='000'+temp[1]+'.jpg'
			elif len(temp[1])==2:
				filename+='00'+temp[1]+'.jpg'
			else:
				filename+='0'+temp[1]+'.jpg'
			path1 = os.path.join(path, filename)
			ext_face(path, path1, filename)
			
			filename = temp[0]+'_'
			if len(temp[2])==1:
				filename+='000'+temp[2]+'.jpg'
			elif len(temp[2])==2:
				filename+='00'+temp[2]+'.jpg'
			else:
				filename+='0'+temp[2]+'.jpg'
			path2 = os.path.join(path, filename)
			ext_face(path, path2, filename)                
		
		else:
			path = 	os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[0])
			filename = temp[0]+'_'
			if len(temp[1])==1:
				filename+='000'+temp[1]+'.jpg'
			elif len(temp[1])==2:
				filename+='00'+temp[1]+'.jpg'
			else:
				filename+='0'+temp[1]+'.jpg'	
			path1 = os.path.join(path, filename)
			ext_face(path, path1, filename) 
			
			path = 	os.path.join(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\lfw_funneled',temp[2])
			filename = temp[2]+'_'
			if len(temp[3])==1:
				filename+='000'+temp[3]+'.jpg'
			elif len(temp[3])==2:
				filename+='00'+temp[3]+'.jpg'
			else:
				filename+='0'+temp[3]+'.jpg'	
			path2 = os.path.join(path, filename)
			ext_face(path, path2, filename)


if __name__ == '__main__':
	extract_data(r'C:\Users\Dev\Desktop\Ongoing_projects\Face_Recognition\Data\pairsDevTrain.txt')





