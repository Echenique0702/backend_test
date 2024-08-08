# Imagen base de python
FROM python:3.12-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias necesarias para compilar paquetes Python
RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Copiar el archivo de requerimientos y actualizar pip
COPY ./requirements/base.txt /app/requirements/base.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements/base.txt


# Copiar todo el código del proyecto
COPY . .


# Exponer el puerto 8000
EXPOSE 8000
