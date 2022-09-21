d1 = {'a':7}
d1['b'] = 9
d1['a'] = 67
del d1['a']
print(d1)
d1 = {'a':7, 'b':9, 'c': 89}
print(d1)
d5 = d1.copy()
print(d5)
print(d1.items())
print(d1.keys())
print(d1.values())
print(d1.get('c'))
print('---------------------')
d2 = dict(ff=77)
print(d2)
d1.update(d2)
print(d1)
t = d1.pop('a')
print(t)
print(d1)
print('---------------------')
d3 = dict.fromkeys([1,2,3,4,5],'value')
print(d3)
price = {'meat': 3, 'bread': 1, 'water': 0.2}
users = {'Alex': {'password': 12345, 'id': 222},
         'Bob': {'password': 5789, 'id': 4040}}

def buy():
    pay = 0
    while True:
        enter = input('что покупаем?\n ')
        if enter == 'end':
            break
        pay += price[enter]
    return pay

print(buy())

