t = int(input())
n=1
for i in range(t):
    a, b = (list(map(int, input().split())))
    print("Case #", n,":", a, "+", b, "=", a+b)
    n= n+1