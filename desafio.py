'''
* Criar variavéis para nome(str), idade (int)
* altura(float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC  da pessoa com 2 casas decimais ( peso e na altura da pessoa)
* Exibir um texto com todos os valores na usando o F-String (com chaves)
'''

nome = 'Eduardo Prestes'
idade = 21
altura = 1.70
peso = 74
anoAtual = 2021
anoNascimento = anoAtual-idade
imc = peso/(altura*altura)

print(f'{nome} tem {idade} anos, sua altura é {altura} metros e possui {peso}kg. Nasceu em {anoNascimento} '
      f'e possui o IMC de:{imc:.2f}')
