#INPUT 1 - RANDOM(NR,MAX*)  2 - LIST


from random import *
from copy import copy
from time import time
from math import log,sqrt



############################# sortari ########################


def bubblesort(l):
    if(len(l)>=30000):
        return "Algoritm inoptim, nu se va executa sortarea"
    k=copy(l)
    ok=1
    for i in range(1,len(k)-1):
        ok=0
        for j in range(len(k)-i):           
            if(k[j]>k[j+1]):
                ok=1
                k[j],k[j+1]=k[j+1],k[j]
        if ok==0:
            break
    return k

def cmmdc(l):
    i=0
    while l[i]==0:
        i-=-1
    d=l[i]
    for i in range(1,len(l)):
        c=l[i]
        if c == 0:
            break
        while c != 0: 
            if c>=d:
                c-=d
            else:
                d-=c
    return d

def countsort(l):
    if len(l)==0:
        return l
    d=cmmdc(l)
    m=min(l)    # daca numerele nu pot fi aduse intr-un interval
    M=max(l)    # mai mic decat 1mil, nu se vor sorta elementele 
    if M//d-m//d>=100000:
        return "Algoritm inoptim, nu se va executa sortarea"
    m//=d
    k=copy(l)
    p=0     #pentru a sti la final daca elementele au fost prelucrate
    if M//d-m//d<1000:     # in acest caz optimizarea consuma timp inutil(cred)
        p=1                     #
        for i in range(len(k)):     # prelucrare lista
            k[i]=k[i]//d-m
        M-=m    # maximul listei prelucrate
        
    f=[0]*(M+1)
    for i in k:
        f[i]+=1
    j=0
    for i in range(M+1):
        while f[i]>0:
            k[j]=i
            j+=1 
            f[i]-=1
    if p==1:
        for i in range(len(k)):
            k[i]=(k[i]+m)*d
    return k

def convert(k):
    K=[]
    for values in k.values():
        for value in values:
            K.append(value)
    return K
    

def radixsort(l):
    L=copy(l)
    baza_radix=256
    curent=1
    k={}
    n=(int(log(max(l),baza_radix)) + 1)
    for _ in range(n):
        for i in range(baza_radix):
            k[i]=[]
        for i in L:
            k[(i//curent)%baza_radix].append(i)
        L=convert(k)
        curent*=baza_radix
    return L

def pivot(l):                           #mediana a 3 numere random din lista
    a,b,c=choice(l),choice(l),choice(l)
    if a>b:
	    if a < c:
	        return a
	    elif b > c:
	        return b
	    else:
	        return c
    else:
	    if a > c:
	        return a
	    elif b < c:
	        return b
	    else:
	        return c


def quicksort(l):
    p=pivot(l)
    low=[]
    high=[]
    return l
    
def merge(l1,l2):
    i=0
    j=0
    l3=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    while i < len(l1): 
            l3.append(l1[i])
            i+=1
    while j < len(l2): 
            l3.append(l2[j])
            j+=1
    return l3
    
def mergesort(l):
    if len(l)<=1:
        return l
    m=len(l)//2
    l1=l[:m]
    l2=l[m:]
    k1=mergesort(l1)
    k2=mergesort(l2)
    k=merge(k1,k2)
    return k
    

def generator(nr,maxim=1000000):
    l=[]
    for i in range(nr):
	    value=randint(0, maxim)
	    l.append(value)
    return l
    
    
############################# validare+timp ###################


def timp():
    t = time()
    format(float(t), '.2f')
    t = float(t)
    return t

def Test(func,l):
    t = timp()
    m = func(l)
    t = timp()-t
    if isinstance(m, str):
        return -1, -1
    if m==sorted(m):
        return 1, t
    else:
        return 0, t

############################# teste ##########################

##  -1 = Sortare inoptima
##  0 = Sortare incorecta
##  1 = Sortare corecta

def Test1_lista_data():
    global f
    l = f.readline().split()
    l = [int(i) for i in l]
    return l

def Test2_lista_generata():
    global f
    z = f.readline()
    x, y = z.split()
    x, y = int(x), int(y)
    print("Generare numere...")
    print()
    l = generator(x, y)
    return l

def Test3_lista_crescatoare():
    maxim = 10000
    l = [i for i in range(1,maxim+1)]
    return l

def Test4_lista_descrescatoare():
    maxim = 10000
    l = [maxim-i for i in range(maxim)]
    return l

def Test5_same_number():
    nr = 1
    maxim = 10000
    l = [nr for _ in range(maxim)]
    return l

def Test6_lista_vida():
    l = []
    return l

def Test7_putine_nr_mari():
    nr = 500
    max = 100000
    l = generator(nr,max)
    return l

def Test8_multe_nr_mici():
    nr = 100000
    max = 100
    l = generator(nr,max)
    return l

############################# main ###########################

f=open("input.txt")
sortari=[bubblesort,countsort,radixsort,quicksort,mergesort]
teste=[Test1_lista_data, Test2_lista_generata, Test3_lista_crescatoare, Test4_lista_descrescatoare, Test5_same_number, Test6_lista_vida, Test7_putine_nr_mari, Test8_multe_nr_mici]
timpi=[]
for i in range(len(teste)):
    timpi.append([0]*len(sortari))
    

i=0
for test in teste:
    print(test.__name__,end="\n-----------------------------------------------\n")
    j=0
    l = test()
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
    i+=1
print(timpi)

f.close()
