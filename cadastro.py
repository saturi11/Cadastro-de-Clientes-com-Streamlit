import streamlit as st
import pandas as pd
from datetime import date


# Função para gravar os dados do cliente no arquivo "clientes.csv"
def gravar_dados(nome, data_nasc, tipo):
    # Verifica se o nome foi preenchido e se a data de nascimento é válida (anterior ou igual à data atual)
    if nome and data_nasc <= date.today():
        # Abre o arquivo "clientes.csv" no modo de append (adicionar novos dados) e com codificação UTF-8
        with open("clientes.csv", "a", encoding="utf-8") as file:
            # Escreve os dados do cliente (nome, data de nascimento e tipo) no arquivo, separados por vírgulas
            file.write(f"{nome},{data_nasc},{tipo}\n")
        # Define o estado de sucesso no Streamlit, usado para informar o usuário sobre o sucesso da operação
        st.session_state["sucesso"] = True
    else:
        # Se os dados forem inválidos, o estado de sucesso é definido como False
        st.session_state["sucesso"] = False


# Configura a página no Streamlit com título e ícone
st.set_page_config(
    page_title="Cadastro de clientes",  # Título da página
    page_icon="📖",  # Ícone que aparece no navegador
)

# Título principal da página
st.title("Cadastro de clientes")

# Adiciona uma linha divisória na interface do Streamlit
st.divider()

# Campo de entrada de texto para o nome do cliente
nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

# Campo de entrada de data para a data de nascimento do cliente
dt_nasc = st.date_input("Data de nascimento", format="DD/MM/YYYY")

# Dropdown para selecionar o tipo de cliente: Pessoa Física ou Pessoa Jurídica
tipo = st.selectbox("Tipo de cliente", ["Pessoa Fisica", "Pessoa Juridica"])

# Botão para cadastrar o cliente; quando clicado, chama a função `gravar_dados` com os argumentos nome, dt_nasc, e tipo
btn_cadastrar = st.button(
    "Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, tipo]
)

# Verifica se o botão foi clicado e exibe uma mensagem de sucesso ou erro com base no estado
if btn_cadastrar:
    if st.session_state["sucesso"]:
        # Exibe uma mensagem de sucesso se o cliente for cadastrado corretamente
        st.success("cliente cadastrado com  sucesso!", icon="🔥")
    else:
        # Exibe uma mensagem de erro se houver problemas ao cadastrar o cliente
        st.error(
            "Erro ao cadastrar cliente. Verifique os dados e tente novamente.",
            icon="😢",
        )
