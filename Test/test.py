import unittest
from input_output import InputOutput
import pandas as pd


class InputOutputTest(unittest.TestCase):

    def test_nama_produk_IO(self):
        nama_sheet = 'PCT 185'
        df = pd.read_excel('Tabel Input Ouput 2016.xlsx', sheet_name=nama_sheet)
        r1 = InputOutput(df)
        nama_industri = r1.nama_produk_IO()[0]
        self.assertEqual(nama_industri, 'Padi') 

    def test_analisis_IO(self):
        nama_sheet = 'PCT 185'
        df = pd.read_excel('Tabel Input Ouput 2016.xlsx', sheet_name=nama_sheet)
        r1 = InputOutput(df)
        nama_industri = r1.nama_produk_IO()[0]
        hasil_analisis = r1.analisis_IO(nama_industri)
        expected_result = {
            'industri': 'Padi', 
            'test': [-0.0, 0.0], 
            'multiplier': [1.3772127274059245, 3.0802845828809793], 
            'linkage': [0.8952399289184213, 0.6018468445328643, 0.041744556216208595]
        }
        self.assertEqual(hasil_analisis, expected_result)

if __name__=='__main__':
    unittest.main()
