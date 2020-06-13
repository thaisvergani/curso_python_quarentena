class Jogador:
    """
    Criar um novo arquivo com a classe Jogador
    - a classe Jogador deve possuir um atributo para a pontuação 
         e um para o nome.
    - criar um método de classe para buscar todos os jogadores do arquivo
       e retornar uma lista de objetos do tipo Jogador.
    - criar um método de classe para buscar o jogador pelo nome 
        recebe por parâmetro a string do nome
        retorna um novo objeto do tipo jogador 
    """
   
    # jogadores = list()
    jogadores = []

    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
        type(self).jogadores.append(self)

    @classmethod
    def buscar_jogadores(cls, filename):            
        ''' metodo de classe para buscar todos os jogadores  
         do arquivo 
        '''
        try:
            with open(filename, 'rt') as file:
                data = file.read()
        except IOError:
            print('não foi possivel abrir o arquivo')

        jogadores = data.split('\n')
        for j in jogadores:
            nome, pontuacao = j.split('=')
            novo_j = Jogador(nome, int(pontuacao))

    @classmethod
    def buscar_jogador(cls, nome):
        for obj in cls.jogadores:
            if obj.nome == nome:
                return obj
    
