#Contador de vocais e consoantes

def contar_vogais_consoantes():
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    
    vogais_cont = 0
    consoantes_cont = 0
    
    for char in frase:
        if char in vogais:
            vogais_cont += 1
        elif char in consoantes:
            consoantes_cont += 1
    
    print("Vogais:", vogais_cont)
    print("Consoantes:", consoantes_cont)

contar_vogais_consoantes()
