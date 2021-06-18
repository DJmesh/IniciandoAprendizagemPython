"""
Iniciar com letra, pode conter números, separar _., letras minúsculas
"""
nome = 'Eduardo Prestes'
print(nome, type(nome))
idade = 21
altura = 1.70
e_maior = idade >= 18
peso = 74
imc = peso/(altura*altura)
'''
data_1 = False # bool
data_atual = 2019 # int
'''


print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print('Seu IMC é:', imc)
print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)


