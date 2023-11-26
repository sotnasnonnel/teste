import streamlit as st
import pandas as pd 
import time

#setar o grafico na pagina
st.set_page_config(
    layout="wide",
    page_title="Música Spotfy"
)

#cacheamento
@st.cache_data
def load_data():
#ler tabela
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    return df

df = load_data()

#compartilhar informações com outra pagina
st.session_state["df_spotify"] = df

#colocar artist no eixo X ou por track
df.set_index("Track", inplace=True)

#criar variavel artista
artists = df["Artist"].value_counts().index

#componentes de filtros (widgets)
#linkando filtro com o grafico
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

#seleção em cadeia
albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)
df_filtered2 = df[df["Album"] == album]


#selecionar botao para aparecer o gráfico
agree = st.checkbox('Mostrar Gráfico')
if agree:
    st.bar_chart(df_filtered2["Stream"])

#criar colunas na pagina
col1, col2 = st.columns(2)
#col1, col2 = st.columns([0.7,0.3]) um grafico 70% e o outro 30%

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

#cacheamento e multipages#
    



