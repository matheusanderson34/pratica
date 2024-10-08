def fatorial(n):
    if n < 0:
        raise ValueError("O numero precisa ser inteiro positivo.")
    elif n == 0 or  n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
try:
    numero = int(input("Digite um numero inteiro nao-negativo: "))
    fatorial_final = fatorial(numero)
    print(f"O fatorial de {numero} é {fatorial_final}.")
except ValueError as e:
    print(e)