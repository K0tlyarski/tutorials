x = 'абвгдеежзийклмнопрстуфхцчшщ'
y = input('Vvdeite stroku \n')

for i in x:
    count = 0
    for r in y:
        if i == r:
            count+=1
    if count>0:

        print('Букв ',i ,' ', count)

k = 0
#range(start,stop,step)
for k in range(2,10,3):
    print(k)