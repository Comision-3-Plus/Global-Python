from clases import Detector, Radiacion, Virus, Sanador

def main():
    matriz=[]
    print("Ingrese la matriz de 6x6")
    for i in range(6):
        while True:
            Adn = input().upper()
        
            if len(Adn) == 6 and all(letra in {'A', 'G', 'T', 'C'} for letra in Adn):
                matriz.append(Adn)
                break
            else:
                print("Error: La cadena debe tener exactamente 6 letras y solo letras A, G, T o C.")
            

    detector = Detector()
    sanador = Sanador()
    
    print("ADN original:")
    for fila in matriz:
        print(fila)

    opcion=0
    while opcion!=4: 
        opcion = int(input("¿Qué deseas hacer? (1: Detectar mutantes, 2: Mutar, 3: Sanar 4: Salir): "))
        if opcion == 1:
            if detector.detectar_mutantes(matriz):
                print(True)
            else:
                print(False)
        elif opcion == 2:
            tipo_mutacion = input("¿Deseas mutar con radiación (H/V) o virus (D)? ").upper()
            
            adn = ""
            while adn not in ["A", "G", "T", "C"]:
                try:
                    adn = input("Qué ADN deseas cambiar (A, G, T, C): ").upper()
                except ValueError:
                    print("Entrada inválida, por favor ingresa A, G, T, o C.")

            
            if tipo_mutacion == 'H' or tipo_mutacion == 'V':
                radiacion = Radiacion(adn)
                nueva_matriz = radiacion.crear_mutante(matriz, (1, 0), tipo_mutacion)
            else:
                virus = Virus(adn)
                nueva_matriz = virus.crear_mutante(matriz, (0, 0))

            print("ADN mutado:")
            for fila in nueva_matriz:
                print(fila)
            matriz=nueva_matriz
        elif opcion == 3:
            nueva_matriz = sanador.sanar_mutantes(matriz, detector)
            print("ADN sanado:")
            for fila in nueva_matriz:
                print(fila)
        elif opcion==4:
            print("Salio del programa con exito")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
