# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:03:19 2021

@author: rodrigo
"""

def somaTudo(lista):
    print(type(lista))               
    if type(lista)==int:
        return lista
    else:
        if len(lista)==1:
            return somaTudo(lista[0])
        elif len(lista)==2:
            return somaTudo(lista[0]) + somaTudo(lista[-1])
        else:
            return somaTudo(lista[0]) + somaTudo(lista[1:])
    
# listaGabarito = [[0, 3, 5, 1], 2, 3, [2, [5, 6, 7, [1, 4, 6]], 3], 2, [3, 5, 10, [6]]]
listaGabarito = [1,[1,2],1,[2]]
print(somaTudo(listaGabarito))