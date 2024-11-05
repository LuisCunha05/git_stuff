
def fiboPrinter(count: int):
    if type(count) != int:
        raise TypeError("count precisa ser um inteiro!")
    if int(count) > 0:
        raise TypeError("count precisa ser maior que zero")

    n_2 = 0
    n_1 = 1
    fn = None

    if(count == 1):
        print(0)
        return
    elif(count == 2):
        print('0, 1')
        return
    
    print('0, 1', end=', ')

    for i in range(count - 2):
        fn  = n_2 + n_1
        n_2, n_1 = n_1, fn
        print(fn, end=', ')
    print()

while True:
    try:
        num = int(input('Digite a quantidade de digitos de fibonaci ou 0 para sair:\n').strip())

    except Exception as e:
        print(f'Erro: {e}\nDigite um número inteiro')

    else:
        if(num == 0):
            quit()
        fiboPrinter(num)