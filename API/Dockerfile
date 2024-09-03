# Usa una imagen base de Python
FROM python:3.12-alpine3.17
# Establece el directorio de trabajo en el contenedor
WORKDIR /app
# Copia los archivos locales al contenedor
COPY requirements.txt requirements.txt
# Instala las dependencias
RUN pip install -r requirements.txt
COPY . .
# Define el comando por defecto
#CMD [ "python", "-m", "fastapi", "run", "--host=0.0.0.0" ] # Se usa esta configuración para Flask.
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8090", "--reload"]