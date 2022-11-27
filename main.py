# Programação Python do Zero ao Avançado 2022 - Andre Iacono

#  single line commenter

"""
in block commentary
"""

"""
types of data:
    string - str("text")
    number - integer / float (fraction)
    boolean - bool
    
changing data: 
    str() -> to string
    int() -> to integer
    float() -> to float
    
x = str(2)
y = int(5)
z = float(10)

print(x + x)
print(y + y)
print(z + z)
   
"""

"""
nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")
cidade = input("Em que cidade você mora? ")

# não aceita imprimir dois tipos de dados diferentes
print('A ' + nome + ' tem ' + idade + ' anos e mora em ' + cidade)

"""

"""
ano_nascimento = int(input("Em que ano você nasceu? "))
print(type(ano_nascimento))
ano_atual = 2022

idade = ano_atual - ano_nascimento

print("Sua idade é: " + str(idade))

"""

"""
fruta = "Abacate"

print(fruta[-1]) # conta de trás pra frente

valor = str(99.75)


print(valor[3:])  # da posição 3 até o final
print(valor[:3])  # da posição inicial até a posição 3
"""

"""

formatted string

nome = "Patricia"
sobrenome = "Rangel"
profissao = "desenvolvedora"


texto = nome + " " + sobrenome + " é uma excelente " + profissao
texto_formatado = f'A {nome} {sobrenome} é uma excelente {profissao}'
print(texto)
print(texto_formatado)
"""

"""

# string methods
mensagem = ' eu adoro comida Caseira'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())  # primeira letra da string maiúscula
print(mensagem.find('c'))
print(mensagem.find('C'))  # python é case sensitive
print(mensagem.replace('adoro', 'amo'))
print(mensagem.strip())  # remove os espaços antes do primeiro caractere

"""

"""
math operations

soma = 2 + 2
mult = 2 * 2
div = 2 / 2
sub = 2 - 2
exp = 2 ** 2

print(soma)
print(mult)
print(div)
print(sub)
print(exp)
"""

"""
comparison operators

== Equal
!= not equal
> greater than 
< lesser than
>= greater than or equal to
<= lesser than or equal to

num1 = 10
num2 = 5

print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 >= num2)

print("oi" > "ola")
"""





