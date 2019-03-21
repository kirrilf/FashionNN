


import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 
import cv2

import TestFashion as TF


image = Image.open("21.jpg") #Открываем изображение.

draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.




for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = a + b + c
		if (S > (((255 + 100) // 2) * 3)):
			a, b, c = 255, 255, 255
		else:
			a, b, c = 0, 0, 0
		draw.point((i, j), (a, b, c))

'''
k = 0
S = 0
for i in range(20, width-20):
	for j in range(30, height-10):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		s = (a + b + c)//3
	S+=s
	k+=1

print(S//k)
'''


'''

for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = (a + b + c) // 3
		draw.point((i, j), (S, S, S))
'''


image.save("ans.jpg", "JPEG")
del draw


im = cv2.imread("ans.jpg")

#x = (im.shape[0]//2)-20

#im = im[x:im.shape[0]-50]

#im = im[20:x]


#cv2.imshow("Cropped image", im)
#cv2.waitKey(0)


resized = cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA)







s1 = []

for i in resized:
	s = []
	
	for j in i:
		#k = (j[0]+j[1]+j[2])/3
		s.append(255-j[1])

	s1.append(s)
	




print(TF.st(s1))

