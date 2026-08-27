import pandas as pd
import geopandas as gpd
from pathlib import Path
import os

# Definir rutas relativas
DIRECTORIO_RAIZ = Path(__file__).resolve().parent.parent

# Detectar si existe la carpeta de datos reales, si no, usar la de muestra
if (DIRECTORIO_RAIZ / "data").exists():
    DIRECTORIO_DATOS = DIRECTORIO_RAIZ / "data"
    print("Usando carpeta de datos REALES (data/)")
else:
    DIRECTORIO_DATOS = DIRECTORIO_RAIZ / "data_sample"
    print("Usando carpeta de datos de MUESTRA (data_sample/)")

def cargar_datos_año(año):
    """Carga los 4 archivos de un año específico."""
    ruta_año = DIRECTORIO_DATOS / str(año)
    
    if not ruta_año.exists():
        print(f"Advertencia: La ruta {ruta_año} no existe. Saltando...")
        return None
    
    print(f"Cargando datos del año {año}...")
    
    datos = {
        "listings": pd.read_csv(ruta_año / "listings.csv", low_memory=False),
        "reviews": pd.read_csv(ruta_año / "reviews.csv", low_memory=False),
        "calendar": pd.read_csv(ruta_año / "calendar.csv.gz", compression='gzip', low_memory=False),
        "neigh": pd.read_csv(ruta_año / "neighbourhoods.csv"),
	"mapa_barrios": gpd.read_file(ruta_año / "neighbourhoods.geojson")
    }
    return datos

def main():
    años_analisis = [2025, 2026]
    db = {}
    
    for año in años_analisis:
        datos_cargados = cargar_datos_año(año)
        if datos_cargados:
            db[str(año)] = datos_cargados
            
    print("\n¡Carga completada con éxito!")
    
    if "2025" in db:
        mapa_25 = db["2025"]["mapa_barrios"]
        print(f"Mapa de 2025 cargado con {mapa_25.shape[0]} barrios/polígonos.")
        # Si quisieras ver el mapa rápido, podrías usar: mapa_25.plot()

if __name__ == "__main__":
    main()