"""Implementation of the game of life"""

import numpy as np
import matplotlib.pyplot as plt
import gameoflifelib as gol
GRID_SIZE = 25
N_ITER = 10
cellsgrid = np.zeros([GRID_SIZE, GRID_SIZE])
nextcellsgrid = np.zeros([GRID_SIZE, GRID_SIZE])

# Introduce cells
cellsgrid[14,15] = 1
cellsgrid[15,15] = 1
cellsgrid[15,15] = 1
cellsgrid[15,16] = 1
cellsgrid[15,17] = 1


plt.imshow(cellsgrid)
plt.show()
for i in range(N_ITER):
    neigmat = gol.get_neig_mat(cellsgrid)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if(cellsgrid[row,col]==1 and neigmat[row,col]<2):
                nextcellsgrid[row,col]=0
            elif(cellsgrid[row,col]==1):
                nextcellsgrid[row,col]=1
            elif(cellsgrid[row,col]==0 and neigmat[row,col]>=3):
                nextcellsgrid[row,col]=1
    cellsgrid=nextcellsgrid
    plt.imshow(cellsgrid)
    plt.show()





# plt.figure(1)
# plt.subplot(121)
# plt.imshow(neigmat)
# plt.subplot(122)
# plt.imshow(cellsgrid)
# plt.show()




