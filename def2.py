def ExclusiveItem(*args, key = False): #позиционные параметры пере аргс, ключевые параметры после аргс
    NewList = []
    for i in args:
        for y in i:
            if y not in NewList:
                NewList.append(y)
    if key == True:
        NewList.sort()

    return NewList

z = [9, 8 ,7, 6]
x = [8, 8, 9, 7 ,6 ,5]
c = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

t = ExclusiveItem(z,x,c, key = True)
print(t)