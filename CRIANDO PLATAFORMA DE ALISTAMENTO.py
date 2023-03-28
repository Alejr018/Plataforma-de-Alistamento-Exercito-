from datetime import date
atual = date.today().year
print('Olá,seja muito Bem Vindo ao site do alistamento do Exército Brasileiro,para prosseguirmos coloque seus dados abaixo ')
nome1 = str(input('Digite seu primeiro nome:')).capitalize()
print('------------------------------------------------------------------------------------------------------')
nome2 = str(input('Digite seu segundo nome:')).capitalize()
print('------------------------------------------------------------------------------------------------------')
idade = int(input('Digite o ano que você nasceu '))
print('------------------------------------------------------------------------------------------------------')
idade2 = atual - idade
print('Olá {} {},você nasceu em {},então atualmente você tem {} anos de idade'.format(nome1, nome2, idade,idade2))
print('------------------------------------------------------------------------------------------------------')
if idade2 == 19:
    print('Já está na hora de você se alistar.')
elif idade2 >= 19:
    saldo = idade2 - 18
    print('''Já passou  do prazo para você se alistar,você devieria ter se alistado a {} anos 
vá urgentemente para um TG mais próximo de você ou \n entre em www.alistamento.eb.mil.br para se alistar.'''.format(saldo))
elif idade2 <= 17:
    saldo = 18 - idade2
    print('''Ainda não está na hora de você se alistar,ainda faltam {} anos para você se alistar,fique atento'''.format(saldo))


