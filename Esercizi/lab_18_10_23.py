# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:04:44 2023

@author: Leonardo
"""

def is_sorted(l):
    for c in range(0,len(l)-1):
        if l[c]>l[c+1] : return False
    return True

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.

def check_pwd(pwd: str) -> bool:
    l1,l2,l3,l4='','','',''
    
    if 6<len(pwd)<=16:
        for c in pwd:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                l1+=c
            elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                l2+=c
            elif c in '0123456789':
                l3+=c
            elif c in '$#@':
                l4+=c
            else: return False
        
        if l1!='' and l2!='' and l3!='' and l4!='':
            return True
        else: return False
    
    return False

# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    new_list=[]
    for c in a:
        if c in b : new_list.append(c) 
    return new_list


# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
   
    l=[]
    l2=[]
    for c in a:
        if c not in l2:
            if a.index(c)==len(a)-1:
                l.append((c,1))
                break
            cont=1
            l2.append(c)
            for b in a[a.index(c)+1:]:
                if b==c: cont+=1
            l.append((c,cont))
            
    return sorted(l,key=value)

def value(elem):
    return elem

















