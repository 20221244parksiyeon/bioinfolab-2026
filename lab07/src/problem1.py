
def f(x):
    print(x * 2)

def g(x):
    return x * 2

a = f(3)
b = g(3)
print(a, b)
print(g(g(3)))
print(f(f(3)))
