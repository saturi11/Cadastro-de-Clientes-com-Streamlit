# Cadastro de Clientes com Streamlit

Este é um projeto simples de uma aplicação web para o **Cadastro e Exibição de Clientes** utilizando **Streamlit** e **Pandas**. A aplicação permite que você cadastre novos clientes, visualize os clientes já cadastrados, filtre os registros por nome ou tipo de cliente e faça o download da lista de clientes em formato CSV.

## Funcionalidades

- **Cadastro de Clientes**: Cadastre clientes com nome, data de nascimento e tipo (Pessoa Física ou Jurídica).
- **Validação de Dados**: A data de nascimento não pode ser no futuro, e o nome do cliente deve ser preenchido.
- **Exibição de Clientes**: Exibe todos os clientes cadastrados em uma tabela interativa.
- **Filtragem de Dados**: Permite filtrar os clientes cadastrados por nome ou tipo.
- **Download de Dados**: Baixe a lista de clientes filtrados em formato CSV.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Python**: Linguagem de programação utilizada para a lógica da aplicação.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Instalar as dependências listadas no arquivo `requirements.txt`

### Passos

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/cadastro-clientes-streamlit.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd cadastro-clientes-streamlit
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o projeto:

    ```bash
    streamlit run app.py
    ```

5. Acesse a aplicação em seu navegador:

    ```
    http://localhost:8501
    ```

## Arquivos do Projeto

- **app.py**: Arquivo principal da aplicação. Contém a lógica para cadastro e exibição dos clientes.
- **clientes.csv**: Arquivo onde os dados dos clientes são armazenados. Ele é atualizado automaticamente quando um novo cliente é cadastrado.
- **requirements.txt**: Arquivo contendo as dependências do projeto (Streamlit e Pandas).

## Como Usar

1. Abra a aplicação localmente.
2. **Cadastro de Clientes**:
   - Insira o nome do cliente.
   - Selecione a data de nascimento.
   - Escolha o tipo de cliente (Pessoa Física ou Pessoa Jurídica).
   - Clique no botão **Cadastrar**.
3. **Exibir Clientes**:
   - Todos os clientes cadastrados são exibidos automaticamente.
   - Use o campo de busca para procurar clientes pelo nome.
   - Filtre os clientes por tipo (Pessoa Física ou Jurídica).
   - Faça o download da tabela filtrada em formato CSV clicando no botão **Baixar clientes em CSV**.

## Estrutura do Projeto
cadastro-clientes-streamlit/

├── app.py               # Arquivo principal da aplicação (lógica de cadastro e exibição de clientes)

├── clientes.csv         # Arquivo de dados dos clientes cadastrados

├── requirements.txt     # Lista de dependências necessárias para o projeto

└── README.md            # Documentação completa do projeto

## Melhorias Futuras

- **Validações mais robustas**: Verificar melhor a entrada de dados, como evitar nomes vazios ou duplicados.
- **Paginação da tabela**: Implementar paginação para melhor visualização em grandes volumes de dados.
- **Autenticação**: Adicionar um sistema de login para proteção dos dados.
