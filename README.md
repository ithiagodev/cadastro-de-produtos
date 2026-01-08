# **Sistema de Cadastro de Produtos (CRUD)**

O **Sistema de Cadastro de Produtos (CRUD)** foi desenvolvido em **Python** e permite **criar, listar, atualizar e deletar produtos** por meio de um menu interativo no terminal.
Os dados são armazenados utilizando **SQLite**, garantindo simplicidade, portabilidade e fácil manutenção sem necessidade de servidor externo.

---

## **Funcionalidades**

* Adicionar novos produtos
* Listar todos os produtos ou um produto específico por ID
* Atualizar informações de produtos existentes
* Deletar produtos do banco de dados
* Validações de entrada para evitar dados inválidos

---

## **Tecnologias Utilizadas**

* **Python 3**
* **SQLite3** (banco de dados embutido)
* Interface via **terminal (CLI)**

---

## **Requisitos**

Certifique-se de ter o seguinte instalado em sua máquina:

* **Python 3.10 ou superior**
* Sistema operacional compatível com Python (Windows, Linux ou macOS)

> **Obs:**
> Este projeto utiliza apenas bibliotecas padrão do Python, portanto **não é necessário instalar dependências externas**.

---

## **Estrutura dos Arquivos**

```
├── app.py
├── models.py
└── products.db (gerado automaticamente)
```

### **Descrição dos Arquivos**

### **`app.py`**

Arquivo principal do sistema.
Responsável por:

* Exibir o menu de opções
* Receber entradas do usuário
* Validar dados informados
* Chamar as funções de banco de dados definidas em `models.py`

### **`models.py`**

Arquivo responsável pela lógica de banco de dados. Contém as funções:

* **`create_table()`** → Cria a tabela de produtos caso não exista
* **`create_product()`** → Insere um novo produto no banco
* **`get_product()`** → Retorna todos os produtos ou um produto específico por ID
* **`update_product()`** → Atualiza campos de um produto existente
* **`delete_product()`** → Remove um produto do banco de dados

### **`products.db`**

Arquivo do banco de dados SQLite.
É criado automaticamente ao executar o sistema pela primeira vez.

---

## **Estrutura da Tabela**

A tabela `products` é criada automaticamente com a seguinte estrutura:

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0)
);
```

---

## **Como Executar o Projeto**

1. **Clone ou baixe o repositório**
2. Abra o terminal na pasta do projeto
3. Execute o comando:

```bash
python app.py
```

---

## **Menu do Sistema**

Ao iniciar o programa, o seguinte menu será exibido:

```
1. Adicionar produto
2. Listar produtos
3. Atualizar produtos
4. Deletar produtos
5. Sair
```

---

## **Fluxo de Funcionamento**

### **1. Adicionar Produto**

O usuário informa:

* Nome do produto
* Descrição
* Preço
* Quantidade em estoque

O sistema valida os dados e salva o produto no banco.

---

### **2. Listar Produtos**

* Digite `0` para listar **todos os produtos**
* Digite um **ID específico** para visualizar apenas um produto

---

### **3. Atualizar Produto**

* Informe o ID do produto
* Pressione **ENTER** para manter o valor atual de qualquer campo
* Apenas os campos alterados serão atualizados no banco

---

### **4. Deletar Produto**

* Informe o ID do produto
* O sistema confirma se o produto existe antes de remover

---

### **5. Sair**

Finaliza a execução do programa.

---

## **Validações Implementadas**

* Nome do produto não pode ser vazio
* Preço não pode ser negativo
* Estoque não pode ser negativo
* ID deve ser um número válido e maior que zero

---

**Dica:**
Este projeto é ideal para portfólio iniciante/intermediário e pode ser facilmente adaptado para outros tipos de cadastro.