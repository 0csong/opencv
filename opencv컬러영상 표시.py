import cv2
from  matplotlib import pyplot as plt

img='./lenna.bmp' #./만하면 같은 파일에 있다는것을 나타낸다
imgBGR=cv2.imread(img) #파일을 imgBGR로 저장한다 opencv는 파일을 BGR로 저장
plt.axis('off')# x,y축을 표시하지않는다

imgRGB=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB) #파일을 RGB로 바꾼다 Matploblib은 RGB채널 순서로 처리하기 때문
plt.imshow(imgRGB)
plt.show() #window에 보이게한다
