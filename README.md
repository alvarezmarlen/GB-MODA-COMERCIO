# GB-MODA-COMERCIO

Plataforma web para documentar, preservar y compartir historias de moda y comercio local. Los usuarios pueden registrar cronicas sobre oficios tradicionales, con soporte multiidioma, mapa interactivo y panel de administracion.

## Stack tecnologico

| Capa | Tecnologia |
|------|-----------|
| Backend | Python 3.11 + Flask 3.1 + SQLAlchemy 2.0 + SQLite |
| Autenticacion | JWT (flask-jwt-extended) |
| Frontend | Vue 3 + Vue Router 4 + vue-i18n 9 |
| Build | Vite 8 |
| Tests | pytest (backend) + vitest (frontend) |
| Infraestructura | Docker + docker-compose |

## Estructura del proyecto

```
├── backend/
│   ├── app/
│   │   ├── app.py                  # Fabrica de la aplicacion Flask
│   │   ├── core/                   # Configuracion, JWT handlers, extensiones
│   │   ├── features/
│   │   │   ├── auth/               # Login, logout, refresh token
│   │   │   ├── stories/            # CRUD de historias + imagenes
│   │   │   └── users/              # CRUD de usuarios
│   │   └── init_db.py              # Inicializador de la base de datos
│   ├── tests/                      # Tests unitarios con pytest
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/                    # Llamadas HTTP al backend
│   │   ├── components/             # Componentes Vue (atomos, organismos, templates)
│   │   ├── composables/            # Estado reactivo (auth, stories)
│   │   ├── i18n/                   # Traducciones (6 idiomas)
│   │   ├── router/                 # Rutas + guards de autenticacion
│   │   └── views/                  # Paginas (Home, Login, Admin...)
│   ├── tests/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── .env                            # Variables de entorno (no commiteado)
```

## Requisitos previos

- Docker y docker-compose instalados
- Git

## Como ejecutar

```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd MODA-COMERCIO

# 2. Crear archivo .env con las claves necesarias
# (consultar backend/.env para las variables requeridas)

# 3. Iniciar los contenedores
docker compose up --build

# 4. Acceder
# Frontend: http://localhost:5173
# Backend API: http://localhost:5000
```

## Variables de entorno

Crear un archivo `.env` en la raiz o en `backend/.env` con:

```bash
FLASK_SECRET_KEY=<clave-secreta-flask>
JWT_SECRET_KEY=<clave-secreta-jwt>
```

## Funcionalidades principales

- **Autenticacion JWT** — login con access token (1h) y refresh token (30d), blacklist de tokens revocados
- **Gestion de historias** — crear, editar, eliminar historias con imagenes
- **Panel de administracion** — vista global de todas las historias con opciones de modificar y borrar
- **Dashboard de usuario** — perfil personal y listado de historias propias
- **Internacionalizacion** — 6 idiomas: espanol, ingles, euskera, frances, arabe y rumano
- **Mapa interactivo** — exploracion de oficios por continente
- **Responsive** — adaptado a movil y escritorio

## API endpoints

### Autenticacion
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| POST | `/auth/login` | Iniciar sesion (devuelve access + refresh token) |
| POST | `/auth/logout` | Cerrar sesion (revoca el token) |
| POST | `/auth/refresh` | Renovar access token |

### Historias
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/stories` | Listar todas las historias (con filtros opcionales) |
| POST | `/stories` | Crear una nueva historia |
| GET | `/stories/:id` | Obtener una historia por ID |
| PUT | `/stories/:id` | Actualizar una historia |
| DELETE | `/stories/:id` | Eliminar una historia |
| POST | `/stories/:id/images` | Subir imagen a una historia |

### Usuarios
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/users` | Listar usuarios |
| POST | `/users` | Registrar nuevo usuario |
| GET | `/users/:id` | Obtener usuario por ID |
| PUT | `/users/:id` | Actualizar datos de usuario |
| DELETE | `/users/:id` | Eliminar usuario |

## Tests

```bash
# Tests del backend
cd backend && pytest

# Tests del frontend
cd frontend && npm test
```

## Equipo

| Nombre | GitHub |
|--------|--------|
| Marlene Alvarez | [@alvarezmarlen](https://github.com/alvarezmarlen) |
| Gabriel Hernandez | [@yggabo](https://github.com/yggabo) |
| Naia Arenaza | [@Naiare7](https://github.com/Naiare7) |
| Jorge Cereceda | [@jorgecereceda](https://github.com/jorgecereceda) |
| German Illan | [@GermanIllan](https://github.com/GermanIllan) |

## Licencia

GB-MODA-COMERCIO — Proyecto educativo.
