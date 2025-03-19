import os
import shutil
import datetime

def backup(source_dir, backup_dir):
    # Crear un nombre de directorio de respaldo con la fecha actual
    date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_subdir = os.path.join(backup_dir, f"backup_{date_str}")

    # Crear el directorio de respaldo
    os.makedirs(backup_subdir, exist_ok=True)

    # Copiar todos los archivos y subdirectorios del directorio fuente al directorio de respaldo
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        backup_item = os.path.join(backup_subdir, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, backup_item)
        else:
            shutil.copy2(source_item, backup_item)

    print(f"Backup completado: {backup_subdir}")

if __name__ == "__main__":
    source_directory = "/ruta/al/directorio/origen"
    backup_directory = "/ruta/al/directorio/respaldo"
    backup(source_directory, backup_directory)