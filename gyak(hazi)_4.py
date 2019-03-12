import numpy as np

def inverseVector(a):
    b = np.array(a[a.size-1])
    for i in range(a.size-2,-1,-1):
        b = np.append(b,a[i])
    return b

# a = np.arange(10,50)
# b = inverseVector(a)
# print(a)
# print(b)

import math
def maxv(n):
    k=-math.inf
    h=math.inf
    s=-1
    for i in range(n.size):
        s+=1
        if n[i]>k:
            k=n[i]
            ki=i
        if h>n[i]:
            h=n[i]
            hi=i
    return k, h, ki, hi

n=np.array(np.ceil(100*np.random.random(30)),dtype='uint8')
k, h, ki, hi= maxv(n)
# print(n)
# print("max: {}, {}-edik helyen ; min: {}, {}-edik helyen".format(k, ki, h, hi))

def maxv_2(n):
    idx=np.where((n==n.max()) | (n==n.min()))
    return n.max(), n.min(), idx

n=np.array(np.ceil(100*np.random.random(30)),dtype='uint8')
# print(maxv_2(n))

def rep(n):
    k=-math.inf
    ki=0
    for i in range(n.size):
        if n[i]>k:
            k=n[i]
            ki=i
    print(n)
    n[ki]=-1
    return n
n=np.array(np.ceil(100*np.random.random(30)),dtype='uint8')
n[n==n.max()]=-1
# print(n)
# print(rep(n))



d =np.array(np.random.randint(1,20,20))

d[d==d.max()]=-1

# print(d)

def sort(v):
    n = v.size
    for i in range(0,n):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i],v[j] = v[j],v[i]
    return v



n=np.array(np.random.randint(1,20,20))
n[(n>3) & (n<8)]=-n[(n>3) & (n<8)]
print((n))
