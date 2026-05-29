# 1. Usamos una imagen oficial de Python ligera como base
FROM python:3.11-slim

# 2. Evita que Python escriba archivos .pyc en el contenedor
ENV PYTHONDONTWRITEBYTECODE=1

# 3. Evita que Python guarde en búfer los mensajes de la terminal (para ver los prints en tiempo real)
ENV PYTHONUNBUFFERED=1

# 4. Establecemos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 5. Copiamos el archivo de requerimientos primero (ayuda a cachear las capas de Docker)
COPY requirements.txt /app/

# 6. Actualizamos pip e instalamos las dependencias del proyecto
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 7. Copiamos todo el resto del código del backend al contenedor
COPY . /app/

# NUEVO: Aseguramos la carpeta de imágenes y declaramos el volumen genérico
# (Asumiendo que en tu código Flask guardas las fotos en una carpeta llamada 'uploads')
# =====================================================================
RUN mkdir -p /app/uploads
VOLUME ["/app/uploads"]

# 8. Exponemos el puerto 5000 (que es donde corre tu Flask)
EXPOSE 5000

# 9. Comando para arrancar la aplicación usando run.py
CMD ["python", "run.py"]