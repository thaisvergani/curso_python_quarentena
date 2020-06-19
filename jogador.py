import sys

class Jogador:

    jogadores = []

    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        type(self).jogadores.append(self)
        type(self).jogadores.sort(key=lambda obj: obj.nome)
        # have a key parameter to specify a function to be called 
        # on each list element prior to making comparisons.

    @classmethod
    def carregar_jogadores(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                linhas = file.read().splitlines()
            
            for linha in linhas:
                linha.replace(' ', '')
                if len(linha) > 0:
                    nome, pontuacao = linha.split('=')
                    jogador = Jogador(nome, int(pontuacao))

        except IOError as e:
            print('nao foi possivel abrir o arquivo')
            sys.exit(1)

    @classmethod
    def buscar_jogador(cls, nome):
        for obj in cls.jogadores:
            if obj.nome == nome:
                return obj
    
    @classmethod
    def salvar_jogadores(cls, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for jogador in cls.jogadores:
                    file.write(jogador.nome)
                    file.write('=')
                    file.write(str(jogador.pontuacao))
                    file.write('\n')
        except IOError as identifier:
            print('nao foi possivel escrever o arquivo')
            sys.exit(1)

    @classmethod
    def mostrar_pontuacao(cls):
        print('\n')
        
        for jogador in Jogador.jogadores:
            print("|{:<10} |{}|".format(jogador.nome, jogador.pontuacao))
    
        print('\n')
