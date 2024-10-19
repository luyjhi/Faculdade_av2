def cadastrar_moto(motos):
    try:
        moto = {
            'id': len(motos) + 1,  
            'modelo': input("Digite o modelo da moto: "),
            'marca': input("Digite a marca da moto: "),
            'ano': (int)(input("Digite o ano da moto: "))
        }
        motos.append(moto)  
        print("Moto cadastrada com sucesso!")
    except Exception:
        print(f"Erro ao cadastrar moto. Digite um numero inteiro no ano  ")
