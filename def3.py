x = 5
def name():
    x = 333
    def name2():
        nonlocal x
        x = 100
        print(x)
    name2()
    print(x)
name()
print(x)