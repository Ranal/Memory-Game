import random

a = []
b = [[2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]]

def randomize(b):
    for i in b:
        for j in i:
            a.append(j)
            random.shuffle(a)

    f = a[0:4]
    g = a[4:8]
    h = a[8:12]
    j = a[12:16]

    x = []
    x.append(f)
    x.append(g)
    x.append(h)
    x.append(j)
    return x



print(b)
print(randomize(b))

