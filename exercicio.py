numero_digitado = int(input("Digite um número: "))
if numero_digitado % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")









idade_usuario = int(input("Digite sua idaide: "))
if 0 <= idade_usuario <= 12:
    print("Você é uma criança.")
elif 13 <= idade_usuario <= 18:
    print("Você é um adoslescente.")
else:
    print("Você é um adulto.")





nome = 'Junior'
senha = '244'


nome_digitado = input('Digite seu nome: ')
senha_digitada = input('Digite sua senha: ')

if nome_digitado == nome and senha_digitada == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')