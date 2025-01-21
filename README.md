
# Organizador de Archivos por Extensión

Este proyecto de Python organiza archivos en carpetas basadas en su extensión. También permite revertir los cambios realizados utilizando un registro de los archivos antes de ser movidos.

## Características

- **Organización por Extensión:** Clasifica archivos en carpetas basadas en extensiones comunes (documentos, imágenes, vídeos, etc.).
- **Subcategorías Especializadas:** Documentos y Archivos 3D tienen subcategorías específicas.
- **Registro Automático:** Genera un registro (`revert.json`) con las ubicaciones originales y nuevas de los archivos.
- **Reversión Completa:** Devuelve los archivos a sus ubicaciones originales usando el registro.
- **Versiones:** Ofrece dos versiones:
  - **GUI:** Interfaz gráfica usando `Tkinter`.
  - **Consola:** Versión basada en texto para uso en terminales.

## Instalación

1. Clona el repositorio o descarga los archivos.
   ```bash
   git clone https://github.com/AransDino/py-organizador-archivos.git
   cd py-organizador-archivos
   ```
2. Asegúrate de tener Python 3 instalado.
3. Instala las dependencias necesarias si usas la versión GUI:
   ```bash
   pip install tkinter
   ```

### Dependencias

El script utiliza las siguientes bibliotecas estándar de Python (ya incluidas en Python):

- `os`: Gestión de archivos y directorios.
- `shutil`: Operaciones de movimiento y copia de archivos.
- `json`: Manejo de datos estructurados.
- `tkinter` (solo para la versión GUI).

## Uso

### Versión GUI

1. Ejecuta la versión GUI:
   ```bash
   python organizer-gui.py
   ```
2. En la ventana, selecciona:
   - **Organizar Archivos por Extensión:** Clasifica archivos de una carpeta seleccionada.
   - **Revertir:** Deshace la organización y restaura los archivos.

### Versión Consola

1. Ejecuta la versión de consola:
   ```bash
   python organizer-console.py
   ```
2. Selecciona una opción del menú:
   - **Organizar archivos:** Introduce la ruta de la carpeta que deseas organizar. Se crea una subcarpeta llamada `Organizados` dentro de la carpeta seleccionada.
   - **Revertir organización:** Introduce la ruta de la carpeta que contiene `Organizados` para restaurar los archivos a su ubicación original.
   - **Salir:** Finaliza el programa.

### Cambios en la Estructura del Repositorio

- **Archivos eliminados:**
  - `organizer.py` ya no está disponible.
- **Nuevos Archivos:**
  - `organizer-gui.py`: Versión gráfica.
  - `organizer-console.py`: Versión de consola.
  - `organizer-console-dev.py`: Archivo de desarrollo para pruebas.

### Categorías Soportadas

- **Configuraciones y Backups:** `.ini`, `.conf`, `.cfg`, `.bak`, etc.
- **Documentos:** `.pdf`, `.docx`, `.xlsx`, `.xlsm`, etc. (subcategorías: `PDFs`, `Word`, `Hojas de Cálculo`, etc.).
- **Imágenes:** `.jpg`, `.png`, `.tiff`, etc.
- **Vídeos:** `.mp4`, `.avi`, `.mkv`, etc.
- **Audios:** `.mp3`, `.wav`, `.flac`, etc.
- **Archivos 3D:** `.stl`, `.obj`, `.fcstd` (subcategoría: `Modelos Propios`), etc.
- **Diseño y Gráficos:** `.psd`, `.ai`, `.svg`, etc.
- **Comprimidos:** `.zip`, `.rar`, `.7z`, etc.
- **Códigos y Scripts:** `.py`, `.js`, `.html`, `.css`, etc.

### Reversión

El proceso de organización genera un archivo `revert.json` en la carpeta `Organizados`. Este archivo contiene un registro de las ubicaciones originales y nuevas de los archivos, lo que permite revertir el proceso.

## Contribuciones

Contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto, por favor abre un `issue` o envía un `pull request`.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
