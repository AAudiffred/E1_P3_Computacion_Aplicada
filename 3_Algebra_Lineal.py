import numpy as np


# Solución por Regla de Cramer
def determinante(matriz):
    det = matriz[0][0]*matriz[1][1]*matriz[2][2] + \
          matriz[0][1]*matriz[1][2]*matriz[2][0] + \
          matriz[0][2]*matriz[1][0]*matriz[2][1] - \
          matriz[0][2]*matriz[1][1]*matriz[2][0] - \
          matriz[0][0]*matriz[1][2]*matriz[2][1] - \
          matriz[0][1]*matriz[1][0]*matriz[2][2]
    return det


def solve_system(matriz, resultados):
    det_A = determinante(matriz)
    det_X = determinante([[resultados[0], matriz[0][1], matriz[0][2]],
                        [resultados[1], matriz[1][1], matriz[1][2]],
                        [resultados[2], matriz[2][1], matriz[2][2]]])
    det_Y = determinante([[matriz[0][0], resultados[0], matriz[0][2]],
                        [matriz[1][0], resultados[1], matriz[1][2]],
                        [matriz[2][0], resultados[2], matriz[2][2]]])
    det_Z = determinante([[matriz[0][0], matriz[0][1], resultados[0]],
                        [matriz[1][0], matriz[1][1], resultados[1]],
                        [matriz[2][0], matriz[2][1], resultados[2]]])
    x = det_X/det_A
    y = det_Y/det_A
    z = det_Z/det_A
    return x, y, z


matriz = [[0.25, 0.15, 0],
          [0.45, 0.50, 0.75],
          [0.30, 0.35, 0.25]]
resultados = [1.5, 5, 3]

x1, y1, z1 = solve_system(matriz, resultados)
print("Solución por Regla de Cramer")
print("x1 =", x1)
print("y1 =", y1)
print("z1 =", z1)



# Solución con Numpy
A = np.array([[0.25, 0.15, 0],
              [0.45, 0.50, 0.75],
              [0.30, 0.35, 0.25]])
b = np.array([1.5, 5, 3])

x2 = np.linalg.solve(A, b)

print("Solución con Numpy")
print("x2 =", x2[0])
print("y2 =", x2[1])
print("z2 =", x2[2])
