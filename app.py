import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Datathon - Passos Mágicos"
)

tab0, tab1 = st.tabs(["Introdução", "Visão Geral dos Dados"])

with tab0:      

    st.markdown("## Introdução")

    paragrafo1_tab0 = 'Em um mundo marcado por desigualdades sociais, as organizações não governamentais (ONGs) desempenham um papel fundamental na construção de comunidades mais justas e inclusivas. Entre essas instituições, a "Passos Mágicos" se destaca como um farol de esperança. Fundada em 1992 por Michelle Flues e Dimetri Ivanoff, a ONG evoluiu significativamente ao longo dos anos, expandindo sua atuação e aprimorando sua abordagem para oferecer não apenas educação, mas também suporte psicológico, desenvolvimento pessoal e comunitário a crianças e jovens de baixa renda do município de Embu-Guaçu.'
    paragrafo2_tab0 = 'Ao analisar os dados históricos e atuais da organização, buscamos entender não apenas as tendências educacionais, mas também os fatores emocionais e sociais que moldam o progresso dos beneficiados pela ONG. A identificação de elementos-chave de sucesso permitirá não apenas reconhecer, mas também amplificar os aspectos mais eficazes do trabalho da "Passos Mágicos" e, desse modo, fortalecer o impacto positivo que a ONG traz para as vidas de tantos jovens e crianças, ao oferecer-lhes não apenas educação, mas também a esperança de um futuro melhor.'
    paragrafo3_tab0 = 'A base de dados utilizada na execução deste trabalho foi fornecida pela equipe da "Passos Mágicos" e contém registros detalhados do acompanhamento de cada aluno. Esta base abrange uma variedade de informações, incluindo indicadores de desempenho e observações relevantes, durante todo o período em que os alunos estiveram vinculados à ONG.'

    texto_justificado_tab0 = f"""
        <p style="text-align: justify;">{paragrafo1_tab0}</p>
        <p style="text-align: justify;">{paragrafo2_tab0}</p>     
        <p style="text-align: justify;">{paragrafo3_tab0}</p>     
    """

    st.markdown(texto_justificado_tab0, unsafe_allow_html=True) 

with tab1:      

    st.markdown("## Visão Geral dos Dados")