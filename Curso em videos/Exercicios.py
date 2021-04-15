#Nome: Daniel Vitor Oliveira Bertoldo
#Professor: Gustavo Guanabara (Curso em video)

#Conteudo de aula
'''
-----Tipos Primitivos-----

int: Números Inteiros
float: Números Reais
Boolean: Valores Lógicos
Str/String: Letras/Palavras/Frases

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
media = (numero1 + numero2)/2
print(f"A média dos valores {numero1} e {numero2} é {media}")
if media >= 6:
    print("Parabéns você foi aprovado.")
elif media < 6:
    print("Parabéns você foi reprovado.")
'''

#Exercícios

'''
1 - Crie um programa que escreva "Olá. Mundo!" na tela.

Resposta:
print("Olá. Mundo!")
'''

'''
2 - Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

Resposta:
nome = input("Digite o seu nome: ")
print(f"É um prazer te conhecer, {nome}")
'''

'''
3 - Crie um programa que leia dois números e mostre a soma deles.

Resposta:
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
res = n1 + n2
print(f"A soma dos valores informados é {res}")
'''

'''
4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
primitivo e todas as informações possiveis sobre ele.

Resposta:
info = input("Digite algo: ")
print(type(info))
print(f"O valor ({info}) é \nLower: {info.islower()}\nUpper: {info.isupper()}\nNumeric: {info.isnumeric()}\nAlpha: {info.isalpha()}\nAlpha Numeric: {info.isalnum()}")
'''

'''
5 - 
'''
