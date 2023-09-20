# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas_str = input("Digite as suas 4 notas bimestrais: ").split()

notas_int = []

for nota_str in notas_str:
  nota_int = int(nota_str)
  notas_int.append(nota_int)

media = sum(notas_int)/len(notas_int)

print(f"A média das suas notas é: {media}")