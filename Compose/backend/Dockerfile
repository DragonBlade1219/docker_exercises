FROM python:3.12-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]