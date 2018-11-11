import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# a nevű mappából beolvasás
kepek = glob.glob("a/*.bmp")
pixelek = []
print(kepek)
kepek.sort()
print(kepek)

# komment jelek kiszedésével az eredményt láthatjuk 
# a beállított határ a maximális pixelérték 0.4-szerese
for file in kepek:
    img = cv2.imread(file, 0)
    print(np.max(img))
    _, th = cv2.threshold(img, np.max(img)*0.4, 255, cv2.THRESH_BINARY)
    #print(th)
    #cv2.imshow("th",th)
    tmp = np.zeros(shape=(100, 130))
    tmp = th[200:400,250:380]
    #plt.imshow(tmp)
    #plt.show()
    szama = np.sum(tmp)
    print(szama)
    pixelek.append(szama/255)

plt.plot(pixelek)
plt.show()
