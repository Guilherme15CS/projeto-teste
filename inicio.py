nome = input('Digite seu nome: ')
idade = int(input('Quantos anos você tem? '))
print(f'Seu nome é {nome} e tem {idade} anos')
if idade >= 18:
    print('Você é maior de idade, você tem liberdade para a vida')
else:
    resto = 18 - idade
    print(f'Você ainda é menor de idade, continue estudando para que em {resto} anos você seja um adulto independente')