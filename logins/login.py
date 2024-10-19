def verificar_usuario_padrao(usuarios):
    if not usuarios: 
        usuarios.append({'usuario': 'marcelino', 'senha': 'paoevinho'})  

def login(usuarios):
    verificar_usuario_padrao(usuarios) 
    try:
        usuario_login = input("Digite o nome de usuário: ")
        senha_login = input("Digite a senha: ")

        for usuario in usuarios:
            if usuario['usuario'] == usuario_login and usuario['senha'] == senha_login:
                print("Login bem-sucedido!")
                return True
        print("Usuário ou senha incorretos!")
        return False
    except Exception:
        print(f"Erro ao fazer login")
        return False
