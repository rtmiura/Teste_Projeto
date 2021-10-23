import random
from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    
def tratamento(palavra):    
    # print(conteudo_lista)
    palavra=palavra.upper().strip()
    palavra=remover_acentos(palavra)
    palavra=palavra.replace(' ','-')
    return palavra

lista_arquivos=['lista_palavras_paises.txt','lista_palavras_animais.txt','lista_palavras_frutas.txt']

palavras=[]
for arquivo in lista_arquivos:
    temp = open(arquivo, 'r', encoding="utf-8")
    conteudo = temp.read()    
    temp.close()
    conteudo_lista=conteudo.split('\n')
    palavras+=conteudo_lista
    
palavras_formatadas=[]
for palavra in palavras:
    palavras_formatadas.append(tratamento(palavra))

# dicionario_letras={}
# for palavra in palavras_formatadas:
#     for letra in palavra:
#         if letra in dicionario_letras:
#             dicionario_letras[letra]+=1
#         elif letra!='-':
#             dicionario_letras[letra]=1
            
# Letras=[*dicionario_letras.keys()]
# Letras.sort(key=lambda x:dicionario_letras[x],reverse=True)
# Vogais=['A','E','I','O','U']
# Vogais.sort(key=lambda x:dicionario_letras[x],reverse=True)
# Consoantes=[L for L in Letras if L not in Vogais]
# Consoantes.sort(key=lambda x:dicionario_letras[x],reverse=True)

lista_letras_jogadas=['A','N','G','U'] #externo
# palavra_secreta='*A***'
palavra_secreta='GUIANA'#externo

# lista_Tudo=['A','E','I','O','U','R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
# Letras_Descobertas={}
# lista_letras_jogadas_Erradas=[]



# Numero_letras=len(palavra_secreta)
# Numero_letras_escondidas=palavra_secreta.count('*')

# Palavras_Possiveis=[palavra for palavra in palavras_formatadas if len(palavra)==Numero_letras]





# ## Arrumando para excluir baseado nas letras abertas
# if len(Palavras_Possiveis)>1:
#     for i in range(len(palavra_secreta)):
#         if palavra_secreta[i]!='*' and i not in Letras_Descobertas:
#             Letras_Descobertas[i]=palavra_secreta[i]      
#             Palavras_Possiveis_Letra_Letra=[]
#             for palavra in Palavras_Possiveis:
#                 if palavra[i]==palavra_secreta[i]:
#                     Palavras_Possiveis_Letra_Letra.append(palavra)
#             try:              
#                 if len(Palavras_Possiveis_Letra_Letra)>0:
#                     Palavras_Possiveis=Palavras_Possiveis_Letra_Letra.copy()
#                     print(f'Reduzi minha busca para {len(Palavras_Possiveis)} palavras')
#             except:
#                 print('Não Reduziu as possibilidades')
                
# ## Arrumando para excluir baseado nas erradas            
# for letra in lista_letras_jogadas:
#     if letra not in lista_letras_jogadas_Erradas and letra not in Letras_Descobertas.values():
#         lista_letras_jogadas_Erradas.append(letra)

# palavras_a_remover=[]
# for letra in lista_letras_jogadas_Erradas:
#     for palavra in Palavras_Possiveis:
#         if letra in palavra:
#             if palavra not in palavras_a_remover:
#                 palavras_a_remover.append(palavra)
       
# for palavra in palavras_a_remover:
#     Palavras_Possiveis.remove(palavra)
# print(f'Reduzi minha busca para {len(Palavras_Possiveis)} palavras')

# ##  Definindo chute se ainda tiver mais de uma possibilidade     
# if len(Palavras_Possiveis)>=1:
#    dicionario_externo={}
#    for i in range(len(palavra_secreta)):
#        if Palavras_Possiveis[0][i] not in Letras_Descobertas.values():
#            dicionario_letras={}
#            for palavra in Palavras_Possiveis:
#                if palavra[i] in dicionario_letras:
#                    dicionario_letras[palavra[i]]+=1
#                elif palavra[i]!='-':
#                    dicionario_letras[palavra[i]]=1
                   
#            Letras=[*dicionario_letras.keys()]
#            Letras.sort(key=lambda x:dicionario_letras[x],reverse=True)
#            dicionario_externo[i]=[Letras[0],dicionario_letras[Letras[0]]]           
                
        
#    Pos_Externa=[*dicionario_externo.keys()]
#    Pos_Externa.sort(key=lambda x:dicionario_externo[x][1],reverse=True)
#    proxima_letra=dicionario_externo[Pos_Externa[0]][0]

# ##  Se deu ruim e não achou a palavra vamos para o desespero
# if len(Palavras_Possiveis)<1:
#     chute_desesperado=[]
#     for letra in lista_Tudo:
#         if letra not in lista_letras_jogadas:
#             chute_desesperado.append(letra)
#     proxima_letra =random.choice(chute_desesperado)  
    
    
class Jogador_Monstro(object):
    
    def __init__(self,nome):
        
        self.name=nome
        self.vitorias=0
        self.derrotas=0
        self.pontos=0
        self.lista_Tudo=['A','E','I','O','U','R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
        
        self.primeiro_filtro=True        
        self.Letras_Descobertas={}
        self.lista_letras_jogadas_Erradas=[]        
        self.lista_conhecimento()
        
    def lista_conhecimento(self):
        lista_arquivos=['lista_palavras_paises.txt','lista_palavras_animais.txt','lista_palavras_frutas.txt']

        palavras=[]
        for arquivo in lista_arquivos:
            temp = open(arquivo, 'r', encoding="utf-8")
            conteudo = temp.read()    
            temp.close()
            conteudo_lista=conteudo.split('\n')
            palavras+=conteudo_lista
            
        self.palavras_formatadas=[]
        for palavra in palavras:
            self.palavras_formatadas.append(tratamento(palavra))    
    
    def inicia_remocao_por_tamanho(self,palavra_secreta):
        self.Numero_letras=len(palavra_secreta)
        self.Palavras_Possiveis=[palavra for palavra in self.palavras_formatadas if len(palavra)==self.Numero_letras]
        print(f'Por tamanho da palavra, reduzi minha busca para {len(self.Palavras_Possiveis)} palavras')
        
    def tenta_nova_letra(self,lista_letras_jogadas,palavra_secreta):
        
        if self.primeiro_filtro:
            self.inicia_remocao_por_tamanho(palavra_secreta)
            self.primeiro_filtro=False            
            
        self.lista_letras_jogadas=lista_letras_jogadas
        self.palavra_secreta=palavra_secreta        
        self.Numero_letras_escondidas=self.palavra_secreta.count('*')
        
        
        
        ## Arrumando para excluir baseado nas letras abertas
        indice_correto=[]
        if len(self.Palavras_Possiveis)>=1:
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i]!='*' and i not in self.Letras_Descobertas:
                    self.Letras_Descobertas[i]=self.palavra_secreta[i]      
                    Palavras_Possiveis_Letra_Letra=[]
                    for palavra in self.Palavras_Possiveis:
                        if palavra[i]==self.palavra_secreta[i]:
                            Palavras_Possiveis_Letra_Letra.append(palavra)
                    try:              
                        if len(Palavras_Possiveis_Letra_Letra)>0:
                            self.Palavras_Possiveis=Palavras_Possiveis_Letra_Letra.copy()
                            print(f'Por comparaçao letra a letra reduzi minha busca para {len(self.Palavras_Possiveis)} palavras')
                    except:
                        print('Não Reduziu as possibilidades')
        
        para_retirar=[]
        for Letra_aberta in self.Letras_Descobertas.values():
            for palavra in self.Palavras_Possiveis:
                for i in range(len(palavra)):
                    if palavra[i]==Letra_aberta and self.palavra_secreta[i]=='*':
                        if palavra not in para_retirar:
                            para_retirar.append(palavra)
        
        for palavra in para_retirar:
            self.Palavras_Possiveis.remove(palavra)
            print(f'Com base nas letras certas nas posições erradas, reduzi minha busca para {len(self.Palavras_Possiveis)} palavras')
                                
        
                        
        ## Arrumando para excluir baseado nas erradas            
        for letra in self.lista_letras_jogadas:
            if letra not in  self.lista_letras_jogadas_Erradas and letra not in self.Letras_Descobertas.values():
                 self.lista_letras_jogadas_Erradas.append(letra)

        palavras_a_remover=[]
        for letra in  self.lista_letras_jogadas_Erradas:
            for palavra in self.Palavras_Possiveis:
                if letra in palavra:
                    if palavra not in palavras_a_remover:
                        palavras_a_remover.append(palavra)
       
        for palavra in palavras_a_remover:
            self.Palavras_Possiveis.remove(palavra)
        print(f'Com base nas letras erradas, reduzi minha busca para {len(self.Palavras_Possiveis)} palavras')
        
        ##  Definindo chute se ainda tiver mais de uma possibilidade     
        if len(self.Palavras_Possiveis)>=1:
           dicionario_externo={}
           for i in range(len(self.palavra_secreta)):
               if self.Palavras_Possiveis[0][i] not in self.Letras_Descobertas.values():
                   dicionario_letras={}
                   for palavra in self.Palavras_Possiveis:
                       if palavra[i] in dicionario_letras:
                           dicionario_letras[palavra[i]]+=1
                       elif palavra[i]!='-':
                           dicionario_letras[palavra[i]]=1
                           
                   Letras=[*dicionario_letras.keys()]
                   Letras.sort(key=lambda x:dicionario_letras[x],reverse=True)
                   dicionario_externo[i]=[Letras[0],dicionario_letras[Letras[0]]]           
                        
                
           Pos_Externa=[*dicionario_externo.keys()]
           Pos_Externa.sort(key=lambda x:dicionario_externo[x][1],reverse=True)
           self.proxima_letra=dicionario_externo[Pos_Externa[0]][0]
           
           
        ##  Se deu ruim e não achou a palavra vamos para o desespero
        elif len(self.Palavras_Possiveis)<1:
             chute_desesperado=[]
             for letra in self.lista_Tudo:
                 if letra not in self.lista_letras_jogadas:
                     chute_desesperado.append(letra)
             self.proxima_letra =random.choice(chute_desesperado)  
       
        return self.proxima_letra
    
    def reinicia_Robo(self):
        self.primeiro_filtro=True        
        self.Letras_Descobertas={}
        self.lista_letras_jogadas_Erradas=[]    
        


a=Jogador_Monstro('Teste')
Letra=a.tenta_nova_letra(lista_letras_jogadas,palavra_secreta)
print(Letra)
# a.reinicia_Robo()