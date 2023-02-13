""" Module for The Game of Life program"""
import numpy as np

def get_neig_mat(mat):
    """Returns the matrix of neighbours."""
    neigmat = np.zeros(mat.shape)
    xsize, ysize = mat.shape
    for row in range(xsize):
        for col in range(ysize):
            neigmat[row, col] = neig_sum(row, col, mat)
    return neigmat

def neig_sum(row, col, mat):
    """Returns the neighbours of a given cell"""
    summation = 0
    xlen=mat.shape[0]-1
    ylen=mat.shape[1]-1
    if in_bounds(row, col, mat.shape):
        summation = inner_neig_sum(row,col,mat)
    elif(row==0 and col==0):
        summation = left_upper_corner_neig_sum(row,col,mat)
    elif(row==0 and col<ylen):
        summation = upper_bound_neig_sum(row,col,mat)
    elif(row==0 and col==ylen):
        summation = right_upper_corner_neig_sum(row,col,mat)
    elif(row<xlen and col==0):
        summation = left_bound_neig_sum(row,col,mat)
    elif(row!=xlen and col==ylen):
        summation = right_bound_neig_sum(row,col, mat)
    elif(row==xlen and col==0):
        summation = left_lower_corner_neig_sum(row,col,mat)
    elif (row==xlen and col<ylen):
        summation = lower_bound_neig_sum(row,col,mat)
    else:
        summation = right_lower_corner_neig_sum(row,col,mat)
    return summation

def right_lower_corner_neig_sum(row,col,mat):
    """Sums the neighbours of the right lower corner"""
    top = mat[row-1,col]
    topleft = mat[row-1,col-1]
    left = mat[row,col-1]
    return top+topleft+left

def lower_bound_neig_sum(row,col,mat):
    """Sums the neighbours of the lower bound"""
    left = mat[row,col-1]
    topleft = mat[row-1,col-1]
    top = mat[row-1,col]
    topright = mat[row-1,col+1]
    right = mat[row,col+1]
    return top+topright+right+topleft+left

def left_lower_corner_neig_sum(row,col,mat):
    """Sums the neighbours of the left lower corner cell"""
    top = mat[row-1,col]
    topright = mat[row-1,col+1]
    right = mat[row,col+1]
    return top+topright+right

def right_bound_neig_sum(row,col, mat):
    """Sums the neighbours of the right bound cells"""
    top = mat[row-1,col]
    topleft = mat[row-1,col-1]
    left = mat[row,col-1]
    bottomleft = mat[row+1,col-1]
    bottom = mat[row+1,col]
    return left+top+bottom+topleft+bottomleft

def left_bound_neig_sum(row,col,mat):
    """Sums the neighbours of the left bound cells"""
    top = mat[row-1,col]
    topright = mat[row-1,col+1]
    right = mat[row,col+1]
    bottomright = mat[row+1,col+1]
    bottom = mat[row+1,col]
    return right+top+bottom+bottomright+topright

def right_upper_corner_neig_sum(row,col,mat):
    """Sums the neighbours of the right upper corner cell"""
    left = mat[row,col-1]
    bottom = mat[row+1,col]
    bottomleft = mat[row+1,col-1]
    return left+bottom+bottomleft

def upper_bound_neig_sum(row,col,mat):
    """Sums the neighbours of the upper bound cells"""
    right = mat[row,col+1]
    left = mat[row,col-1]
    bottom = mat[row+1,col]
    bottomright = mat[row+1,col+1]
    bottomleft = mat[row+1,col-1]
    return right+left+bottom+bottomright+bottomleft

def inner_neig_sum(row,col,mat):
    """Sums the neighbours of the in bounds cells"""
    left = mat[row,col-1]
    right = mat[row,col+1]
    top = mat[row-1,col]
    bottom = mat[row+1,col]
    topleft = mat[row-1,col-1]
    topright = mat[row-1,col+1]
    bottomleft = mat[row+1,col-1]
    bottomright = mat[row+1,col+1]
    return left+right+top+bottom+topleft+topright+bottomleft+bottomright

def left_upper_corner_neig_sum(row,col,mat):
    """Sums the neighbours of the left upper corner cell"""
    right = mat[row,col+1]
    bottom = mat[row+1,col]
    bottomright = mat[row+1,col+1]
    return right+bottom+bottomright

def in_bounds(row, col, matshape):
    """Checks if the cell is not a border of the grid"""
    xbound = matshape[0]-1
    ybound = matshape[1]-1
    if(row==0 or col==0) or (row==xbound or col==ybound):
        res = False
    else:
        res = True
    return res
