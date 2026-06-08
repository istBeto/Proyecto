from faker import Faker
import pandas as pd
import random
import os
from datetime import datetime, timedelta

fake = Faker('es_MX')

os.makedirs("../datos", exist_ok=True)


# CLIENTES


clientes = []

for i in range(1, 501):
    clientes.append([
        i,
        fake.name(),
        random.randint(18, 70),
        random.choice(["M", "F"]),
        fake.city()
    ])

df_clientes = pd.DataFrame(
    clientes,
    columns=["id_cliente", "nombre", "edad", "sexo", "ciudad"]
)

df_clientes.to_csv("../datos/clientes.csv", index=False)


# PRODUCTOS


productos_nombres = [
    "Laptop",
    "Monitor",
    "Teclado",
    "Mouse",
    "Audifonos",
    "Tablet",
    "Impresora",
    "Router",
    "Webcam",
    "Disco SSD"
]

productos = []

for i in range(1, 51):
    nombre = random.choice(productos_nombres)

    costo = random.randint(500, 5000)
    precio = costo * random.uniform(1.2, 1.8)

    productos.append([
        i,
        nombre,
        "Tecnologia",
        round(precio, 2),
        costo
    ])

df_productos = pd.DataFrame(
    productos,
    columns=[
        "id_producto",
        "nombre",
        "categoria",
        "precio",
        "costo"
    ]
)

df_productos.to_csv("../datos/productos.csv", index=False)


# SUCURSALES


sucursales = [
    [1, "Sucursal Norte", "Toluca"],
    [2, "Sucursal Centro", "CDMX"],
    [3, "Sucursal Sur", "Puebla"],
    [4, "Sucursal Oriente", "Queretaro"]
]

df_sucursales = pd.DataFrame(
    sucursales,
    columns=["id_sucursal", "nombre", "ciudad"]
)

df_sucursales.to_csv("../datos/sucursales.csv", index=False)


# EMPLEADOS


empleados = []

for i in range(1, 51):
    empleados.append([
        i,
        fake.name(),
        random.choice([
            "Vendedor",
            "Gerente",
            "Supervisor",
            "Administrativo"
        ])
    ])

df_empleados = pd.DataFrame(
    empleados,
    columns=[
        "id_empleado",
        "nombre",
        "puesto"
    ]
)

df_empleados.to_csv("../datos/empleados.csv", index=False)


# PROVEEDORES


proveedores = []

for i in range(1, 31):
    proveedores.append([
        i,
        fake.company(),
        fake.phone_number()
    ])

df_proveedores = pd.DataFrame(
    proveedores,
    columns=[
        "id_proveedor",
        "empresa",
        "telefono"
    ]
)

df_proveedores.to_csv("../datos/proveedores.csv", index=False)


# VENTAS


ventas = []

fecha_inicio = datetime.now() - timedelta(days=180)

for i in range(1, 10001):

    fecha = fecha_inicio + timedelta(
        days=random.randint(0, 180)
    )

    cantidad = random.randint(1, 5)

    producto = random.randint(1, 50)

    total = round(
        random.uniform(500, 15000),
        2
    )

    ventas.append([
        i,
        fecha.date(),
        random.randint(1, 500),
        producto,
        random.randint(1, 4),
        cantidad,
        total
    ])

df_ventas = pd.DataFrame(
    ventas,
    columns=[
        "id_venta",
        "fecha",
        "id_cliente",
        "id_producto",
        "id_sucursal",
        "cantidad",
        "total"
    ]
)

df_ventas.to_csv("../datos/ventas.csv", index=False)


# RESUMEN


print("\nDATOS GENERADOS")
print("---------------------")
print("Clientes:", len(df_clientes))
print("Productos:", len(df_productos))
print("Sucursales:", len(df_sucursales))
print("Empleados:", len(df_empleados))
print("Proveedores:", len(df_proveedores))
print("Ventas:", len(df_ventas))