# Predicción de Precios de Airbnb en Valencia mediante Machine Learning, Datos Espaciales y Visión Artificial

## 📌 Descripción del Proyecto

Este proyecto desarrolla un pipeline avanzado de Machine Learning para predecir el precio por noche de alojamientos de Airbnb en la ciudad de Valencia.

A diferencia de modelos tradicionales, este enfoque se distingue por la integración de tres fuentes de datos multimodales:

1. **Datos Tabulares:** Histórico de precios y calendarios (2025-2026).
2. **Datos Geoespaciales y de Entorno (OSMnx):** Proyecciones UTM y cálculo de distancias exactas a puntos de interés (Playa, Ciudad de las Artes) y densidad de ocio/transporte en un radio de 500m.
3. **Visión Artificial (Zero-Shot CLIP):** Extracción automatizada de atributos estéticos (piscinas, luminosidad, terrazas) a partir de las fotografías de los alojamientos utilizando modelos fundacionales de OpenAI.

El modelo se entrena de forma robusta con validación *Out-of-Time* (entrenamiento en 2025, test en 2026), garantizando métricas fiables y libres de fugas de datos (Data Leakage).

## Estructura del Repositorio

* `data_sample/`: Muestra reducida de los datasets originales y resultados de la IA visual para ejecutar el proyecto en modo demostración.

* `src/`: Notebooks principales del proyecto.
  * `01_Procesamiento_Imagenes.ipynb`: Pipeline offline para descargar y procesar las imágenes con CLIP.
  * `02_Analisis_Airbnb.ipynb`: Pipeline principal de preprocesamiento espacial, entrenamiento (Random Forest / Gradient Boosting / Redes Neuronales) y evaluación.
* `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## Instalación y Configuración

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)