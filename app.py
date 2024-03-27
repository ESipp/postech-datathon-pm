import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

st.set_page_config(
    page_title="Datathon - Passos Mágicos"
)

st.title('Passos Mágicos - Analytics')


tab0, tab1, tab2, tab3, tab4 = st.tabs(["Introdução", "Visão Geral dos Dados", "Forecast e What-if", "Ponto de Virada", "IDEB"])

with tab0:      

    st.markdown("## Introdução")

    paragrafo1_tab0 = 'Em um mundo marcado por desigualdades sociais, as organizações não governamentais (ONGs) desempenham um papel fundamental na construção de comunidades mais justas e inclusivas. Entre essas instituições, a <a href="https://passosmagicos.org.br/" target="_blank"><b>Passos Mágicos</b></a> se destaca como um farol de esperança. Fundada em 1992 por Michelle Flues e Dimetri Ivanoff, a ONG evoluiu significativamente ao longo dos anos, expandindo sua atuação e aprimorando sua abordagem para oferecer não apenas educação, mas também suporte psicológico, desenvolvimento pessoal e comunitário a crianças e jovens de baixa renda do município de Embu-Guaçu.'
    paragrafo2_tab0 = 'Ao analisar os dados históricos e atuais da organização, buscamos entender não apenas as tendências educacionais, mas também os fatores emocionais e sociais que moldam o progresso dos beneficiados pela ONG. A identificação de elementos-chave de sucesso permitirá não apenas reconhecer, mas também amplificar os aspectos mais eficazes do trabalho da <a href="https://passosmagicos.org.br/" target="_blank"><b>Passos Mágicos</b></a> e, desse modo, fortalecer o impacto positivo que a ONG traz para as vidas de tantos jovens e crianças, ao oferecer-lhes não apenas educação, mas também a esperança de um futuro melhor.'
    paragrafo3_tab0 = 'A base de dados utilizada na execução deste trabalho foi fornecida pela equipe da <a href="https://passosmagicos.org.br/" target="_blank"><b>Passos Mágicos</b></a> e contém registros detalhados do acompanhamento de cada aluno. Esta base abrange uma variedade de informações, incluindo indicadores de desempenho e observações relevantes, durante todo o período em que os alunos estiveram vinculados à ONG.'

    texto_justificado_tab0 = f"""
        <p style="text-align: justify;">{paragrafo1_tab0}</p>
        <p style="text-align: justify;">{paragrafo2_tab0}</p>     
        <p style="text-align: justify;">{paragrafo3_tab0}</p>     
    """

    st.markdown(texto_justificado_tab0, unsafe_allow_html=True) 

with tab1:      

    st.markdown("## Visão Geral dos Dados")

    paragrafo1_tab1 = 'O primeiro passo para entender a relevância e o impacto da <b>Passos Mágicos</b> é analisar os números macros da ONG ao longo dos anos.'

    texto_justificado_tab1 = f"""
        <p style="text-align: justify;">{paragrafo1_tab1}</p>
    """

    st.markdown(texto_justificado_tab1, unsafe_allow_html=True) 

    df_dados_gerais = pd.read_csv('dados/dados_gerais.csv', delimiter=';', thousands='.')


    # Criando o gráfico de colunas para alunos, bolsistas e universitários
    fig1 = go.Figure()

    # Adicionando colunas para alunos, bolsistas e universitários
    fig1.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Alunos'], name='Alunos'))
    fig1.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Bolsistas'], name='Bolsistas'))
    fig1.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Universitarios'], name='Universitários'))

    # Personalizando o layout do primeiro gráfico
    fig1.update_layout(title='Número de Alunos, Bolsistas e Universitários ao Longo dos Anos',
                    xaxis_title='Ano',
                    yaxis_title='Número',
                    barmode='group',
                    legend_title='Grupo')

    # Exibindo o primeiro gráfico
    st.plotly_chart(fig1)

    paragrafo2_tab1 = 'É evidente o crescimento do número de alunos ao longo do tempo, o que iniciou-se com 70 alunos em 2016 já atingia 1.100 alunos ainda no ano de 2023. Destaca-se o aumento de cerca de 329% ocorrido entre 2016 e 2017.'
    paragrafo3_tab1 = 'Além disso, com o desenvolvimento da ONG é visto que também surgiram bolsistas e universitários. Outro destaque é a variação do número de universitários entre 2019 (2) para 2020 (26) gerando um aumento de 1.200%'

    texto_justificado_1_tab1 = f"""
        <p style="text-align: justify;">{paragrafo2_tab1}</p>     
        <p style="text-align: justify;">{paragrafo3_tab1}</p>     
    """

    st.markdown(texto_justificado_1_tab1, unsafe_allow_html=True) 

    # Criando o gráfico de colunas para professores, psicólogos, psicopedagogos, psiquiatras e assistentes sociais
    fig2 = go.Figure()

    # Adicionando colunas para professores, psicólogos, psicopedagogos, psiquiatras e assistentes sociais
    fig2.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Professores'], name='Professores'))
    fig2.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Psicologos'], name='Psicólogos'))
    fig2.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Psicopedagogos'], name='Psicopedagogos'))
    fig2.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Psiquiatras'], name='Psiquiatras'))
    fig2.add_trace(go.Bar(x=df_dados_gerais['Ano'], y=df_dados_gerais['Assistentes_Sociais'], name='Assistentes Sociais'))

    # Personalizando o layout do segundo gráfico
    fig2.update_layout(title='Número de Professores e Profissionais de Apoio ao Longo dos Anos',
                    xaxis_title='Ano',
                    yaxis_title='Número',
                    barmode='group',
                    legend_title='Grupo')

    # Exibindo o segundo gráfico
    st.plotly_chart(fig2)
    
    paragrafo4_tab1 = 'Obviamente, esse crescimento só foi possível devido ao crescimento dos profissionais trabalhando na <b>Passos Mágicos</b>. É interessante analisar como o crescimento dos professores ocorreu praticamente de forma linear, mostrando avanço em todos os anos com exceção do ano de 2020 fortemente atingido pela Pandemia de COVID-19.'
    paragrafo5_tab1 = 'Acrescentado a isso, o crescimento da ONG também oportunizou a entrada de novos profissionais chegando a um total de 22 no ano de 2023.'

    texto_justificado_2_tab1 = f"""
        <p style="text-align: justify;">{paragrafo4_tab1}</p>
        <p style="text-align: justify;">{paragrafo5_tab1}</p>
    """
    
    st.markdown(texto_justificado_2_tab1, unsafe_allow_html=True)


    df_dados_gerais['Total_Alunos'] = df_dados_gerais[['Alunos', 'Bolsistas', 'Universitarios']].sum(axis=1)
    df_dados_gerais['Total_Profissionais'] = df_dados_gerais[['Professores', 'Psicologos', 'Psicopedagogos', 'Psiquiatras', 'Assistentes_Sociais']].sum(axis=1)


    # Criando o gráfico de linha para a soma dos alunos e dos profissionais ao longo dos anos
    fig = go.Figure()

    # Adicionando linhas para a soma dos alunos e dos profissionais
    fig.add_trace(go.Scatter(x=df_dados_gerais['Ano'], y=df_dados_gerais['Total_Alunos'], mode='lines', name='Total de Alunos'))

    # Adicionando uma segunda escala para os profissionais
    fig.add_trace(go.Scatter(x=df_dados_gerais['Ano'], y=df_dados_gerais['Total_Profissionais'], mode='lines', name='Total de Profissionais', yaxis='y2'))

    # Personalizando o layout do gráfico
    fig.update_layout(title='Total de Alunos e Profissionais ao Longo dos Anos',
                    xaxis_title='Ano',
                    yaxis_title='Total de Alunos',
                    legend_title='Grupo',
                    yaxis2=dict(title='Total de Profissionais', overlaying='y', side='right'))

    # Exibindo o gráfico
    st.plotly_chart(fig)
    
    paragrafo6_tab1 = 'Podemos analisar essa relação traçando as linhas de Total de Alunos e Total de Profissionais ao longo dos anos - por questões de escala, foi utilizado um eixo secundário para o número de profissionais. Ao criar essa análise podemos ver que ambas séries acompanham uma tendência de crescimento similar o que só fomenta o entendimento de que o crescimento do número de alunos auxiliados pela ONG é diretamente ligado pela estrutura que a mesma consegue proporcionar. Esse fato reitera a importância de investimentos e "padrinhos" para manter e reforçar essa tendência.'

    texto_justificado_3_tab1 = f"""
        <p style="text-align: justify;">{paragrafo6_tab1}</p>
    """
    
    st.markdown(texto_justificado_3_tab1, unsafe_allow_html=True) 

    # Removendo a coluna de ano
    df_dados_sem_ano = df_dados_gerais.drop(columns=['Ano'])

    # Calculando a matriz de correlação
    correlation_matrix = df_dados_sem_ano.corr()

    # Criando um heatmap com Seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlação')

    # Exibindo o heatmap
    st.pyplot(plt)

    paragrafo7_tab1 = 'De uma maneira mais técnica, podemos analisar a matriz de correlação destes dados. Obviamente, muitos números estão correlacionados então o foco é analisar a relação do total de alunos com total de profissionais onde temos uma correlação positiva de 0.9. Embora não se possa afirmar, é fortemente identificada essa relação como uma causalidade onde o crescimento da <b>Passos Mágicos</b> possibilita a mesma a ajudar mais e mais crianças e adolescentes.'

    texto_justificado_4_tab1 = f"""
        <p style="text-align: justify;">{paragrafo7_tab1}</p>
    """
    
    st.markdown(texto_justificado_4_tab1, unsafe_allow_html=True)



with tab2:   
    st.markdown("## Forecast")
    
    paragrafo1_tab2 = 'Para entender o impacto do crescimento da <b>Passos Mágicos</b> foram aplicadas as seguintes técnicas de forecast: Média Móvel Simples, Regressão Linear Simples, Método Naive, Random Forest e Suavização Exponencial Simples.'

    texto_justificado_tab2 = f"""
        <p style="text-align: justify;">{paragrafo1_tab2}</p>
    """
    
    st.markdown(texto_justificado_tab2, unsafe_allow_html=True) 

    # Dados existentes
    anos_exist = df_dados_gerais['Ano'].values
    alunos_exist = df_dados_gerais['Alunos'].values

    # Previsão com média móvel simples
    media_movel = np.mean(alunos_exist)
    forecast_media_movel = np.full(len(anos_exist) + 5, media_movel)
    forecast_media_movel = np.round(forecast_media_movel).astype(int)
    

    # Previsão com regressão linear simples
    modelo_regressao = LinearRegression()
    modelo_regressao.fit(anos_exist.reshape(-1, 1), alunos_exist)
    anos_futuros_regressao = np.arange(anos_exist[0], anos_exist[-1] + 6).reshape(-1, 1)
    forecast_regressao = modelo_regressao.predict(anos_futuros_regressao)
    forecast_regressao = np.round(forecast_regressao).astype(int)

    # Previsão com método Naive
    last_observation = alunos_exist[-1]
    forecast_naive = np.full(len(anos_exist) + 5, last_observation)
    forecast_naive = np.round(forecast_naive).astype(int)

    # Previsão com Random Forest
    modelo_random_forest = RandomForestRegressor()
    modelo_random_forest.fit(anos_exist.reshape(-1, 1), alunos_exist)
    anos_futuros_rf = np.arange(anos_exist[0], anos_exist[-1] + 6).reshape(-1, 1)
    forecast_random_forest = modelo_random_forest.predict(anos_futuros_rf)
    forecast_random_forest = np.round(forecast_random_forest).astype(int)

    # Previsão com suavização exponencial simples
    modelo_suav_exp = SimpleExpSmoothing(alunos_exist)
    resultado_suav_exp = modelo_suav_exp.fit()
    forecast_suav_exp = resultado_suav_exp.forecast(len(anos_exist) + 5)
    forecast_suav_exp = np.round(forecast_suav_exp).astype(int)

    # Criando o gráfico com Plotly
    fig = go.Figure()

    # Adicionando dados existentes
    fig.add_trace(go.Scatter(x=anos_exist, y=alunos_exist, mode='lines+markers', name='Total de Alunos', line=dict(width=3)))

    # Adicionando previsões
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_media_movel, mode='lines', name='Média Móvel Simples', line=dict(dash='dash', width=1)))
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_regressao, mode='lines', name='Regressão Linear Simples', line=dict(dash='dash', color='green', width=1)))
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_naive, mode='lines', name='Método Naive', line=dict(dash='dash', width=1)))
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_random_forest, mode='lines', name='Random Forest', line=dict(dash='dash', width=1)))
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_suav_exp, mode='lines', name='Suavização Exponencial Simples', line=dict(dash='dash', width=1)))

    # Personalizando layout
    fig.update_layout(title='Previsões de Alunos desde o Início até os Próximos 5 Anos',
                    xaxis_title='Ano',
                    yaxis_title='Total de Alunos')

    # Exibindo o gráfico
    st.plotly_chart(fig)

    paragrafo2_tab2 = 'Devido ao tamanho pequeno do dataset, técnicas que requerem mais dados como Naive, Random Forest e Suavização Exponencial Simples acabaram não conseguindo performar como o esperado. A Média Móvel Simples também não encaixou-se para o caso de uso em questão, ficando visível que a Regressão Linear Simples obteve os melhores resulstados e dá uma boa visão de curto prazo.'

    texto_justificado_1_tab2 = f"""
        <p style="text-align: justify;">{paragrafo2_tab2}</p>
    """
    
    st.markdown(texto_justificado_1_tab2, unsafe_allow_html=True) 


    # Criando o gráfico com Plotly
    fig = go.Figure()

    # Adicionando dados existentes
    fig.add_trace(go.Scatter(x=anos_exist, y=alunos_exist, mode='lines+markers', name='Dados Exist.'))

    # Adicionando previsões
    fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_regressao, mode='lines', name='Regressão Linear Simples', line=dict(dash='dash', color='green')))

    # Personalizando layout
    fig.update_layout(title='Total de Alunos + Regressão Linear Simples (5 anos)',
                    xaxis_title='Ano',
                    yaxis_title='Total de Alunos')

    # Exibindo o gráfico
    st.plotly_chart(fig)
    
    
    st.markdown("### Cenários de Crescimento (What-if)")
    
    paragrafo3_tab2 = 'Com o intuito de servir como ferramenta para a <b>Passos Mágicos</b> foi desenvolvido uma pequena aplicação onde pode-se simular cenários de crescimento baseado em um fator de aumento. Esse fator pode ser escolhido abaixo, assim como o número de anos futuros para ser previsto. O funcionamento é simples, esse valor é multiplicado frente aos dados atuais como uma pequena simulação de crescimento para a ONG, entendendo quais são as suas prospecções - a performance será melhor ao focar em análies de curto prazo. Ao utilizar essa ferramenta, os gestores da <b>Passos Mágicos</b> podem criar cenários e entender a quais patamares esses novos investimentos podem levar a ONG:'

    texto_justificado_2_tab2 = f"""
        <p style="text-align: justify;">{paragrafo3_tab2}</p>
    """
    
    st.markdown(texto_justificado_2_tab2, unsafe_allow_html=True)
    
    input_aumento = st.number_input('Percentual de aumento (1 = 100%):', value=0.5, step=0.1)
    input_anos = st.slider('Número de anos:', min_value=1, max_value=10, value=5)
                    
    if st.button('Simulação'):
        aumento = input_aumento
        anos = input_anos

        # Aplicando o aumento ao conjunto de dados original
        alunos_exist_aumento = alunos_exist * (1 + aumento)

        # Ajustando a regressão linear ao conjunto de dados com aumento
        modelo_regressao_aumento = LinearRegression()
        modelo_regressao_aumento.fit(anos_exist.reshape(-1, 1), alunos_exist_aumento)

        anos_futuros_regressao = np.arange(anos_exist[0], anos_exist[-1] + anos).reshape(-1, 1)
        forecast_regressao_aumento = modelo_regressao_aumento.predict(anos_futuros_regressao)

        # Arredondando os valores de forecast_regressao_aumento para inteiros
        forecast_regressao_aumento_int = np.round(forecast_regressao_aumento).astype(int)


        # Criando o gráfico com Plotly
        fig = go.Figure()

        # Adicionando dados existentes
        fig.add_trace(go.Scatter(x=anos_exist, y=alunos_exist, mode='lines+markers', name='Dados Exist.'))

        # Adicionando previsões
        fig.add_trace(go.Scatter(x=anos_futuros_regressao.flatten(), y=forecast_regressao_aumento_int, mode='lines', name='Regressão Linear Simples', line=dict(dash='dash', color='green')))

        # Personalizando layout
        fig.update_layout(title='Cenários de Crescimento (What-if)',
                        xaxis_title='Ano',
                        yaxis_title='Total de Alunos')

        # Exibindo o gráfico
        st.plotly_chart(fig)


with tab3:      

    st.markdown("## Ponto de Virada")

    paragrafo1_tab3 = 'O <b>Ponto de Virada</b> representa um estágio crucial no desenvolvimento do aluno, no qual ele manifesta ativamente várias dimensões de sua jornada dentro da Associação. Nesse momento, é essencial que o aluno esteja consciente da importância da educação ao reconhecer o valor do conhecimento adquirido e a relevância do aprendizado como processo de construção de novos conhecimentos. Passar pelo Ponto de Virada deve significar que o aluno está pronto para protagonizar a transformação de sua vida por meio da educação onde outrora era coadjuvante.'
    paragrafo2_tab3 = 'Nessa perspectiva, vamos analisar alguns fatores possivelmente envolvidos com o <b>Ponto de Virada</b>.'

    texto_justificado_tab3 = f"""
        <p style="text-align: justify;">{paragrafo1_tab3}</p>
        <p style="text-align: justify;">{paragrafo2_tab3}</p>  
    """

    st.markdown(texto_justificado_tab3, unsafe_allow_html=True)

    # Lendo o arquivo CSV gerado e transformando ele em um XLSX antes de lê-lo
    df = pd.read_csv("dados/dados.csv", sep = ";", encoding = "iso-8859-1")
    df.to_excel("dados/dados.xlsx", index = False)
    df = pd.read_excel("dados/dados.xlsx")

    # Ajustando algumas colunas do DF
    df['INDE']  = pd.to_numeric(df['INDE'], errors='coerce')
    df['IAA']   = pd.to_numeric(df['IAA'], errors='coerce')
    df['IEG']   = pd.to_numeric(df['IEG'], errors='coerce')
    df['IPS']   = pd.to_numeric(df['IPS'], errors='coerce')
    df['IDA']   = pd.to_numeric(df['IDA'], errors='coerce')
    df['IPP']   = pd.to_numeric(df['IPP'], errors='coerce')
    df['IPV']   = pd.to_numeric(df['IPV'], errors='coerce')
    df['IAN']   = pd.to_numeric(df['IAN'], errors='coerce')

    # Criando uma coluna para conseguir ordenar os alunos de acordo com o número deles
    df['NUMERO_ALUNO'] = df['ALUNO'].str.split('-').str[1].astype(int)

    # Apagando os dados dos alunos que acabaram sendo disponibilizados com erros
    df.drop(df[(df['ALUNO'] == 'ALUNO-1259')].index, inplace = True)
    df.drop(df[df['PONTO_VIRADA'] == '#NULO!'].index, inplace = True)

       
    st.markdown("### Alunos que atingiram ou não o Ponto de Virada")

    df_ponto_virada = df.groupby(["ANO", "PONTO_VIRADA"])["PONTO_VIRADA"].count().unstack().fillna(0)
   
    fig = px.bar(df_ponto_virada, 
                 x=df_ponto_virada.index, 
                 y=df_ponto_virada.columns,
                 labels={'value': 'Quantidade', 'variable': 'Ponto de Virada'},                 
                 barmode='group')
    
    fig.update_layout(yaxis_range=[0, 1000])  # Limitar o eixo y entre 0 e 1000
    fig.update_xaxes(title="Ano")  
    fig.update_yaxes(title="Quantidade")
    fig.update_layout(legend_title="Ponto de Virada")     
    st.plotly_chart(fig)

    paragrafo3_tab0 = 'Podemos observar que o Ponto de Virada é alcançado por apenas uma minoria dos alunos, representando um percentual relativamente baixo, situado na faixa dos 15% nos anos de 2020 e 2022. O ano de 2021 apresenta um percentual de cerca de 18%, mas com uma quantidade menor de alunos em momento de Ponto de Virada. Ao passo que em 2022, apesar de voltar ao percentual médio, a quantidade de alunos nesse momento aumenta significativamente, o que pode indicar resiliência em manter os resultados alcançados, considerando o período após a pandemia e o aumento conjunto no quadro de profissionais atuantes na ONG. O indicativo de que a maioria dos alunos não experimenta esse ponto de transformação ou mudança significativa em seu processo educacional durante esses períodos analisados levanta questões sobre os fatores subjacentes que influenciam essa pequena porcentagem de alunos e o que pode ser feito para aumentar o alcance desse ponto crítico de desenvolvimento educacional. Afinal, o envolvimento de outros profissionais, mais relacionados ao acompanhamento psíquico, emocional e social para além da vertente pedagógica ainda é recente e a proporção de professores e alunos se manteve crescente.'

    texto_justificado_2_tab3 = f"""
        <p style="text-align: justify;">{paragrafo3_tab0}</p>       
    """

    st.markdown(texto_justificado_2_tab3, unsafe_allow_html=True)

    st.markdown("### Número de Profissionais Atuando na ONG")

    df_ponto_virada_sim = df[df['PONTO_VIRADA'] == "Sim"].groupby(["ANO"])["PONTO_VIRADA"].count()
    
    fig, ax1 = plt.subplots()    
    anos = df_ponto_virada_sim.index.tolist()
    ax1.plot(anos, df_ponto_virada_sim, marker="o", linestyle="-", color="b")
    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Alunos que atingiram o Ponto de Virada", color="b")
    ax1.set_ylim(80, 130)
    ax1.tick_params(axis='y', labelcolor='b')

    # Adicionar os valores de cada ponto com posição ajustada
    for i, txt in enumerate(df_ponto_virada_sim):
        ax1.text(anos[i], txt + 0.3, str(txt), ha='center', va='bottom')  # Ajustando a posição vertical

    # Definir os anos como categorias no eixo X
    ax1.set_xticks(anos)

    # Adicionar o segundo eixo Y
    ax2 = ax1.twinx()
    valores_secundarios = {2020: 12, 2021: 16, 2022: 21}  # Número de profissionais trabalhando na ONG em cada ano
    valores_secundarios_anos = list(valores_secundarios.keys())
    valores_secundarios_valores = list(valores_secundarios.values())
    ax2.plot(valores_secundarios_anos, valores_secundarios_valores, marker="s", linestyle="--", color="g")
    ax2.set_ylabel("Número de profissionais", color="g")
    ax2.tick_params(axis='y', labelcolor='g')

    # Adicionar os valores de cada ponto do segundo eixo Y com posição ajustada
    for i, valor in enumerate(valores_secundarios_valores):
        ax2.text(valores_secundarios_anos[i], valor + 0.15, str(valor), ha='center', va='bottom', color='g')  # Ajustando a posição vertical

    
    plt.grid(True)    
    st.pyplot(fig)

    paragrafo4_tab0 = 'Ao analisarmos a relação entre o número de profissionais na ONG e o número de alunos que alcançaram o Ponto de Virada, podemos observar um crescimento gradual, embora modesto. Inicialmente, a proporção era de 12,77%, aumentando para 14,81% e posteriormente para 18,58%. Essa tendência sugere uma possível correlação entre o aumento do suporte oferecido pelos profissionais da ONG e o crescimento do número de alunos capazes de atingir esse marco educacional crucial. Reforçando a resiliência em manter proporcionalmente os resultados com o aumento da quantidade de alunos e indicando que o envolvimento de profissionais voltados ao bem estar psíquico, emocional e social podem trazer resultados maiores no médio-prazo.'
    
    texto_justificado_3_tab3 = f"""
        <p style="text-align: justify;">{paragrafo4_tab0}</p>       
    """

    st.markdown(texto_justificado_3_tab3, unsafe_allow_html=True)

    st.markdown("### Notas de Português e Matemática")

    media_por_ano_com_pv = df.groupby(['ANO', 'PONTO_VIRADA'])[['NOTA_MAT', 'NOTA_PORT', 'NOTA_ING']].mean().reset_index()
    media_por_ano_com_pv['ANO'] = media_por_ano_com_pv['ANO'].astype(str)    
    st.write(media_por_ano_com_pv)

    paragrafo5_tab0 = 'Apesar de os dados das notas de Matemática, Português e Inglês estarem disponíveis apenas para o ano de 2022, é evidente que uma discrepância significativa na média das notas é observada entre os alunos que atingiram o Ponto de Virada e aqueles que não o alcançaram. Isso sugere que a percepção desse ponto crítico ocorreu em um período em que os alunos estavam mais dedicados às aulas e avaliações. Esta observação implica não apenas na importância da dedicação dos alunos, mas também levanta questões sobre o papel do currículo, dos métodos de ensino e do ambiente educacional no processo de alcance desse ponto de virada.'

    texto_justificado_4_tab3 = f"""
        <p style="text-align: justify;">{paragrafo5_tab0}</p>       
    """

    st.markdown(texto_justificado_4_tab3, unsafe_allow_html=True)
    
    st.markdown("### Média dos Indicadores")

    medias = df.groupby(['ANO', 'PONTO_VIRADA'])[['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']].mean()    
    medias.reset_index(inplace=True)   
    medias['ANO'] = medias['ANO'].astype(int).astype(str)
    st.write(medias)

    paragrafo6_tab0 = 'Da mesma forma que foi observado com as notas, uma tendência semelhante se manifestou nos diversos indicadores avaliados. Incluindo autoavaliação, engajamento, aspectos psicossociais, aprendizado e avaliação psicopedagógica. Essa consistência sugere que há uma inter-relação complexa entre esses diferentes aspectos do desenvolvimento do aluno. Essa análise mais profunda aponta para a necessidade de uma abordagem holística na compreensão do progresso educacional, levando em consideração não apenas o desempenho acadêmico, mas também fatores socioemocionais e psicopedagógicos que impactam o processo de aprendizagem e crescimento pessoal do aluno, possibilitando uma maior clareza de propósito na jornada da educação e aumentando o potencial do Ponto de Virada.'

    texto_justificado_5_tab3 = f"""
        <p style="text-align: justify;">{paragrafo6_tab0}</p>       
    """

    st.markdown(texto_justificado_5_tab3, unsafe_allow_html=True)


with tab4:      

    st.markdown("## IDEB")

    paragrafo1_tab4 = 'O Índice de Desenvolvimento da Educação Básica (IDEB) é uma métrica utilizada no Brasil para avaliar a qualidade do ensino nas escolas públicas, levando em conta o desempenho dos alunos em avaliações padronizadas e a taxa de aprovação. Sua importância reside no fato de que oferece um panorama objetivo sobre a eficácia do sistema educacional, permitindo identificar pontos fortes e fracos e orientando políticas públicas para melhorar o ensino.'
    paragrafo2_tab4 = 'No âmbito do projeto em questão, a análise do Índice de Desenvolvimento da Educação Básica (IDEB) nas escolas e no município de Embu-Guaçu desempenha um papel fundamental. Através dessa avaliação, torna-se possível identificar lacunas na educação pública onde a intervenção da ONG Passos Mágicos pode ser direcionada de maneira estratégica. Isso assegura que os recursos sejam alocados de forma eficaz, visando elevar a qualidade do ensino e proporcionar oportunidades igualitárias de aprendizagem para todos os alunos do município.'


    texto_justificado_1_tab4 = f"""
        <p style="text-align: justify;">{paragrafo1_tab4}</p>       
        <p style="text-align: justify;">{paragrafo2_tab4}</p>       
    """

    st.markdown(texto_justificado_1_tab4, unsafe_allow_html=True)

    df_ideb_por_escola = pd.read_excel('dados/ideb_saeb_por_escola.xlsx')
    df_ideb_por_escola_embu_guacu = df_ideb_por_escola[df_ideb_por_escola['nome_municipio'] == 'Embu-Guaçu']
    df_ideb_por_escola_embu_guacu = df_ideb_por_escola_embu_guacu[df_ideb_por_escola_embu_guacu['ideb'] != '-']
    df_ideb_por_escola_embu_guacu[['saeb_matematica', 'saeb_portugues', 'saeb_nota_media', 'ideb']] = df_ideb_por_escola_embu_guacu[['saeb_matematica', 'saeb_portugues', 'saeb_nota_media', 'ideb']].astype(float)


    df_ideb_por_municipio = pd.read_excel('dados/ideb_saeb_por_municipio.xlsx')

    st.markdown("### IDEB do Município de Embu-Guaçu")

    fig0 = go.Figure()

    fig0.add_trace(go.Bar(x=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2017) & (df_ideb_por_municipio['rede'] == 'Pública')]['ciclo'], 
                        y=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2017) & (df_ideb_por_municipio['rede'] == 'Pública')]['ideb'], 
                        name='2017'))
    fig0.add_trace(go.Bar(x=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2019) & (df_ideb_por_municipio['rede'] == 'Pública')]['ciclo'], 
                        y=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2019) & (df_ideb_por_municipio['rede'] == 'Pública')]['ideb'], 
                        name='2019'))
    fig0.add_trace(go.Bar(x=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2021) & (df_ideb_por_municipio['rede'] == 'Pública')]['ciclo'], 
                        y=df_ideb_por_municipio[(df_ideb_por_municipio['ano'] == 2021) & (df_ideb_por_municipio['rede'] == 'Pública')]['ideb'], 
                        name='2021'))

    fig0.update_layout(title='Valor do IDEB do Município de Embu-Guaçu por Ano Escolar',
                    xaxis_title='Ano Escolar',
                    yaxis_title='IDEB',
                    barmode='group',                    
                    legend_title='Ano')

    st.plotly_chart(fig0)

    paragrafo3_tab4 = 'Através da análise do gráfico, percebe-se um crescimento no IDEB entre os anos de 2017 e 2019, especialmente nos anos finais do ensino (do 6º ao 9º ano) e no ensino médio. Entretanto, ocorreu uma reversão nesse cenário nos anos subsequentes, com uma queda significativa nos valores do IDEB entre 2019 e 2021, particularmente nos anos iniciais do ensino (do 1º ao 5º ano). Esta diminuição acentuada pode ser atribuída, em grande parte, aos desafios enfrentados durante a pandemia de COVID-19. O impacto da interrupção das aulas presenciais, adaptações no ensino remoto e as disparidades no acesso às tecnologias educacionais podem ter contribuído para esse declínio no desempenho educacional, evidenciando a necessidade de estratégias específicas de recuperação e apoio pedagógico para mitigar esses efeitos adversos.'

    texto_justificado_2_tab4 = f"""
        <p style="text-align: justify;">{paragrafo3_tab4}</p>               
    """

    st.markdown(texto_justificado_2_tab4, unsafe_allow_html=True)

    st.markdown("### IDEB por Escola do Município de Embu-Guaçu")

    df_ideb_por_escola_embu_guacu = df_ideb_por_escola_embu_guacu.sort_values(by='ideb', ascending=False)

    fig1 = go.Figure()

    fig1.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['ideb'], name='2017'))
    fig1.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['ideb'], name='2019'))
    fig1.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]['ideb'], name='2021'))

    fig1.update_layout(title='Valor do IDEB por Escola do Município de Embu-Guaçu nos Anos Iniciais (1º ao 5º ano)',
                    xaxis_title='Escolas',
                    yaxis_title='IDEB',
                    barmode='group',
                    legend_title='Ano',
                    width=900,  
                    height=600,  
                    yaxis_tickangle=-45)  
    
    st.plotly_chart(fig1)


   
    fig2 = go.Figure()

    fig2.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['ideb'], name='2017'))
    fig2.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['ideb'], name='2019'))
    fig2.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]['ideb'], name='2021'))
    
    fig2.update_layout(title='Valor do IDEB por Escola do Município de Embu-Guaçu nos Anos Finais (6º ao 9º ano)',
                    xaxis_title='Escolas',
                    yaxis_title='IDEB',
                    barmode='group',
                    legend_title='Ano',
                    width=800,
                    height=600, 
                    yaxis_tickangle=-45)
  
    st.plotly_chart(fig2)

    
    fig3 = go.Figure()

    fig3.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['ideb'], name='2017'))
    fig3.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['ideb'], name='2019'))
    fig3.add_trace(go.Bar(x=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['nome_escola'], y=df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]['ideb'], name='2021'))

    fig3.update_layout(title='Valor do IDEB por Escola do Município de Embu-Guaçu no Ensino Médio',
                    xaxis_title='Escolas',
                    yaxis_title='IDEB',
                    barmode='group',
                    legend_title='Ano',
                    width=600, 
                    height=500, 
                    yaxis_tickangle=-45) 
   
    st.plotly_chart(fig3)

    paragrafo4_tab4 = 'O comportamento do Índice de Desenvolvimento da Educação Básica (IDEB) no município de Embu-Guaçu reflete-se de forma semelhante nos dados específicos por escola, revelando uma tendência de declínio nos anos recentes, especialmente entre 2019 e 2021, em decorrência dos impactos da pandemia.'

    texto_justificado_3_tab4 = f"""
        <p style="text-align: justify;">{paragrafo4_tab4}</p>               
    """

    st.markdown(texto_justificado_3_tab4, unsafe_allow_html=True)


    st.markdown("#### IDEB por Escola nos Anos Iniciais (1º ao 5º ano)")


    df_2017 = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]

    df_2017 = df_2017.sort_values(by='ideb', ascending=True)   
    ideb_2017 = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AI') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2017)]['ideb'].mean()
       
    colors = ['#1f77b4' if ideb >= ideb_2017 else '#aec7e8' for ideb in df_2017['ideb']]
    
    fig4 = go.Figure()
    
    fig4.add_trace(go.Bar(x=df_2017['ideb'], y=df_2017['nome_escola'],
                        name='2017', orientation='h', marker_color=colors))
    
    fig4.add_vline(x=ideb_2017, line_dash="dash", line_color="black")
    
    fig4.add_annotation(x=ideb_2017 + 0.2, y=15, text=f"IDEB Embu-Guaçu: {ideb_2017}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig4.update_layout(title='Valor do IDEB 2017 por Escola do Município de Embu-Guaçu nos Anos Iniciais (1º ao 5º ano)',
                    xaxis_title='IDEB 2017',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig4)

    df_2019 = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]
    df_2019 = df_2019.sort_values(by='ideb', ascending=True)
    ideb_2019 = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AI') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2019)]['ideb'].mean()

    colors = ['#1f77b4' if ideb >= ideb_2019 else '#aec7e8' for ideb in df_2019['ideb']]

    fig5 = go.Figure()
    
    fig5.add_trace(go.Bar(x=df_2019['ideb'], y=df_2019['nome_escola'],
                        name='2019', orientation='h', marker_color=colors))
    
    fig5.add_vline(x=ideb_2019, line_dash="dash", line_color="black")
    
    fig5.add_annotation(x=ideb_2019 + 0.2, y=16, text=f"IDEB Embu-Guaçu: {ideb_2019}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig5.update_layout(title='Valor do IDEB 2019 por Escola do Município de Embu-Guaçu nos Anos Iniciais (1º ao 5º ano)',
                    xaxis_title='IDEB 2019',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig5)


    df_2021 = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AI')]
    df_2021 = df_2021.sort_values(by='ideb', ascending=True)
    ideb_2021 = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AI') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2021)]['ideb'].mean()

    colors = ['#1f77b4' if ideb >= ideb_2021 else '#aec7e8' for ideb in df_2021['ideb']]

    fig6 = go.Figure()
    
    fig6.add_trace(go.Bar(x=df_2021['ideb'], y=df_2021['nome_escola'],
                        name='2021', orientation='h', marker_color=colors))
    
    fig6.add_vline(x=ideb_2021, line_dash="dash", line_color="black")
    
    fig6.add_annotation(x=ideb_2021 + 0.2, y=15, text=f"IDEB Embu-Guaçu: {ideb_2021}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig6.update_layout(title='Valor do IDEB 2021 por Escola do Município de Embu-Guaçu nos Anos Iniciais (1º ao 5º ano)',
                    xaxis_title='IDEB 2021',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig6)


    st.markdown("#### IDEB por Escola nos Anos Finais (6º ao 9º ano)")

    df_2017_af = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]
    df_2019_af = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]
    df_2021_af = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'AF')]
    
    df_2017_af = df_2017_af.sort_values(by='ideb', ascending=True)
    df_2019_af = df_2019_af.sort_values(by='ideb', ascending=True)
    df_2021_af = df_2021_af.sort_values(by='ideb', ascending=True)

    ideb_2017_af = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AF') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2017)]['ideb'].mean()
    ideb_2019_af = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AF') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2019)]['ideb'].mean()
    ideb_2021_af = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'AF') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2021)]['ideb'].mean()


    colors1 = ['#1f77b4' if ideb >= ideb_2017_af else '#aec7e8' for ideb in df_2017_af['ideb']]
    colors2 = ['#1f77b4' if ideb >= ideb_2019_af else '#aec7e8' for ideb in df_2019_af['ideb']]
    colors3 = ['#1f77b4' if ideb >= ideb_2021_af else '#aec7e8' for ideb in df_2021_af['ideb']]


    fig7 = go.Figure()
    
    fig7.add_trace(go.Bar(x=df_2017_af['ideb'], y=df_2017_af['nome_escola'],
                        name='2017', orientation='h', marker_color=colors1))
    
    fig7.add_vline(x=ideb_2017_af, line_dash="dash", line_color="black")
    
    fig7.add_annotation(x=ideb_2017_af + 0.2, y=10, text=f"IDEB Embu-Guaçu: {ideb_2017_af}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig7.update_layout(title='Valor do IDEB 2017 por Escola do Município de Embu-Guaçu nos Anos Finais (6º ao 9º ano)',
                    xaxis_title='IDEB 2017',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig7)


    fig8 = go.Figure()
    
    fig8.add_trace(go.Bar(x=df_2019_af['ideb'], y=df_2019_af['nome_escola'],
                        name='2019', orientation='h', marker_color=colors2))
    
    fig8.add_vline(x=ideb_2019_af, line_dash="dash", line_color="black")
    
    fig8.add_annotation(x=ideb_2019_af + 0.2, y=12, text=f"IDEB Embu-Guaçu: {ideb_2019_af}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig8.update_layout(title='Valor do IDEB 2019 por Escola do Município de Embu-Guaçu nos Anos Finais (6º ao 9º ano)',
                    xaxis_title='IDEB 2019',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig8)


    fig9 = go.Figure()
    
    fig9.add_trace(go.Bar(x=df_2021_af['ideb'], y=df_2021_af['nome_escola'],
                        name='2021', orientation='h', marker_color=colors3))
    
    fig9.add_vline(x=ideb_2021_af, line_dash="dash", line_color="black")
    
    fig9.add_annotation(x=ideb_2021_af + 0.2, y=12, text=f"IDEB Embu-Guaçu: {ideb_2021_af}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig9.update_layout(title='Valor do IDEB 2021 por Escola do Município de Embu-Guaçu nos Anos Finais (6º ao 9º ano)',
                    xaxis_title='IDEB 2021',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=600,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig9)




    st.markdown("#### IDEB por Escola no Ensino Médio")

    df_2017_em = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2017) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]
    df_2019_em = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2019) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]
    df_2021_em = df_ideb_por_escola_embu_guacu[(df_ideb_por_escola_embu_guacu['ano'] == 2021) & (df_ideb_por_escola_embu_guacu['ciclo'] == 'EM')]
    
    df_2017_em = df_2017_em.sort_values(by='ideb', ascending=True)
    df_2019_em = df_2019_em.sort_values(by='ideb', ascending=True)
    df_2021_em = df_2021_em.sort_values(by='ideb', ascending=True)

    ideb_2017_em = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'EM') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2017)]['ideb'].mean()
    ideb_2019_em = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'EM') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2019)]['ideb'].mean()
    ideb_2021_em = df_ideb_por_municipio[(df_ideb_por_municipio['ciclo'] == 'EM') & (df_ideb_por_municipio['rede'] == 'Pública') & (df_ideb_por_municipio['ano'] == 2021)]['ideb'].mean()

    colors1_em = ['#1f77b4' if ideb >= ideb_2017_em else '#aec7e8' for ideb in df_2017_em['ideb']]
    colors2_em = ['#1f77b4' if ideb >= ideb_2019_em else '#aec7e8' for ideb in df_2019_em['ideb']]
    colors3_em = ['#1f77b4' if ideb >= ideb_2021_em else '#aec7e8' for ideb in df_2021_em['ideb']]
    

    fig10 = go.Figure()
    
    fig10.add_trace(go.Bar(x=df_2017_em['ideb'], y=df_2017_em['nome_escola'],
                        name='2017', orientation='h', marker_color=colors1_em))
    
    fig10.add_vline(x=ideb_2017_em, line_dash="dash", line_color="black")
    
    fig10.add_annotation(x=ideb_2017_em + 0.2, y=6, text=f"IDEB Embu-Guaçu: {ideb_2017_em}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig10.update_layout(title='Valor do IDEB 2017 por Escola do Município de Embu-Guaçu no Ensino Médio',
                    xaxis_title='IDEB 2017',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=300,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig10)


    fig11 = go.Figure()
    
    fig11.add_trace(go.Bar(x=df_2019_em['ideb'], y=df_2019_em['nome_escola'],
                        name='2019', orientation='h', marker_color=colors2_em))
    
    fig11.add_vline(x=ideb_2019_em, line_dash="dash", line_color="black")
    
    fig11.add_annotation(x=ideb_2019_em + 0.2, y=8, text=f"IDEB Embu-Guaçu: {ideb_2019_em}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig11.update_layout(title='Valor do IDEB 2019 por Escola do Município de Embu-Guaçu no Ensino Médio',
                    xaxis_title='IDEB 2019',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=400,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig11)


    fig12 = go.Figure()
    
    fig12.add_trace(go.Bar(x=df_2021_em['ideb'], y=df_2021_em['nome_escola'],
                        name='2021', orientation='h', marker_color=colors3_em))
    
    fig12.add_vline(x=ideb_2021_em, line_dash="dash", line_color="black")
    
    fig12.add_annotation(x=ideb_2021_em + 0.2, y=4, text=f"IDEB Embu-Guaçu: {ideb_2021_em}", showarrow=True,
                    arrowhead=1, arrowcolor="black", arrowsize=0.5,
                    arrowwidth=2, ax=70, ay=-30)
    
    fig12.update_layout(title='Valor do IDEB 2021 por Escola do Município de Embu-Guaçu nos no Ensino Médio',
                    xaxis_title='IDEB 2021',
                    yaxis_title='Escolas',
                    legend_title='Ano',
                    barmode='group',
                    width=800, 
                    height=300,
                    plot_bgcolor='rgba(255,255,255,0)', 
                    font=dict(family='Arial', size=12, color='black'), 
                    legend=dict(x=0, y=1.0, bgcolor='rgba(255,255,255,0.5)'), 
                    margin=dict(l=200, r=50, t=70, b=50), 
                    )
    
    st.plotly_chart(fig12)


    st.markdown("#### Localização das Escolas do Município de Embu-Guaçu com Desempenho Ruim no IDEB")

    coordenadas_escolas = {
        'AMANDA CONSUELO DA CUNHA ESCOLA MUNICIPAL': (-23.867716889795453, -46.790130881181234),
        'ESCOLA MUNICIPAL JOAO ALVES': (-23.882388200836104, -46.84855013597809),
        'ETELVINA DELFIM SIMOES EM': (-23.83447173963271, -46.81065281618173),
        'ESCOLA MUNICIPAL MARIA IGNEZ CONCELLES IRMA INES': (-23.80726208790731, -46.83203519864512),
        'CECILIA CRISTINA DE OLIVEIRA RODRIGUES ESCOLA MUNICIPAL': (-23.870709390590278, -46.78891146803589),
        'LORIS NASSIF MATTAR PROFA': (-23.847907585873706, -46.87684725341914),
        'ALFREDO SCHUNK ESCOLA MUNICIPAL': (-23.874592459464882, -46.7780885762005),
        'LEVI PEREIRA MARTINS PROFESSOR': (-23.922059766915865, -46.86920741439455),
        'DONIZETTI APARECIDO LEITE PROFESSOR': (-23.88200854220514, -46.79276327820527)        
    }

    df = pd.DataFrame(list(coordenadas_escolas.items()), columns=['Escola', 'Coordenadas'])

    
    fig = px.scatter_mapbox(df, lat=[coord[0] for coord in df['Coordenadas']], 
                            lon=[coord[1] for coord in df['Coordenadas']], 
                            hover_name='Escola', zoom=12)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_traces(marker=dict(size=15))
    
    st.plotly_chart(fig)
