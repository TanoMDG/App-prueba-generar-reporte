import streamlit as st
import plotly.express as px
import datetime
from utils.api_covid import get_data_country
from utils.reportes import generar_reporte
from utils.email_utils import enviar_email
import os, json

with open("config.json") as f:
    config = json.load(f)

st.title("Reporte diario COVID-19 📈")
pais = config["country"]
df = get_data_country(pais)
hoy = df['date'].max().date()
file_path, df_today, df_hist = generar_reporte(df)

st.write(f"**País:** {pais}\n**Fecha del último dato:** {hoy}")

st.subheader("Casos diarios")
fig = px.line(df_hist, x="date", y="confirmed", title="Casos confirmados totales")
st.plotly_chart(fig)

st.subheader("Detalle del día")
st.dataframe(df_today)

if st.button("Enviar reporte por email"):
    enviar_email(file_path)
    st.success("Reporte enviado por email ✅")
