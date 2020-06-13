import random

def buscar_palavras_do_arquivo(
        filename='forca_python.txt',
        debug=True) -> list:
    """
    recebe como parametro a localização do arquivo
    retorna uma lista com as palavras
    """

    try:
        with open(filename, 'rt') as file:
            data = file.read()
    except IOError:
        print('não foi possivel abrir o arquivo')

    a = data.split('\n')

    return a

def jogar():
    palavras = buscar_palavras_do_arquivo(filename='forca_python.txt')

    palavra = random.choice(palavras).upper()
    codificada = list('_' * len(palavra))

    tentativas = 0

    while True:
        letra = input('digite uma letra ').upper()

        if letra in palavra:

            for index, l in enumerate(palavra):

                if letra == l:
                    codificada[index] = letra

            print('A Palavra e: {p_codificada}'.format(
                p_codificada=' '.join(codificada)
            )
            )

            if ''.join(codificada) == palavra:
                print('Ganhou :)')
                break

        else:
            tentativas += 1
            print('Voce errou pela {} vez'.format(tentativas))

            if tentativas >= 6:
                print('Morreu')
                break
            
