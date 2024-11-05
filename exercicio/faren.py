
def toCelsius(num: float) -> float:
    temp = (num - 32) * (5/9)
    return temp

def toFaren(num: float) -> float:
    temp = (num * (9/5)) + 32
    return temp

while True:
    try:
        num = int(input('Digite o número para calcular\n1: Fahrenheit\n2: Celsius\n0: Sair\n').strip())

    except Exception as e:
        print(f'Erro: {e}\nDigite um número inteiro')

    else:
        if(num == 0):
            quit()
        elif(not (num == 1 or num == 2)):
            print('Digite um número correspondendo a uma opção!')

        try:
            valor = float(input('Digite a temperatura que deseja converter:\n'))
        except Exception as e:
            print('Valor incorreto: {e}')

        match(num):
            case 1:
                print(f'A temp.: {valor} em Fahrenheit: {toFaren(valor):.2f}\n')
            case 2:
                print(f'A temp.: {valor} em Celsius: {toCelsius(valor):.2f}\n')
