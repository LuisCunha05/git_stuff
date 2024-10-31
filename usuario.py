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
            print(f'O livro: {titulo} já está emprestado')
            return False
        
        if(len(self.livros) >= self.getMaxEmprestimo()):
            print(f'O usuário já possui o máximo de livros emprestados!')
            return False

        self.livros.append(titulo)
        return True
    
    def removerLivro(self, titulo: str) -> bool:
        if(len(self.livros) == 0):
            print('O usuario não possui livros para remover!')
            return False
        if(titulo not in self.livros):
            print('O usuário não possui este livro emprestado!')
            return False

        del self.livros[self.livros.index(titulo)]
        return True
