# def x(a): return a+5


# print(x(5))

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(3)

print(mydoubler(11))
