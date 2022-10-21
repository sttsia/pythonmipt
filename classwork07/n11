def x(a):
    k = 0
    c = []
    a = list(map(lambda x: x ** 2, a))
    for i in range(len(a)):
        for x in a[i:]:
            k += x
            c.append((k/len(a[i:]))**0.5)
            k = 0
    return(c)