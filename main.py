# %%
import pandas as pd
import streamlit as st
import openpyxl
from pathlib import Path

# arquivo = Path(r"D:\Lucas\GitHub\caixas_paletes\dados.xlsx")

df = pd.read_excel('dados.xlsx', sheet_name='tabela')
st.subheader('MF - Localização caixas paletes')

df['SKU CAIXA'] = df['SKU CAIXA'].str.upper()
lista_sku = df['SKU CAIXA'].unique()

st.set_page_config(layout='wide', page_icon='📦', page_title='MF - localização caixas')

sku = st.text_input('Pesquisar sku')

if not sku:
    st.stop()
else:  
    sku = (sku.replace(' ', '_') + '_lj').upper()
    if sku in lista_sku:  
        palete = df[df['SKU CAIXA'] == sku]['PALET (40 +-)'].unique().tolist()
        posicao = df[df['SKU CAIXA'] == sku].iloc[0]['POSIÇÃO (1 A 12)']
        st.metric(label='SKU', value=sku)   
        # st.metric(label='Palete', value=palete)
        # st.text(f'Paletes: {palete}')

        col1, col2, col3 = st.columns(3)

        col1.write('Palete:')
        for item in palete:
            col1.write(item)

        col2.metric(label='Posição', value=posicao)
    else:
        st.warning('SKU não encontrado')

# %%