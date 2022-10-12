from input_output import InputOutput
import pandas as pd

nama_sheet = 'PCT 185'
df = pd.read_excel('Tabel Input Ouput 2016.xlsx', sheet_name=nama_sheet)
r1 = InputOutput(df)

nama_industri = r1.nama_produk_IO()[0]
hasil_analisis = r1.analisis_IO(nama_industri)
print(nama_industri)
print(hasil_analisis)