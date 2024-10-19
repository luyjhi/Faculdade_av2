def atualizar_moto(motos):
    try:
        id_moto = int(input("Digite o ID da moto que deseja atualizar: "))
        for moto in motos:
            if moto['id'] == id_moto:
                moto['modelo'] = input("Novo modelo: ")
                moto['marca'] = input("Nova marca: ")
                moto['ano'] = (int)(input("Novo ano: "))
                print("Moto atualizada com sucesso!")
                return
        print("Moto não encontrada.")
    except ValueError:
        print("Erro: ID inválido.")
    except Exception :
        print(f"Erro ao atualizar moto .Digite um numero inteiro no ID")
