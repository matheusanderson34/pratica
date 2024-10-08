def verificacao(email):
    return "@" in email

login = input("Digite seu email: ")
if verificacao(login):
    print("O email possui o '@'")
    
else:
    print("ERRO. O email nao possui o '@'")
