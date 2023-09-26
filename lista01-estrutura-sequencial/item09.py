# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9). 
temp_fahrenheit = int(input("Informe a temperatura em Fahrenheit: "))

temp_celcius = 5 * ((temp_fahrenheit - 32) / 9)

print(f"A temperatura em Celsius é: {round(temp_celcius)}°C.")
