from models import create_table, create_product, get_product, update_product, delete_product

def menu():
    print("="*30)
    print(f'{"Cadastro de Produtos":^30}')
    print("="*30)
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Atualizar produtos")
    print("4. Deletar produtos")
    print("5. Sair")
    print("-"*30)

def print_products(products):
    print("-" * 90)
    print(
        f"{'Nr.':>3} "
        f"{'Nome':<25} "
        f"{'Descrição':<30} "
        f"{'Preço':>10} "
        f"{'Estoque':>10}"
    )
    print("-" * 90)

    for i, product in enumerate(products, start=1):
        _, name, description, price, stock = product
        print(
            f"{i:>3} "
            f"{name:<25} "
            f"{description:<30} "
            f"R$ {price:>7.2f} "
            f"{stock:>10}"
        )
    print("")

create_table()

while True:
    menu()
    option = input("\nEscolha uma opção: ")

    if option == '1':
        print("\nAdicionando produto:")
        while True:
            name = input("Digite o nome do produto: ").strip()
            if name != "":
                break
            print("O nome do produto não pode ser vazio.")

        description = input("Digite a descrição do produto: ").strip()

        while True:
            try:
                price = float(input("Digite o preço do produto: "))
                break
            except ValueError:
                print("Digite um preço válido.")

        while True:
            try:
                stock = int(input("Digite a quantidade do produto em estoque: "))
                break
            except ValueError:
                print("Digite uma quantidade válida.")

        create_product(name, description, price, stock)
        print(f"\nProduto '{name}' adicionado com sucesso!\n")


    elif option == '2':
        print("\nListando produto:")
        while True:
            try:
                product_id = int(input("Digite o ID do produto (0 para listar todos): "))
                if product_id == 0:
                    products = get_product()
                    print("Lista de todos os produtos:")
                    print_products(products)
                else:
                    product = get_product(product_id)

                    if product is None:
                        print("\nProduto não encontrado.")
                    else:
                        print("Produto listado:")
                        print_products([product])
                break
            except ValueError:
                print("Digite um ID válido.")


    elif option == '3':
        print("\nAtualizando produto:")
        while True:
            try:
                product_id = int(input("Digite o ID do produto a ser atualizado: "))
                if product_id > 0:
                    break
                else:
                    print("O ID deve ser maior que zero.")
            except ValueError:
                print("Digite um ID válido.")

        name = input("Digite o novo nome (ENTER para manter): ").strip()
        if name == "":
            name = None

        description = input("Digite a nova descrição (ENTER para manter): ").strip()
        if description == "":
            description = None

        while True:
            price_input = input("Digite o novo preço (ENTER para manter): ").strip()
            if price_input == "":
                price = None
                break
            else:
                try:
                    price = float(price_input)
                    break
                except ValueError:
                        print("Preço inválido.")
                        price = None

        while True:
            stock_input = input("Digite a nova quantidade (ENTER para manter): ").strip()
            if stock_input == "":
                stock = None
                break
            else:
                try:
                    stock = int(stock_input)
                    break
                except ValueError:
                    print("Quantidade inválida.")
                    stock = None

        update_product(
            product_id,
            name=name,
            description=description,
            price=price,
            stock=stock
        )

        print(f"\nProduto ID '{product_id}' atualizado com sucesso!\n")


    elif option == '4':
        print("\nDeletando produto:")
        while True:
            try:
                product_id = int(input("Digite o ID do produto a ser deletado: "))
                if product_id > 0:
                    deleted = delete_product(product_id)
                    if deleted:
                        print(f"\nProduto ID '{product_id}' deletado com sucesso!\n")
                        break
                    else:
                        print("\nProduto não encontrado.")
                else:
                    print("O ID deve ser maior que zero.")
            except ValueError:
                print("Digite um ID válido.")
    elif option == '5':
        print("\nSaindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")

    input("Pressione Enter para continuar...\n")