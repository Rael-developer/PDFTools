from pathlib import Path

import streamlit as st
import pypdf 

from utilidades import pegar_dados_pdf

def exibir_menu_marca_dagua(coluna):
   with coluna:
      st.markdown("""
      # Adicionar marca d'água

      Selecione um arquivo PDF e uma marca d'água nos seletores abaixo:                 
      """)

      arquivo_pdf = st.file_uploader(
         label='Selecione o arquivo PDF...',
         type='pdf',
         accept_multiple_files=False,
      )
      arquivo_marca = st.file_uploader(
         label="Selecione o arquivo contendo a marca d'água...",
         type='pdf',
         accept_multiple_files=False,
      )
      if arquivo_pdf and arquivo_marca:
         botoes_desativados = False
      else:
         botoes_desativados = True
   clicou_processar = st.button(
        'Clique para processar o arquivo PDF...',
        use_container_width=True,
        disabled=botoes_desativados,
    )
   if clicou_processar:
      dados_pdf = adicionar_marca_dagua(arquivo_pdf=arquivo_pdf, arquivo_marca=arquivo_marca)
      nome_arquivo = f'{Path(arquivo_pdf.name).stem}_marca.pdf'
      st.download_button(
         'Clique para fazer download do arquivo PDF...',
         type='primary',
         data=dados_pdf,
         file_name=nome_arquivo,
         mime='application/pdf',
         use_container_width=True,
      )
      
def adicionar_marca_dagua(arquivo_pdf, arquivo_marca):
   pagina_marca = pypdf.PdfReader(arquivo_marca).pages[0]
   escritor = pypdf.PdfWriter(clone_from=arquivo_pdf)
   for pagina in escritor.pages:
      escala_x = pagina.mediabox.width / pagina.mediabox.width
      escala_y = pagina.mediabox.height / pagina.mediabox.height
      transf = pypdf.Transformation().scale(escala_x, escala_y)
      pagina.merge_transformed_page(pagina_marca, transf, over=False)
   dados_pdf = pegar_dados_pdf(escritor=escritor)
   return dados_pdf
 