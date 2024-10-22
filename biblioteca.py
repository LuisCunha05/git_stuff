class Usuario:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.ativo = True
        self.livros = []
        self.__max_emprestimo = 3

    def getMaxEmprestimo(self) -> int:
        return self.__max_emprestimo
    
    def adicionarLivro(self, titulo: str):
        if(titulo in self.livros):
            raise ValueError(f'O livro: {titulo} já está emprestado')
        
        if(len(self.livros) >= self.getMaxEmprestimo()):
            raise ValueError(f'O usuário já possui o máximo de livros emprestados!')

        self.livros.append(titulo)

        return self
    
class Livro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int, capa_dura: bool, quantidade: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.capa_dura = capa_dura
        self.__quantidade = quantidade

    def getQuantidade(self) -> int:
        return self.__quantidade
    
    def setQuantidade(self, quantidade: int):
        """Utilizado para adicionar ou remover livros. Quantidade pode ser negativo. Raises ValueError se o resultado de adicionar a quantidade resulta em um número negativo"""
        if(self.getQuantidade() + quantidade < 0):
            raise ValueError('Livro não pode ter uma quantidade negativa')

        self.__quantidade += quantidade
    
    def __str__(self) -> str:
        return f"""
            Título: {self.titulo},
            Autor: {self.autor},
            Número de páginas: {self.numero_paginas},
            Capa dura: {'Sim' if self.capa_dura else 'Não'},
            Quantidade disponivel: {self.__quantidade}
        """


class Livros:
    Acervo: list[Livro] = []

    def __init__(self) -> None:
        pass

    @staticmethod
    def cadastrar(livro: Livro):
        Livros.Acervo.append(livro)

    @staticmethod
    def listar():
        for idx, book in enumerate(Livros.Acervo):
            print(f'Livro {idx}: {book.titulo}')
    
    @staticmethod
    def getAtributos(index: int):
        print(Livros.Acervo[index])
    
    
