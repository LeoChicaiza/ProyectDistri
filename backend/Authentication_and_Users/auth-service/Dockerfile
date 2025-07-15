FROM python:3.10-slim

# 1) Dependencias de compilación + SSL + GCC
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      libffi-dev \
      libssl-dev \
      python3-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2) Instala T O D A S las libs desde requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 3) Copia el código
COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app"

# 4) Expón y arranca
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "4"]