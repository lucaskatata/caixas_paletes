# %%
import pandas as pd
import streamlit as st

arquivo = r"D:\Lucas\GitHub\caixas_paletes\dados.xlsx"

df = pd.read_excel(arquivo, sheet_name='tabela')


df['SKU CAIXA'] = df['SKU CAIXA'].str.upper()

st.set_page_config(layout='wide', page_icon='📦', page_title='MF - localização caixas')
st.title('MF - Localização caixas paletes')

sku = st.text_input('Pesquisar sku')

if not sku:
    st.stop()
else:    
    sku = (sku.replace(' ', '_') + '_lj').upper()
    palete = df[df['SKU CAIXA'] == sku].iloc[0]['PALET (40 +-)']
    posicao = df[df['SKU CAIXA'] == sku].iloc[0]['POSIÇÃO (1 A 12)']
    st.metric(label='SKU', value=sku)   
    st.metric(label='Palete', value=palete)
    st.metric(label='Posição', value=posicao)

