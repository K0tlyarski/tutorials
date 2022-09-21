import math
PI = math.pi

def Radius():
    n = float(input('Diametr: '))
    n /=2
    return n
def Height():
    m = float(input('Height: '))
    return m



def volume():
    r = Radius()
    h = Height()
    s = PI*r**2
    v = s*h
    return v
#print(volume())

def Mass(g):
    n = float(input('удельный вес : '))
    return g*n/1000
print('Весс: ', Mass(volume()))