'''
11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária
para pintá-la, sabendo que cada lata de tinta pinta 2m².
'''
altura = float(input("Digite a altura da sua parede: "))
largura = float(input("Digite a largura da sua parede: "))
area = altura*largura
qntinta = area / 2
print(f"A quantide de tinta para uma parede com área de {area}m² é de {qntinta}l de tinta")