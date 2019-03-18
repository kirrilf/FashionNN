

import numpy as np
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("Clo1.jpg")

resized = cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA)

#print(resized)

#k = 0
s1 = []

for i in resized:
	s = []
	for j in i:
		s.append(j[0])
		s.append(j[1])
		s.append(j[2])

	s1.append(s)
	#s.clear()
	#tt = np.array(s)
	##np.column_stack((a, b))
	#print(s)
	#pritn(tt)

	#k+=1

gg = np.array(s1)
print(gg)


	