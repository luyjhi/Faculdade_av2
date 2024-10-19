from logins.login import login
from cadastros.cadastrar_moto import cadastrar_moto
from listar.listar_moto import listar_motos
from atualizar.atualizar_moto import atualizar_moto
from deletar.deletar_moto import deletar_moto

usuarios = []
motos = []


def menu_principal():
    print("-=-" * 90)
    print("\n1. Cadastrar Moto")
    print("2. Listar Motos")
    print("3. Atualizar Moto")
    print("4. Deletar Moto")
    print("5. Sair")
    print("-=-" * 90)

def sistema():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_moto(motos)
        elif opcao == "2":
            listar_motos(motos)
        elif opcao == "3":
            atualizar_moto(motos)
        elif opcao == "4":
            deletar_moto(motos)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if login(usuarios):
    sistema()
