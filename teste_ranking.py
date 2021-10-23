# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:19:10 2021

@author: rodrigo
"""
import csv

def abrir_rank():   
    arquivo = open('ranking.csv', 'r', encoding = "utf-8")
    read_csv = csv.reader(arquivo, delimiter=',', lineterminator='\n')

    ranking = {}

    for line in read_csv:
        if len(line)>1:
            nome_jogador_rank = line[0]
            vitorias_jogador_rank = int(line[1])
            derrotas_jogador_rank = int(line[2])
            pontuacao_jogador_rank = int(line[3])
            ranking[nome_jogador_rank] = [vitorias_jogador_rank,derrotas_jogador_rank, pontuacao_jogador_rank]
    arquivo.close()
    return ranking   
 
def atualiza_rank(ranking,dic_jogadores):

    for jogador in dic_jogadores:
        if jogador in ranking:
            ranking[jogador][0] += dic_jogadores[jogador].retorna_n_vitorias()
            ranking[jogador][1] += dic_jogadores[jogador].retorna_n_derrotas()
            ranking[jogador][2] += dic_jogadores[jogador].retorna_pontos()
        else:
            lista_prov=[]
            lista_prov.append(dic_jogadores[jogador].retorna_n_vitorias())             
    
            lista_prov.append(dic_jogadores[jogador].retorna_n_derrotas())
            lista_prov.append(dic_jogadores[jogador].retorna_pontos())
            ranking[jogador] = lista_prov   
            
def reescreve_csv(ranking):
    ranking_lista=[]
    for key,lista in ranking.items():
        ranking_lista.append([key]+lista)
        
    arquivo = open('ranking.csv', 'w', encoding = "utf-8")
    csv.writer(arquivo, delimiter =',', lineterminator = '\n').writerows(ranking_lista)
    arquivo.close()

   



rank_historico=abrir_rank()
# atualiza_rank(rank_historico,dic_jogadores)
rank_historico['Rodrigo']=[1,0,10]
reescreve_csv(rank_historico)