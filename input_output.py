# Created by FAWDY

import pandas as pd
import numpy as np

class InputOutput:
    '''
    Author: Fawdy
    Dokumentasi Class untuk analisis Input/Output
    Referensi Chapter 2 dan Chapter 6 Input-Output Analysis by Rob E. Miller
    Chapter 2: Foundations of Input-Output Analysis
    Chapter 6: Multiplier in the Input-Output Model
    Chapter 12: Supply-Side Models, Linkages, and Important Coefficeints

    ...
    Cara instalasi class ini:
    install setup.py dengan cara run command ini di terminal linux:
    pip install Impor_Baja_IO
    Impor_Baja_IO adalah nama folder tempat menyimpan setup.py

    ...
    Attributes:
    a. data file: dataframe
    nama file adalah hasil read excel data asli BPS. Harus data format ASLI.
    Terdapat 3 jenis sheet dalam data asli BPS:
    1. PCT 185
    2. BCT 185
    3. BCD 185


    Methods:
    a. nama_produk_IO
    b. analisis_IO
    
    '''

    def __init__(self, data_file):
        '''
        Setup atribut input data untuk method
        '''
        self.data_file = data_file
    
    def nama_produk_IO(self):
        '''
        Method ini untuk menghasilkan output nama produk yang ada di tabel Input-Output
        '''
        df = self.data_file
        df_extracted = df.iloc[3:,2:].reset_index().drop(columns=['index'])
        nama_produk = df_extracted.iloc[2:,0].reset_index().iloc[:185,1]
        return nama_produk

    def analisis_IO(self, nama_industri, tambahan_berapa=1):
        '''
        Input parameters:
        a. nama_industri: str
        merupakan salah satu nama_produk dari method nama_produk_IO
        b. tambahan_berapa: int
        merupakan nilai perubahan [default 1] untuk mengihitung multiplier.
        bisa diganti dengan nilai int tertentu [misal 100000]
        Kalau demand side: delta fd (final demand)
        kalau supply side: delta va (value added)
        ...

        Method ini untuk estimasi:
        a. Multiplier dari demand dan supply side
        b. Linkage (Backward (BL), Forward (FL), Net Backward (NBL))
        - Angka BL menunjukkan bahwa nama_produk memliki kategori (above average)
          atau linkage yang kuat sebagai pembeli apabila angkanya di atas 1
        - Angka FL menunjukkan bahwa nama_produk memliki kategori (above average)
          atau linkage yang kuat sebagai suplier apabila angkanya di atas 1
        - Angka Net Backward Linkage by Dietzenbacher (2005)
          In particular, if Net BL >1 then economy-wide output generated by
          final demand in j is larger than the amount of js output that is generated by all the other
          industries final demands. So industry j can be said to be more important for the others
          than the others are for industry j, and j would thus be identified as a key sector by this
          measure.
        '''
        # Preparing the matrix
        df = self.data_file
        df_extracted = df.iloc[3:,2:].reset_index().drop(columns=['index'])
        nama_produk = df_extracted.iloc[2:,0].reset_index().iloc[:185,1]
        df_Z = df_extracted.iloc[2:187, 1:186].reset_index().drop(columns=['index'])
        series_output = df_extracted.iloc[2:187,-2].reset_index().drop(columns=['index'])
        mat_Z = df_Z.to_numpy(dtype=int)
        vec_output = series_output.to_numpy(dtype=int)
        mat_output = vec_output * np.identity(len(vec_output))
        inv_x = np.linalg.inv(mat_output)
        mat_A = np.matmul(mat_Z, inv_x)

        df_fd = df_extracted.iloc[2:187, 194].reset_index().drop(columns=['index'])
        mat_fd = df_fd.to_numpy(dtype=int)
        df_impor = df_extracted.iloc[2:187, 199].reset_index().drop(columns=['index'])
        mat_impor = df_impor.to_numpy(dtype=int)
        df_marjin = df_extracted.iloc[2:187, 203].reset_index().drop(columns=['index'])
        mat_marjin = df_marjin.to_numpy(dtype=int)
        df_pajak = df_extracted.iloc[2:187, 204].reset_index().drop(columns=['index'])
        mat_pajak = df_pajak.to_numpy(dtype=int)
        mat_fd_new = mat_fd - mat_impor - mat_marjin - mat_pajak

        mat_res = np.identity(len(mat_A)) - mat_A
        mat_L = np.linalg.inv(mat_res) # Leontief Matrix
        # Test Demand Side
        mat_test = np.matmul(mat_L, mat_fd_new)
        test = vec_output - mat_test # Tested!!!
        result_test_demand = np.round(np.mean(test), 3) #TESTED!!!

        # Demand-Side Multiplier besi dan baja dasar (Exogenous Model)
        indeks_bb = nama_produk[nama_produk==nama_industri].index[0]
        delta_fd = pd.DataFrame([0] * len(mat_fd_new))
        vec_dfd = delta_fd.to_numpy(dtype=int)
        vec_dfd[indeks_bb] = tambahan_berapa # disesuaikan dengan nilai impor industri
        new_output = np.matmul(mat_L, vec_dfd)
        multiplier = 0
        for i in range(0, len(new_output)):    
            multiplier = multiplier + new_output[i]

        # Supply-Side Multiplier besi dan baja dasar (Exogenous Model)
        mat_B = np.matmul(inv_x, mat_Z) # allocation coeffcient
        mat_res2 = np.identity(len(mat_B)) - mat_B
        mat_G = np.linalg.inv(mat_res2) # the output inverse
        df_va = df_extracted.iloc[194, 1:186].reset_index().drop(columns=['index'])
        mat_va = df_va.to_numpy(dtype=int)
        df_pajak_input = df_extracted.iloc[189, 1:186].reset_index().drop(columns=['index'])
        mat_pajak_input = df_pajak_input.to_numpy(dtype=int)
        df_impor_input = df_extracted.iloc[190, 1:186].reset_index().drop(columns=['index'])
        mat_impor_input = df_impor_input.to_numpy(dtype=int)
        mat_va_new = mat_va + mat_pajak_input + mat_impor_input

        # Test Supply Side
        mat_test_supply = np.matmul(np.transpose(mat_va_new), mat_G)
        test_supply = vec_output - np.transpose(mat_test_supply) # TESTED!!!
        result_test_supply = np.round(np.mean(test_supply), 3) #TESTED!!!

        delta_va = pd.DataFrame([0] * len(mat_va_new))
        vec_dva = delta_va.to_numpy(dtype=int)
        vec_dva[indeks_bb] = tambahan_berapa # disesuaikan dengan tambahan value added idustri
        new_output_supply = np.matmul(mat_G, vec_dva)
        multiplier_supply = 0
        for i in range(0, len(new_output_supply)):    
            multiplier_supply = multiplier_supply + new_output_supply[i]

        # Linkage
        colsum_A = np.sum(mat_A, axis=0)
        rowsum_A = np.sum(mat_A, axis=1)
        nrow_A = mat_A.shape[0]
        # ncol_A = mat_A.shape[1]
        denominator_BL = np.matmul(colsum_A, rowsum_A)
        numerator_BL = nrow_A * colsum_A
        backward_linkage = numerator_BL/denominator_BL # Normalized backward linkage
        bl_j = backward_linkage[indeks_bb] # Direct Backward Linkage untuk nama produk
        
        # Direct Forward Linkage
        colsum_B = np.sum(mat_B, axis=0)
        rowsum_B = np.sum(mat_B, axis=1)
        nrow_B = mat_B.shape[0]
        # ncol_B = mat_B.shape[1]
        denominator_FL = np.matmul(colsum_B, rowsum_B)
        numerator_FL = nrow_B * colsum_B
        forward_linkage = numerator_FL/denominator_FL # Normalized forward linkage
        fl_j = forward_linkage[indeks_bb]

        # Net bakward linkage by Dietzenbacher (2005)
        mat_fd_id = mat_fd_new * np.identity(len(mat_fd_new))
        net_BL = np.sum((np.matmul((np.matmul(mat_L, mat_fd_id)), inv_x)), axis=0)
        net_bl_j = net_BL[indeks_bb]
        
        result_dict = {
            'industri': nama_industri,
            'test': [result_test_demand, result_test_supply],
            'multiplier': [multiplier[0], multiplier_supply[0]],
            'linkage': [bl_j, fl_j, net_bl_j]
            }
        return result_dict
