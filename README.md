# Image-based-Face-Detection-and-Recognition
We used LFW dataset to train our model. Our model uses pretrained inception network to generate embeddings and MTCNN for face extraction. We are getting 96.5% accuracy on the dataset. 

For the gui application however we have used pretrained facenet network (to generate embeddings) from keras to get maximum accuracy, next we trained a network to check whether two embeddings are of same person or not.

The Face extraction file extracts faces from the dataset this may take around 1 hour but is a one time process. The utils function loads the data.

To get the model that performs classification use the below link. We are getting overall accuracy of 99% when using facenet + check model. 

Link for check model:
https://drive.google.com/file/d/1Y0WH3jUDJo1AMNw1PedqXFsXBP-EZUbg/view?usp=sharing

Dependencies:

Tensorflow
Keras
MTCNN (Face Extraction)
FaceNet (Generate Embeddings)
Opencv (To capture Images)
