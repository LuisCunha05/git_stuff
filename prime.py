def isOdd(num: int):
    assert type(num) == int, f'O valor {num} precisa ser um inteiro!'

    return num & 1

def isPrime(number: int):
    assert type(number) == int, f'O valor {number} precisa ser um inteiro!'

    if(isOdd(number)):
        for i in range(3, int(number ** 0.5) + 1, 2):
            if(not (number % i)):
                return False
        return True
    else:
        if(number == 2):
            return True
        return False

while True:
    try:
        num = int(input('Digite uma número para testar se é Primo ou 0 para sair:\n').strip())

    except Exception as e:
        print(f'Erro: {e}\nDigite um número inteiro')

    else:
        if(num == 0):
            quit()
        print(isPrime(num))
