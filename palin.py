def isPalindrome(word: str) -> bool:
    if(type(word) != str):
        raise TypeError
    
    for i in range(len(word) // 2):
        if(word[i] != word[-(i + 1)]):
            return False
    return True

while True:
    palavra  = input('Digite uma palavra para testar palin ou 0 para sair:\n')
    if(palavra == '0'):
        quit()
    print(isPalindrome(palavra))