# %%
import pandas as pd
import streamlit as st
import openpyxl
from pathlib import Path

# arquivo = Path(r"D:\Lucas\GitHub\caixas_paletes\dados.xlsx")

df = pd.read_excel('dados.xlsx', sheet_name='tabela')

df['SKU CAIXA'] = df['SKU CAIXA'].str.upper()
lista_sku = df['SKU CAIXA'].unique()

st.set_page_config(layout='wide', page_icon='📦', page_title='MF - localização caixas')
st.title('MF - Localização caixas paletes')

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
        st.text(f'Paletes: {palete}')
        st.metric(label='Posição', value=posicao)
    else:
        st.warning('SKU não encontrado')

# %%
df[df['SKU CAIXA'] == 'M16_400_BRANCO_LJ']