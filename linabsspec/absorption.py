#
# absorption.py
#
# Calculates linear Absorption Spectrum
# See README for more info
#

def Absorption(E,Mu,Type = "gaus",gamma = 0.000001,nSp = 1000,Write=False,Show=False):
    import numpy as np
    from checkinput import CheckInput
    from plotabsorption import PlotAbsorption

    # Check if input causes errors and overwrite to default if possible
    E,Mu,Type,gamma,nSp,Write,Show = CheckInput(E,Mu,Type,gamma,nSp,Write,Show)

    # Shape of input
    sE = np.shape(E)
    sMu = np.shape(Mu)

    # Create abs variables
    Abs = np.zeros((nSp,1))
    w = np.zeros((nSp,1))
    sgamma = np.shape(gamma)

    # Create w vector (w stands for omega, e.g. the incomming light frequency)
    # Expand range by 10gamma + 10% to include edges of spectrum.
    minE = np.min(np.min(E))
    maxE = np.min(np.max(E))
    minw = minE - 10*np.mean(gamma) - 0.05*(maxE-minE)
    maxw = maxE + 10*np.mean(gamma) + 0.05*(maxE-minE)
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

#import numpy as np
#from DemoHamiltonian import Hamiltonian

#E, Mu = Hamiltonian()
#Absorption(E,Mu,gamma=0.001,Write=False,Show=True)
