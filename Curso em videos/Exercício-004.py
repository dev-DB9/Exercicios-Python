'''
4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
primitivo e todas as informações possiveis sobre ele.
'''

info = input("Digite algo: ")
print(type(info))
print(f"O valor ({info}) é \nLower: {info.islower()}\nUpper: {info.isupper()}\nNumeric: {info.isnumeric()}\nAlpha: {info.isalpha()}\nAlpha Numeric: {info.isalnum()}")
