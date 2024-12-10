#Tabuada

import time

def tabuada():
    numero = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        time.sleep(1)  # Pausa de 1 segundo entre cada linha

tabuada()