# Etapa 1: Crear el volumen y copiar los archivos
FROM python:3.11 AS volumen_instancia

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Crea el volumen
VOLUME /app

# Copia los archivos del proyecto al volumen
COPY . /app

# Etapa 2: Ejecutar los comandos del Dockerfile
FROM python:3.11

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos desde la etapa anterior (volumen_instancia)
COPY --from=volumen_instancia /app /app

# Instalamos las dependencias desde el archivo requirements.txt
RUN pip install -r requirements.txt
# RUN python app/manage.py migrate

# Exponemos el puerto interno 80
EXPOSE 80

# Ejecutamos el comando para hacer las migraciones a la BD, collectstatic e iniciar el servidor Django
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:80