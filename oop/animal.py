"""
Atividade (17/10)
Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, representando subdivisões até chegar a classes específicas como Ornitorrinco, Morcego e Baleia.

Criação das Classes Principais:

Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
Características Específicas:

Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
Mamíferos: método amamentar().
Aves: método voar().
Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
Atributos e Métodos:

Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes).
"""

class Animal:
    def __init__(self,  nome_cientifico: str, habitat: str, alimentacao: str) -> None:
        self.nome_cientifico = nome_cientifico
        self.habitat = habitat
        self.alimentacao = alimentacao
    
    def comer(self):
        print(f'Animal {self.nome_cientifico}: Yami yami')
    
    def dormir(self):
        print(f'Animal {self.nome_cientifico}: ZZzzzZ...')
    
    def seMovimentar(self):
        print(f'Animal {self.nome_cientifico}: move-se')
    
    def __str__(self) -> str:
        return f'Nome Científico: {self.nome_cientifico}, Habitat: {self.habitat}, Alimentacao: {self.alimentacao}'

class Vertebrado(Animal):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)
        self.esqueleto = esqueleto
        self.coluna_vertebral = True

    def alongar(self):
        print(f'Animal {self.nome_cientifico}: aloga-se')


class Peixe(Vertebrado):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str, cartilagem: bool) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)
        self.cartilagem = cartilagem

    def nada(self):
        print(f'O Peixe {self.nome_cientifico}: nada...')

class Mamifero(Vertebrado):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def amamenta(self):
        print(f'O Mamifero {self.nome_cientifico} amamenta!')



class Ave(Vertebrado):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str, pode_voar: bool = True) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)
        self.pode_voar = pode_voar

    def voa(self):
        if(self.pode_voar):
            print(f'A Ave {self.nome_cientifico} voa!')
        else:
            print(f'A Ave {self.nome_cientifico} NÂO voa!')

class Reptil(Vertebrado):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)
        self.escama = True
    
    def seEscondeDoSol(self):
        print(f'O Réptil {self.nome_cientifico} se esconde do sol!')

class Morcego(Mamifero):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def voa(self):
        print(f'O morcego {self.nome_cientifico} voa!')
    
    def seMovimentar(self):
        self.voa()

class Ornitorrinco(Mamifero):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)
    
    def colocaOvo(self):
        print(f'O Mamifero {self.nome_cientifico} coloca ovo!')
    

class Baleia(Mamifero):
    def __init__(self, nome_cientifico: str, esqueleto: str, habitat: str, alimentacao: str) -> None:
        super().__init__(nome_cientifico, esqueleto, habitat, alimentacao)

    def nadar(self):
        print(f'A baleia nada!')
    
    def seMovimentar(self):
        self.nadar()
