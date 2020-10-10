import random

def flip():
    x = 100.0
    for i in range(7):
        result = random.randint(0,1)
        if result == 0:
            x += 1
        else:
            x = 1 / x 
    return x 

def simulate(a):
    s = 0
    for i in range(a):
        s += flip() / a 
    return s 


if __name__ == '__main__':
    print(simulate(1000000))

