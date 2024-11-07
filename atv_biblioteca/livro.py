from database import DB

class Livro:
    def __init__(self) -> None:
        self._titulo: str = ''
        self._autor: str = ''
        self._genero: str = ''
        self._isbn: str = ''
        self._status: int = None #1:disponivel,2-emprestado,3-extraviado,4-danificado
        self._id_usuario: int = None

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

    def setIdUsuario(self, id_usuario: int):
        if(type(id_usuario) != int):
            raise TypeError('Tipo esperado: int')
        if(id_usuario <= 0):
            raise ValueError('Valor precisa ser maior que 0')

        self._id_usuario = id_usuario

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

    def getIdUsuario(self) -> int:
        return self._id_usuario
    
    def getAsDb(self) -> tuple:
        return (self._titulo, self._autor, self._genero, self._isbn, self._status)

    def __str__(self) -> str:
        return f'{self._titulo}, {self._autor}'

    def __iter__(self):
        return iter((self._titulo, self._autor, self._genero, self._isbn, self._status, self._id_usuario))

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

    def addIdUsuario(self, id_usuario: int):
        self._livro.setIdUsuario(id_usuario)
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
        if(self._livro.getIdUsuario() is not None and self._livro.getIdUsuario() <= 0):
            raise ValueError(f'O atributo IdUsuario precisa ser maior que Zero')
        return self._livro

class GerenciarLivro:
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
            db.exec('select id_livro from livro where isbn=%s', (isbn,))
            id, = db.f_one()

            if(not id):
                print(f'Livro com Isbn: {isbn}, já foi adicionado!')
                return False

            query = """
                insert into usuario
                    (titulo, autor, genero, isbn, status_livro)
                    values (%s,%s,%s,%s,%s)
                """

            db.exec(query=query, args=novo.getAsDb())
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

    teste = LivroBuilder().addTitulo('apa').addAutor('caa').addGenero('da').addIsbn('007').addStatus().build()

    print(*teste.getAsDb())