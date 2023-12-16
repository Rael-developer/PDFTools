import streamlit as st
from streamlit_option_menu import option_menu

import menu_combinar
import menu_extrair
import menu_marca_dagua
import menu_imagens

st.set_page_config(
    page_title='PDFTools',
    page_icon=':page_facing_up:',
    layout='wide',
)

_, col2, _ = st.columns(3)

with col2:
    st.title('PDFTools')
    st.markdown("""
    ### Escolha a opção desejada abaixo:      
    """)

entradas_menu = {
    'Extrair página': 'file-earmark-pdf-fill',
    'Combinar PDFs': 'plus-square-fill',
    "Adicionar marca d'água": 'droplet-fill',
    'Imagens para PDF': 'file-earmark-richtext-fill',
}

escolha = option_menu(
    menu_title=None,
    orientation='horizontal',
    options=list(entradas_menu.keys()),
    icons=list(entradas_menu.values()),
    default_index=0,
)

_, col2, _ = st.columns(3)
with col2:
    if escolha == 'Extrair página':
        menu_extrair.exibir_menu_extrair(coluna=col2)
    elif escolha == 'Combinar PDFs':
        menu_combinar.exibir_menu_combinar(coluna=col2)
    elif escolha == "Adicionar marca d'água":
        menu_marca_dagua.exibir_menu_marca_dagua(coluna=col2)
    elif escolha == 'Imagens para PDF':
        st.write('Clicou imagens')
        menu_imagens.exibir_menu_imagens(coluna=col2)
