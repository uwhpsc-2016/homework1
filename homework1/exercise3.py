# Hint: you should only need the following functions from numpy and scipy
from numpy import diag, tril, triu, dot, array
from numpy.linalg import norm
from scipy.linalg import solve_triangular

def decompose(A):
    pass

def jacobi_step(D, L, U, b, xk):
    pass

def jacobi_iteration(A, b, x0, epsilon=1e-8):
    pass

def gauss_seidel_step(D, L, U, b, xk):
    pass

def gauss_seidel_iteration(A, b, x0, epsilon=1e-8):
    pass
