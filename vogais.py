def quantidade_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for char in s:
        if char  in vogais:
            contador +=1
            
    return contador

palavra = input("Digite alguma palavra: ")
numero_vogais = quantidade_vogais(palavra)

print(f"Número de vogais na palavra: {numero_vogais}")