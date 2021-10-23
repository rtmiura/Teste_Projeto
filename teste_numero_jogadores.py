def Numero(Jogadores):
    try:
        N=input('Quantos jogadores irão jogar nesta rodada? ')
        assert type(N) == int
        return N
    except:
        print('Digite um número válido para definir a quantidade de jogadores')
        return Numero()

a=Numero()