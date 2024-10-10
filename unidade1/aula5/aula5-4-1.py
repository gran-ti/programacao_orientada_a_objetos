# Inicializa a lista de produtos vazia
produtos = []

# Verifica se existe um arquivo de produtos e o carrega
try:
    with open('produtos.txt',) as arquivo:
        for linha in arquivo:
            codigo, nome, quantidade = linha.strip().split(',')
            produtos.append({'codigo': codigo, 'nome':nome, 'quantidade':int(quantidade)})
except FileNotFoundError:
    pass

while True:
    # Exibe o menu de opções
    print('\n\nEsco1ha uma opção: ')
    print('1 - Incluir produto')
    print('2 - Consultar produto')
    print('3 - Alterar produto')
    print('4 - Excluir produto')
    print('5 - Listar produtos')
    print('0 - Sair')
    
    # Lê a opção escolhida pelo usuário
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        # Inclui um novo produto na lista
        codigo = input( 'Código: ')
        nome = input('Nome: ')
        quantidade = input('Quantidade: ')
        produtos.append({'codigo':codigo, 'nome':nome, 'quantidade':int(quantidade)})
        
        # Grava a lista de produtos no arquivo
        with open('produtos.txt', 'w') as arquivo:
            for produto in produtos :
                arquivo.write(f"{produto['codigo']},{produto['nome']},{produto['quantidade']}\n")
        
        print('Produto incluído com sucesso! ')

    elif opcao == '2':
        # Consulta um produto na lista
        codigo = input('Código: ')
        for produto in produtos:
            if produto['codigo'] == codigo:
                print(f"Nome: {produto['nome']}" )
                print(f"Quantidade: {produto['quantidade']}")
                break
        else:
            print('Produto não encontrado! ')
    
    elif opcao == '3':
        # Altera um produto na lista
        codigo = input( 'Código: ')
        for produto in produtos:
            if produto['codigo'] == codigo:
                nome = input('Novo nome: ')
                quantidade = input( 'Nova quantidade: ')
                produto['nome'] = nome
                produto['quantidade'] = int(quantidade)

                # Grava a lista de produtos no arquivo
                with open('produtos.txt','w') as arquivo:
                    for produto in produtos:
                        arquivo.write(f"{produto['codigo']}, {produto['nome']} , {produto['quantidade']}\n")
                    
                    print('Produto alterado com sucesso!')
                    break
            else:
                print('Produto não encontrado!')
    
    elif opcao == '4':
        # Exclui um produto na lista
        codigo = input('Código: ')
        for i, produto in enumerate(produtos):
            if produto['codigo'] == codigo:
                del produtos [i]

                # Grava a lista de produtos no arquivo
                with open('produtos.txt','w') as arquivo:
                    for produto in produtos:
                        arquivo.write(f"{produto['codigo']}, {produto['nome']}, {produto['quantidade']}\n")
                
                print('Produto excluído com sucesso!')
                break
        else:
            print('Produto não encontrado!')
    
    elif opcao == '5':
        # Lista todos os produtos da lista
        print('Lista de produtos:')
        for produto in produtos:
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
    
    elif opcao == '0':
        break