nome = input('Digite seu nome: ')
idade = int(input('Quantos anos você tem? '))
print(f'Seu nome é {nome} e tem {idade} anos')
if idade <= 10:
    print('Você ainda está no fundamental 1')
elif 11 <= idade <= 14:
    print('Você está no fundamental 2')
elif 15 <= idade <=18:
    print('Você está no ensino médio')
else:
    print('Você já terminou a escola')
