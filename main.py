#INPUT 1 - RANDOM(NR,MAX*)  2 - LIST


from random import *
from copy import copy
from time import time
from math import log,sqrt
from sortari import *



########################## generator de numere ################
    

def generator(nr,maxim=1000000):
    l=[]
    for i in range(nr):
	    value=randint(0, maxim)
	    l.append(value)
    return l
    
    
############################# validare+timp ###################


def timp():
    t = time()
    t = round(t,2)
    return t

def Test(func,l):
    t = timp()
    m = func(l)
    t = round(timp()-t,2)
    if isinstance(m, str):
        return -1, -1
    if m==sorted(m):
        return 1, t
    else:
        return 0, t

##  -1 = Sortare inoptima
##  0 = Sortare incorecta
##  1 = Sortare corecta

############################## worst time ####################

def best(l):
    m=-1
    for i in l:
        if m==-1:
            m=i
        elif i<=m and i!=-1:
            m=i
    return m


############################# main ###########################

f=open("input.txt")
sortari=[bubblesort,countsort,radixsort,quicksort,mergesort]
f.readline()
n=int(f.readline())
timpi=[]
for i in range(n):
    timpi.append([0]*5)

for i in range(n):
    j=0
    m,M=f.readline().split()
    m,M=int(m),int(M)
    print("Testul numarul {} : {} numere cu maximul {}".format(i+1,m,M),end="\n-----------------------------------------------\n")
    l = generator(m,M)
    for sr in sortari:
        print(sr.__name__)
        v,t = Test(sr, l)
        timpi[i][j]=float(t)
        if v == 1:
            print("Sortare corecta")
            print("{} secunde".format(t))
        elif v==-1:
            print("Sortare inoptima")
        else:
            print("Sortare incorecta")
        print()
        j+=1
    w=max(timpi[i])
    b=best(timpi[i])
    print("Cel mai bun timp {}, cel mai slab timp {}\n".format(b,w))
print(timpi)

f.close()
