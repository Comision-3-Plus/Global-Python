from clases import Detector, Radiacion, Virus, Sanador
def main():
    matriz = [
        "AGATCA",
        "GATTCA",
        "CAACAT",
        "GAGCTA",
        "ATTGCG",
        "CTGTTC"
    ]
    detector = Detector()
    radiacion = Radiacion("T")
    virus = Virus("T")
    sanador = Sanador()

    print("ADN original:")
    for fila in matriz:
        print(fila)

    opcion = input("¿Qué deseas hacer? (1: Detectar mutantes, 2: Mutar, 3: Sanar): ")
    if opcion == '1':
        if detector.detectar_mutantes(matriz):
            print("Se detectó un mutante en el ADN.")
        else:
            print("No se detectaron mutantes.")
    elif opcion == '2':
        tipo_mutacion = input("¿Deseas mutar con radiación (H/V) o virus (D)? ")
        if tipo_mutacion == 'H' or tipo_mutacion == 'V':
            nueva_matriz = radiacion.crear_mutante(matriz, (1, 0), tipo_mutacion)
        else:
            nueva_matriz = virus.crear_mutante(matriz, (0, 0))
        print("ADN mutado:")
        for fila in nueva_matriz:
            print(fila)
    elif opcion == '3':
        nueva_matriz = sanador.sanar_mutantes(matriz, detector)
        print("ADN sanado:")
        for fila in nueva_matriz:
            print(fila)
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()