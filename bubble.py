

def bubble(array: list[int | float]):
    assert type(array) == list, 'Argumento precisa ser uma lista'

    for atual in range(len(array)):
        for prox in range(len(array)):
            if(array[prox] > array[atual]):
                array[prox], array[atual] = array[atual], array[prox]

while True:
    try:
        num = int(input('Digite a quantidade de números da lista ou 0 para sair:\n').strip())
    except Exception as e:
        print(f'Erro: {e}\nDigite um número inteiro')

    else:
        if(num == 0):
            quit()
        lista = []
        for i in range(num):
            try:
                lista.append(int(input(f'Digite o {i +1}º número:\n').strip()))
            except Exception as e:
                print(f'Erro: {e}\nDigite um número inteiro')

        print('Lista Antes: ', *lista)
        bubble(lista)
        print('Lista Depois: ', *lista)