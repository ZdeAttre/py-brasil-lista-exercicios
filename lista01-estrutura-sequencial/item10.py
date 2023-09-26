# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp_celcius = int(input("Informe a temperatura em Celsius: "))

temp_fahrenheit = (temp_celcius * (9/5)) + 32

print(f"A temperatura em Fahrenheit é: {round(temp_fahrenheit)}°F.")
