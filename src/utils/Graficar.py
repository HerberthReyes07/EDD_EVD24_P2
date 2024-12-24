import subprocess
import time


class Graficar:
    def graficar(self, path: str, grafico: str):
        try:
            # Escribe el contenido de "grafico" en un archivo
            with open("graficas_edd/aux_grafico.dot", "w", encoding="utf-8") as fichero:
                fichero.write(grafico)
        except Exception as e:
            print(f"Error al escribir el archivo aux_grafico.dot: {e}")
            return

        try:
            # Ejecuta el comando para generar el gráfico
            comando = f"dot -Tsvg -o {path} graficas_edd/aux_grafico.dot"
            result = subprocess.run(comando, shell=True, check=True)

            # Espera 500 ms para dar tiempo a la generación del archivo
            time.sleep(0.5)
            print("Se ha graficado correctamente!")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando dot: {e}")
        except Exception as e:
            print(f"Error al generar la imagen para el archivo aux_grafico.dot: {e}")