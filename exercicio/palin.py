def isPalindrome(word: str) -> bool:
    if(type(word) != str):
        raise TypeError

    word = word.replace(' ', '')

    for i in range(len(word) // 2):
        if(word[i].lower() != word[-(i + 1)].lower()):
            return False
    return True

while True:
    palavra  = input('Digite uma palavra para testar palin ou 0 para sair:\n')
    if(palavra == '0'):
        quit()
    print(isPalindrome(palavra))