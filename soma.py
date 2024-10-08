def soma(lista_num):
    if not lista_num:
        raise ValueError ("A lista não pode estar vazia.")
    
    soma = sum(lista_num)
    return soma

try:
    numeros = [float (x) for x in input("Digite os números: ").split()]
    soma_final = soma(numeros)
    print(f"A soma dos numeros é {soma_final}")
    
except ValueError as e:
    print(e)