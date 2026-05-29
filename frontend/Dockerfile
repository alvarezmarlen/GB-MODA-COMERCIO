# Usamos una imagen de Node.js
FROM node:20-alpine

# Creamos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de dependencias
COPY package*.json ./

# Instalamos las dependencias
RUN npm install

# Copiamos el resto del código del frontend
COPY . .

# Exponemos el puerto típico de desarrollo (cambialo si usas Vite - 5173 o Angular - 4200)
EXPOSE 5173
# Comando para arrancar el frontend en modo desarrollo
CMD ["npm", "run", "dev"]