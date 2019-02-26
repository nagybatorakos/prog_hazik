#5

# def sorrend(n):
#     ls=n.split(",")
#
#
#
#     return sorted(ls)
#
#
# n=input()
# ls=[n]
# print(sorrend(n))

def lanc(szoveg, n):
    if len(szoveg)>2 and n>2:
        return szoveg[:n]
    else:
        return szoveg

str=input()
n=int(input())
print(lanc(str,n))

#push test
