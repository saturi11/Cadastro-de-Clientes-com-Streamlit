import streamlit as st
import pandas as pd

# Carregar os dados do CSV
dados = pd.read_csv("clientes.csv")

# Título da página
st.set_page_config(page_title="Clientes cadastrados", page_icon="📋")
st.title("Clientes Cadastrados")

# Verifica se há dados no arquivo CSV
if not dados.empty:
    # Adiciona uma linha divisória
    st.divider()

    # Mostra o número total de clientes cadastrados
    st.subheader(f"Total de clientes cadastrados: {len(dados)}")

    # Adiciona um campo de busca para filtrar os clientes por nome
    filtro_nome = st.text_input("Buscar cliente pelo nome")

    # Adiciona um filtro para o tipo de cliente
    filtro_tipo = st.selectbox(
        "Filtrar por tipo de cliente",
        options=["Todos", "Pessoa Fisica", "Pessoa Juridica"],
    )

    # Aplica os filtros
    if filtro_nome:
        dados = dados[dados["nome"].str.contains(filtro_nome, case=False, na=False)]

    if filtro_tipo != "Todos":
        dados = dados[dados["tipo"] == filtro_tipo]

    # Exibe a tabela com os dados filtrados
    st.dataframe(dados)

    # Adiciona um botão para baixar os dados filtrados como CSV
    csv = dados.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Baixar clientes em CSV",
        data=csv,
        file_name="clientes_filtrados.csv",
        mime="text/csv",
    )
else:
    st.warning("Nenhum cliente cadastrado no momento.")
