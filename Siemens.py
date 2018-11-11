import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# szürkeárnyalatos beolvasás
grey = cv2.imread('csillag.bmp',0)

# sarokpontok a transzformációhoz
p1 = np.float32([[253,207], [280,208], [259,358], [262,358]])
p2 = np.float32([[0,0], [20,0], [0,200], [20,200]])

#ezt kikommentelve a kiválaszott keret látszik
'''
p11 = np.array([[253,207], [280,208], [261,358], [259,358]], np.int32)
p1_=p11.reshape((-1, 1, 2))
grey_ = cv2.polylines(grey, [p1_], True, color=(255), thickness = 1)
plt.imshow(grey_)
plt.show()
'''
# transzformáció
M = cv2.getPerspectiveTransform(p1, p2)
szelet = cv2.warpPerspective(grey, M, (20, 200))

plt.imshow(szelet)
plt.show()

# kontraszt vizsgálat a képen végigsöpörve
kontraszt = []
y = []
kord = []
c = []
for i in range(200):
    kontraszt.append((np.max(szelet[i,:])-np.min(szelet[i,:]))/(np.max(szelet[i,:])+np.min(szelet[i,:])))
    # a perspektíva miatt nem lineáris ami a képen is jól látszik
    y.append(math.sqrt(i)/200)
    kord.append((kontraszt[-1], y[-1]))
    c.append(i)
    
# kapott értékek megjelenítése
plt.scatter(y, kontraszt, c = c)
plt.show()
