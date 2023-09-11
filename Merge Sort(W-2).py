import time
import random
import matplotlib.pyplot as plt
def ms(ls):
    if len(ls)>1:
        mid = len(ls)//2
        lt = ls[:mid]
        rt = ls[mid:]
        ms(lt)
        ms(rt)
        i=0
        j=0
        k=0
        while i<len(lt) and j < len(rt):
            if lt[i] <= rt[j]:
                ls[k] = lt[i]
                i+=1
            else:
                ls[k] = rt[j]
                j+=1
            k+=1
        while i<len(lt):
            ls[k] = lt[i]
            k+=1
            i+=1
        while j<len(rt):
            ls[k] = rt[j]
            k+=1
            j+=1
s1 = time.time()
x = []
y = []
m = int(input("Enter no.of test cases:"))
for _ in range(m):
    arr = []
    n = int(input("Enter no.of numbers:"))
    for _ in range(n):
        a = random.randrange(100)
        arr.append(a)
    print("Before Sorting:",arr)
    ms(arr)
    print("After Sorting:", arr)
    s2 = time.time()
    print("Time Taken:",s2-s1)
    y.append(s2-s1)
    x.append(n)

plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Merge Sort')
plt.show()

                
            
          
        
    
