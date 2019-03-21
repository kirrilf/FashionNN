import cv2

im = cv2.imread("18.jpg")

print(im.shape)

x = im.shape[0]//2

u = im.shape[1]

print(x, u)

im = im[1:x]
#resized = cv2.resize(im, (int(x), int(u)), interpolation = cv2.INTER_AREA)

cv2.imshow("Cropped image", im)
cv2.waitKey(0)

'''
#resized = cv2.resize(im, (28, 72), interpolation = cv2.INTER_AREA)

#res1 = resized[11:39]
#[28:48]
 
cv2.imshow("Cropped image", res1)
cv2.waitKey(0)

res2 = resized[14:25]

'''