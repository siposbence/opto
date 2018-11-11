import cv2
import numpy as np
import matplotlib.pyplot as plt

#szurkeárnyalatos beolvasás
grey = cv2.imread('homog.bmp',0)
plt.imshow(grey)
plt.show()

# üres változó létrehozása a kapott eredmények tárolására
homog = np.zeros(shape=(9, 13))
plt.imshow(homog)
plt.show()

# hálózás és a téglalapok összegzése
for i in range(13):
    for j in range(9):
        tmp = cv2.rectangle(grey,(48+i*46,50+j*46),(74+i*46,70+j*46),(0,255,0),3)
        homog[j,i] = np.sum(grey[50+j*46:70+j*46, 48+i*46:74+i*46])

#eredmény megjelenítése
plt.imshow(homog)
plt.show()
print(homog)
