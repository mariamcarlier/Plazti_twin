import sys
from rich import print
#from rich.console import Console
# ------------------------------------------------------------
from typing import List
from rich.console import Console, OverflowMethod

from datetime import datetime

print({'nombre': 'Calculadora', 'version': 1.0, 'activa': True})


# Istancia global 
console= Console()
console.print("FOO", style="white on blue")
console.print("rooockkk!!!", style="black on red") #TIPO SUBRAYADO


#normas : método dibujará una línea horizontal con un título opcional, lo cual es una buena manera de dividir la salida de la terminal en secciones.
console.rule("[bold purple]Chapter 2")

# Justificar / Alineación
style = "bold white on blue"
console.print("Rich", style=style)
console.print("Rich", style=style, justify="left")
console.print("Rich", style=style, justify="center")
console.print("Rich", style=style, justify="right")

# La justificación a la izquierda rellenará el texto a la derecha con espacios, mientras que la justificación predeterminada no lo hará. Solo notará la diferencia si establece un color de fondo con el styleargumento.

console.status("Monkeying around...", spinner="monkey")

# ------------------------------------------------------------
#OVERFLOW - DESBORDAMIENTO
# Puedes especificar cómo Rich debe gestionar el desbordamiento con el overflowargumento

#from typing import List
#from rich.console import Console, OverflowMethod

console = Console(width=14)
supercali = "supercalifragilisticexpialidocious"

overflow_methods: List[OverflowMethod] = ["fold", "crop", "ellipsis"]
for overflow in overflow_methods:
    console.rule(overflow)
    console.print(supercali, overflow=overflow, style="bold blue")
    console.print()

    #La opción predeterminada es “fold”, que colocará los caracteres sobrantes en la siguiente línea, creando tantas líneas nuevas como sean necesarias para que quepa el texto.
    #El método "crop" trunca el texto al final de la línea, descartando cualquier carácter que pudiera desbordarse.
    #El método “elipsis” es similar a “crop”, pero insertará un carácter de puntos suspensivos (“…”) al final de cualquier texto que haya sido truncado.

#También puede configurar overflow en “ignore”, lo que permite que el texto continúe en la siguiente línea. En la práctica, esto se verá igual que “crop” a menos que también lo configure crop=Falseal llamar a print().

# ------------------------------------------------------------
#CONSOLE STYLE
blue_console = Console(style="white on blue")
blue_console.print("I'm blue. Da ba dee da ba di.")


# ------------------------------------------------------------
# Exportador
console = Console(record=True)
"""Después de escribir el contenido, puede llamar a export_text()o export_svg()para export_html()obtener la salida de la consola como una cadena. También puede llamar a save_text(), save_svg()o save_html()para escribir el contenido directamente en el disco."""

# ------------------------------------------------------------
#consola de errores

#También puedes configurar el styleparámetro en la consola para que los mensajes de error sean visualmente distintos. Aquí te mostramos cómo hacerlo:

error_console = Console(stderr=True, style="bold red")

# ------------------------------------------------------------
#salida del archivo - FILE

#debe ser un objeto similar a un archivo abierto para escribir texto. Podrías usar esto para escribir en un archivo sin que la salida aparezca en la terminal

#import sys
#from rich.console import Console
#from datetime import datetime


#paging
"""Si necesita presentar un texto extenso al usuario, puede usar un paginador para mostrarlo. Un paginador suele ser una aplicación del sistema operativo que, como mínimo, permite desplazarse pulsando una tecla, y que a menudo también permite desplazarse verticalmente por el texto y otras funciones."""

#from rich.__main__ import make_test_card
#from rich.console import Console

#console = Console()
#with console.pager():
#    console.print(make_test_card())

#pantalla alternativa
"""mostrará un diccionario con formato legible en la pantalla alternativa antes de volver al indicador de comandos después de 5 segundos."""

from time import sleep
from rich.console import Console

console = Console()
with console.screen():
    console.print(locals())
    sleep(5)

#un renderizable screen()que se mostrará en la pantalla alternativa cuando llame a update().
#from time import sleep

#from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console = Console()

with console.screen(style="bold white on red") as screen:
    for count in range(5, 0, -1):
        text = Align.center(
            Text.from_markup(f"[blink]Don't Panic![/blink]\n{count}", justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text))
        sleep(1)