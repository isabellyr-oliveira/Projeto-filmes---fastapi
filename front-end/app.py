# pip install streamlit requests
import streamlit as st
import requests

#Rodar o stramlit 
# python -m streamlit run app.py
#URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de Filmes")

menu = st.sidebar.radio("Menu",
    ["Listar Filmes", "Cadastrar Filme"]
    )
if menu == "Listar Filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
       filmes = response.json().get("filmes", [])
    else:
        st.error("Erro ao tentar conectar com a API.")