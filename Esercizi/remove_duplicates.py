# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:51:25 2023

@author: Leonardo
"""

def remove_duplicates(elem):
    l=[]
    ld=[]
    for i in range(len(elem)):
        a=0
        if i < len(elem)-1:
            for c in range(i+1,len(elem)):
                if elem[i] == elem[c]:  
                    a+=1
                    ld.append(elem[i])
                    
        if a==0 and elem[i]  not in ld: l.append(elem[i])
        
    return l
        