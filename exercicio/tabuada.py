
while True:
    num = input('Digite o número para exibir a tabuada ou 0 para Sair.\n')
    try:
        num = int(num)

        if(int(num) == 0):
            quit()

        print(f'Tabuada {num}:')
        print(*[f'{num:4} x {i:4}: {num * i:4}' for i in range(1, 11)], sep='\n')
        print()

    except TypeError:
        print('Digite um número inteiro')
