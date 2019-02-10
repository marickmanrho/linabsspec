def Absorption(E,Mu,Type = "gaus",gamma = 0.1,nSp = 1000,Write=False,Show=False):
    import numpy as np

    # Check if input causes errors and overwrite to default if possible
    E,Mu,Type,gamma,nSp,Write,Show = CheckInput(E,Mu,Type,gamma,nSp,Write,Show)

    # Shape of input
    sE = np.shape(E)
    sMu = np.shape(Mu)

    # Create abs variables
    Abs = np.zeros((nSp,1))
    w = np.zeros((nSp,1))
    sgamma = np.shape(gamma)

    # Create w vector
    # expand range by 2gamma + 20% to include edges
    minE = np.min(np.min(E))
    maxE = np.min(np.max(E))
    minw = minE - 10*np.mean(gamma) - 0.1*(maxE-minE)
    maxw = maxE + 10*np.mean(gamma) + 0.1*(maxE-minE)
    for i in range(nSp):
        w[i] = minw + i*(maxw-minw)/nSp

    # Calculate Absorption
    for i in range(sE[0]):
        for j in range(nSp):
            factor = -1.0*(E[i]-w[j])**2/(2*gamma[i])
            Abs[j] += Mu[i]**2*np.exp(factor)

    # Plot Absorption
    if Show:
        PlotAbsorption(w,Abs)

def CheckInput(E,Mu,Type,gamma,nSp,Write,Show):
    import warnings
    import numpy as np
    # Check input parameters
    if (Type != "gaus" and Type != "lor"):
        msg = "Absorption convolution type " + str(Type) + " is not known."
        exit(msg)

    error = 1
    if (type(E) != np.ndarray or type(Mu) != np.ndarray):
        msg = "Input E or Mu is not a numpy array type."
        exit(msg)

    if (type(E) != np.ndarray):
        E = np.asarray(E)
    if (type(Mu) != np.ndarray):
        Mu = np.asarray(Mu)

    sE = np.shape(E)
    sMu = np.shape(Mu)
    if (sE[0] != sMu[0]):
        msg = "Size of E and Mu are not compatible."
        exit(msg)

    if (nSp < sE[0]):
        msg = "Number of spectral points (nSp) < then the size of E."
        exit(msg)

    if (nSp < 10*sE[0]):
        msg = "Number of spectral points (nSp) is sparse with respect to the size of E."
        warnings.warn(msg,UserWarning)

    if (type(Write) != bool):
        msg = "Write is not recognized as true or false, using default Write = False instead."
        warnings.warn(msg,UserWarning)

    if (type(Show) != bool):
        msg = "Show is not recognized as true or false, using default Show = True instead."
        warnings.warn(msg,UserWarning)

    # Overwrite input if needed
    if (type(Write) != bool):
        Write = False
    if (type(Show) != bool):
        Show = False

    # Create a gamma for each energy E
    if np.isscalar(gamma):
        gamma = np.zeros((sE[0],1)) + gamma
    # Or make sure input is numpy array
    elif (type(gamma) != np.ndarray):
        gamma = np.asarray(gamma)

    # Convert Mu if needed
    if (sMu[1] > 1):
        temp_Mu = Mu
        Mu = np.zeros((sE[0],1))
        for i in range(sE[0]):
            for j in range(sMu[1]):
                Mu[i] = Mu[i] + temp_Mu[i][j]

    return(E,Mu,Type,gamma,nSp,Write,Show)

def PlotAbsorption(w,Abs):
    import matplotlib.pyplot as plt
    plt.plot(w,Abs)
    plt.ylabel('Absorption')
    plt.xlabel('Energy')
    plt.title('Linear Absorption')
    plt.show()

import numpy as np
from DemoHamiltonian import Hamiltonian

E, Mu = Hamiltonian()
Absorption(E,Mu,Write=False,Show=True)
