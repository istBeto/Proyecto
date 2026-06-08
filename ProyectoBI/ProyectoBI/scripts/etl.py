import sqlite3
import pandas as pd


# CONEXIONES


transaccional = sqlite3.connect("../datos/empresa.db")
warehouse = sqlite3.connect("../datos/warehouse.db")


# EXTRAER DATOS


clientes = pd.read_sql(
    "SELECT * FROM clientes",
    transaccional
)

productos = pd.read_sql(
    "SELECT * FROM productos",
    transaccional
)

sucursales = pd.read_sql(
    "SELECT * FROM sucursales",
    transaccional
)

ventas = pd.read_sql(
    "SELECT * FROM ventas",
    transaccional
)


# DIM CLIENTE


clientes.to_sql(
    "dim_cliente",
    warehouse,
    if_exists="replace",
    index=False
)


# DIM PRODUCTO


productos.to_sql(
    "dim_producto",
    warehouse,
    if_exists="replace",
    index=False
)

# DIM SUCURSAL

sucursales.to_sql(
    "dim_sucursal",
    warehouse,
    if_exists="replace",
    index=False
)


# DIM TIEMPO


dim_tiempo = pd.DataFrame()

dim_tiempo["fecha"] = pd.to_datetime(
    ventas["fecha"]
)

dim_tiempo["dia"] = dim_tiempo["fecha"].dt.day
dim_tiempo["mes"] = dim_tiempo["fecha"].dt.month
dim_tiempo["anio"] = dim_tiempo["fecha"].dt.year

dim_tiempo = dim_tiempo.drop_duplicates()

dim_tiempo.to_sql(
    "dim_tiempo",
    warehouse,
    if_exists="replace",
    index=False
)


# FACT VENTAS


fact_ventas = ventas.copy()

fact_ventas.rename(
    columns={
        "total": "ingresos"
    },
    inplace=True
)

fact_ventas.to_sql(
    "fact_ventas",
    warehouse,
    if_exists="replace",
    index=False
)

warehouse.commit()

transaccional.close()
warehouse.close()

print("\nETL COMPLETADO")
print("Dimensiones cargadas")
print("Fact table cargada")