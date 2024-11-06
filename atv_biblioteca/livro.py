from typing import Literal
from database import DB

class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, isbn: str, status: Literal['Disponível', 'Emprestado'] = 'Disponível') -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.status: Literal['Disponível', 'Emprestado'] = status
        self.id_usuario: int = None

    def __str__(self) -> str:
        return f'{self.titulo}, {self.autor}'


class GerenciarLivro:

    @staticmethod
    def novaInstanciaLivro(isbn: str) -> Livro:
        try:
            db = DB()
            query = """select titulo,autor,genero,isbn,status_livro from livro where isbn=%s"""

            db.exec(query, (isbn,))
            data = db.f_one()

            return Livro(titulo=data[0],autor=data[1], genero=data[2], isbn=data[3], status=data[4])
        except Exception as e:
            print(e)

    
    @staticmethod
    def adicionarLivro(titulo: str, autor: str, genero: str, isbn: str, status: Literal['Disponível', 'Emprestado'] = 'Disponível') -> bool:
        """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn ja existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""
        try:
            db = DB()
            db.exec('select id_livro from livro where isbn=%s', (isbn,))
            id, = db.f_one()

            if(not id):
                print(f'Livro com Isbn: {isbn}, já foi adicionado!')
                return False

            query = """
                insert into usuario
                    (titulo, autor, genero, status_livro, isbn)
                    values (%s,%s,%s,%s,%s)
                """

            db.exec(query=query, args=(titulo, autor, genero, status, isbn))
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(e)
    
    
    
    
    
    
    
    
    
    

    # def emprestarLivro(self, usuario):
    #     from usuario import Usuario
    #     usuario: Usuario = usuario
    #     try:
    #         db = DB()
    #         db.exec('select status_livro from livro where codigo=%s', (self.codigo,))
    #         status,  = db.f_one()
    #         print(status)

    #         if(status != 'Disponível'):
    #             return
            
    #     except Exception as e:
    #         print(e)

    #     if(self.status != 'Disponivel'):
    #         print('Livro já está emprestado!')
    #         return False
    #     self.status = 'Emprestado'
    #     self.usuario = usuario
    #     return True
    
    # def devolverLivro(self):
    #     if(self.status != 'Emprestado'):
    #         print('Livro não está emprestado!')
    #         return False
    #     self.status = 'Disponível'
    #     self.usuario = None
    #     return True

if __name__ == "__main__":
    db = DB()
    db.exec('select status_livro from livro where isbn=%s', ('003',))
    status, = db.f_one()
    print(GerenciarLivro.novaInstanciaLivro('006'))