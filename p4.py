def fun(p, t, r):
    return (p * t * r) / 100
p = int(input("Enter the first number:"))
t = int(input("Enter the second number:"))
r = int(input("Enter the third number:"))
res = fun(p, t, r)
print(res)