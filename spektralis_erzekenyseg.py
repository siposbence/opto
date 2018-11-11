# szükséges könyvtárak
import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import csv

# a színek mappa bmp elemeinek beolvasása
kepek = glob.glob("szinek/*.bmp")
summa = []
summa_b = []
summa_g = []
summa_r = []
print(kepek)
# a nevek sorba rendezése
kepek.sort()
print(kepek)
#képek beolvasása és szummázása
for file in kepek:
    img = cv2.imread(file, 0)
    summa.append(np.sum(img)/255)
    summa_b.append(np.sum(img[:,:,0])/255)
    summa_g.append(np.sum(img[:,:,1])/255)
    summa_r.append(np.sum(img[:,:,2])/255)

# az eredmények megjelenítése
plt.plot(summa)
plt.show()
plt.plot(x, summa_b/np.max(summa_b))
plt.show()
plt.plot(x, summa_g/np.max(summa_g))
plt.show()
plt.plot(x, summa_r/np.max(summa_r))
plt.show()
#print(kepek)


# kapott értékek csv-ba mentése
with open('erzekenyseg.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(kepek)
    wr.writerow(summa)
