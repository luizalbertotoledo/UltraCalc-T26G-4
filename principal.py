from os import system as cls
cls ("cls")

historico = "historico.txt"
contador = 1

# Esse codigo ira ler o arquivo 'historico.txt'.

with open("historico.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print (f"{contador}: {linha.strip()}")
        contador = contador + 1