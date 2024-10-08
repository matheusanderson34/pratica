def conversao_temperatura(temperatura, unidade):
    if unidade.upper() == "C":
        return (temperatura * 9,5) + 32
    elif unidade.upper() == "F":
        return (temperatura - 32) * 5/9
    
    else:
        raise ValueError("Unidade invalida. Por favor utilize 'C' para Celsius ou 'F' para Fahrenheit. ")
    
    
try:
    temperatura = float(input("Digite a temperatura a ser convertida: "))
    unidade = input("Digite a unidade |C para Celsius| ou |F para Fahrenheit|:")
    temperatura_convertida = conversao_temperatura(temperatura, unidade) 
    print(f"A temperatura convertida é: {temperatura_convertida:.2f}")
    
except ValueError as e:
    print(e)