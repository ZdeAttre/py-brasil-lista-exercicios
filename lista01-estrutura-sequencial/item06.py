# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 

raio = input("Insira o raio do círculo que deseja calcular: ")

area = 3.14 * float(raio) ** 2

print(f"A área do círculo: {round(area, 2)}")