m = [1, 2, 1, 3, 4, 'a', [1, 2, 3], [68, 77 ]]
print(m[3])
print(m[-1][1])
m[0]=33
print(m)
m[1] += 45
print(m)
m[6], m[7] = m[7] , m[6]
print(m)
m = m + [7]
print(m)
n = list('stroka')
print(n)

k = list(range(1, 21))
o = []
b = k.copy()
#срез это b = k[start:stop:step]
for i in k:
    if i % 2 == 0:
        o.append(i)
        k.remove(i)
print(o)
print(k)
print(b)

# x = [9, 8, 7, 6]
# print(x)
# x.append(45)
# print(x)
# x.insert(2, 9)
# print(x)
# print(x.count(9))
# x.sort()
# print(x)
# x.reverse()
# print(x)
# y = x.pop(1)
# print(y)
# print(x)
# x.remove(7)
# print(x)
#
# x.extend(['s', 'r'])
# print(x)
# h = x.copy()
# print(x)
# x.clear()