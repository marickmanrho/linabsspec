#
# Unittests for Absorption()
#
import unittest
import numpy as np
from absorption import *

class test_input(unittest.TestCase):
    # Test if error is raised when E or Mu are complex
    def test_E_cinput(self):
        E = np.array(complex(1,1))
        Mu = np.zeros((1,1)) + 1
        try:
            with self.assertRaises(ValueError): Absorption(E,Mu)
        except:
            self.fail('No error raised on complex E.')
    def test_Mu_cinput(self):
        E = np.zeros((1,1))
        Mu = np.array(complex(1,1))
        try:
            with self.assertRaises(ValueError): Absorption(E,Mu)
        except:
            self.fail('No error raised on complex Mu.')

    # Test with DemoHamiltonian
    def test_demo(self):
        from demohamiltonian import Hamiltonian
        try:
            E,Mu = Hamiltonian()
            Absorption(E,Mu)
        except:
            self.fail('Demo Hamiltonian did not result in completed run by absorption.py')

if __name__ == '__main__':
    unittest.main()
