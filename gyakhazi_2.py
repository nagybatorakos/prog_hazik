import string
#def longest_word("input.txt","output.txt"):
# try:
#     fin= open("input.txt", "r")
#     fout= open("output.txt", "w")
#     ls=[]
#     k=0
#
#     for i in fin:
#         str=""
#         for j in i:
#             if j not in string.punctuation:
#                 str+=j
#             words=str.split()
#             for n in words:
#                 if len(n)>k:
#                     ls.append(n)
#                     k=len(n)
#                 elif len(n)== k:
#                     ls.append(n)
#
#
#     print("hossz: {k}", file=fout)
#     for i in ls:
#         print(i, file=fout)
#     fin.close()
#     fout.close()
# except FileNotFoundError:
#     print("nem talalhato fajl")

# valami nemjo

def Longest(c,h):
    ls=[]
    k=0

    for i in c:
        str=""
        for j in i:
            if j not in string.punctuation:
                str+=j
            words=str.split()
            for n in words:
                if len(n)>k:
                    # ls.append(n)
                    k=len(n)
                # elif len(n)== k:
                #     ls.append(n)
            for b in words:
                if len(b)== k:
                    ls.append(b)

    return k, ls


try:
    be= open("input.txt", "r")
    ki= open("output.txt", "w")
    print(Longest(be, ki), file=ki)


    be.close()
    ki.close()

except FileNotFoundError:
    print("nem talalhato fajl")
