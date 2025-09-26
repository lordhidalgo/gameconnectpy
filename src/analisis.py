from pathlib import Path
import pandas as pd
from preprocess import (
    load_data,
    handle_missing_values,
    standardize_text,
    clean_price_column,
)

# Función para imprimir títulos con estilo
def print_title(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

# Función para imprimir resultados destacados
def print_result(label, value, emoji=""):
    print(f"{emoji} {label}: {value}")

# Cargar datos
juegos   = load_data(Path("data/juegos.csv"))
pedidos  = load_data(Path("data/pedidos.json"))

# Manejo de valores nulos
juegos   = handle_missing_values(juegos, strategy="drop")
pedidos  = handle_missing_values(pedidos, strategy="fill0")

# Estandarizar texto en columnas de texto
juegos = standardize_text(juegos, ["nombre", "categoria"])

# Limpiar columna de precios (eliminar $ y convertir a float)
juegos = clean_price_column(juegos, "precio")

# Validar columnas clave para el merge
required_cols_juegos  = {"id_juego", "nombre", "categoria", "precio"}
required_cols_pedidos = {"id_juego", "cantidad"}

missing_juegos  = required_cols_juegos - set(juegos.columns)
missing_pedidos = required_cols_pedidos - set(pedidos.columns)

if missing_juegos:
    raise KeyError(f"Faltan columnas en juegos.csv: {missing_juegos}")
if missing_pedidos:
    raise KeyError(f"Faltan columnas en pedidos.json: {missing_pedidos}")

# Unir pedidos con juegos por ID
merged = pedidos.merge(juegos, on="id_juego", how="inner")

# Análisis de Frecuencia
ventas_por_juego = merged.groupby("nombre")["cantidad"].sum()
juego_top = ventas_por_juego.idxmax()
print_title("📊 Videojuego con más ventas")
print_result("Videojuego más vendido (unidades)", juego_top, "🔥")

# Análisis de Agregación
merged["ingresos"] = merged["precio"] * merged["cantidad"]
ingresos_por_categoria = merged.groupby("categoria")["ingresos"].sum()

print_title("💰 Ingresos totales por categoría")
for categoria, ingreso in ingresos_por_categoria.items():
    print_result(f"Categoría '{categoria}'", f"${ingreso:,.2f}", "💵")

# Análisis con Filtrado y Conteo
pedidos_grandes = merged[merged["cantidad"] > 2].shape[0]
print_title("📦 Pedidos grandes")
print_result("Número de pedidos con más de 2 unidades", pedidos_grandes, "📬")

# Fin del análisis
print("\n✅ Análisis completado con éxito!")
