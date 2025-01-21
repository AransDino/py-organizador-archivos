import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def organizar_archivos_por_extension(carpeta_origen, log_text):
    """
    Organiza los archivos de la carpeta especificada en subcarpetas según sus extensiones.
    Dentro de Documentos y Archivos 3D, se crean subcarpetas adicionales según el tipo.
    """
    carpeta_destino = os.path.join(os.path.expanduser("~"), "Downloads", "Organizados")
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
                log_text.insert(tk.END, f"Movido: {archivo_origen} -> {archivo_destino}\n")
                log_text.see(tk.END)
                log_text.update()
            except Exception as e:
                log_text.insert(tk.END, f"Error al mover {archivo_origen}: {e}\n")

    with open(registro_archivo, "w") as f:
        json.dump(registro_rutas, f, indent=4)

    resumen = [f"Total de archivos organizados: {total_archivos}"]

    for categoria, cantidad in conteo_categorias.items():
        resumen.append(f"{categoria}: {cantidad} archivo(s)")

    return "\n".join(resumen)

def revertir_organizacion(log_text):
    """
    Revierte la organización de los archivos moviéndolos de vuelta a su ubicación original.
    """
    carpeta_destino = os.path.join(os.path.expanduser("~"), "Downloads", "Organizados")
    registro_archivo = os.path.join(carpeta_destino, "revert.json")

    if not os.path.exists(registro_archivo):
        log_text.insert(tk.END, "No se encontró un registro de organización para revertir.\n")
        return

    with open(registro_archivo, "r") as f:
        registro_rutas = json.load(f)

    for archivo_origen, archivo_destino in registro_rutas.items():
        try:
            os.makedirs(os.path.dirname(archivo_origen), exist_ok=True)
            shutil.move(archivo_destino, archivo_origen)
            log_text.insert(tk.END, f"Revertido: {archivo_destino} -> {archivo_origen}\n")
            log_text.see(tk.END)
            log_text.update()
        except Exception as e:
            log_text.insert(tk.END, f"Error al revertir {archivo_destino}: {e}\n")

    os.remove(registro_archivo)
    log_text.insert(tk.END, "\nOrganización revertida correctamente.\n")

def ejecutar_organizacion():
    """
    Ejecuta la organización de archivos por extensión.
    """
    carpeta = filedialog.askdirectory(title="Seleccione la carpeta para organizar")
    if not carpeta:
        messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")
        return

    ventana_progreso = tk.Toplevel()
    ventana_progreso.title("Progreso de la Organización")
    ventana_progreso.geometry("800x500")

    log_text = tk.Text(ventana_progreso, wrap=tk.WORD)
    log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_botones = tk.Frame(ventana_progreso)
    frame_botones.pack(pady=10)

    boton_revertir = tk.Button(frame_botones, text="Revertir", bg="red", fg="white", state=tk.DISABLED)
    boton_revertir.grid(row=0, column=0, padx=10)

    boton_salir = tk.Button(frame_botones, text="Salir", bg="green", fg="white", command=ventana_progreso.destroy)
    boton_salir.grid(row=0, column=1, padx=10)

    resumen = organizar_archivos_por_extension(carpeta, log_text)

    def revertir():
        revertir_organizacion(log_text)
        boton_revertir.config(state=tk.DISABLED)

    boton_revertir.config(state=tk.NORMAL, command=revertir)

    log_text.insert(tk.END, f"\nOrganización completada. Resumen:\n{resumen}\n")
    log_text.see(tk.END)

ventana = tk.Tk()
ventana.title("Organizador de Archivos por Extensión")
ventana.geometry("400x200")

label = tk.Label(ventana, text="Organice sus archivos en subcarpetas por extensión", font=("Arial", 12))
label.pack(pady=10)

boton_organizar = tk.Button(ventana, text="Organizar Archivos por Extensión", command=ejecutar_organizacion, font=("Arial", 12))
boton_organizar.pack(pady=20)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, font=("Arial", 12), bg="red", fg="white")
boton_salir.pack(pady=10)

ventana.mainloop()
