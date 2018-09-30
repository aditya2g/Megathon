# Import the necessary packages
import numpy as np
import cv2
import glob,os

# Defining the range of RGB values for the water 
boundaries = [
	# ([150, 150, 120], [240, 240, 150])
	([150, 150, 120], [250, 225, 155])
]

# Opening the file to write
file_write = open("images.txt",'w+')

# Reading the files from the given directory
for f in (glob.glob(os.path.join('./*.png'))):
	image = cv2.imread(f)
	
	# Color Segmenting the image for finding water	
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# Running the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
		# Writing the test image for further computation
		cv2.imwrite('test.jpeg',output)

		# Reading the image and converting it to grayscale
		I1 = cv2.imread("test.jpeg",0)
		ret,thresh = cv2.threshold(I1,60,255,cv2.THRESH_BINARY)
		# Defining kernels for opening and closing enhancements
		kernel = np.ones((3,3),np.uint8)
		kernel1 = np.ones((150,150),np.uint8)
		opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
		closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel1)

		# grey_3_channel = cv2.cvtColor(closing, cv2.COLOR_GRAY2BGR)
		# Writing the image name to file if it contains water
		ans1 = np.sum(closing)/255
		if (ans1 > 1000):
			file_write.write(str(f) + '\n')

		# vertical = np.hstack((image,grey_3_channel))
		# cv2.imshow("images",vertical)
		# cv2.waitKey(0)
file_write.close()