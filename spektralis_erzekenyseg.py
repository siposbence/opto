# szükséges könyvtárak
import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import csv

# a színek mappa bmp elemeinek beolvasása
kepek = glob.glob("szinek/*.bmp")
summa = []
print(kepek)
# a nevek sorba rendezése
kepek.sort()
print(kepek)
#képek beolvasása és szummázása
for file in kepek:
    img = cv2.imread(file, 0)
    summa.append(np.sum(img)/255)

# az eredmények megjelenítése
plt.plot(summa)
plt.show()
#print(kepek)


# kapott értékek csv-ba mentése
with open('erzekenyseg.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(kepek)
    wr.writerow(summa)
