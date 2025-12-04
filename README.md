# Generador de Gráficos 2D

## Descripción

Este proyecto es un generador de gráficos 2D que permite visualizar datos de municipios de Antioquia mediante gráficos de barras. Utiliza las librerías **Pandas** para el manejo de datos y **Matplotlib** para la creación de visualizaciones.

La aplicación genera gráficos de barras que muestran las ventas promedio por municipio, facilitando la visualización y análisis de datos demográficos y económicos de la región.

## URL del Repositorio GitHub

```
https://github.com/yojhnnv11/GRAFICOS-2D
```

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/GRAFICOS-2D.git
cd GRAFICOS-2D
```

### 2. Crear el Entorno Virtual

**Importante:** Este proyecto utiliza un entorno virtual para evitar instalar dependencias globalmente. Esto es una buena práctica que asegura la reproducibilidad del proyecto.

```bash
python -m venv .venv
```

### 3. Activar el Entorno Virtual

**En Windows:**
```bash
.venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instalar las Dependencias

Una vez activado el entorno virtual, instale todas las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene todas las dependencias con sus versiones específicas congeladas para garantizar la reproducibilidad del proyecto.

## Ejecución del Proyecto

Para ejecutar el proyecto desde cero, asegúrese de tener el entorno virtual activado y ejecute:

```bash
python src/main.py
```

Esto generará:
1. Una visualización en consola de los datos de los municipios
2. Un gráfico de barras interactivo mostrando las ventas promedio por municipio

## Estructura del Proyecto

```
GRAFICOS-2D/
├── src/
│   ├── main.py          # Punto de entrada principal de la aplicación
│   └── utils.py         # Funciones de utilidad para creación de gráficos
├── .venv/               # Entorno virtual (ignorado por Git)
├── .gitignore          # Archivos y directorios ignorados por Git
├── requirements.txt    # Dependencias del proyecto con versiones congeladas
└── README.md           # Este archivo
```

## Funcionalidades

- **Creación de DataFrames**: Utiliza Pandas para estructurar datos de municipios
- **Visualización de Datos**: Muestra datos en consola de forma organizada
- **Generación de Gráficos**: Crea gráficos de barras personalizados con Matplotlib
- **Modularidad**: Código organizado en módulos reutilizables

## Dependencias Principales

- **pandas** (2.3.3): Manipulación y análisis de datos
- **matplotlib** (3.10.7): Creación de gráficos y visualizaciones
- **numpy** (2.3.4): Operaciones numéricas (dependencia de pandas y matplotlib)

Todas las dependencias y sus versiones están especificadas en `requirements.txt` para garantizar la reproducibilidad.

## Guías de Colaboración

### Uso de Ramas y Pull Requests

Este proyecto utiliza un flujo de trabajo basado en ramas (branches) y Pull Requests (PRs) para facilitar la colaboración:

1. **Crear una rama nueva** para cada nueva funcionalidad o corrección:
   ```bash
   git checkout -b nombre-de-la-rama
   ```

2. **Realizar cambios** y hacer commits descriptivos

3. **Subir la rama** al repositorio remoto:
   ```bash
   git push origin nombre-de-la-rama
   ```

4. **Crear un Pull Request** en GitHub para revisar los cambios antes de fusionarlos con la rama principal

### Mensajes de Commit Descriptivos

Es importante escribir mensajes de commit claros y descriptivos que expliquen qué cambios se realizaron y por qué. Ejemplos:

```
✅ Buen mensaje:
feat: Agregar función para generar gráficos de líneas
fix: Corregir error en cálculo de promedios
docs: Actualizar README con instrucciones de instalación

❌ Mal mensaje:
cambios
fix
update
```

Formato recomendado:
- **feat**: Nueva funcionalidad
- **fix**: Corrección de errores
- **docs**: Cambios en documentación
- **refactor**: Refactorización de código
- **test**: Agregar o modificar tests
- **style**: Cambios de formato (no afectan el código)

## Solución de Problemas

### Error al importar módulos

Si encuentra errores de importación, asegúrese de:
- Ejecutar el script desde la raíz del proyecto
- Tener el entorno virtual activado
- Haber instalado todas las dependencias con `pip install -r requirements.txt`

### El gráfico no se muestra

- Asegúrese de tener una interfaz gráfica disponible
- En algunos entornos, puede ser necesario usar `plt.savefig()` en lugar de `plt.show()`

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## Autor

[Su nombre aquí]

---

**Nota importante:** Recuerde actualizar la URL del repositorio GitHub en la sección correspondiente de este README.

