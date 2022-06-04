from multiprocessing.sharedctypes import Value
import unittest
from romanos import convertir_a_numero


class RomanosTest(unittest.Testcase):

    def test_unidades(self):
        self.assertEqual(convertir_a_numero("I"), 1)
        self.assertEqual(convertir_a_numero("V"), 5)
        self.assertEqual(convertir_a_numero("X"), 10)
        self.assertEqual(convertir_a_numero("L"), 50)
        self.assertEqual(convertir_a_numero("C"), 100)
        self.assertEqual(convertir_a_numero("D"), 500)
        self.assertEqual(convertir_a_numero("M"), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(covertir_a_numero("IV"), 4)
        self.assertEqual(covertir_a_numero("IX"), 9)
        self.assertEqual(covertir_a_numero("XL"), 40)
        self.assertEqual(covertir_a_numero("CCV"), 205)
        self.assertEqual(covertir_a_numero("MCXXIII"), 1123)

    def test_no_resta_mas_de_un_orden_de_magnitud(self):
        #self.assertRaises(ValueError, covertir_a_numero, "IC")
        #self.assertRaises(ValueError, covertir_a_numero, "XC")
        with self.assertRaises(ValueError)



        
if __name__ == "__main__":
    unittest,main()
