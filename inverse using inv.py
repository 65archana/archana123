import matplotlib.pyplot as plt
import numpy as np
matA = np.matrix(np.random.rand(3, 2))
# print the first matrix
print('The first matrix is :\n', matA)

inverseMatA = matA.getI()
print('\nThe inverse of the first matrix is :\n', inverseMatA)
