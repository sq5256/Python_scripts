def f(n):
    if n==1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
n = int(input("请输入第n项："))
sum1 = 0
while n >= 1:
    sum1 = sum1 + f(n)
    n = n - 1
print(sum1)
