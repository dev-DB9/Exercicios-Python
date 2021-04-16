'''
10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considerando a cotação do dolar hojé US$1,00 = R$5,67
'''
valor = float(input("Digite quantos Reais você tem na carteira: "))
dolar = valor / 5.67
print(f"Quantidade de R${valor} que você possui na carteira, equivale a US${dolar} dolares de acorto com a cotação atual (R$5.67).")
