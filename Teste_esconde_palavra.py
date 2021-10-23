# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:19:32 2021

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

arquivo = open('Lista_Teste.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
    
arquivo.close()
conteudo_lista=conteudo.split('\n')

lista_escondida=[]

for i in conteudo_lista:
    escondida,n=esconde_palavra(i)
    lista_escondida.append(escondida)
    print(f'{i} --> {escondida}')
