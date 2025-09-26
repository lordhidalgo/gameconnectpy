# 🎮 GameConnect – Data Analytics



Proyecto en Python para el análisis de datos de ventas de un e-commerce ficticio llamado **GameConnect**. Esta aplicación te permite cargar, limpiar, preparar y analizar datos para extraer **información valiosa**. El proyecto sigue una **estructura de Git Flow** para demostrar buenas prácticas de desarrollo.

### Características Principales

* **Ingesta de Datos:** Carga datos de archivos CSV y JSON.
* **Preprocesamiento:** Maneja valores nulos, estandariza texto y limpia formatos de precios.
* **Análisis:** Combina y analiza datos para responder preguntas clave sobre el negocio.

---

## 📂 Estructura del Proyecto
gameconnect-analytics/
├─ data/
│  ├─ juegos.csv (Datos de ejemplo de videojuegos)
│  └─ pedidos.json (Datos de ejemplo de pedidos)
├─ src/
│  ├─ preprocess.py (Módulo de funciones para limpieza y carga)
│  └─ analisis.py (Script principal de análisis)
├─ .gitignore
└─ README.md

---

## ⚙️ Requisitos

* Python 3.11 o superior
* `pandas`

---

## 🚀 Instalación y Uso

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/](https://github.com/)<lordhidalgo>/gameconnectpy.git
    cd gameconnect-analytics
    ```

2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    # venv\Scripts\activate
    # En macOS / Linux:
    # source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install pandas
    ```

4.  **Ejecuta el análisis:**
    ```bash
    cd src
    python analisis.py
    ```

### Ejemplo de Salida en Consola:

Videojuego más vendido (por unidades): CyberQuest

Ingresos totales por categoría:

category
acción        1200.0
aventura       950.0
estrategia     600.0
Name: revenue, dtype: float64

Número de pedidos con más de 2 unidades: 8


---

## 📊 Preguntas de Análisis Respondidas

El script `analisis.py` utiliza las funciones de preprocesamiento para responder las siguientes preguntas:

1.  **Análisis de Frecuencia:** ¿Cuál es el videojuego más vendido?
2.  **Análisis de Agregación:** ¿Cuál es el ingreso total por categoría de juego?
3.  **Análisis con Filtrado y Conteo:** ¿Cuántos pedidos contienen más de 2 unidades?

---

## 📁 Datos de Ejemplo

Los archivos `juegos.csv` y `pedidos.json` simulan un dataset del mundo real con **inconsistencias** como texto inconsistente, símbolos monetarios y valores faltantes, lo que demuestra la utilidad del módulo de preprocesamiento.

---

## 🌳 Flujo de Trabajo con Git Flow

Este proyecto se gestiona siguiendo el modelo de Git Flow:

* `master`: Rama protegida para **versiones estables**.
* `develop`: Rama base para integrar **nuevas características**.
* `feature/*`: Ramas de desarrollo para cada **nueva funcionalidad**.
* **Pull Requests:** Se utilizan para fusionar ramas `feature/*` en `develop` y, finalmente, en `master`.

---

## ✍️ Autor

Proyecto desarrollado por **[Mario Hidalgo]** como parte del **Momento 2 – Data Analytics**.