# coding: utf-8

from game import jogar

def menu():
    while True:
        print('-- JOGO DA FORCA -- ')
        print('1 - Ver placar')
        print('2 - Jogar')
        print('3 - Sair')
        opcao = int(input(
            'Digite a opção selecionada:')
            )
        if opcao == 2:
            jogar()
        elif opcao == 3:
            break
        else:
            print('opcao invalida')

if __name__ == '__main__':
    menu()
