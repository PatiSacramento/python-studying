# functions

"""
def boas_vindas():
    print('Oi')

boas_vindas()

"""

"""
soma

def somar_dois_numeros():
    num1 = 10
    num2 = 5
    resultado = num1 + num2
    print(resultado)


# deixar dois espaços antes de chamar função


somar_dois_numeros()
"""

"""
parametros e argumentos


def boas_vindas(nome, quantidade):
    print(f'Olá, {nome}')
    print(f'Temos {quantidade} laptops em estoque')


boas_vindas('Patricia', 3)


"""

"""
argumento default e non-default

# o parâmetro non-default DEVE vir primeiro
# quantidade -> default. Caso não passe o argumento, a variável assumirá esse valor
def boas_vindas(nome, quantidade=6):
    print(f'Olá, {nome}')
    print(f'Temos {quantidade} laptops em estoque')


boas_vindas('Patricia', 9)
"""

"""
return


def cliente1(nome):
    print(f'Olá, {nome}')


cliente1('Patricia')


def cliente2(nome):
    return nome


print(cliente2('Jorge'))
"""

"""
xargs


# * -> não tem número definido. Podem ser vários argumentos


def soma(x=None, *numeros):
    # ou x = 0...
    for numero in numeros:
        x += numero
    return x


print(soma(1, 2, 3, 4, 5))
"""

"""
nomeando xargs

# dois ** indicam que você pode nomear os parâmetros depois e adicionar mais
def agencia(**carro):
    return carro


print(agencia(modelo='fusca', cor='rosa', motor=1.0))
print(agencia(modelo='fusca', cor='preto', placa=1234))
"""

"""
importando módulos


import math

print(math.factorial(5))
print(math.floor(2.7))
print(math.ceil(2.7))
"""

