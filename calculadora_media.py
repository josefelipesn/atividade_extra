#Calculadora de média

def calcular_media():
    soma = 0
    contador = 0
    while True:
        nota = float(input("Digite uma nota (ou -777 para encerrar): "))
        if nota == -777:
            break
        soma += nota
        contador += 1
    if contador > 0:
        media = soma / contador
        print("a média do aluno é:", media)
    else:
        print("Não foi inserida nenhuma nota.")

calcular_media()