price = {'meat': 3, 'bread': 1, 'water': 0.2}
NewPrice = {}
for i in price.keys():
    NewPrice[i] = round(price[i] * 0.85, 2)
print(NewPrice)
print(price)
# new = {}
# for key,value in price.items():
#     new[value] = key
# print(new)
for value in price.values():
    print(value)