# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:21:33 2021

@author: rodrigo
"""


def esconde_palavra(palavra):
    lista_nova_palavra=[]
    contador=0
    for letra in palavra:
        if letra.isalpha():
            lista_nova_palavra.append('*')
            contador+=1
        else:
            lista_nova_palavra.append(letra)
    nova_palavra=''.join(lista_nova_palavra)
    return nova_palavra, contador

palavra='onça-pintada'

nova_palavra,numero_letras=esconde_palavra(palavra)