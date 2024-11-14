from database import DB

class Livro:
    def __init__(self) -> None:
        self._titulo: str = ''
        self._autor: str = ''
        self._genero: str = ''
        self._isbn: str = ''
        self._status: int = None #1:disponivel,2-emprestado,3-extraviado,4-danificado

    def setTitulo(self, titulo: str):
        if(type(titulo) != str):
            raise TypeError('Tipo esperado: str')
        if(titulo == ''):
            raise ValueError('Valor não pode ser vazio')

        self._titulo = titulo

    def setAutor(self, autor: str):
        if(type(autor) != str):
            raise TypeError('Tipo esperado: str')
        if(autor == ''):
            raise ValueError('Valor não pode ser vazio')

        self._autor = autor

    def setGenero(self, genero: str):
        if(type(genero) != str):
            raise TypeError('Tipo esperado: str')
        if(genero == ''):
            raise ValueError('Valor não pode ser vazio')

        self._genero = genero

    def setIsbn(self, isbn: str):
        if(type(isbn) != str):
            raise TypeError('Tipo esperado: str')
        if(isbn == ''):
            raise ValueError('Valor não pode ser vazio')

        self._isbn = isbn

    def setStatus(self, status: int = 1):
        """Status do livro são: 1:disponivel, 2:emprestado, 3:extraviado, 4:danificado"""
        if(type(status) != int):
            raise TypeError('Tipo esperado: int')
        if(status < 1 or status > 4):
            raise ValueError('Valor precisa ser [1,4]')

        self._status = status

    def getTitulo(self) -> str:
        return self._titulo

    def getAutor(self) -> str:
        return self._autor

    def getGenero(self) -> str:
        return self._genero

    def getIsbn(self) -> str:
        return self._isbn

    def getStatus(self) -> int:
        return self._status

    def getAsDb(self) -> tuple:
        return (self._titulo, self._autor, self._genero, self._isbn, self._status)

    def createQuery(self) -> str:
        return """
                insert into livro
                    (titulo, autor, genero, isbn, status_livro)
                    values (%s,%s,%s,%s,%s)
                """
    
    def deleteQuery(self) -> str:
        return 'delete from livro where isbn=%s'

    def getIdLivroQuery(self) -> str:
        return 'select id_livro from livro where isbn=%s'
    
    def setEmprestadoQuery(self) -> str:
        return 'update livro set status_livro=2 where isbn=%s'
    
    def alterLivroQuery(self, titulo: bool | None = False, autor: bool | None = False, genero: bool | None = False, status: bool | None = False) -> str:
        """
        Gera o query para alterar os dados selecionados pelos argumentos verdadeiros no método.
        Example:
            update livro set titulo=%s,autor=%s,genero=%s,status_livro=%s where isbn=%s
        """

        query = 'update livro set '
        columns = []

        if(titulo):
            columns.append('titulo=%s')
        if(autor):
            columns.append('autor=%s')
        if(genero):
            columns.append('genero=%s')
        if(status):
            columns.append('status_livro=%s')
        
        query += ','.join(columns) + ' where isbn=%s'

        return query

    def __str__(self) -> str:
        return f'{self._titulo}, {self._autor}'

    def __iter__(self):
        return iter((self._titulo, self._autor, self._genero, self._isbn, self._status))

class LivroBuilder:
    def __init__(self) -> None:
        self._livro = Livro()

    def addTitulo(self, titulo: str):
        self._livro.setTitulo(titulo)
        return self

    def addAutor(self, autor: str):
        self._livro.setAutor(autor)
        return self

    def addGenero(self, genero: str):
        self._livro.setGenero(genero)
        return self

    def addIsbn(self, isbn: str):
        self._livro.setIsbn(isbn)
        return self

    def addStatus(self, status: int = 1):
        self._livro.setStatus(status)
        return self

    def build(self):
        if(self._livro.getTitulo() == ''):
            raise ValueError(f'O atributo Titulo não pode ser vazio')
        if(self._livro.getAutor() == ''):
            raise ValueError(f'O atributo Autor não pode ser vazio')
        if(self._livro.getGenero() == ''):
            raise ValueError(f'O atributo Genero não pode ser vazio')
        if(self._livro.getIsbn() == ''):
            raise ValueError(f'O atributo Isbn não pode ser vazio')
        if(self._livro.getStatus() is None):
            raise ValueError(f'O atributo Status precisa ser um int')
        return self._livro

def dynamicTuple( isbn: str, titulo: str = None, autor: str = None, genero: str = None, status: int = None) -> tuple:
    dynamicTuple.__code__


class ControllerLivro:
    @staticmethod
    def instanceFromDB(isbn: str) -> Livro:
        try:
            db = DB()
            query = """select titulo,autor,genero,isbn,status_livro from livro where isbn=%s"""

            db.exec(query, (isbn,))
            data = db.f_one()

            return Livro(titulo=data[0],autor=data[1], genero=data[2], isbn=data[3], status=data[4])
        except Exception as e:
            print(e)

    
    @staticmethod
    def adicionarLivro(titulo: str, autor: str, genero: str, isbn: str, status: int = 1) -> bool:
        """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn ja existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""
        try:
            novo: Livro =(LivroBuilder()
                            .addTitulo(titulo)
                            .addAutor(autor)
                            .addGenero(genero)
                            .addIsbn(isbn)
                            .addStatus(status)
                            .build()
                        )
        except (ValueError, TypeError) as e:
            print(f'Erro ao criar instância de Livro:\n{e}')
            return False

        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, isbn)

            if(not id_livro):
                print(f'Livro com Isbn: {isbn}, já foi adicionado!')
                return False

            db.exec(query=novo.createQuery(), args=novo.getAsDb())
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
    
    @staticmethod
    def adicionarLivroFromInstance(livro: Livro):
        """Adiciona um novo livro ao banco de dados. Verifica primeiro se Isbn ja existe no banco e aborta caso sim. Retorna um Bool com status de sucesso da operação de adição"""

        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, livro)

            if(id_livro):
                print(f'Livro com Isbn: {livro.getIsbn()}, já foi adicionado!')
                return False

            db.exec(query=livro.createQuery(), args=livro.getAsDb())
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
    
    @staticmethod
    def alterarLivro(livro: Livro, titulo: str = None, autor: str = None, genero: str = None, status: int = None) -> bool:
        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, livro)

            if(not id_livro):
                print(f'Livro com Isbn: {livro.getIsbn()}, não foi encontrado!')
                return False

            #Gerando tuple para query
            arg = []
            if(titulo):
                arg.append(titulo)
            if(autor):
                arg.append(autor)
            if(genero):
                arg.append(genero)
            if(status):
                arg.append(status)
            arg.append(livro.getIsbn())
            arg = tuple(arg)

            db.exec(query=livro.alterLivroQuery(titulo=titulo, autor=autor, genero=genero, status=status), args=arg)
            db.commit()
            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False

    @staticmethod
    def emprestarLivro(livro: Livro, id_usuario: int):
        # from usuario import Usuario
        # usuario: Usuario = usuario
        try:
            db = DB()
            id_livro = ControllerLivro.getIdLivro(db, livro)

            db.exec('select devolvido from emprestimo where id_livro=%s and id_usuario=%s order by id_emprestimo desc' , (id_livro, id_usuario))

            result = db.f_one()
            if(result):
                result = result[0]
            else:
                print('Erro: Usuário inexistente')
                return False

            if(not ControllerLivro.alterarLivro(livro=livro, id_usuario=id_usuario, status=2)):
                print('')
                return False

            db.close()
            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False

    @staticmethod
    def devolverLivro(livro: Livro):
        try:
            if(not ControllerLivro.alterarLivro(livro=livro, status=1)):
                return False

            return True
        except Exception as e:
            print(f'Erro ao connectar ao banco de dados: {e}')
            return False
    
    @staticmethod
    def getIdLivro(database:DB, livro: Livro | str) -> int:
        """Retorna o id do livro caso exista, Raises ValueError se livro não exister no banco de dados"""

        if(isinstance(livro, Livro)):
            database.exec(livro.getIdLivroQuery(), (livro.getIsbn(),))
        elif(type(livro) == str):
            database.exec('select id_livro from livro where isbn=%s', (livro,))
        else:
            raise TypeError('Livro não corresponde a um tipo válido')

        id_livro = database.f_one()

        if(not id_livro):
            raise ValueError('Livro inexistente')

        id_livro = id_livro[0]
        return id_livro

if __name__ == "__main__":
    teste = LivroBuilder().addTitulo('test1').addAutor('test2').addGenero('test3').addIsbn('007').addStatus().build()

    #print(ControllerLivro.adicionarLivroFromInstance(teste))
    print(ControllerLivro.devolverLivro(teste))