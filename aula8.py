"""
Entrada e saída de dados
"""

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
ano_nascimento = 2021-int(idade)

print(f'{nome} tem {idade} anos, e nasceu em {ano_nascimento}')
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')

numero_1 = int(input('Digite um número: '))
numero_2 = input("Digite outro número: ")
numero_2 = int(numero_2)

print( numero_1 + numero_2)
print(f'{type(numero_1)} e {type(numero_2)}')