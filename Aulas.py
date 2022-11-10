def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print("Ola, Deus!")

# Verifica qual dos dois valores é maior x ou y.

x = eval(input('digite um valor para x: '))
y = eval(input('digite um valor para y: '))
if x == y:
    print('x e y são iguais!')
elif x > y:

    print('x é maior que y!')

else:
    print('y é maoir que x!')

# Descobre se o número inserido é par ou ímpar.

x = eval(input('digite um valor para descobrir se ele é par ou ímpar: '))

if x % 2 == 0:
    print('É par!')
else:
    print('É ímpar!')

# Soma os números pares, de uma lista gerada aleatoriamente.

import random

x = random.sample(range(6), 6)
print(x)

soma = 0
for i in x:
    if (i % 2 == 0):
        soma = soma + i

print(f'soma dos números pares da lista: {soma}')

# Verifica de acordo com a nota do aluno se ele está aprovado.

x = eval(input('digite uma nota para saber sua situação acadêmica: '))

if x >= 7:

    situacao = 'aprovado'

elif x >= 5:

    situacao = 'em recuperação'

else:
    situacao = 'reprovado'

print(f'O estudante está {situacao}.')

# Verifica desconto sobre valor do produto, de acordo com a quantidade de produtos comprados.


x = eval(input('digite a quantidade de produtos:'))

x = x * 10
print(f'valor sem descoto:{x}')

if x <= 100:
    desconto = 'Sem desconto'


elif x <= 200:
    desconto = '10% de desconto'
    preco = (10 / 100) * x
    x = x - preco
else:
    desconto = '20% de desconto'
    preco = (20 / 100) * x
    x = x - preco

print(f'Valor da compra R$:{x} ' + f'oferta:{desconto}')

# Função que verifica o menor valor de uma lista.


import random

d = random.sample(range(6), 6)
print(d)


def menor(list):
    i = 0
    while i == list:
        i += 1
    return i


s = menor(d)

print(s)

#  Função que verifica os números pares e soma eles.


import random

d = random.sample(range(6), 6)
print(d)


def soma_par(list):
    s = 0
    for i in list:
        if i % 2 == 0:
            s = s + i
    return s


e = soma_par(d)
print(e)

# Função que verifica o fatorial de um número e soma eles

x = eval(input('digite um numero e descubra seu fatorial: '))


def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


z = fatorial(x)

for d in reversed(range(0, x)):
    d += 1
    print(f'x {d}')

print(f'fatorial: {z}')

# verifica o indice da lista, depopis a letra do indece encontrado.
# obs: lembrando que a contagem é iniciada do indece "0".

lista = ["cachorro", "hamster", ["pato", "galinha", "porco"], "gato"]

print(lista[3][2])
