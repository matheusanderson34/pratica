def media(lista_num):
    if not lista_num:
        raise ValueError ("A lista não pode estar vazia.")
    
    soma = sum(lista_num)
    media = soma / len(lista_num)
    return media

try:
    numeros = [float (x) for x in input("Digite os números: ").split()]
    media_final = media(numeros)
    print(f"A media dos numeros é {media_final}")
    
except ValueError as e:
    print(e)