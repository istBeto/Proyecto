import sqlite3

# Crear Data Warehouse

conexion = sqlite3.connect("../datos/warehouse.db")

cursor = conexion.cursor()


# DIM CLIENTE

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_cliente(
    id_cliente_sk INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    nombre TEXT,
    edad INTEGER,
    sexo TEXT,
    ciudad TEXT
)
""")


# DIM PRODUCTO


cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_producto(
    id_producto_sk INTEGER PRIMARY KEY,
    id_producto INTEGER,
    nombre TEXT,
    categoria TEXT,
    precio REAL,
    costo REAL
)
""")


# DIM TIEMPO

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_tiempo(
    id_tiempo_sk INTEGER PRIMARY KEY,
    fecha DATE,
    dia INTEGER,
    mes INTEGER,
    anio INTEGER
)
""")


# DIM SUCURSAL


cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_sucursal(
    id_sucursal_sk INTEGER PRIMARY KEY,
    id_sucursal INTEGER,
    nombre TEXT,
    ciudad TEXT
)
""")


# FACT VENTAS


cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_ventas(
    id_fact INTEGER PRIMARY KEY,

    id_cliente_sk INTEGER,
    id_producto_sk INTEGER,
    id_tiempo_sk INTEGER,
    id_sucursal_sk INTEGER,

    cantidad INTEGER,
    ingresos REAL
)
""")

conexion.commit()
conexion.close()

print("\nDATA WAREHOUSE CREADO")
print("Archivo warehouse.db generado correctamente")