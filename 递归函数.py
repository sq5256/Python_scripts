def f(x):
    y = x*x+x-6
    return y
a = float(input("请输入a："))
b = float(input("请输入b："))
global c
while True:
    c = (b+a)/2
    if f(a)*f(c) >0:
        a1 = c
    else:
        b = c
    if f(c) == 0 :
        break
print("方程的解在为: {}".format(c))
