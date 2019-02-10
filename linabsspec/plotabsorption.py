#
# plotabsorption.py
#
# A matplotlib script to nicely plot absorption spectra.
#
def PlotAbsorption(w,Abs):
    import matplotlib.pyplot as plt
    plt.plot(w,Abs)
    plt.ylabel('Absorption')
    plt.xlabel('Energy')
    plt.title('Linear Absorption')
    plt.show()
