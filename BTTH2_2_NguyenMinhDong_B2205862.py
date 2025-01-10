import numpy as np

def createArray():
    arr = np.empty((1, 12))
    for i in range(0, 12):
        np.append(arr, [5 * i])

    return arr

array = createArray()
print(array)

# matrix = createMatrixFromArray(array)
# printMatrix(matrix)
