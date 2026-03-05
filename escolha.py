import cmath # Biblioteca para números complexos e raízes de negativos
import math

def calcular_raiz_quadrada():
    try:
        # Solicita o número ao usuário
        entrada = input("Digite um número para calcular a raiz quadrada: ")
        numero = float(entrada)
        
        if numero < 0:
            # Para números negativos, usa cmath
            resultado = cmath.sqrt(numero)
            return resultado
            
        else:
            # Para positivos, usa math ou cmath (ambos funcionam)
            resultado = math.sqrt(numero)
            return resultado
                        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

    