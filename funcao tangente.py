from os import system as limptela
limptela("cls")
import math

angulo_g = float(input('Digite o ângulo em graus: '))

angulo_r= math.radians(angulo_g)

resultado = math.tan(angulo_r)

print(f'A tangente é: {resultado}')