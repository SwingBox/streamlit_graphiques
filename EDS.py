import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

datasets = {
    "Titanic": sns.load_dataset("titanic"),
    "Flights": sns.load_dataset("flights"),
    "Tips": sns.load_dataset("tips"),
    "Penguins": sns.load_dataset("penguins"),
    "Iris": sns.load_dataset("iris")
}

st.title("Manipulation de données et création de graphiques")

dataset_user = st.selectbox("Quel dataset veux-tu utiliser ?", list(datasets.keys()))
df = datasets[dataset_user]
st.dataframe(df, use_container_width=True)

colonnes_user = df.columns.tolist()
colonneX = st.selectbox("Choisissez la colonne X", colonnes_user)
colonneY = st.selectbox("Choisissez la colonne Y", colonnes_user)

graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ["scatter_chart", "line_chart", "bar_chart"])

if colonneX and colonneY:
    if graphique == "scatter_chart":
        fig = px.scatter(df, x=colonneX, y=colonneY, title="Scatter Plot")
    elif graphique == "line_chart":
        fig = px.line(df, x=colonneX, y=colonneY, title="Line Chart")
    elif graphique == "bar_chart":
        fig = px.bar(df, x=colonneX, y=colonneY, title="Bar Chart")
    else:
        fig = None

    if fig:
        st.plotly_chart(fig)

if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Ma matrice de corrélation")

  
    df_corr = df.select_dtypes(include='number')

    if df_corr.shape[1] >= 2:
        corr = df_corr.corr()

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='magma', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Corrélation impossible")
