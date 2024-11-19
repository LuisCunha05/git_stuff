from model import Livro, LivroBuilder

if __name__ == '__main__':
    teste = (LivroBuilder()
                .addAutor('dd')
                .addGenero('da')
                .addId(2)
                .addStatus()
                .addTitulo('hahaha')
                .build())
    
    print(teste)