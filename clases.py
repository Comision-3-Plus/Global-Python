class Detector:
    def __init__(self):
        self.matriz = []

    def detectar_mutantes(self, matriz):
        self.matriz = matriz
        if self._detectar_horizontal() or self._detectar_vertical() or self._detectar_diagonal():
            return True
        return False
    
    def _detectar_horizontal(self):
        for fila in self.matriz:
            if self._repeticion(fila):
                return True
        return False
    
    def _detectar_vertical(self):
        for columna in range(len(self.matriz[0])):
            secuencia = ''.join([self.matriz[fila][columna] for fila in range(len(self.matriz))])
            if self._repeticion(secuencia):
                return True
            return False
        
    def _detectar_diagonal(self):
        n = len(self.matriz)
        for i in range(n-3):
            for j in range(n-3):
                diagonal_principal = ''.join([self.matriz[i+k][j+k] for k in range(4)])
                diagonal_secundaria = ''.join([self.matriz[i+k][j+3-k] for k in range(4)])
                if self._repeticion(diagonal_principal) or self._repeticion(diagonal_secundaria):
                    return True
        return False
    
    def _repeticion(self, secuencia):
        for i in range(len(secuencia) - 3):
            if secuencia[i:i+4] == secuencia[i] * 4:
                return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)

    def crear_mutante(self, matriz, posicion_inicial, orientacion_de_la_mutacion):
        try:
            if orientacion_de_la_mutacion == 'H':
                fila, columna = posicion_inicial
                matriz[fila] = matriz[fila][:columna] + self.base_nitrogenada * 4 + matriz[fila][columna+4:]
            elif orientacion_de_la_mutacion == 'V':
                fila, columna = posicion_inicial
                for i in range(4):
                    matriz[fila+i] = matriz[fila+i][:columna]
            return matriz
        except Exception as e:
            print(f"Error creando mutante: {e}")
            return None
        
class Virus(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)

    def crear_mutante(self, matriz, posicion_inicial):
        try: 
            fila, columna = posicion_inicial
            for i in range(4):
                matriz[fila+i] = matriz[fila+i][:columna+i] + self.base_nitrogenada + matriz[fila+i][columna+i+1:]
            return matriz
        except Exception as e:
            print(f"Error creando mutante: {e}")
            return None

class Sanador:
    def __init__(self):
        pass

    def sanar_mutantes(self, matriz, detector):
        if detector.detectar_mutantes(matriz):
            return self._generar_adn_no_mutante(len(matriz))
        return matriz
    
    def _generar_adn_no_mutante(self, n):
        import random
        bases = ['A', 'T', 'C', 'G']
        nueva_matriz = [''.join(random.choice(bases) for _ in range(n)) for _ in range(n)]
        return nueva_matriz