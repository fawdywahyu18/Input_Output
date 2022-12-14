'''
    DOKUMENTASI ANALISIS IO
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

    '''
    __init__
    Setup atribut input data untuk method
    '''

    '''
    nama_produk_IO
    Method ini untuk menghasilkan output nama produk yang ada di tabel Input-Output
    '''

    '''
    analisis_IO
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
        