import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conexion = sqlite3.connect("../datos/warehouse.db")

query = """
SELECT
    substr(fecha,1,7) as mes,
    COUNT(*) as total_ventas
FROM fact_ventas
GROUP BY mes
ORDER BY mes
"""

ventas_mes = pd.read_sql(query, conexion)

plt.figure(figsize=(10,5))
plt.plot(
    ventas_mes["mes"],
    ventas_mes["total_ventas"],
    marker="o"
)

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad de Ventas")

plt.tight_layout()

plt.savefig("../evidencias/ventas_por_mes.png")

print("Grafica ventas_por_mes.png creada")

conexion = sqlite3.connect("../datos/empresa.db")

query = """
SELECT
    nombre,
    SUM(precio - costo) AS utilidad
FROM productos
GROUP BY nombre
ORDER BY utilidad DESC
LIMIT 10
"""

rentables = pd.read_sql(query, conexion)

plt.figure(figsize=(10,5))

plt.bar(
    rentables["nombre"],
    rentables["utilidad"]
)

plt.title("Productos Más Rentables")
plt.xlabel("Producto")
plt.ylabel("Utilidad")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../evidencias/productos_rentables.png")

print("Grafica productos_rentables.png creada")

conexion.close()