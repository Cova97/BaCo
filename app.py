class AutomataFinito:
    def __init__(self):
        self.estados = {'q1', 'q2', 'q3'}
        self.estado_inicial = 'q1'
        self.estado_final = 'q3'
        self.alfabeto = {'0', '1'}
        self.transiciones = {
            'q1': {'0': 'q2', '1': 'q3'},
            'q2': {'0': 'q1', '1': 'q3'},
            'q3': {'0': 'q2', '1': 'q1'}
        }
    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False 
            estado_actual = self.transiciones[estado_actual][simbolo]
        return estado_actual in self.estado_final
def main():
    automata = AutomataFinito()
    cadena = "0000"

    if automata.validar_cadena(cadena):
        print(f"La cadena '{cadena}' es aceptada por el autómata.")
    else:
        print(f"La cadena '{cadena}' no es aceptada por el autómata.")
if __name__ == '__main__':
    main()
