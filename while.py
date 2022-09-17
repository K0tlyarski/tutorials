x = ''

while len(x)<5:
    y=input('vvod ')
    if y == 'o':
        continue
    if y == 'l':
        break
    x += y
else:
    print(x)
print('it work')