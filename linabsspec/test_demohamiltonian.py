import unittest
import numpy as np
from DemoHamiltonian import *

class TestHamGen(unittest.TestCase):
    # Test if output has right dimensions
    def testDim(self):
        N = 2
        v,w = Hamiltonian(N,1,1,1,1)
        a = np.shape(v)
        b = np.shape(w)
        self.assertEqual(a,(N,))
        self.assertEqual(b,(N,N))

if __name__ == '__main__':
    unittest.main()
