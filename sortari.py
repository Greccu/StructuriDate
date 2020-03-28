from copy import copy
from math import log,sqrt
from random import choice


def bubblesort(l):
    if (len(l) >= 30000):
        return "inoptim"
    k = copy(l)
    ok = 1
    for i in range(1, len(k) - 1):
        ok = 0
        for j in range(len(k) - i):
            if (k[j] > k[j + 1]):
                ok = 1
                k[j], k[j + 1] = k[j + 1], k[j]
        if ok == 0:
            break
    return k


def cmmdc(l):
    if len(l)==0:
        return 0
    i = 0
    while i<len(l)-1 and l[i] == 0:
        i -= -1
    d = l[i]
    for i in range(1, len(l)):
        c = l[i]
        if c == 0:
            break
        while c != 0:
            if c >= d:
                c -= d
            else:
                d -= c
    return d


def countsort(l):
    if len(l) == 0:
        return l
    m = min(l)  # daca numerele nu pot fi aduse intr-un interval
    M = max(l)  # mai mic decat 10k, nu se vor sorta elementele
    if M - m >= 10000:
        return "inoptim"
    d = cmmdc(l)
    if d==0:
        return l
    m //= d
    k = copy(l)
    p = 0  # pentru a sti la final daca elementele au fost prelucrate
    if M // d - m // d < 1000:  # in acest caz optimizarea consuma timp inutil(cred)
        p = 1  #
        for i in range(len(k)):  # prelucrare lista
            k[i] = k[i] // d - m
        M -= m  # maximul listei prelucrate

    f = [0] * (M + 1)
    for i in k:
        f[i] += 1
    j = 0
    for i in range(M + 1):
        while f[i] > 0:
            k[j] = i
            j += 1
            f[i] -= 1
    if p == 1:
        for i in range(len(k)):
            k[i] = (k[i] + m) * d
    return k


def convert(k):
    K = []
    for values in k.values():
        for value in values:
            K.append(value)
    return K


def radixsort(l):
    if len(l)==0 or max(l)==0:
        return l
    L = copy(l)
    baza_radix = 256
    curent = 1
    k = {}
    n = (int(log(max(l), baza_radix)) + 1)
    for _ in range(n):
        for i in range(baza_radix):
            k[i] = []
        for i in L:
            k[(i // curent) % baza_radix].append(i)
        L = convert(k)
        curent *= baza_radix
    return L


def pivot(a,b,c):  # mediana a 3 numere random din lista
    if a > b:
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

def partition(l,st, dr):
    p = pivot(choice(l[st:dr + 1]), choice(l[st:dr + 1]), choice(l[st:dr + 1]))
    i = st - 1
    j = dr + 1
    while 1:
        i += 1
        while l[i] < p:
            i += 1
        j -= 1
        while l[j] > p:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
        else:
            return j

def qs(l,st,dr):
    if st < dr:
        p = partition(l,st, dr)
        qs(l, st, p)
        qs(l, p + 1, dr)


def quicksort(l):
    L=copy(l)
    qs(L,0,int(len(L)-1))
    return L


def merge(l1, l2):
    i = 0
    j = 0
    l3 = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    while i < len(l1):
        l3.append(l1[i])
        i += 1
    while j < len(l2):
        l3.append(l2[j])
        j += 1
    return l3


def mergesort(l):
    if len(l) <= 1:
        return l
    m = len(l) // 2
    l1 = l[:m]
    l2 = l[m:]
    k1 = mergesort(l1)
    k2 = mergesort(l2)
    k = merge(k1, k2)
    return k