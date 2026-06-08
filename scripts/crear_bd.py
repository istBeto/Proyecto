import sqlite3
import pandas as pd

conexion = sqlite3.connect("../datos/empresa.db")

# ====================
# LEER CSV
# ====================

clientes = pd.read_csv("../datos/clientes.csv")
productos = pd.read_csv("../datos/productos.csv")
sucursales = pd.read_csv("../datos/sucursales.csv")
empleados = pd.read_csv("../datos/empleados.csv")
proveedores = pd.read_csv("../datos/proveedores.csv")
ventas = pd.read_csv("../datos/ventas.csv")

# ====================
# GUARDAR TABLAS
# ====================

clientes.to_sql(
    "clientes",
    conexion,
    if_exists="replace",
    index=False
)

productos.to_sql(
    "productos",
    conexion,
    if_exists="replace",
    index=False
)

sucursales.to_sql(
    "sucursales",
    conexion,
    if_exists="replace",
    index=False
)

empleados.to_sql(
    "empleados",
    conexion,
    if_exists="replace",
    index=False
)

proveedores.to_sql(
    "proveedores",
    conexion,
    if_exists="replace",
    index=False
)

ventas.to_sql(
    "ventas",
    conexion,
    if_exists="replace",
    index=False
)

conexion.close()

print("\nBASE DE DATOS CREADA")
print("Archivo: empresa.db")
print("Tablas cargadas correctamente")