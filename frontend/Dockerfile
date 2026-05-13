# ── Etapa 1: construir la app Vue ────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app

# PRIMERO copiamos package.json solo (caché de Docker)
COPY package*.json ./

# Docker hace el npm install AQUÍ DENTRO — no en tu terminal
RUN npm install

# Copiamos el resto del código fuente
COPY . .

# Compilamos Vue para producción
RUN npm run build

# ── Etapa 2: servir el build con Nginx ───────────────────
FROM nginx:alpine

# Copiamos solo el resultado del build (carpeta dist/)
COPY --from=builder /app/dist /usr/share/nginx/html

# Configuración de Nginx para Vue Router (rutas SPA)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80