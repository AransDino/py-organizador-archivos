import os
import shutil
import json

def organizar_archivos_por_extension(carpeta_origen):
    """
    Organiza los archivos de la carpeta especificada en subcarpetas según sus extensiones.
    Dentro de Documentos y Archivos 3D, se crean subcarpetas adicionales según el tipo.
    """
    carpeta_destino = os.path.join(carpeta_origen, "Organizados")
    os.makedirs(carpeta_destino, exist_ok=True)

    registro_rutas = {}
    registro_archivo = os.path.join(carpeta_destino, "revert.json")

    categorias = {
        "Configuraciones y backups": [".ini", ".conf", ".cfg", ".bak", ".backup", ".log", ".temp", ".tmp", ".swp"],
        "Backups": [".bak", ".backup", ".customization"],
        "Calendarios": [".ics", ".ical"],
        "Contactos": [".vcf"],
        "Documentos": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".csv", ".odt", ".ods", ".odp", ".xlsm", ".rtf"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".ico", ".avif", ".cr3", ".webp"],
        "Vídeos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v", ".camrec", ".rm", ".vob"],
        "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".amr", ".opus"],
        "Comprimidos": [".rar", ".zip", ".7z", ".tar", ".gz", ".bz2", ".xz", ".dmg", ".iso"],
        "Programas": [".exe", ".msi", ".apk", ".bat"],
        "Archivos 3D": [".stl", ".obj", ".fbx", ".gltf", ".glb", ".3ds", ".blend", ".ply", ".3mf", ".dae", ".x3d", ".step", ".fcstd", ".fcbak"],
        "Diseño y Gráficos": [".psd", ".ai", ".eps", ".indd", ".xd", ".fig", ".sketch", ".cdr", ".svg"],
        "Torrents": [".torrent"],
        "CNC": [".lbrn2", ".nc", ".cnc"],
        "Códigos y Scripts": [".dart", ".ps1", ".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".rb", ".swift", ".go", ".ts", ".sh", ".json", ".xml", ".sql", ".yaml", ".md", ".ino"],
        "KLM y Rutas": [".kml", ".kmz", ".gpx"],
        "Certificados": [".cer", ".crt", ".der", ".pem", ".pfx", ".p12"],
        "Otros": [".log", ".tmp", ".bak", ".dat", ".bin", ".cfg"]
    }

    subcategorias_documentos = {
        "PDFs": [".pdf"],
        "Word": [".docx", ".doc", ".odt"],
        "Hojas de Cálculo": [".xlsx", ".xls", ".csv", ".ods"],
        "Macros": [".xlsm"],
        "Presentaciones": [".pptx", ".ppt", ".odp"],
        "Textos": [".txt", ".rtf"]
    }

    conteo_categorias = {categoria: 0 for categoria in categorias.keys()}
    total_archivos = 0

    for root, _, files in os.walk(carpeta_origen):
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            archivo_origen = os.path.join(root, file)

            categoria = "Otros"
            for key, extensiones in categorias.items():
                if extension in extensiones:
                    categoria = key
                    break

            carpeta_categoria = os.path.join(carpeta_destino, categoria)
            os.makedirs(carpeta_categoria, exist_ok=True)

            if categoria == "Documentos":
                subcategoria = "Otros Documentos"
                for key, extensiones in subcategorias_documentos.items():
                    if extension in extensiones:
                        subcategoria = key
                        break

                carpeta_subcategoria = os.path.join(carpeta_categoria, subcategoria)
                os.makedirs(carpeta_subcategoria, exist_ok=True)
                archivo_destino = os.path.join(carpeta_subcategoria, file)
            elif categoria == "Archivos 3D" and extension == ".fcstd":
                carpeta_modelos_propios = os.path.join(carpeta_categoria, "Modelos Propios")
                os.makedirs(carpeta_modelos_propios, exist_ok=True)
                archivo_destino = os.path.join(carpeta_modelos_propios, file)
            else:
                archivo_destino = os.path.join(carpeta_categoria, file)

            try:
                shutil.move(archivo_origen, archivo_destino)
                registro_rutas[archivo_origen] = archivo_destino
                conteo_categorias[categoria] += 1
                total_archivos += 1
                print(f"Movido: {archivo_origen} -> {archivo_destino}")
            except Exception as e:
                print(f"Error al mover {archivo_origen}: {e}")

    with open(registro_archivo, "w") as f:
        json.dump(registro_rutas, f, indent=4)

    resumen = [f"Total de archivos organizados: {total_archivos}"]

    for categoria, cantidad in conteo_categorias.items():
        resumen.append(f"{categoria}: {cantidad} archivo(s)")

    return "\n".join(resumen)

def revertir_organizacion():
    """
    Revierte la organización de los archivos moviéndolos de vuelta a su ubicación original.
    """
    carpeta_destino = None

    while not carpeta_destino:
        carpeta_destino = input("Introduce la ruta de la carpeta donde se creó la carpeta 'Organizados': ").strip()
        carpeta_destino = os.path.join(carpeta_destino, "Organizados")
        registro_archivo = os.path.join(carpeta_destino, "revert.json")

        if not os.path.exists(registro_archivo):
            print("No se encontró un registro de organización para revertir en la carpeta especificada.")
            carpeta_destino = None

    with open(registro_archivo, "r") as f:
        registro_rutas = json.load(f)

    for archivo_origen, archivo_destino in registro_rutas.items():
        try:
            os.makedirs(os.path.dirname(archivo_origen), exist_ok=True)
            shutil.move(archivo_destino, archivo_origen)
            print(f"Revertido: {archivo_destino} -> {archivo_origen}")
        except Exception as e:
            print(f"Error al revertir {archivo_destino}: {e}")

    os.remove(registro_archivo)
    print("\nOrganización revertida correctamente.")

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Organizar archivos")
        print("2. Revertir organización")
        print("3. Salir")
        opcion = input("Opción (1/2/3): ").strip()

        if opcion == "1":
            carpeta_origen = input("Introduce la ruta de la carpeta que deseas organizar: ").strip()
            if not os.path.isdir(carpeta_origen):
                print("Error: La ruta especificada no es válida o no es una carpeta.")
                continue
            resumen = organizar_archivos_por_extension(carpeta_origen)
            print(f"\n{resumen}")
        elif opcion == "2":
            revertir_organizacion()
        elif opcion == "3":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
