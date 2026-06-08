import streamlit as st
import sqlite3
import pandas as pd
import altair as alt
from datetime import datetime

st.set_page_config(
    page_title="DataVision Store BI",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
}

div[data-testid="metric-container"] {
    background-color: #1E2530;
    border: 1px solid #2E3748;
    padding: 20px;
    border-radius: 15px;
    transition: all 0.3s ease;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    border: 1px solid #4E8CFF;
    box-shadow: 0px 0px 20px rgba(78,140,255,0.4);
}

.dashboard-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.dashboard-subtitle {
    text-align: center;
    color: #B0B0B0;
    margin-bottom: 25px;
}

section[data-testid="stSidebar"] {
    background-color: #151A23;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-title">DataVision Store</div>
<div class="dashboard-subtitle">Business Intelligence Dashboard</div>
""", unsafe_allow_html=True)

st.caption(f"Ultima actualizacion: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

conexion = sqlite3.connect("../datos/empresa.db")

ventas = pd.read_sql("SELECT COUNT(*) total FROM ventas", conexion)
ingresos = pd.read_sql("SELECT SUM(total) total FROM ventas", conexion)
ticket = pd.read_sql("SELECT AVG(total) promedio FROM ventas", conexion)
productos = pd.read_sql("SELECT COUNT(*) total FROM productos", conexion)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Ventas Totales", f"{ventas['total'][0]:,}")
c2.metric("Ingresos Totales", f"${ingresos['total'][0]:,.0f}")
c3.metric("Ticket Promedio", f"${ticket['promedio'][0]:,.0f}")
c4.metric("Productos", f"{productos['total'][0]:,}")

st.divider()

st.info(
    "Este dashboard permite monitorear el desempeño comercial de DataVision Store mediante indicadores clave de negocio, comportamiento de ventas y análisis de clientes."
)

st.sidebar.header("Filtros")

sucursal = st.sidebar.selectbox(
    "Sucursal",
    ["Todas", "1", "2", "3", "4"]
)

ventas_df = pd.read_sql("SELECT * FROM ventas", conexion)
productos_df = pd.read_sql("SELECT * FROM productos", conexion)

if sucursal != "Todas":
    ventas_df = ventas_df[ventas_df["id_sucursal"] == int(sucursal)]

st.subheader("Ventas por Mes")

ventas_mes = ventas_df.copy()
ventas_mes["mes"] = ventas_mes["fecha"].astype(str).str.slice(0, 7)

ventas_mes = (
    ventas_mes
    .groupby("mes", as_index=False)
    .agg(ventas=("id_venta", "count"))
)

grafica_mes = alt.Chart(ventas_mes).mark_line(point=True).encode(
    x=alt.X("mes:N", title="Mes"),
    y=alt.Y("ventas:Q", title="Ventas"),
    tooltip=["mes", "ventas"]
).properties(
    height=350
).interactive()

st.altair_chart(grafica_mes, use_container_width=True)

st.subheader("Ventas por Sucursal")

ventas_sucursal = (
    ventas_df
    .groupby("id_sucursal", as_index=False)
    .agg(ventas=("id_venta", "count"))
)

grafica_sucursal = alt.Chart(ventas_sucursal).mark_bar().encode(
    x=alt.X("id_sucursal:N", title="Sucursal"),
    y=alt.Y("ventas:Q", title="Ventas"),
    tooltip=["id_sucursal", "ventas"]
).properties(
    height=350
).interactive()

st.altair_chart(grafica_sucursal, use_container_width=True)

st.subheader("Productos Mas Rentables")

rentables = productos_df.copy()
rentables["utilidad"] = rentables["precio"] - rentables["costo"]

rentables = (
    rentables
    .groupby("nombre", as_index=False)
    .agg(utilidad=("utilidad", "sum"))
    .sort_values("utilidad", ascending=False)
    .head(10)
)

grafica_rentables = alt.Chart(rentables).mark_bar().encode(
    x=alt.X("nombre:N", sort="-y", title="Producto"),
    y=alt.Y("utilidad:Q", title="Utilidad"),
    tooltip=["nombre", "utilidad"]
).properties(
    height=350
).interactive()

st.altair_chart(grafica_rentables, use_container_width=True)

st.subheader("Top 10 Clientes")

top_clientes = (
    ventas_df
    .groupby("id_cliente", as_index=False)
    .agg(gasto=("total", "sum"))
    .sort_values("gasto", ascending=False)
    .head(10)
)

st.dataframe(top_clientes, use_container_width=True)

conexion.close()