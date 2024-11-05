# PROYECTO-LENGUAJES
 Analizador de Cadenas y Máquina de Turing

Este proyecto implementa un analizador de cadenas que combina múltiples funcionalidades de validación y visualización, incluyendo una Máquina de Turing de dos cintas.

 Funcionalidades Principales

 1. Validación de Cadenas
    - Utiliza expresiones regulares para validar el formato de las cadenas de entrada
    - Genera una tabla de transiciones que muestra el proceso de validación
    - Mantiene una pila de errores para símbolos no válidos

 2. Visualización de Autómata
    - Genera árboles de derivación visuales para cada cadena procesada
    - Los estados finales se colorean en verde (aceptación) o rojo (rechazo)
    - Utiliza Graphviz para crear representaciones gráficas claras

 3. Máquina de Turing de Dos Cintas
    - Procesa la entrada utilizando dos cintas separadas:
    - Primera cinta: lee símbolos en posiciones impares
    - Segunda cinta: lee símbolos en posiciones pares
    - Implementa lectura bidireccional (izquierda a derecha y viceversa)
    - Genera dos tablas de transición:
    - Una para movimientos hacia la derecha
    - Otra para movimientos hacia la izquierda
    - Muestra el estado de las cintas y la posición de los cabezales en cada paso

 Uso del Programa

1. Coloque las cadenas a analizar en el archivo `cadena.txt`
2. Ejecute el script principal
3. El programa generará:
   - Validación de cada cadena
   - Tablas de transición
   - Árboles de derivación
   - Visualización del proceso de la Máquina de Turing

 Requisitos
    - Python 3.x
    - Biblioteca Graphviz
    - Biblioteca re (incluida en Python)

