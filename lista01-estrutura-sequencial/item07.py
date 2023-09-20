# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Quadrado com 1 lado igual = 1 valor")
print("Quadrado com 2 lados iguais = 2 valores")
print("Quadrado com 4 lados diferentes = 4 valores\n")
lados_str = input("Informe o valor dos lados do quadrado: ").split()

lados_int = []

if len(lados_str) == 1 :
  area = int(lados_str[0]) ** 2
  dobro = area * 2

  print(f"O dobro da área é: {dobro}")
elif len(lados_str) == 2 :

  for lado in lados_str:
    lado_int = int(lado)
    lados_int.append(lado_int)

  area = lados_int[0] * lados_int[1] 
  dobro = area * 2

  print(f"O dobro da área é: {dobro}")
elif len(lados_str) == 4 :

  for lado in lados_str:
    lado_int = int(lado)
    lados_int.append(lado_int)

  area = sum(lados_int)  
  dobro = area * 2

  print(f"O dobro da área é: {dobro}")  
else :
  print(f"Isso não é um quadrado, possue {len(lados_str)} lados.")