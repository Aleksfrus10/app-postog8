import streamlit as st
import pandas as pd

campos = [
    "VIGILANTE LÍDER (UN-30)",
    "RP-23",
    "RP-22",
    "RP-21",
    "PORTARIA 01 A",
    "PORTARIA 01 B",
    "PORTARIA 01 C",
    "PORTARIA 02",
    "PORTARIA 04",
    "PORTARIA 06",
    "PORTARIA 07",
    "PORTARIA 09",
    "PORTARIA 10 A",
    "PORTARIA 10 B",
    "PORTARIA 10 C",
    "POSTO 11",
    "PORTARIA 15 A",
    "PORTARIA 15 B",
    "PORTARIA 16 A",
    "PORTARIA 16 B",
    "TUBOVIA",
    "UTE/S-10",
    "CRUZEIRO",
    "CFTV-UTE",
    "CISP A",
    "CISP B",
    "RECEPÇÃO PV-10",
    "CREDENCIAMENTO",
    "RECEPÇÃO CEAD A",
    "RECEPÇÃO CEAD B",
    "RECEPÇÃO CEAD UTE",
    "RECEPÇÃO BALANÇA"
]

st.title("Formulário de Preenchimento de Postos")

dados = {}
for campo in campos:
    dados[campo] = st.text_input(campo)

if st.button("Salvar"):
    df = pd.DataFrame([dados]).T
    df.columns = ['Preenchimento']
    df.to_excel("preenchimento.xlsx")
    df.to_csv("preenchimento.csv")
    st.success("Dados salvos com sucesso!")
    st.dataframe(df)

