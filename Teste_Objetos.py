# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:07:03 2021

@author: rodrigo
"""


class Campo(object):
    def __init__(self,Objetos):
        self.Pessoas={}
        self.Opnioes={}
        
        for objeto in Objetos:
            self.Pessoas[objeto.name]=objeto
    
    def opniao(self,nome):
        if nome in self.Opnioes:
            Lista=self.Opnioes[nome]
            Lista.append(self.Pessoas[nome].falar())
            self.Opnioes[nome]=Lista
        else:
            self.Opnioes[nome]=[self.Pessoas[nome].falar()]
            
    def falar(self,nome,grava):
        self.Pessoas[nome].gravar(grava)

    
class Pessoa(object):
    def __init__(self,name):
        self.name=name
    def falar(self):
        a=input('Fale algo')
        return a
    def gravar(self,x):
        self.x=x

    
    
Takeshi=Pessoa('Takeshi')
Veri=Pessoa('Veri')

Campo1=Campo([Takeshi,Veri])
Campo2=Campo([Takeshi,Veri])

Campo1.opniao('Veri')

Campo1.falar('Takeshi','Now')
Campo2.falar('Takeshi','Agora')