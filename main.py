import json
import os
from tabulate import tabulate


# Variável global para rastrear o ID atual
id_atual = 0

#Gerar Id aleatorio, e verificar o ultimo Id do Arquivo
def gerar_id(produtos):
    
    if produtos:
        return produtos[-1]['id'] + 1  
    else:
        return 1


# Função Carregar Usuarios
def carregar_produtos():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists("estoque_produtos.json"):
        with open("estoque_produtos.json", 'w') as f:
            json.dump([], f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open("estoque_produtos.json", 'r') as f:
        return json.load(f)


# Função Cadastrar Usuarios
def adicionar_produtos(nome_do_produto, categoria, quantidade_estoque,preco):
    
    produtos = carregar_produtos()
# novo usuario
    produtos.append({'id': gerar_id(produtos), 'nome': nome_do_produto, 'categoria': categoria,'quantidade': quantidade_estoque, 'preco': preco})


    with open("estoque_produtos.json", 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("😎 PRODUTO ADICIONADO COM SUCESSO!")
    
#Listar todos os produtos 
def listar_produtos():
 produtos = carregar_produtos()

 if produtos:
        # Cabeçalhos das colunas da tabela
        cabecalhos = ["ID", "NOME", "CATEGORIA", "QUANTIDADE", "PREÇO"]
        
        # Dados para a tabela (extraímos as informações dos produtos)
        tabela = [
            [produto['id'], produto['nome'], produto['categoria'], produto['quantidade'], produto['preco']]
            for produto in produtos
        ]
        
        # Exibir a tabela
        print("=" * 50)
        print("LISTA DE PRODUTOS:")
        print("-" * 50)
        print(tabulate(tabela, headers=cabecalhos, tablefmt="grid", stralign="center"))
        print("=" * 50)
 else:
        print("😒 NENHUM PRODUTO CADASTRADO.")
                   

def atualizar_produto(id_produto):
    produtos = carregar_produtos()

    # Verifica se o ID informado existe
    produto_encontrado = None
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_encontrado = produto
            break
    
    if produto_encontrado is None:
        print(f"😒 Produto com ID {id_produto} não encontrado.")
        return
    
    # Solicitar ao usuário quais campos deseja atualizar
    print("=" * 50)
    print(f"ID: {produto_encontrado['id']}")
    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Categoria: {produto_encontrado['categoria']}")
    print(f"Quantidade em Estoque: {produto_encontrado['quantidade']}")
    print(f"Preço: R$ {produto_encontrado['preco']:.2f}")
    print("=" * 50)
    
    nome = input(f"Novo Nome (atual: {produto_encontrado['nome']}): ")
    if nome:
        produto_encontrado['nome'] = nome
    
    categoria = input(f"Nova Categoria (atual: {produto_encontrado['categoria']}): ")
    if categoria:
        produto_encontrado['categoria'] = categoria
    
    try:
        quantidade = int(input(f"Nova Quantidade (atual: {produto_encontrado['quantidade']}): "))
        if quantidade >= 0:
            produto_encontrado['quantidade'] = quantidade
        else:
            print("Quantidade não pode ser negativa!")
            return
    except ValueError:
        print("Valor inválido para quantidade.")
        return
    
    try:
        preco = float(input(f"Novo Preço (atual: {produto_encontrado['preco']}): "))
        if preco >= 0:
            produto_encontrado['preco'] = preco
        else:
            print("Preço não pode ser negativo!")
            return
    except ValueError:
        print("Valor inválido para preço.")
        return

    # Atualizar o arquivo com as alterações
    with open("estoque_produtos.json", 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

    print("😎 Produto atualizado com sucesso!")



def excluir_produto(id_produto):
    produtos = carregar_produtos()

    # Verifica se o ID informado existe
    produto_encontrado = None
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_encontrado = produto
            break
    
    if produto_encontrado is None:
        print(f"😒 Produto com ID {id_produto} não encontrado.")
        return
    
    # Exibir os detalhes do produto e pedir confirmação
    print("=" * 50)
    print(f"ID: {produto_encontrado['id']}")
    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Categoria: {produto_encontrado['categoria']}")
    print(f"Quantidade em Estoque: {produto_encontrado['quantidade']}")
    print(f"Preço: R$ {produto_encontrado['preco']:.2f}")
    print("=" * 50)
            
    confirmacao = input(f"Você tem certeza que deseja excluir o produto '{produto_encontrado['nome']}' (ID: {id_produto})? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Ação de exclusão cancelada.")
        return

    # Remover o produto da lista
    produtos.remove(produto_encontrado)

    # Atualizar o arquivo com a lista de produtos após a exclusão
    with open("estoque_produtos.json", 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

    print(f"😎 Produto '{produto_encontrado['nome']}' excluído com sucesso!")

#Buscar Produto  Solicita o usuario buscar o produto do json
def buscar_produto():
    produtos = carregar_produtos()

    if not produtos:
        print("😒 Nenhum produto cadastrado no inventário.")
        return

    # Solicitar ao usuário o critério de busca (ID ou Nome)
    criterio = input("Deseja buscar por [1] ID ou [2] Nome? Digite o número: ").strip()
    
    if criterio == "1":
        try:
            id_produto = int(input("Digite o ID do produto: ").strip())
            resultados = [produto for produto in produtos if produto['id'] == id_produto]
        except ValueError:
            print("❌ ID inválido! Deve ser um número inteiro.")
            return
    elif criterio == "2":
        nome_produto = input("Digite parte do nome do produto: ").strip().lower()
        resultados = [produto for produto in produtos if nome_produto in produto['nome'].lower()]
    else:
        print("❌ Opção inválida! Digite [1] ou [2].")
        return

    # Exibir resultados
    if resultados:
        print("=" * 50)
        print("Produto(s) encontrado(s):")
        print("-" * 50)
        for produto in resultados:
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Quantidade em Estoque: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("=" * 50)
    else:
        print("😒 Nenhum produto encontrado com o critério fornecido.")

    
def menu_inicial():
    print("=" *55 )
    print( " ---->>> BEM VINDO A AGILSTORE <<<---- ")
    print("          1 - ACESSAR ESTOQUE ")
    print("          2 - SAIR ")
    print("=" *55 )


def limpar_tela():
    os.system("cls")


def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR NOVO PRODUTO")
    print("2. LISTAR PRODUTOS")
    print("3. ATUALIZAR PRODUTO")
    print("4. EXCLUIR PRODUTO")
    print("5. BUSCAR PRODUTO")
    print("6. VOLTAR AO MENU ANTERIOR")

def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO:\n>>> "))
        
        
        match (opcao_inicial):
            case 1:
            
                limpar_tela()
                
                while True:
                  exibir_menu()
                  opcao = int(input("ESCOLHA UMA OPÇÃO:\n>>>"))
                  
                  match (opcao):
                      
                        case 1:
                            print("DIGITE OS DADOS DO PRODUTO:")
                            nome_produto = input("NOME DO PRODUTO: \n>>>")
                            categoria = input("CATEGORIA DO PRODUTO: \n>>>")
                            quantidade_estoque = int(input("QUANTIDADE DO PRODUTO:\n>>>"))
                            preco = float(input("PREÇO DO PRODUTO\n>>>"))
                          
                          
                            adicionar_produtos(nome_produto,categoria,quantidade_estoque,preco)
                          
                        case 2 :
                            limpar_tela()
                            listar_produtos()
                            
                        case 3:
                            limpar_tela()
                            print("DIGITE O |ID| DO PRODUTO  A SER ATUALIZADO:")
                            nome_produto = int(input("NOME DO PRODUTO: \n>>>"))
                            atualizar_produto(nome_produto)
                            
                        case 4:
                            limpar_tela()
                            print("DIGITE O |ID| DO PRODUTO  A SER EXCLUIDO:")
                            nome_produto = int(input("NOME DO PRODUTO: \n>>>"))
                            excluir_produto(nome_produto)
                        case 5:
                            
                            limpar_tela()
                            buscar_produto()
                        case 6:
                            break
                        
                        case __:
                            limpar_tela()
                            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!") 
                            
                        
                      
                    
            case 2:
                limpar_tela()
                break
            case __:
                limpar_tela()
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
        
        



if __name__ == "__main__":
    main()