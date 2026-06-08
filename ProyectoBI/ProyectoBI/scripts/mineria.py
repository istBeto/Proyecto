import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

conexion = sqlite3.connect("../datos/empresa.db")

query = """
SELECT
    id_cliente,
    COUNT(*) AS frecuencia,
    SUM(total) AS gasto_total
FROM ventas
GROUP BY id_cliente
"""

clientes = pd.read_sql(query, conexion)

X = clientes[["frecuencia", "gasto_total"]]

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clientes["cluster"] = kmeans.fit_predict(X)

plt.figure(figsize=(8,6))

plt.scatter(
    clientes["frecuencia"],
    clientes["gasto_total"],
    c=clientes["cluster"]
)

plt.xlabel("Frecuencia de Compra")
plt.ylabel("Gasto Total")
plt.title("Segmentación de Clientes (K-Means)")

plt.tight_layout()

plt.savefig("../evidencias/segmentacion_clientes.png")

print("Segmentacion creada correctamente")

conexion.close()