import time

def ks(we,v,c):
    n = len(we)
    t = [[0 for _ in range(c+1)] for _ in range(n+1)]
    s1 = time.time()
    for i in range(1,n+1):
        for w in range(1,c+1):
            if we[i-1] <= w:
                t[i][w] = max(v[i-1]+t[i-1][w-we[i-1]],t[i-1][w])
            else:
                t[i][w] = t[i-1][w]
    s2 = time.time()
    ti = s2-s1
    print("table:")
    for i in t:
        print(i)
    i = n
    w = c
    items = []
    while i>0 and w>0:
        if t[i][w] != t[i-1][w]:
            items.append(i-1)
            w -= we[i-1]
        i-=1
    print("Max:",t[n][c])
    print("Items selected:", items)
    print("Time Taken:", ti)

w = [int(x) for x in input("Weights:").split()]
v = [int(x) for x in input("Values:").split()]
c = int(input("Capacity:"))
ks(w,v,c)
