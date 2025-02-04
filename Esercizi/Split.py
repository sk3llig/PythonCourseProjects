# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:34:52 2023

@author: Leonardo
"""

def split_string(string: str, characters: str = ''):
    l=[]
    c=0
    for i in range (len(string)):
        if string[i] == characters:
            l.append(string[c:i])
            c=i+1
        if i==len(string)-1:
            l.append(string[c:i+1])
    return l

print(split_string('leonardo',))