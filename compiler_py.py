import time
import subprocess
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


code_line1 = "python"
code_line2 = "C:/Users/heber/Documents/gestor-archivos-latex"
# code_line3 = str("\capitulo[2]{HEBER} C:\Users\heber\Documents\LaTeX\fisica\preba")
# \cargarPractica{FIS100-2019II-CussiTitoEddy-practica1} C:\Users\heber\Documents\LaTeX\fisica\prueba
code_line3 = input(str("code line 3: "))


# run a script every time a directory change is detected
def run_script(script_name):
    subprocess.call(script_name, shell=True)

def on_modified(event):
    print("Archivo modificado: " + event.src_path +"\n")
    print("Copilando: " + event.src_path +"\n")
    # subprocess.call(code_line1+" "+event.src_path+" "+code_line3, shell=True)
    subprocess.call(code_line1+" "+event.src_path+" create "+code_line3, shell=True)

event_handler = FileSystemEventHandler()
path = Path(code_line2)
event_handler.on_modified = on_modified

observer = Observer()
observer.schedule(event_handler, path, recursive=False)
observer.start()

try:
    print("Monitoreo inicializado")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

















