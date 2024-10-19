def deletar_moto(motos):
    try:
        id_moto = int(input("Digite o ID da moto que deseja deletar: "))
        for moto in motos:
            if moto['id'] == id_moto:
                motos.remove(moto)
                print("Moto deletada com sucesso!")
                return
        print("Moto não encontrada.")
    except ValueError:
        print("Erro: ID inválido. Digite um numero inteiro")
    except Exception:
        print(f"Erro ao deletar moto")
