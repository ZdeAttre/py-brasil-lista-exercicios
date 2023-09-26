# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro. 
#   c. o terceiro elevado ao cubo.
valores = input("Forneça 2 números inteiros e um real: ").split()

num1 = int(valores[0])
num2 = int(valores[1])
num3 = float(valores[2])

exp_a = (num1*2)+(num2/2)
exp_b = (num1*3)+num3
exp_c = num3**3

print(f"Expressão A: ({num1} x 2) + ({num2}/2) = {exp_a}")
print(f"Expressão B: ({num1} x 3) + {num3} = {exp_b}")
print(f"Expressão C: {num3}^3 = {exp_c}")
