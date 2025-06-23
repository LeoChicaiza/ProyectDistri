FROM python:3.9-slim
 
WORKDIR /app
 
# Primero copia solo requirements.txt para aprovechar el cache de Docker
COPY requirements.txt .
 
RUN pip install --no-cache-dir -r requirements.txt
 
# Luego copia el resto de los archivos
COPY . .
 
ENV PYTHONPATH="${PYTHONPATH}:/app"
 
# Configuración recomendada para producción
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8013", "--workers", "4"]
