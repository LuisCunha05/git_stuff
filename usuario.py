from livro import Livro
from database import DB

class Usuario:
    def __init__(self, nome: str, cpf: str, telefone:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.ativo = True
        self.livros: list[str] = []

        db = DB()

        db.exec('insert into usuario(nome,cpf,telefone) values (%s, %s, %s)', (self.nome, self.cpf, self.telefone))
        db.commit()

        db.exec('select id_usuario from usuario where cpf=%s', (self.cpf,))
        self.id,  = db.f_one()
        db.close()

    def emprestarLivro(self, livro:Livro) -> bool:
        if(livro.titulo in self.livros):
            print(f'O livro: {livro.titulo} já está emprestado')
            return False

        self.livros.append(livro.titulo)

        try:
            db = DB()
            db.exec('insert into emprestimo(id_usuario,id_livro,devolvido) values (%s, %s, %s)', (self.id, livro.id, 0))
            db.commit()
        except Exception as e:
            print(f'Erro ao conectar no banco de dados:\n{e}')

        return True
    
    def devolverLivro(self, titulo: str) -> bool:
        if(len(self.livros) == 0):
            print('O usuario não possui livros para devolver!')
            return False
        if(titulo not in self.livros):
            print('O usuário não possui este livro emprestado!')
            return False

        del self.livros[self.livros.index(titulo)]
        db = DB()
        db.exec()
        return True

if __name__ == "__main__":
    co = Usuario('Lalau', '123', '321')

