# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:53:00 2021

@author: rodrigo

"""

from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def tratamento(palavra):    
    # print(conteudo_lista)
    palavra=palavra.upper().strip()
    palavra=remover_acentos(palavra)
    palavra=palavra.replace(' ','-')
    return palavra

def tratamento_letra(letra,Palavra_secreta):    
    if letra.upper()=='Ç':
        if not('Ç' in Palavra_secreta.upper()):
            return letra.upper().strip()
        else:
            # for 'Ç' in #Ideia Julia
            return tratamento(letra)
    else:
        return tratamento(letra)
    

letra=tratamento_letra('ç','cobiça')