from usuario import Usuario
from database import DB

class ControllerUsuario:

    @staticmethod
    def getIdUsuario(database: DB ,usuario: Usuario | str):
        """Retorna o id do livro caso exista, Raises ValueError se livro não exister no banco de dados"""

        if(isinstance(usuario, Usuario)):
            database.exec(usuario.getIdUsuario(), (usuario.cpf,))
        elif(type(usuario) == str):
            database.exec('select id_usuario from usuario where cpf=%s', (usuario,))
        else:
            raise TypeError('Usuario não corresponde a um tipo válido')

        id_livro = database.f_one()

        if(not id_livro):
            raise ValueError('Livro inexistente')

        id_livro = id_livro[0]
        return id_livro