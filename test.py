import math

def f(x):
    return x**2 - 10 * math.log10(x) - 3

a = 2
b = 3
epsilon = 0.000001

if f(a) * f(b) >= 0:
    print("The given interval does not contain a root.")
else:
    print("n  an        bn        xn+1      f(an)     f(bn)     f(xn+1)")
    n = 0
    while abs(b - a) >= epsilon:
        x = (a + b) / 2
        print(f"{n}  {a:.6f}   {b:.6f}   {x:.6f}   {f(a):.6f}   {f(b):.6f}   {f(x):.6f}")
        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        n += 1
    print(f"The root is {x:.6f} and it took {n} iterations to converge.")
