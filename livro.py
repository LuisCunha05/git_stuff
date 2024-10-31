from typing import Literal
from usuario import Usuario
from database import DB

class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, codigo: str,status: Literal['Disponível', 'Emprestado'] = 'Disponível') -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.status: Literal['Disponível', 'Emprestado'] = status
        self.usuario: Usuario = None

        try:
            db = DB()
            query = """
                insert into usuario
                    (titulo, autor, genero, status_livro, codigo)
                    values (%s,%s,%s,%s,%s)
                """
            db.exec(query=query, args=(titulo, autor,genero, status, codigo))
            db.commit()
            db.close()
        except Exception as e:
            print(e)

    def emprestarLivro(self, usuario: Usuario):
        try:
            db = DB()
            db.exec('select status_livro from livro where codigo=%s', (self.codigo,))
            status,  = db.f_one()
            print(status)

            if(status != 'Disponível'):
                return
            
            
        except Exception as e:
            print(e)

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
        self.status = 'Disponível'
        self.usuario = None
        return True
    
    def __str__(self) -> str:
        return f'{self.titulo}, {self.autor}'
    

if __name__ == "__main__":
    db = DB()
    db.exec('select status_livro from livro where codigo=%s', ('003',))
    status, = db.f_one()
    print(status)