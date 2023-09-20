# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = input("Informe o quanto você ganha por hora: ")
horas_mes = input("Agora informe quantas horas você fez nesse mês: ")

salario = float(valor_por_hora) * int(horas_mes)

print(f"O seu sálario do mês é: R$ {round(salario, 2)}.")