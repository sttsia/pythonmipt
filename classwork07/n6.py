a=list(map(int, input().split()))
for i in range (-3, -len(a)-1):
    if abs(i)%2==0:
        print(a(i))
