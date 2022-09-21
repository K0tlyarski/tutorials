import os
import time

spisok = []

for adress, dirs, files in os.walk('/Users/vadimkotlarskij/Desktop/practica'):
    for file in files:
        full = os.path.join(adress, file)
        if '.txt' in full:
            if time.time() - os.path.getctime(full) < 86400:
                spisok.append(full)




print(spisok)

