class Detector:
    def __init__(self,matriz):
        self.matriz = matriz
        for i in range(36):
            print(matriz[i],end=" ")
            if i==5 or i==11 or i==17 or i==23 or i==29 or i==35:
              print(" ")
        
      
    
    def printearMatriz(self):
        print(self.matriz)
        
    def obtener_mutaciones(self):
       self.vertical()
       self.horizontal()
        
        
    def horizontal(self):
      for j in range(0, len(self.matriz), 6):
        a = t = c = g = 0     
        for i in range(6):
            if self.matriz[i]=="A":
                a=a+1
            elif self.matriz[i]=="T":
                t=t+1
            elif self.matriz[i]=="C":
                c=c+1
            elif self.matriz[i]=="G":
                g=g+1      
        if max(a, t, c, g) >= 4:
                print(f"Hay una mutación en la fila {j // 6 + 1}")
        else:
                print(f"No hay mutación en la fila {j // 6 + 1}")
        
    def vertical(self):
        for j in range(6):
         a = t = c = g = 0     
        for i in range(j,36,6):
            if self.matriz[i]=="A":
                a=a+1
            elif self.matriz[i]=="T":
                t=t+1
            elif self.matriz[i]=="C":
                c=c+1
            elif self.matriz[i]=="G":
                g=g+1      
        if max(a, t, c, g) >= 4:
                print(f"Hay una mutación en la columna {j + 1}")
        else:
                print(f"No hay mutación en la columna {j + 1}")   
           
            
entrada = input("Ingrese la matriz de 6x6 de Adenina (A), Timina (T), Citosina (C) y Guanina (G).\n ")
matriz = Detector(list(entrada))
matriz.obtener_mutaciones()
