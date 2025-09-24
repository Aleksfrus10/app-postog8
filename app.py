import streamlit as st
import pandas as pd
from io import BytesIO

# Lista de campos
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

st.set_page_config(page_title="Formulário de Postos", layout="wide")
st.title("Formulário de Preenchimento de Postos")
st.write("Preencha os campos abaixo e clique em 'Enviar'. O arquivo Excel será gerado para download.")

# Formulário em Streamlit
with st.form("form_postos"):
    dados = {}
    for campo in campos:
        dados[campo] = st.text_input(campo)
    
    enviar = st.form_submit_button("Enviar")

    if enviar:
        # Validação: campos vazios
        campos_vazios = [c for c, v in dados.items() if not v.strip()]
        if campos_vazios:
            st.error(f"Os seguintes campos não podem ficar vazios: {', '.join(campos_vazios)}")
        else:
            # Criar DataFrame transposto
            df = pd.DataFrame([dados]).T
            df.columns = ['Preenchimento']

            # Exibir DataFrame
            st.success("Formulário enviado com sucesso!")
            st.dataframe(df)

            # Criar arquivo Excel em memória
            output = BytesIO()
            df.to_excel(output, index=True, engine='openpyxl')
            output.seek(0)

            # Botão de download
            st.download_button(
                label="Baixar Excel",
                data=output,
                file_name="preenchimento_postos.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
