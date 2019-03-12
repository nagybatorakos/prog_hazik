import sys

def colors(args):
    L1=[]
    L2=[]
    k=0
    for i in args:
        if i=="L:":
            k+=1
            continue
        if k==1:
            L1.append(i)
        if k==2:
            L2.append(i)
    return L1, L2


# L1, L2 = colors(sys.argv[1:])
# for e in L1:
#     if e in L2:
#         L1.remove(e)
# print(L1)

def first_n(n, outfile):
    k=0
    s=""
    for i in range(1, n+1):
        k+=i
        s+= str(i)+"+"
    print(s[0:-1]+"="+str(k),file=outfile)



# n = int(sys.argv[1])
# outfile = open(sys.argv[2],'w')
# first_n(n,outfile)
# outfile.close()


def num_to_time(n, fout):
    day = n//(3600*24)
    n = n%(3600*24)
    hour = n//3600
    n = n%3600
    min = n//60
    sec = n%60
    print('{} day {} hours {} minutes and {} seconds'.format(day,hour,min,sec))

# n=int(sys.argv[1])
# fout=open(sys.argv[2], "w")
# num_to_time(n,fout)
# fout.close()


def l_counter(s, n):
    k=0
    for i in s:
        if i==n:
            k+=1
    return k

s=sys.argv[1]
n="a"
# print(l_counter(s,n))

def counter(u):
    n=0
    s=""
    k=0
    for i in u:
        if "0"<=i<="9":
            s+=i
            k=1
        else:
            if k==1:
                n+=int(s)
                k=0
                s=""
    return n

# print(counter(sys.argv[1]))
import numpy as np
def rand(n,s):
    s=int(s)
    k=np.random.randint(0, 100, s)
    n=open(sys.argv[1], "w")
    print(k, file=n)
    n.close()
    fin=open(sys.argv[1], "r")
    i=0
    return (np.sum(k))


# print(rand(sys.argv[1], sys.argv[2]))
import random
def rand_2(n,s):
    s=int(s)
    k=0
    for i in range(s):
        j=random.randint(1,101)
        k+=j
        print(j, file=n)
    return k

# n=open(sys.argv[1], "w")
# s=sys.argv[2]
# print(rand_2(n,s))
# n.close()
