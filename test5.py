import numpy as np

def gs(A, x0, b, itmax):
    # Performs ‘‘itmax’’ iterations of Jacobi/Gauss-Seidel/SOR on Ax = b
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    D = np.diag(np.diag(A))

    for i in range(n):
        for j in range(n):
            if i < j:
                U[i, j] = -A[i, j]
            if i > j:
                L[i, j] = -A[i, j]

    M = np.linalg.inv(D - L)
    B = M @ U  # B is GS iteration matrix

    # M = np.linalg.inv(D); B = M @ (L + U) # Use this for Jacobi
    # w = 1.1; b = w * b; M = np.linalg.inv(D - w * L); B = M @ ((1 - w) * D + w * U) # Use this for SOR

    resid = np.zeros(itmax)
    for iter in range(itmax):
        soln = B @ x0 + M @ b
        if np.linalg.norm(b, 2) == 0:
            soln = soln / np.linalg.norm(soln, 1)  # Normalize when b=0.
        resid[iter] = np.linalg.norm(A @ soln - b, 2)
        x0 = soln

    resid = resid.reshape((itmax, 1))
    if np.linalg.norm(b, 2) == 0:
        soln = soln / np.linalg.norm(soln, 1)  # Normalize when b = 0.

    return soln, resid

A = np.array([[0.5, 0.5, 0, 0], [0, 0.5, 0.5, 0], [0, 0, 0.5, 0.5], [0.125, 0.125, 0.25, 0.5]])
b = np.array([0, 0, 0, 0])
x0 = np.zeros(4)
itmax = 50
soln, resid = gs(A, x0, b, itmax)

print("Solution:")
print(soln)

print("Residuals:")
print(resid)
