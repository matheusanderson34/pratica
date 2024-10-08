def conta_palavras(s):
    palavras = s.strip().split()
    return len(palavras)

frase = input("Digite alguma frase: ")
num_palavras = conta_palavras(frase)
print(f"O numero de palavras na frase é: {num_palavras}")