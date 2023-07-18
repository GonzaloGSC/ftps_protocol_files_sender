import subprocess
import platform
import os

# Obtener la ruta absoluta del directorio del script actual
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas relativas al directorio del script
ruta_al_entorno = os.path.join(ruta_script, ".env") # Reemplazar con la ruta correcta
ruta_al_script = os.path.join(ruta_script, "script.py") # Reemplazar con la ruta correcta

# Ruta al intérprete de Python
ruta_python = ruta_al_entorno + r"\Scripts\python.exe" # Reemplazar con la ruta correcta

# Comando para activar el entorno virtual y ejecutar el archivo script.py con la versión de Python específica
comando_activar_entorno = ""
sistema_operativo = platform.system()

if sistema_operativo == "Windows":
    comando_activar_entorno = '{}\\Scripts\\activate.bat && {} "{}"'.format(ruta_al_entorno, ruta_python, ruta_al_script)
elif sistema_operativo == "Linux":
    comando_activar_entorno = 'source "{}/bin/activate" && {} "{}"'.format(ruta_al_entorno, ruta_python, ruta_al_script)
# print("comando_activar_entorno:", comando_activar_entorno)
# Abrir una nueva consola y ejecutar el comando en el entorno virtual
subprocess.call(comando_activar_entorno, shell=True)
