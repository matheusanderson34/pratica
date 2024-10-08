def primo(numeros):
    if numeros <= 1:
        return False
    for i in range(2, int(numeros**0.5) + 1):
        if numeros % i == 0:
            return False
    return True
    
try:
    numero = int(input("Digite um numero: "))
    if primo(numero):
        print(f"{numero} é um numero primo.")
    else:
        print(f"{numero} nao é um numero primo.")  
except ValueError:
    print("ERRO. Por favor insira um numero real valido.")