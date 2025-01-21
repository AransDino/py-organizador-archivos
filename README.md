
# Organizador de Archivos por Extensión

Este script de Python organiza archivos en carpetas basadas en su extensión, facilitando la organización y clasificación de archivos en el sistema. Además, permite revertir los cambios realizados utilizando un registro de los archivos antes de ser movidos.

## Características

- Clasifica archivos en carpetas basadas en sus extensiones, con soporte para subcategorías específicas.
- Registro automático de ubicaciones originales para permitir la reversión.
- Interfaz gráfica de usuario (GUI) sencilla creada con `Tkinter`.
- Soporte para múltiples tipos de archivos: documentos, imágenes, vídeos, audios, programas, archivos 3D, y más.

## Instalación

1. Clona el repositorio o descarga el archivo.
   ```bash
   git clone https://github.com/AransDino/py-organizador-archivos.git
   cd organizador-archivos
   ```
2. Asegúrate de tener Python 3 instalado en tu sistema.
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencias

El script utiliza las siguientes bibliotecas estándar de Python:

- `os` (gestión de archivos y directorios).
- `shutil` (operaciones de movimiento y copia de archivos).
- `json` (manejo de registros en formato JSON).
- `tkinter` (creación de la interfaz gráfica de usuario).

No es necesario instalar dependencias adicionales, ya que estas están incluidas en Python por defecto.

## Uso

1. Ejecuta el script:
   ```bash
   organizer.py
   ```
2. Se abrirá una ventana GUI con las siguientes opciones:
   - **Organizar Archivos por Extensión:** Selecciona una carpeta y organiza los archivos dentro de subcarpetas.
   - **Revertir:** Si ya organizaste los archivos, esta opción los devolverá a su ubicación original.

### Categorías Soportadas

- **Configuraciones y Backups:** `.ini`, `.conf`, `.cfg`, `.bak`, `.log`, etc.
- **Documentos:** `.pdf`, `.docx`, `.xlsx`, `.pptx`, etc.
  - Subcategorías: `PDFs`, `Word`, `Hojas de Cálculo`, `Macros`, `Presentaciones`, `Textos`.
- **Imágenes:** `.jpg`, `.png`, `.tiff`, etc.
- **Vídeos:** `.mp4`, `.avi`, `.mkv`, etc.
- **Audios:** `.mp3`, `.wav`, `.flac`, etc.
- **Archivos 3D:** `.stl`, `.obj`, `.fcstd` (subcategoría: `Modelos Propios`), etc.
- **Diseño y Gráficos:** `.psd`, `.ai`, `.svg`, etc.
- **Comprimidos:** `.zip`, `.rar`, `.7z`, etc.
- **Códigos y Scripts:** `.py`, `.js`, `.html`, `.css`, etc.

### Reversión

El proceso de organización genera un archivo `revert.json` en la carpeta destino, que contiene un registro de las ubicaciones originales y nuevas de los archivos. Esto permite revertir el proceso en cualquier momento.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto, crea un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

