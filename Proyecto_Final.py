import re
from graphviz import Digraph

class TuringMachine:
    def __init__(self):
        self.tape1 = []  # Cinta para símbolos en posiciones impares
        self.tape2 = []  # Cinta para símbolos en posiciones pares
        self.head1 = 0   # Cabezal para tape1
        self.head2 = 0   # Cabezal para tape2
        self.state = 'q0'
        self.direction = 'right'  # Dirección inicial
        
    def initialize_tapes(self, input_string):
        # Inicializar las cintas con símbolos en posiciones pares e impares
        self.tape1 = ['B'] + [input_string[i] for i in range(0, len(input_string), 2)] + ['B']
        self.tape2 = ['B'] + [input_string[i] for i in range(1, len(input_string), 2)] + ['B']
        self.head1 = 1
        self.head2 = 1
        
    def move_heads(self, direction):
        if direction == 'right':
            self.head1 += 1
            self.head2 += 1
        else:
            self.head1 -= 1
            self.head2 -= 1
            
    def get_transition(self, current_state, symbol1, symbol2):
        # Tabla de transiciones para la máquina de Turing
        transitions = {
            'q0': {
                ('a', 'B'): ('q1', ('X', 'B'), 'right'),
                ('B', 'b'): ('q2', ('B', 'Y'), 'right'),
            },
            'q1': {
                ('a', 'B'): ('q1', ('X', 'B'), 'right'),
                ('B', 'b'): ('q2', ('B', 'Y'), 'right'),
                ('B', 'B'): ('q3', ('B', 'B'), 'left'),
            },
            'q2': {
                ('a', 'B'): ('q1', ('X', 'B'), 'right'),
                ('B', 'b'): ('q2', ('B', 'Y'), 'right'),
                ('B', 'B'): ('q3', ('B', 'B'), 'left'),
            },
            'q3': {
                ('X', 'Y'): ('q3', ('X', 'Y'), 'left'),
                ('B', 'B'): ('q4', ('B', 'B'), 'right'),
            },
            'q4': {
                ('X', 'Y'): ('q4', ('a', 'b'), 'right'),
                ('B', 'B'): ('qf', ('B', 'B'), 'right'),
            }
        }
        return transitions.get(current_state, {}).get((symbol1, symbol2), None)

    def run(self, input_string):
        self.initialize_tapes(input_string)
        steps = []
        
        while self.state != 'qf':
            current_config = {
                'state': self.state,
                'tape1': self.tape1.copy(),
                'tape2': self.tape2.copy(),
                'head1': self.head1,
                'head2': self.head2,
                'direction': self.direction
            }
            steps.append(current_config)
            
            symbol1 = self.tape1[self.head1]
            symbol2 = self.tape2[self.head2]
            
            transition = self.get_transition(self.state, symbol1, symbol2)
            
            if transition is None:
                print(f"No hay transición definida para el estado {self.state} con símbolos {symbol1}, {symbol2}")
                return steps
                
            new_state, (new_symbol1, new_symbol2), direction = transition
            
            self.tape1[self.head1] = new_symbol1
            self.tape2[self.head2] = new_symbol2
            self.state = new_state
            self.direction = direction
            self.move_heads(direction)
            
        return steps

def generate_transition_tables():
    dot = Digraph(comment='Tablas de Transición')
    dot.attr(rankdir='LR')
    
    # Tabla 1 - Movimientos hacia la derecha
    with dot.subgraph(name='cluster_0') as c:
        c.attr(label='Tabla de Transición - Dirección Derecha')
        estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'qf']
        for estado in estados:
            c.node(estado + '_r', estado)
        
        c.edge('q0_r', 'q1_r', 'a,B/X,B')
        c.edge('q1_r', 'q2_r', 'B,b/B,Y')
        c.edge('q2_r', 'q1_r', 'a,B/X,B')
        c.edge('q3_r', 'q4_r', 'B,B/B,B')
        c.edge('q4_r', 'qf_r', 'B,B/B,B')
    
    # Tabla 2 - Movimientos hacia la izquierda
    with dot.subgraph(name='cluster_1') as c:
        c.attr(label='Tabla de Transición - Dirección Izquierda')
        for estado in estados:
            c.node(estado + '_l', estado)
        
        c.edge('q1_l', 'q3_l', 'B,B/B,B')
        c.edge('q2_l', 'q3_l', 'B,B/B,B')
        c.edge('q3_l', 'q3_l', 'X,Y/X,Y')
    
    dot.render('tablas_transicion', format='png', cleanup=True)

def print_tapes(tape1, tape2, head1, head2):
    print("\nCinta 1 (símbolos impares):", end=" ")
    for i, symbol in enumerate(tape1):
        if i == head1:
            print(f"[{symbol}]", end=" ")
        else:
            print(symbol, end=" ")
            
    print("\nCinta 2 (símbolos pares): ", end=" ")
    for i, symbol in enumerate(tape2):
        if i == head2:
            print(f"[{symbol}]", end=" ")
        else:
            print(symbol, end=" ")
    print("\n")

# Funciones originales del código anterior
def generarTabla(mensaje):
    pilaErrores = []
    estado = '0'
    tabla = [['|||'],['|0|'],['|1|'],['|2|'],['|3|'],['|4|']]
    pasarG4 = False
    
    for i in mensaje:
        i = "|" + i + "|"
        if estado == "0":
            tabla[0].append(i)
            if i == "|a|":
                tabla[1].append("|1|")
                estado = '1'
            else:
                tabla[1].append("|0|")
                pilaErrores.append(i)
                
        elif estado == "1":
            tabla[0].append(i)
            if i == "|b|":
                tabla[2].append("|2|")
                estado = '2'
            else:
                tabla[2].append("|1|")
                pilaErrores.append(i)

        elif estado == "2":
            tabla[0].append(i)
            estado = "3"
            tabla[3].append("|3|")

        elif estado == "3":
            tabla[0].append(i)
            if i == "|b|":
                tabla[4].append("|1|")
                estado = "1"
            elif i == "|a|":
                tabla[4].append("|3|")
                estado = "3"
            elif i == "|*|":
                tabla[4].append("|4|")
                estado = "4"

        elif estado == "4":
            tabla[0].append(i)
            if i == "|#|":
                tabla[5].append("|4|")
                estado = "4"
            elif i == "|a|":
                tabla[5].append("|1|")
                estado = "1"
            elif i == "|b|":
                tabla[5].append("|2|")
                estado = "2"
            
        for z in range(len(tabla)):
            if len(tabla[z]) < len(tabla[0]):
                tabla[z].append("|-|")
    
    print('Tabla de transiciones original:')
    for r in tabla:
        print(' '.join(map(str,r)))
    print('\nPila de errores\n')
    for z in pilaErrores:
        print(z)

    return pilaErrores

def obtener_siguiente_estado(estado_actual, caracter):
    tabla_transicion = {
        '0': {'a': '1'},
        '1': {'b': '2'},
        '2': {'a': '3'},
        '3': {'a': '3', 'b': '1', '*': '4'},
        '4': {'a': '3', 'b': '1', '#': '4'}
    }
    
    if estado_actual in tabla_transicion and caracter in tabla_transicion[estado_actual]:
        return tabla_transicion[estado_actual][caracter]
    else:
        return '4'

def generar_arbol_derivacion(cadena, numero):
    dot = Digraph(comment=f'Árbol de Derivación - Cadena {numero}')
    dot.attr(rankdir='TB')

    estado_actual = '0'
    for i, caracter in enumerate(cadena):
        estado_siguiente = obtener_siguiente_estado(estado_actual, caracter)

        if estado_siguiente == estado_actual:
            dot.node(f"{estado_actual}", estado_actual)
            dot.edge(f"{estado_actual}", f"{estado_siguiente}", label=caracter)
        else:
            dot.node(f"{estado_actual}", estado_actual)
            dot.node(f"{estado_siguiente}", estado_siguiente)
            dot.edge(f"{estado_actual}", f"{estado_siguiente}", label=caracter)
        
        estado_actual = estado_siguiente

    if estado_actual == '4' and cadena[-1] == '#':
        dot.node(f"{estado_actual}", estado_actual, color='green', style='filled')
    else:
        dot.node(f"{estado_actual}", estado_actual, color='red', style='filled')

    dot.render(f'arbol_derivacion_cadena_{numero}', format='png', cleanup=True)

def main():
    patron = re.compile("(.*a)(.*b)(a)(b\2|a*\*)(#+|a\2|b\3)")
    print("\nValidación de cadenas:")
    
    # Generar tablas de transición de la máquina de Turing
    generate_transition_tables()
    
    try:
        with open("cadena.txt", 'r') as reader:
            for numero, line in enumerate(reader.readlines(), 1):
                cadena = line.strip()
                print(f"\n{'='*50}")
                print(f"Procesando cadena {numero}: {cadena}")
                print(f"{'='*50}")
                
                # Validación con expresión regular y tabla original
                if re.fullmatch(patron, cadena):
                    print('---Es válido---')
                else:
                    print('---No es válido---')
                
                print('\nGenerando tabla de transiciones original:')
                pila = generarTabla(cadena)
                
                # Generar árbol de derivación
                print('\nGenerando árbol de derivación...')
                generar_arbol_derivacion(cadena, numero)
                
                # Procesar con la máquina de Turing
                print('\nProcesando con Máquina de Turing de 2 cintas:')
                tm = TuringMachine()
                steps = tm.run(cadena)
                
                # Mostrar los pasos de la ejecución de la máquina de Turing
                print("\nPasos de ejecución de la Máquina de Turing:")
                for step in steps:
                    print(f"\nEstado: {step['state']}")
                    print(f"Dirección: {step['direction']}")
                    print_tapes(step['tape1'], step['tape2'], step['head1'], step['head2'])
                
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo 'cadena.txt'.")
    except IOError:
        print("Error: Hubo un problema al leer el archivo 'cadena.txt'.")

if __name__ == "__main__":
    main()