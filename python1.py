import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import json
import numpy as np
from pandas.core.frame import DataFrame


from pandas.io.formats.format import DataFrameFormatter
st.title("Aplikasi Penghitung Produksi Minyak")
HandleCodeNegara = open("kode_negara_lengkap.json")
HandleFileProduksi = pd.read_csv("produksi_minyak_mentah.csv")
DataCode = json.load(HandleCodeNegara)

def ConverterNegaraCode(Nama):
    j = 0
    CodeNegaraFul = str(0)
    for i in DataCode:
        DataCode1 = DataCode[j]
        CodeNegara = DataCode1['alpha-3']
        NamaNegara = DataCode1['name']
        if (Nama == "Venezuela"):
            CodeNegaraFul = str("VEN")
        elif (Nama == "Iran"):
            CodeNegaraFul = str("IRN")
        else :
            if(Nama == NamaNegara):
                CodeNegaraFul = CodeNegara
        j = j+1
    j = 0
    return CodeNegaraFul

def ConverterCodeNegaraLengkap(Code):
    j = 0
    NamaNegaraFull = str(0)
    CodeNegara1 = str(0)
    RegionNegara1 = str(0)
    SubRegionNegara1 = str(0)
    for i in DataCode:
        DataCode1 = DataCode[j]
        CodeNegara = DataCode1['alpha-3']
        NamaNegara = DataCode1['name']
        if(Code == CodeNegara):
            NamaNegaraFull = NamaNegara
            CodeNegara1 = DataCode1['country-code']
            RegionNegara1 = DataCode1['region']
            SubRegionNegara1 = DataCode1['sub-region']
        j = j+1
    j = 0
    return CodeNegara1,RegionNegara1,SubRegionNegara1

def ConverterCodeNegara(Code):
    j = 0
    NamaNegaraFull = str(0)
    for i in DataCode:
        DataCode1 = DataCode[j]
        CodeNegara = DataCode1['alpha-3']
        NamaNegara = DataCode1['name']
        if(Code == CodeNegara):
            NamaNegaraFull = NamaNegara
            CodeNegara1 = DataCode1['country-code']
            RegionNegara1 = DataCode1['region']
            SubRegionNegara1 = DataCode1['sub-region']
        j = j+1
    j = 0
    return NamaNegaraFull

NamaBaru1 = []
KodeBaru1 = []
TahunBaru1 = []
ProduksiBaru1 = []
RegionBaru1 = []
SubRegionBaru1 = []
for i in (HandleFileProduksi.index):
    KodeBaruu,RegionBaruu,SubRegionBaruu = ConverterCodeNegaraLengkap(HandleFileProduksi.loc[i,"kode_negara"])
    if (KodeBaruu != str(0)):
        KodeBaru1.append(KodeBaruu)
        NamaBaru1.append(ConverterCodeNegara(HandleFileProduksi.loc[i,"kode_negara"]))
        TahunBaru1.append(HandleFileProduksi.loc[i,"tahun"])
        ProduksiBaru1.append(HandleFileProduksi.loc[i,"produksi"])
        RegionBaru1.append(RegionBaruu)
        SubRegionBaru1.append(SubRegionBaruu)
DataBaru1 = {"Nama Negara" : NamaBaru1,"Kode" : KodeBaru1, "Tahun" : TahunBaru1,
            "Produksi" : ProduksiBaru1, "Region" : RegionBaru1, "Sub-Region" : SubRegionBaru1}
HandleFileProduksi1 = pd.DataFrame(DataBaru1)

ProduksiBaru = [0]
NamaBaru = [0]
j = 0
NamaNegara = HandleFileProduksi.loc[0,"kode_negara"]
NamaBaru[0] = ConverterCodeNegara(NamaNegara)
for i in (HandleFileProduksi.index):
    NamaNegaraC = HandleFileProduksi.loc[i,"kode_negara"]
    if (NamaNegaraC == NamaNegara):
        ProduksiBaru[j] = ProduksiBaru[j] + HandleFileProduksi.loc[i,"produksi"]
    else :
        NamaNegara = NamaNegaraC
        j = j+1
        NamaBaru.append(ConverterCodeNegara(NamaNegaraC))
        ProduksiBaru.append(HandleFileProduksi.loc[i,"produksi"])
for i in range (len(ProduksiBaru)):
    for j in range(i,len(ProduksiBaru)):
        if (ProduksiBaru[j] > ProduksiBaru[i]):
            DataP = ProduksiBaru[i]
            ProduksiBaru[i] = ProduksiBaru[j]
            ProduksiBaru[j] = DataP
            DataK = NamaBaru[i]
            NamaBaru[i] = NamaBaru[j]
            NamaBaru[j] = DataK
for i in range (len(ProduksiBaru)):
    ProduksiBaru[i] = str(ProduksiBaru[i])
loop = 0
while (loop != len(NamaBaru)):
    if (NamaBaru[loop] == "0"):
        NamaBaru[loop] = "-1"
        NamaBaru.remove('-1')
        ProduksiBaru.remove(ProduksiBaru[loop])
        loop = 0
    else:
        loop = loop + 1
for i in range (len(ProduksiBaru)):
    ProduksiBaru[i] = float(ProduksiBaru[i])
DataBaru = {"Nama Negara" : NamaBaru, "Produksi Kumulatif" : ProduksiBaru}
DataFrameBaru = pd.DataFrame(data=DataBaru)
    
NamaBaru1 = []
KodeBaru1 = []
TahunBaru1 = []
ProduksiBaru1 = []
RegionBaru1 = []
SubRegionBaru1 = []
for i in (HandleFileProduksi.index):
    KodeBaruu,RegionBaruu,SubRegionBaruu = ConverterCodeNegaraLengkap(HandleFileProduksi.loc[i,"kode_negara"])
    if (KodeBaruu != str(0)) & (HandleFileProduksi.loc[i,"produksi"] != 0):
        KodeBaru1.append(KodeBaruu)
        NamaBaru1.append(ConverterCodeNegara(HandleFileProduksi.loc[i,"kode_negara"]))
        TahunBaru1.append(HandleFileProduksi.loc[i,"tahun"])
        ProduksiBaru1.append(HandleFileProduksi.loc[i,"produksi"])
        RegionBaru1.append(RegionBaruu)
        SubRegionBaru1.append(SubRegionBaruu)
DataBaru2 = {"Nama Negara" : NamaBaru1,"Kode" : KodeBaru1, "Tahun" : TahunBaru1,
            "Produksi" : ProduksiBaru1, "Region" : RegionBaru1, "Sub-Region" : SubRegionBaru1}
HandleFileProduksiTanpaNol = pd.DataFrame(DataBaru2)

NamaBaru1 = []
KodeBaru1 = []
TahunBaru1 = []
ProduksiBaru1 = []
RegionBaru1 = []
SubRegionBaru1 = []
for i in (HandleFileProduksi.index):
    KodeBaruu,RegionBaruu,SubRegionBaruu = ConverterCodeNegaraLengkap(HandleFileProduksi.loc[i,"kode_negara"])
    if (KodeBaruu != str(0)) & (HandleFileProduksi.loc[i,"produksi"] == 0):
        KodeBaru1.append(KodeBaruu)
        NamaBaru1.append(ConverterCodeNegara(HandleFileProduksi.loc[i,"kode_negara"]))
        TahunBaru1.append(HandleFileProduksi.loc[i,"tahun"])
        ProduksiBaru1.append(HandleFileProduksi.loc[i,"produksi"])
        RegionBaru1.append(RegionBaruu)
        SubRegionBaru1.append(SubRegionBaruu)
DataBaru2 = {"Nama Negara" : NamaBaru1,"Kode" : KodeBaru1, "Tahun" : TahunBaru1,
            "Produksi" : ProduksiBaru1, "Region" : RegionBaru1, "Sub-Region" : SubRegionBaru1}
HandleFileProduksiNol = pd.DataFrame(DataBaru2)

'''Program Start'''

print("Pilih Menu")

Token = st.selectbox("Select Menu yang Anda Inginkan :" , ["0. Default",
                                                          "1. Melihat grafik Produksi Minyak Negara Tertentu",
                                                          "2. Melihat Beberapa Negara Dengan Produksi Minyak Terbesar Pada Tahun Tertentu",
                                                          "3. Melihat Beberapa Negara Dengan Produksi Kumulatif Terbesar",
                                                          "4. Melihat Negara dengan Produksi Ekstrim (Produksi Maksimum, Minimum dan Nol) Pada Tahun Tertentu"])

if(Token == "1. Melihat grafik Produksi Minyak Negara Tertentu"):
    NamaNegara1 = st.text_input("Silahkan Inputkan Nama Negara")
    CodeNegaraFull = ConverterNegaraCode(NamaNegara1)
    st.write("Berikut Plot data Produksi Minyak dari Negara " + NamaNegara1 + " : ")
    try:
        ats = HandleFileProduksi.loc[HandleFileProduksi["kode_negara"] == CodeNegaraFull]
        st.bar_chart(ats)
    except:
        st.write("Tidak ada data Produksi Minyak dari Negara " + str(NamaNegara1))

elif(Token == "2. Melihat Beberapa Negara Dengan Produksi Minyak Terbesar Pada Tahun Tertentu"):
    try:
        Ranking = st.number_input("Silahkan Masukkan Berapa Negara : ", min_value = 0, step = 1)
        Tahun = st.number_input("Silahkan Masukkan Tahun : ", min_value = 1971, max_value = 2015, step = 1)
        DataFrameTahun = HandleFileProduksi1.loc[HandleFileProduksi1["Tahun"]==Tahun]
        DataFrameTahunSort = DataFrameTahun.sort_values(["Produksi"], ascending=[0])
        st.write(DataFrameTahunSort[0:Ranking])
        
    except:
        st.write("Belum ada Data Valid yang Dapat Ditampilkan")

elif(Token == "3. Melihat Beberapa Negara Dengan Produksi Kumulatif Terbesar"):
    try :
        BanyakNegara = st.number_input("Silahkan Input Berapa Banyak Negara Dengan Produksi Terbesar yang Akan Ditampilkan : ", min_value = 0, step = 1)
        if (BanyakNegara < len(NamaBaru)) & (BanyakNegara > 0):
            show1 = DataFrameBaru[0:BanyakNegara]
            st.write(show1)
            show2 = pd.DataFrame(np.random.randn(20,BanyakNegara),Columns = NamaBaru[0:BanyakNegara-1])
            st.bar_chart(DataFrameBaru)
        else :
            st.write("Belum ada Data Valid yang Dapat Ditampilkan")
    except :
        st.write("Belum ada Data Valid yang Dapat Ditampilkan")

elif (Token == "4. Melihat Negara dengan Produksi Ekstrim (Produksi Maksimum, Minimum dan Nol) Pada Tahun Tertentu"):
    try :
        Tahun1 = st.number_input("Masukkan Tahun : ", min_value = 1971, max_value = 2015, step = 1)
        DataFrameTahun1 = HandleFileProduksiTanpaNol.loc[HandleFileProduksiTanpaNol["Tahun"]==Tahun1]
        imax = DataFrameTahun1["Produksi"].idxmax()
        a = HandleFileProduksiTanpaNol.loc[imax, "Nama Negara"]
        st.write("Negara Dengan Penghasil Minyak Terbanyak Pada Tahun " + str(Tahun1))
        st.write("--Nama Negara : " + str(HandleFileProduksiTanpaNol.loc[imax, "Nama Negara"]))
        st.write("--Kode Negara : " + str(HandleFileProduksiTanpaNol.loc[imax, "Kode"]))
        st.write("--Region : " + str(HandleFileProduksiTanpaNol.loc[imax, "Region"]))
        st.write("--Sub-Region : " + str(HandleFileProduksiTanpaNol.loc[imax, "Sub-Region"]))
        st.write("--Produksi Tahun " + str(Tahun1) + " : " + str(HandleFileProduksiTanpaNol.loc[imax, "Produksi"]))
        for i in (DataFrameBaru.index):
            if (HandleFileProduksiTanpaNol.loc[imax, "Nama Negara"] == DataFrameBaru.loc[i,"Nama Negara"]):
                ProduksiKumulatif = DataFrameBaru.loc[i,"Produksi Kumulatif"]
        st.write("--Produksi Akumulatif : " + str(ProduksiKumulatif))

        DataFrameTahun1 = HandleFileProduksiTanpaNol.loc[HandleFileProduksiTanpaNol["Tahun"]==Tahun1]
        imin = DataFrameTahun1["Produksi"].idxmin()
        st.write("Negara Dengan Penghasil Minyak Terkecil (Bukan Nol) Pada Tahun " + str(Tahun1))
        st.write("--Nama Negara         : " + str(HandleFileProduksiTanpaNol.loc[imin, "Nama Negara"]))
        st.write("--Kode Negara         : " + str(HandleFileProduksiTanpaNol.loc[imin, "Kode"]))
        st.write("--Region              : " + str(HandleFileProduksiTanpaNol.loc[imin, "Region"]))
        st.write("--Sub-Region          : " + str(HandleFileProduksiTanpaNol.loc[imin, "Sub-Region"]))
        st.write("--Produksi Tahun " + str(Tahun1) + "      : " + str(HandleFileProduksiTanpaNol.loc[imin, "Produksi"]))
        for i in (DataFrameBaru.index):
            if (HandleFileProduksiTanpaNol.loc[imin, "Nama Negara"] == DataFrameBaru.loc[i,"Nama Negara"]):
                ProduksiKumulatif = DataFrameBaru.loc[i,"Produksi Kumulatif"]
        st.write("--Produksi Akumulatif : " + str(ProduksiKumulatif))

        DataFrameTahun1 = HandleFileProduksiNol.loc[HandleFileProduksiNol["Tahun"]==Tahun1]
        imin = DataFrameTahun1["Produksi"].idxmin()
        st.write("Negara Dengan Penghasil Minyak Nol Pada Tahun " + str(Tahun1))
        st.write ("--Nama Negara : " + str(HandleFileProduksiNol.loc[imin, "Nama Negara"]))
        st.write("--Kode Negara : " + str(HandleFileProduksiNol.loc[imin, "Kode"]))
        st.write("--Region : " + str(HandleFileProduksiNol.loc[imin, "Region"]))
        st.write("--Sub-Region : " + str(HandleFileProduksiNol.loc[imin, "Sub-Region"]))
        st.write("--Produksi Tahun " + str(Tahun1) + " : " + str(HandleFileProduksiNol.loc[imin, "Produksi"]))
        for i in (DataFrameBaru.index):
            if (HandleFileProduksiNol.loc[imin, "Nama Negara"] == DataFrameBaru.loc[i,"Nama Negara"]):
                ProduksiKumulatif = DataFrameBaru.loc[i,"Produksi Kumulatif"]
        st.write("--Produksi Akumulatif : " + str(ProduksiKumulatif))
    except :
        st.write("Belum ada data valid yang dapat ditampilkan")
