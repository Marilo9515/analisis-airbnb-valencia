# Análisis de Big Data: Airbnb Valencia (2025-2026)

Este proyecto analiza los datos de Airbnb de la ciudad de Valencia para los años 2025 y 2026. 

## ⚠️ Nota sobre los datos
Debido a los límites de tamaño de GitHub, la carpeta `data/` original (que contiene los archivos completos `.csv` y `.gz`) **no está incluida en este repositorio**. 

En su lugar, se incluye una carpeta `data_sample/` con las primeras 100 líneas de cada archivo para poder explorar la estructura del código.

## Estructura del proyecto

```
Airbnb_Valencia/
│
├── data/                   <-- Carpeta principal de datos (lee la nota abajo)
│   ├── 2025/
│   │   ├── listings.csv
│   │   ├── reviews.csv
│   │   ├── calendar.csv.gz
│   │   └── neighbourhoods.csv
│   └── 2026/
│       ├── listings.csv
│       ├── reviews.csv
│       ├── calendar.csv.gz
│       └── neighbourhoods.csv
│
├── src/                    <-- Tus scripts de Python
│   └── analisis_airbnb.py  <-- Tu archivo ejecutable principal
│
├── .gitignore              <-- Archivos que no se subirán a GitHub
├── requirements.txt        <-- Librerías necesarias (pandas, etc.)
└── README.md               <-- Explicación de tu proyecto

```

### ¿Cómo ejecutar el proyecto localmente?

1. Clona este repositorio.
2. Descarga los datos reales de [Inside Airbnb](http://insideairbnb.com/get-the-data/) (o tu fuente original).
3. Crea una carpeta llamada `data/` en la raíz del proyecto.
4. Organiza los datos descargados en subcarpetas por año: `data/2025/` y `data/2026/`.
5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt


## Ejecuta el script principal:

python src/analisis_airbnb.py











### 4. (Opcional pero recomendado) Instalar el proyecto en modo editable

Esto permite usar `import src.io.loader` desde cualquier notebook sin
necesidad de manipular `sys.path` manualmente:

```bash
pip install -e .
```

### 5. Abrir y ejecutar los notebooks

Abre la carpeta `notebooks/` en VS Code o Jupyter y ejecuta los notebooks
en orden. Cada notebook incluye en su primera celda una linea de
seguridad que anade la raiz del proyecto al `sys.path`, por lo que
funcionara incluso si el paso 4 no se ha ejecutado.

## Notas para la evaluacion

- Los datos originales (Airbnb Valencia) no se incluyen en el repositorio
  por tamano; ver `notebooks/00_descarga_datos.ipynb` (o instrucciones
  equivalentes) para obtenerlos.
- El pipeline de carga de datos esta en `src/io/loader.py`.
- Los modelos comparados y metricas de evaluacion se documentan en el
  notebook principal de resultados.
