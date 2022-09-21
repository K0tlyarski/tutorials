j = [9, 8 ,7 ,6]
def countlist(par, par2 = False, count = 0): #parametr
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count




print(countlist(j)) #argument
h = ['a', 'f', 'a']
print(countlist(h))
k = [9 ,4 ,5 ,2,3]
print(countlist(k, True))
print(countlist('stroka'))