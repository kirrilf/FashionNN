


import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

image = Image.open("17.jpg") #Открываем изображение. 
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



image.save("ans.jpg", "JPEG")
del draw