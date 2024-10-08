def autenticar(login, senha):

    usuarios = [
        {"login": "teste", "senha": "admin"},
        {"login": "teste2", "senha": "admin2"},
        {"login": "teste3", "senha": "admin3"}, 
        {"login": "teste4", "senha": "admin4"}, 
    ]
    
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            return True 
        
        
    return False

if __name__ == "__main__":
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    if autenticar(login, senha):
        print("Autentificação bem-sucedida.")
    else:
        print("Login ou Senha Invalidos.")
        