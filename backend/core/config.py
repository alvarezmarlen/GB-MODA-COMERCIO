import os

class Config:
    # Obtiene la ruta absoluta de la carpeta actual
    BASE_DIR= os.path.dirname(os.path.abspath(__file__))
    
    # Define dónde se guardará el archivo SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../moda_comercio.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False