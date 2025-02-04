# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:46:05 2023

@author: Leonardo
"""

# Implementare una funzione *ricorsiva* che data una lista contenente valori
# e sottoliste, ritorna una lista contenente tutti i valori. Ad esempio:
# [1, [2, 3]] => [1, 2, 3] e [1, [2, [3, 4]]] => [1, 2, 3, 4]
def flatten_list(elements: list) -> list:
    l=[]
    
    for c in elements:
        
        if type(c)!=list:
            l.append(c)
        else:
            l+=(flatten_list(c))
    
    return l

print(flatten_list([1,2,[3,4,[7,8,[10,11,12,[13,14]]]]]))



# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: list[dict]) -> dict:
    di={}
    for diz in dictionaries:
        for k,v in diz.items():
            di[k]=v
    return di

dic={1:1,2:2}
dic2={3:3,4:4}
dic3={5:5,6:6,1:4}

print(update_dict([dic,dic2,dic3]))

# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: list[dict]) -> dict:
    di={}
    for diz in dictionaries:
        for k,v in diz.items():
            if k not in di.keys():
                di[k]=[v]
            else:
                di[k]+=[v]
            
                
    return di


print(intersect_dict([{"Ciao": 1, "Pippo": 2, "Pluto": 5}, {"Pippo": 3, "Pluto": 4}]))






