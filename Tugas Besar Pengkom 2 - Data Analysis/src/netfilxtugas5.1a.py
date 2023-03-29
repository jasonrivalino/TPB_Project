#sampel data
import pandas as pd
df=pd.read_csv("Netflixoriginal.csv")
print(df.loc[20:29]) #menampilkan data pada baris ke 21 hingga 30 (perhitungan baris dimulai dari 0)
print()              #[select beberapa data dalam range baris tertentu]
print(df.loc[(df["Runtime"]<=90)&(df["IMDb Score"]>=8.5)]) #menampilkan data film yang durasinya kurang dari 90 menit
print()                                                    #dan IMDb Scorenya lebih dari 8.5 [select data dengan range tertentu]
print(df.sort_values(["IMDb Score"], ascending=[0])) #menampilkan urutan data berdasarkan IMDb Score terbesar hingga terkecil
print()                                              #[sort data terbesar hingga terkecil]
print(df.loc[(df["IMDb Score"]>=8.0),["Title","Premiere","Language"]]) #hanya menampilkan judul dan bahasa pada film dengan IMDb Score lebih dari 8.0
print()                                                     #[sampel data pada setiap kolom]