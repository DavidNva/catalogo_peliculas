# 🎥 Catálogo de Películas

Aplicación de escritorio desarrollada con **Python**, usando **Tkinter** para la interfaz gráfica y **SQLite** como base de datos local.  
Incluye un sistema **CRUD completo**, integración de recursos gráficos y empaquetado con **PyInstaller** para su distribución.

---

## 🧩 Funcionalidades

- ✅ Crear, leer, actualizar y eliminar películas
- 💻 Interfaz creada con `Tkinter`
- 📂 Base de datos `SQLite` integrada (persistencia local)
- 📦 Empaquetado como aplicación de escritorio ejecutable (.exe)

---

## 📁 Estructura del Proyecto

📁 CATALOGO_PELICULASD
├── 📁 catalogo_peliculas
│   ├── 📁 build
│   ├── 📁 client
│   │   ├── __init__.py
│   │   └── gui_app.py
│   ├── 📁 database
│   │   └── peliculas.db
│   ├── 📁 dist
│   │   └── catalogo_peliculas
│   ├── 📁 img
│   │   └── cp-logo.ico
│   ├── 📁 model
│   │   ├── __init__.py
│   │   ├── conexion_db.py
│   │   ├── pelicula_dao.py
│   │   └── catalogo_peliculas.py
│   └── catalogo_peliculas.spec
├── 📁 env
├── .gitignore
└── Readme.md

---

## 🛠️ Tecnologías Utilizadas

- **Python**
- **Tkinter** (interfaz gráfica)
- **SQLite3** (base de datos)
- **PyInstaller** (empaquetado)
- Entorno virtual: `venv`

---

## ⚙️ Instalación y Ejecución en Desarrollo

### 1. Clona el repositorio

```bash
git clone <tu_url_del_repo>
cd catalogo_peliculas
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv env

# En Windows
env\Scripts\activate
```

### 3. Instala las dependencias

> Este proyecto no requiere paquetes externos adicionales. Las librerías `tkinter` y `sqlite3` ya vienen incluidas con Python.

Para empaquetar, instala `PyInstaller`:

```bash
pip install pyinstaller
```

### 4. Ejecuta la aplicación

```bash
python catalogo_peliculas.py
```

---

## 🧪 Creación de la Tabla Inicial

Desde la interfaz de la aplicación:

1. Ve al menú **Inicio**
2. Selecciona **"Crear Registro en BD"**
3. Esto creará la tabla `peliculas` dentro del archivo `database/peliculas.db`

---

## 📦 Empaquetado con PyInstaller

Este proyecto incluye un archivo `.spec` personalizado para empaquetar imágenes, íconos y la base de datos.

### 1. Empaqueta con el archivo `.spec`

```bash
pyinstaller catalogo_peliculas.spec
```

> Asegúrate de tener `pyinstaller` instalado en tu entorno virtual.

### 2. Ejecutable final

El ejecutable se generará en:

```
dist/catalogo_peliculas/
```

Puedes copiar esta carpeta a cualquier PC con Windows y ejecutar la app directamente, **sin necesidad de tener Python instalado**.

---

## 📄 Captura de la Aplicación


```
App Catálogo de Películas
[Imagen]
```

---

