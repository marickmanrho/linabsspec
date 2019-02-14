# Linear Absorption Spectrum (libabsspec)

This package will calculate the linear absorption spectrum of a given set of EigenEnergies and Oscillator strengths. Linewidth can be provided optionally.

Developed at the University of Groningen in the Theory of Condensed Matter group.\
Author: Marick Manrho (PhD candidate)

## Installation

Run `pip install .` to install linabsspec and dependencies.

## Usage

The Linear Absorption Spectrum is calculated by calling `Absorption()`.

`Absorption(E,Mu,Type = "gaus",gamma = 0.000001,nSp = 1000,Write=False,Show=False,Filename = "Demo")`

| Variable  |Description                          |Type|
| ---------:|:------------------------------------| -----:|
|`E`        |EigenEnergies of Hamiltonian         |Vector |
|`Mu`       |Oscillator strength of EigenEnergies |Vector |
|`Type`     |The type of line broadening, "gaus" is currently the only supported lineshape.                                        |String|
|`gamma`    |Linewidth per EigenEnergy. If scalar is given the same value is used for each EigenEnergy.                                      |Vector / Scalar|
|`nSp`      |Number of Spectral points            |Scalar|
|`Write`    |Write to file                        |Bolean|
|`Show`     |Show a plot of absorption            |Bolean|
|`Filename` |Filename                             |String|
|`overwrite`|Overwrite file if it already exists  |Bolean|

## Dependencies

This package depends on the following packages:
- `numpy`
- `os`
- `system`
- `matplotlib`

## Contact info & support

When you encounter faulty code, please create an issue on GitHub. Feel free to ask questions via email to m.manrho@rug.nl.
