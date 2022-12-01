# Data structure

"""
lists and methods

cidades = ['Belo Horizonte', 'São Paulo', 'Rio de Janeiro']

print(cidades)

print(cidades[-1]) # negativo -> de trás pra frente. -1 é o último da lista


cidades.append('Fortuna de Minas') # = push js
cidades.remove('São Paulo')
cidades.insert(1, 'Porto Alegre') # insere na posição desejada
cidades.pop(0) # tira o elemento da posição indicada
cidades.sort()
print(cidades)
"""


"""
concatenating lists


numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']

# final = numeros * 2 # multiplica a lista de acordo com o número que você pedir -> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# final = numeros + letras # concatena os dois arrays

# outra opção é

numeros.extend(letras)
print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens[1][0])
"""

"""
unpacking lists

produtos = ['arroz', 'feijão', 'batata', 'chocolate']

item1, *outros, item2 = produtos

print(item1)
print(item2)
print(outros)
"""






