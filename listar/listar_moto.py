def listar_motos(motos):
    if len(motos) == 0:
        print("Nenhuma moto cadastrada.")
    else:
        for moto in motos:
            print(f"ID: {moto['id']}, Modelo: {moto['modelo']}, Marca: {moto['marca']}, Ano: {moto['ano']}")
