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

k = list(range(10))
o = []
for i in k:
    if i == 8:
        continue
    o += [i]
print(o)
print(k)