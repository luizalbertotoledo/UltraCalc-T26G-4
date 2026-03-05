from os import system as limptela
limptela("cls")
import math

def calcular_tangente():
 
 angulo_g = float(input('Digite o ângulo em graus: ')) #usuario Informe o angulo.

 angulo_r= math.radians(angulo_g) #converte grau em radianos

 resultado = math.tan(angulo_r)  #função trigonométriacas (radianos)

 print(f'A tangente de {angulo_g} é {resultado :.4f}') # O resultado 

calcular_tangente()