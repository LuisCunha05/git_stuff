from typing import Literal
from __future__ import annotations

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
    
class Livro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int, codigo: str,status: Literal['Disponivel', 'Emprestado'] = 'Disponivel') -> None:
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.codigo = codigo
        self.status: Literal['Disponivel', 'Emprestado'] = status
        self.usuario: Usuario = None

    def emprestarLivro(self, usuario: Usuario):
        if(self.status != 'Disponivel'):
            print('Livro já está emprestado!')
            return False
        self.status = 'Emprestado'
        self.usuario = usuario
        return True
    
    def devolverLivro(self):
        if(self.status != 'Emprestado'):
            print('Livro não está emprestado!')
            return False
        self.status = 'Disponivel'
        self.usuario = None
        return True
    
    def __str__(self) -> str:
        return f'{self.titulo}, {self.autor}'


class Biblioteca:
    Acervo: list[Livro] = []

    def cadastrar(self, livro: Livro) -> bool:
        if(livro in self.Acervo):
            print("Livro já está cadastrado!")
            return False
            

        self.Acervo.append(livro)

    def listar(self):
        for idx, book in enumerate(self.Acervo):
            print(f'Livro {idx}: {book}')
    
    def getAtributos(self, index: int):
        livro = self.Acervo[index]

        return f"""
            {livro.titulo},
            {livro.autor},
            {livro.status},
            {livro.codigo},
            {livro.usuario}
        """
    
    def fazerEmprestimo(self, usuario: Usuario, livro: Livro) -> bool:
        if(len(usuario.livros) == usuario.getMaxEmprestimo()):
            print('O usuário já atingiu o maximo de emprestimos')
            return False
        
        if(livro.status != 'Disponivel'):
            print('O livro não pode ser emprestado!')
            return False
        
        usuario.adicionarLivro(livro.titulo)
        livro.emprestarLivro(usuario)

    def fazerDevolucao(self, usuario: Usuario, livro: Livro) -> bool:
        if(len(usuario.livros) == 0):
            print('O usuário não possui livros para devolver')
            return False
        
        if(livro.status != 'Emprestado'):
            print('O livro não está emprestado!')
            return False
        
        usuario.adicionarLivro(livro)
        livro.devolverLivro()
