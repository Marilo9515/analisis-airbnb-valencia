import pandas as pd
from pathlib import Path
import os
import shutil

DIRECTORIO_RAIZ = Path(__file__).resolve().parent.parent
RUTA_ORIGEN = DIRECTORIO_RAIZ / "data"
RUTA_DESTINO = DIRECTORIO_RAIZ / "data_sample"

def crear_muestras():
    # Crear la carpeta de destino si no existe
    RUTA_DESTINO.mkdir(exist_ok=True)
    
    años = [2025, 2026]
    archivos = ["listings.csv", "reviews.csv", "calendar.csv.gz", "neighbourhoods.csv"]
    archivo_mapa = "neighbourhoods.geojson"

    for año in años:
        origen_año = RUTA_ORIGEN / str(año)
        destino_año = RUTA_DESTINO / str(año)
        
        if not origen_año.exists():
            continue
            
        destino_año.mkdir(exist_ok=True)
        
# 1. Procesar los CSV (100 filas)

        for archivo in archivos:
            ruta_archivo = origen_año / archivo
            if ruta_archivo.exists():
                print(f"Creando muestra de {año}/{archivo}...")
                
                # Leer solo las primeras 100 filas
                if archivo.endswith('.gz'):
                    df = pd.read_csv(ruta_archivo, compression='gzip', nrows=100, low_memory=False)
                    # Guardar la muestra también comprimida
                    df.to_csv(destino_año / archivo, index=False, compression='gzip')
                else:
                    df = pd.read_csv(ruta_archivo, nrows=100, low_memory=False)
                    df.to_csv(destino_año / archivo, index=False)

# 2. Procesar el GeoJSON (Copiar completo porque pesa muy poco y no se puede cortar)

        ruta_geo = origen_año / archivo_mapa
        if ruta_geo.exists():
            print(f"Copiando archivo completo {año}/{archivo_mapa}...")
            shutil.copy(ruta_geo, destino_año / archivo_mapa)
                    
    print("\n¡Muestras creadas con éxito en data_sample/! # Esta carpeta SÍ se subirá a GitHub.")

if __name__ == "__main__":
    crear_muestras()