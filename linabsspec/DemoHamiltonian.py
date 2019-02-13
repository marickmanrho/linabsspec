
# create a simple demo Hamiltonian to produce some spectral data

def Hamiltonian(N=10,E=0,J=0.1,SigE=0.01,SigJ=0.01):
    import numpy as np
    H = np.zeros((N,N))
    v = np.zeros((N,1))
    w = np.zeros((N,N))
    for i in range(N):
        H[i][i] = E + np.random.normal(0,SigE)
        for j in range(i+1,N):
            H[i][j] = J + np.random.normal(0,SigJ)
            H[j][i] = H[i][j]

    v,w = np.linalg.eig(H)
    return(v,w)
