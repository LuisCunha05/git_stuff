nums = []
menor = 1e300
maior = -1e300
try:
    for i in range(5):
        nums.append(float(input(f'Yep {i}: ')))
except Exception as e:
    print(f'Digite um número. {e}')
else:
    for i, valor in enumerate(nums):
        if(valor > maior):
            maior = valor

        if(valor < menor):
            menor = valor

print(f'Menor número: {menor}, Maior número: {maior}')