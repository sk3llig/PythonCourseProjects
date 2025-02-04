#!/usr/bin/env python
# coding: utf-8

import builtins
if 'profile' not in dir(builtins):
    def profile(X) : return X


# CODICE OPIS ----> BSW4JAFJ
#Codice OPIS per il corso è: BSW4JAFJ Invito gli studenti a compilare il questionario OPIS 
#appena arriviamo a circa 2/3 del corso (circa terza settimana di Novembre)  
# ma forse è aperto già da ora. Il Vademecum per come compilare il questionario
# e' disponibile nel link allegato.
# https://www.uniroma1.it/sites/default/files/field_file_allegati/vademecum_per_studenti_opis_2022_23.pdf
    

# %% Iterable, Iteratori, Generatori
# %reset -f
L  = [1, 2, 3, 4]    # questo puo' anche essere un oggetto che punta ad un file
               # _io.TextIOWrapper Object o qualsiasi cosa che implementa un
               # iteratore/generatore
               
# %%% Spiegazione

## 1) Iterable (list, dict) L[] random access vs sequenziale
#__getitem__ che vi implementa indexing/slicing ossia L[i] (accesso "random")
#__iter__ che vi trasforma iterable  -> iterator

## 2) Iterator
#__iter__ vi ri-rende iteratore
# __next__ per ottenre il valore dopo (nota i valori si chiedono 
# una ad uno, 
#                                      accesso sequenziale) 
# se sbordate da iteratore, solleva errore di tipo Stop Iteration

## Generatori
# sono iteratori ma i dati NON sono tutti memorizzati
# I generatori sono PIGRI, vi rendono il dato solo quando lo volete
# sono piu efficienti in termini di complessità spazile (MEMORIA)
# usateli se avete da iterare UNA sola volta su un insieme GRANDISSIMO di dati
# i generatori si usano SOLO una volta

# 1. parola chiave yield
# 2. definita al volo con list comprehension style e parentesi ()

# %%% Iterable (il for trasforma L in iterator)
for item in L:
    print(item, end=' ')
    
# %%% Come iterare con iteratori/generatori

### ATTENZIONE: #####
# Questi concetti sono mostrati per FAR capire cosa 
# succede nel momento in cui iterate su un interatore
# ma ovviamente USATE CICLO for di norma

# Controlo se la classe lista L
# supporta iteratore
supporta = '__iter__' in dir(list)
print('Supporta gli iteratori!' if supporta else 'NON supporta')

# Ottengo iteratore
iter_L = iter(L)

# prendo il primo elemento
item = next(iter_L)
# lo stampo
print(item, end=' ')
# prendo il secondo elemento
item = next(iter_L)
# lo stampo
print(item, end=' ')

# %%% Controlliamo cosa accademo se prendo elemento che sborda
# vediamo cosa succede se prendo il terzo (che non esiste)
# prendo il TERZO elemento (NON esiste)

#item = next(iter_L)

# %%% Differenza fra Iteratori e Generatori

def genera_lista_pari(N):
    '''
    Torna una lista di numeri pari fino da 0 a N escluso
    '''
    L = []
    for i in range(0, N, 2):
        L.append(i)
    return L


def generator_pari(N):
    '''
    Torna una generatore di numeri pari fino da 0 a N escluso
    '''
    for i in range(0, N, 2):
        yield i
# %%    
pari = genera_lista_pari(10)
print(pari)
pari_gen = generator_pari(10)
#
# ha poco senso ri-trasformarlo SUBITO in una lista ma 
# e' per farvi capire. Se ci fate un ciclo
# for sopra i numeri sono generati via via che
# iterate
# se usate programmazione funzonale/iteratori
# usate list() solamente alla fine della computazione
#################################
# print(list(pari_gen))
#################################
# con list() lo ritrasformo in iterable
for count, i in enumerate(pari_gen):
    print(f'Stampo {i} ma rimane da generare {pari[count+1:]} ')

# %%% Generatore al volo

# somma i numeri da 0 a N compreso
N=100
numeri = (i for i in range(0,N+1)) # definisce un generatore al volo
print(sum(numeri))

# %%% Performance
@profile
def somma_N_gen(N):
    return sum(i for i in range(0,N+1))

@profile
def somma_N(N):
    somma = 0
    for i in range(0,N+1):
        somma += i
    return somma

N = 1000000
s = somma_N_gen(N)
ss = somma_N(N)
assert s == ss == N*(N+1)/2 #formula che Gauss scopri a 7 anni, tempo costante O(1)

# %% Map, Filter, Any/All
L = range(0,10)
# trasforma tutti al cubo
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
cubo_gen = map(lambda item: item**3, L)
# tieni solo i dispari
# [1, 27, 125, 343, 729]
tieni_dispari = filter(lambda item: item % 2 != 0, cubo_gen)
# controlla se esiste ALMENO UN multiplo di 5
div_by_five = map(lambda x : x % 5 == 0, tieni_dispari)
# [False, False, True, False, False]
print(any(div_by_five))
# controlla se TUTTI i numeri sono divisbile per 5
#all(div_by_five)

# %% JSON e request lib (not part of the exam but very interesting to know)

# usato per serializzare oggetti in python come file testuale
import json


files = {
    'files/holmes.txt'       : 'utf-8-sig', 
    'files/alice.txt'        : 'utf-8-sig', 
    'files/frankenstein.txt' : 'utf-8-sig', 
    'files/alice_it.txt'     : 'latin', 
    'files/prince.txt'       : 'utf-8-sig'
    }

scores = list(range(0,len(files)))
       
# %%       
## Salvo struttura python su disco
with open('serializzazione_oggetto.json', mode='wt') as fw:
    # salvo su file lista di dizionari
    json.dump([files,scores],fw, indent=2)

# %%
## La recupero da disco
with open('serializzazione_oggetto.json', mode='rt') as fr:
    # salvo su file lista di dizionari
    files_recoverd, score_recovered = json.load(fr)
    
    

# %% requests, per accedere alle pagine web

## esempio che apre una pagine a scarica tutte le immagini png
## Nota per farlo meglio vi e' XML tree che vi da albero dell' HTMl direttamente

import requests

table = str.maketrans(':-/','___')
URL =  'http://www.python.org'
response  = requests.get(URL)
text = response.text
for line in text.split('\n'):
    if '.png' in line:
        idx = line.find(".png")
        i = idx
        # blocco iterazione se arrivo ad inizio linea
        while i >= 0:
            i-=1
            # mi fermo non appena trovo aperta "
            if line[i] == '"':
                break
        # torno indietro e mi prendo URL PNG
        png_path = line[i+1:idx+4]
        # gestisco solo il caso di https (URL asssolute)
        # FIXME: gestire URL non assoulte (basta concat URL alla url relativa)  
        # NON gestisco ripetizioni
        print(f'> Found direct image, saving it {png_path}')
        file_path_write = 'data/'+png_path.translate(table)
        if png_path.startswith('http'):
            url_img = png_path
        else:
            url_img = URL + png_path
        req_img = requests.get(url_img)
        if req_img.ok:
            with open(file_path_write, mode='wb') as fw:
                    fw.write(req_img.content)
        else:
            print(f'*********\nFailed downloading {url_img}*********')