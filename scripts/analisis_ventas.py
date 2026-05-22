
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset desde la carpeta /datos usando ruta relativa
# para garantizar la reproducibilidad en cualquier entorno
df = pd.read_csv("../datos/ventas.csv")

# Calculamos la venta total por fila multiplicando cantidad por precio
# porque el dataset no trae ese valor precalculado
df["venta_total"] = df["cantidad"] * df["precio"]

# Sumamos todas las ventas para obtener el volumen total del periodo
# Este indicador permite evaluar el desempeño general de la empresa
ventas_totales = df["venta_total"].sum()
print(f"Ventas totales: ${ventas_totales:,.0f}")

# Agrupamos por producto y sumamos cantidades para identificar
# cuál tuvo mayor demanda, independientemente de su precio
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {producto_mas_vendido}")

# Convertimos la columna fecha a tipo datetime para poder
# extraer el mes y agrupar las ventas por período mensual
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["venta_total"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# Generamos un gráfico de barras porque permite comparar visualmente
# el volumen de ventas entre meses de forma clara y directa
fig, ax = plt.subplots()
ventas_por_mes.plot(kind="bar", color="steelblue", edgecolor="black", ax=ax)
ax.set_title("Evolución de Ventas por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")

# Rotamos las etiquetas a horizontal para facilitar la lectura
ax.set_xticklabels([str(m) for m in ventas_por_mes.index], rotation=0)
plt.tight_layout()

# Guardamos el gráfico en /resultados para separar outputs del código fuente
plt.savefig("../resultados/grafico_ventas.png")
plt.show()
print("\nGráfico guardado en /resultados/grafico_ventas.png")
