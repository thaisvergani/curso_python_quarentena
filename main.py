# coding: utf-8

from game import jogar
from jogador import Jogador

def menu():
    
    while True:
        print('-- JOGO DA FORCA -- ')
        print('1 - Ver placar')
        print('2 - Jogar')
        print('3 - Sair')
      
        opcao = int(input('Digite a opção selecionada:'))
      
        if opcao == 1:
            Jogador.mostrar_pontuacao()
        elif opcao == 2:
            jogar()
        elif opcao == 3:
            Jogador.salvar_jogadores('jogadores.txt')
            break
        else:
            print('opcao invalida')

if __name__ == '__main__':
    Jogador.carregar_jogadores('jogadores.txt')
    menu()
