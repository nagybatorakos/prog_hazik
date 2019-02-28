import string
#def longest_word("input.txt","output.txt"):
try:
    fin= open("input.txt", "r")
    fout= open("output.txt", "w")
    ls=[]
    k=0

    for i in fin:
        str=""
        for j in i:
            if j not in string.punctuation:
                str+=j
            words=str.split()
            for n in words:
                if len(n)>k:
                    ls.append(n)
                    k=len(n)
                elif len(n)== k:
                    ls.append(n)


    print("hossz: {k}", file=fout)
    for i in ls:
        print(i, file=fout)
    fin.close()
    fout.close()
except FileNotFoundError:
    print("nem talalhato fajl")

# valami nemjo

