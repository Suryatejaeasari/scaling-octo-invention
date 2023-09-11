import random
import time
import matplotlib.pyplot as plt
def qs(arr,low,high):
    if low<high:
        p = part(arr,low,high)
        qs(arr,low,p-1)
        qs(arr,p+1,high)
def part(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return i+1
s1 = time.time()
x=[]
y=[]
m = int(input("Enter no.of test cases:"))
for _ in range(m):
    arr = []
    n = int(input("Enter no.of numbers:"))
    for _ in range(n):
        a = random.randrange(100)
        arr.append(a)
    print("Before Sorting:",arr)
    qs(arr, 0, len(arr)-1)
    print("After Sorting:", arr)
    s2 = time.time()
    print("Time Taken:",s2-s1)
    y.append(s2-s1)
    x.append(n)

plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Quick Sort')
plt.show()
