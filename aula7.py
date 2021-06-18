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

print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é:{imc:.2f}') # :.2f -> para diminuir as casas decimais
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{n} {i} tem {n} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))