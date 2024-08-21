# Define la imagen base que se usará para construir el contenedor
 
FROM python:3.12.3
 
# Define una variable de entorno para deshabilitar el búfer de salida de Python, lo que mejora la visibilidad de las salidas en los registros
 
ENV PYTHONUNBUFFERED 1
 
RUN apt-get update && apt-get install -y python3 python3-dev libpq-dev gcc build-essential && pip3 install psycopg2-binary
 
 
# Establece el directorio de trabajo dentro del contenedor para /api/
 
WORKDIR /api/
 
# Copia el archivo requirements.txt desde la carpeta actual (donde se encuentra el Dockerfile) al directorio /api/ dentro del contenedor
 
COPY requirements.txt .
 
# Actualiza pip a la última versión
 
RUN pip install --upgrade pip
 
# Instala las dependencias requeridas desde el archivo requirements.txt usando pip
 
RUN pip install -r requirements.txt
 
# Copia todos los archivos desde la carpeta actual al directorio /api/ dentro del contenedor
 
COPY . .
 
 
# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
 
EXPOSE 8000