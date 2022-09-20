x = (9, 8, 7, 6, 5, 99, 34,5)
y = []
# print(x)
# y = tuple("stroka")
# print(y)
# z, c, v,b = x
# print(z)
# print(c)
# print(v)
# print(b)
# print(x[2:4 ])
for i in range(len(x)):
   y.append(x[i]+3)
print(x)
print(y)

t= list(x)
t[0] = 10
x = tuple(t)
print(x)

print(x.count(5)) #cмотрит сколько цифр 5 в кортеже (одинаковых элементов)
print(x.index(8)) #выводит индекс элемента
h = (1, 2, 3)
h += (4, 5)
print(h )