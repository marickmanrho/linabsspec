#
# checkinput.py
#
# Checks the input to Absorption()
# It will make sure all input has the right format to let the code run succesfully.
#

def CheckInput(E,Mu,Type,gamma,nSp,Write,Show):
    import warnings
    import numpy as np

    # Check if Type is one of the supported types
    if (Type != "gaus" and Type != "lor"):
        msg = "Absorption convolution type " + str(Type) + " is not known."
        exit(msg)

    # Make sure E and Mu are real valued numpy arrays
    if (type(E) != np.ndarray or type(Mu) != np.ndarray):
        msg = "Input E or Mu is not a numpy array type. Converting..."
        warnings.warn(msg,UserWarning)

    if (type(E) != np.ndarray):
        E = np.asarray(E)
    if (type(Mu) != np.ndarray):
        Mu = np.asarray(Mu)

    Ecomplex = np.iscomplex(E)
    if Ecomplex.any():
        msg = "E contains complex numbers."
        raise ValueError(msg)
    Mucomplex = np.iscomplex(Mu)
    if Mucomplex.any():
        msg = "Mu contains complex numbers."
        raise ValueError(msg)

    # Determine shape of E and Mu, needed for below checks
    sE = np.shape(E)
    sMu = np.shape(Mu)

    # Prevent Size problems
    if (sE[0] != sMu[0]):
        msg = "Size of E and Mu are not compatible."
        exit(msg)

    # If the number of spectral points (nSp) is smaller then the number of
    # energies (sE[0]) then the output is even less then the stick spectrum.
    if (nSp < sE[0]):
        msg = "Number of spectral points (nSp) < then the size of E."
        exit(msg)

    # Warn if the number of spectral points is poorly covering the data.
    if (nSp < 10*sE[0]):
        msg = "Number of spectral points (nSp) is sparse with respect to the size of E."
        warnings.warn(msg,UserWarning)

    # Make sure Write and Show parameters are True or False
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

    # Create a gamma for each energy E. If gamma is a scaler we use that value
    # for each energy. Otherwise we make sure it is an array with the same size
    # as the number of energies.
    if np.isscalar(gamma):
        gamma = np.zeros((sE[0],1)) + gamma
    # Or make sure input is numpy array
    elif (type(gamma) != np.ndarray):
        gamma = np.asarray(gamma)

    sgamma = np.shape(gamma)
    if sgamma[0]!=sE[0]:
        msg = "Input shape of gamma is not equal to the shape of E."
        exit(msg)

    # Convert Mu if needed. When Mu NxM matrix then we sum the contributions to
    # create a one dimensional Nx1 vector. This happens when working with dipole
    # moments in >1 dimensions.
    if (sMu[1] > 1):
        temp_Mu = Mu
        Mu = np.zeros((sE[0],1))
        for i in range(sE[0]):
            for j in range(sMu[1]):
                Mu[i] = Mu[i] + temp_Mu[i][j]

    # We might have overwritten some parameters, so we return them to the main
    # code to update them there.
    return(E,Mu,Type,gamma,nSp,Write,Show)
