#Rich es una biblioteca de Python para escribir texto enriquecido (con color y estilo) en la terminal, y para mostrar contenido avanzado como tablas, Markdown y código con resaltado de sintaxis.

import time  # 1. Importamos la librería encargada del tiempo
from rich.progress import track
from rich import pretty

#from time import time
# o import time  # 1. Importamos la librería encargada del tiempo  

# ----------------------------------------------------------------
from rich import print
from rich.console import Console


# Creamos una instancia de la consola
console = Console()

# Usamos la consola para imprimir con estilo
console.print("Hola, esto es [bold magenta]Rich[/bold magenta] en acción!")

console.print("Puedes imprimir [italic cyan]colores[/italic cyan] y [underline green]estilos[/underline green] fácilmente.") # underline para barra debajo del texto

print("[italic red]Hello[/italic red] World!") #italic- tipo de fuente-letra
console.log("Hello, World!")

# Crear una barra de progreso
for i in track(range(20), description="PROGRESO ..."):
    #PARA QUE VAYA SG * SG
    time.sleep(1) 
    #la funcion (sleep) sirve para pausar el codigo y ver como avanza la barra- pertenece a un modulo estandar de python - (time)

console.print("[bold yellow] Esto deberà ser amarillo y letra en negrita ☀️ [/bold yellow] ahora con estilos 😼" , style= "green")
#[] \n

console.print("[bold yellow] Esto deberà ser amarillo y letra en negrita ☀️ [/bold yellow] ahora con estilos 😼" , style= "green") #bold paraa negrilla

# ----------------------------------------------------------------
print("="*75)
print("Iniciando el sistema...\n")

# 2. Envolvemos nuestro rango con track() de rich
for paso in track(range(100), description="Cargando pacientes..."):
    
    # 3. Pausamos el código 0.05 segundos en cada iteración para simular trabajo
    time.sleep(0.05) 

console.print("\n [bold green]¡Carga completada con éxito! [/bold green]")



pretty.install()
["Rich and pretty", True]

