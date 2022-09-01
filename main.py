import math


def dividirVencer(B,i,j):
    if i == j:
        print("A"+str(i+1),end=" ")
    else:
        print("(", end=" ")
        q = B[i][j]
        dividirVencer(B,i,q)
        dividirVencer(B,q+1,j)
        print(")", end=" ")
    
def multiplicacionMatrices(D):
    tamano = len(D) - 1
    T = [[0 for x in range(tamano)] for y in range(tamano)]
    B = [[-1 for x in range(tamano)] for y in range(tamano)]

    for i in range(tamano-2, -1, -1):
        for j in range(i+1, tamano):
            q = math.inf
            m = 0
            for k in range(i, j):
                izq = T[i][k]
                der = T[k+1][j]
                v = izq + der + (D[i-1]*D[k]*D[j])
                if v < q:
                    q = v
                    m = k
            T[i][j] = q
            B[i][j] = m
    
    return T, B


#D = [ 10 , 100 , 5 , 50] 
#D = [ 10 , 52354 , 560 , 100, 2335, 123] 
D = [ 10 , 5 , 6, 7, 2, 5, 3, 4] 
T, B = multiplicacionMatrices(D)
min= T[0 ][ len(D)-2 ]

print("minimizacion de operaciones:", min)
dividirVencer(B,0,len(B)-1)
