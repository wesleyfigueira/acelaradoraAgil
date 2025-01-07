# AGILSTORE CRUD

## Descrição
Este projeto é um sistema CRUD (Create, Read, Update, Delete) simples para gerenciamento de produtos em um estoque. Ele permite cadastrar, listar, atualizar, excluir e buscar produtos de maneira interativa, utilizando um arquivo JSON para armazenamento dos dados.

---

## Funcionalidades

### 1. **Adicionar Produto**
- Permite adicionar novos produtos ao estoque.
- Os dados solicitados são:
  - Nome do produto
  - Categoria
  - Quantidade em estoque
  - Preço

### 2. **Listar Produtos**
- Exibe todos os produtos cadastrados em uma tabela formatada.
- A tabela inclui:
  - ID
  - Nome
  - Categoria
  - Quantidade
  - Preço

### 3. **Atualizar Produto**
- Permite atualizar os dados de um produto existente.
- O sistema solicita o ID do produto e os novos valores para:
  - Nome
  - Categoria
  - Quantidade
  - Preço

### 4. **Excluir Produto**
- Exclui um produto do estoque pelo ID.
- Antes da exclusão, o sistema exibe os detalhes do produto e solicita confirmação.

### 5. **Buscar Produto**
- Permite buscar produtos pelo ID ou pelo nome (ou parte do nome).
- Exibe os detalhes dos produtos encontrados.

### 6. **Navegação por Menu**
- Menu inicial para acessar o estoque ou sair do sistema.
- Menu interno com as opções CRUD e voltar ao menu anterior.

---

## Requisitos

- Python 3.6 ou superior
- Biblioteca externa:
  - `tabulate`: utilizada para exibir os produtos em formato de tabela.

Instale a biblioteca necessária com o comando:
```bash
pip install tabulate
```

---

## Como Usar

### 1. **Executando o Sistema**
Execute o script diretamente:
```bash
python nome_do_arquivo.py
```

### 2. **Interação no Sistema**
- Escolha as opções no menu inicial e no menu interno para realizar as operações desejadas.
- As operações de entrada de dados são interativas e guiadas.

---

## Estrutura de Arquivos

- **`estoque_produtos.json`**: Arquivo onde os dados dos produtos são armazenados.
- **`nome_do_arquivo.py`**: Script principal do sistema.

---

## Funcionalidades Técnicas

### **Estrutura do Arquivo JSON**
Cada produto é armazenado no arquivo `estoque_produtos.json` com o seguinte formato:
```json
[
  {
    "id": 1,
    "nome": "Produto Exemplo",
    "categoria": "Categoria Exemplo",
    "quantidade": 10,
    "preco": 29.99
  }
]
```

### **Principais Funções**
- `carregar_produtos`: Carrega os dados do arquivo JSON.
- `adicionar_produtos`: Adiciona um novo produto ao JSON.
- `listar_produtos`: Lista os produtos em formato de tabela.
- `atualizar_produto`: Atualiza os dados de um produto existente.
- `excluir_produto`: Remove um produto do JSON.
- `buscar_produto`: Busca produtos por ID ou nome.

---



## Contato
Em caso de dúvidas ou sugestões, entre em contato:
- **Email**: Wesleyfigueira1993@gmail.com
- **GitHub**: [wesleyfigueira](https://github.com/wesleyfigueira)

