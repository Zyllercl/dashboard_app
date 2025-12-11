import pandas as pd
from pathlib import Path

class DataManager:

    # Inicialización del DataManager con la ruta del archivo CSV.
    def __init__(self, filepath):
        # Paso 1: Convertir a Path el archivo CSV (de String a un Objeto Interactivo)
        path = Path(filepath)

        # Paso 2: Verifica que el archivo existe
        if not path.exists():
            raise FileNotFoundError(f'[ERROR] El archivo no existe: {path}')

        # Paso 3: Guardar la Ruta y preparación del DataFrame
        self.filepath = path
        self.df = None

    # Carga de datos desde el archivo CSV y almacenamiento en variable df
    def load_data(self):
        # Paso 1: Leer el CSV con pandas
        df = pd.read_csv(self.filepath)

        # Paso 2: Convertir la columna 'fecha' a datetime
        df["fecha"] = pd.to_datetime(
            df["fecha"],
            dayfirst = True, # Formato fecha LATAM
            format = "%d/%m/%y" # Formato fecha del CSV
        )

        # Paso 3: Guardar internamente el DataFrame
        self.df = df
        print(f'[INFO] f(load_data) - {df}')

        return df

    # Retorna el DataFrame completo
    def get_raw_data(self):
        # Si los datos aún no se cargan, lo hace automáticamente
        if self.df is None:
            self.load_data()
        
        print(f'[INFO] f(get_raw_data) - {len(self.df)} registros')
        
        return self.df

    # Calculo del total gastado por categoría
    def get_total_for_category(self):
        # Paso 0: Obtener el DataFrame
        df = self.get_raw_data()
        print(f'[INFO] f(get_total_for_category) - Calculando totales por categoría...')

        # Paso 1: Agrupar por categoria y sumar montos
        monto_total = df.groupby("categoria").monto.sum()
        # Paso 2: Convertir en DataFrame
        monto_total = monto_total.reset_index()
        # Paso 3: Renombrar la columna "monto" a "total"
        monto_total = monto_total.rename(columns={"monto":"total"})

        # Paso 4: Retornar un DataFrame con: categoria | total
        return monto_total

if __name__ == '__main__':
    
    from pathlib import Path

    # 1. Ruta dinámica del archivo CSV
    base_dir = Path(__file__).resolve().parent  # Obtener la ruta absoluta de la carpeta donde está data_manager.py
    # data_dir = base_dir / "data"                # Accede a la carpeta "data" (Como ya nos encontramos en dentro de la carpeta "data" se omite)
    filepath = base_dir / "dataset.csv"         # Construye la ruta completa del CSV
    
    print(f'[DATA] Usando archivo: {filepath}')

    # 2. Instanciar DataManager
    manager = DataManager(filepath)

    # 3. Testing de funciones
    print(f'\n[TEST 1] load_data()\n')
    df = manager.load_data()
    print(df)

    print(f'\n[TEST 2] get_raw_data()\n')
    df_raw = manager.get_raw_data()
    print(df_raw)

    print(f'\n[TEST 3] get_total_for_category()\n')
    df_total = manager.get_total_for_category()
    print(df_total)
