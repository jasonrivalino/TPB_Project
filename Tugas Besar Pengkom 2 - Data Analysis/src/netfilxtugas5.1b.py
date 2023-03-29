#sampel data
import pandas as pd
df=pd.read_csv("Netflixoriginal.csv")
print(df.loc[142:151]) #menampilkan data pada baris ke 143 hingga 152 (perhitungan baris dimulai dari 0)
print()                #[select beberapa data dalam range baris tertentu, 10 baris terakhir untuk kasus ini]
print(df.loc[(df["Runtime"]>=120)&(df["IMDb Score"]<=7.5)]) #menampilkan data film yang durasinya lebih dari 120 menit
print()                                                     #dan IMDb Scorenya kurang dari 7.5 [select data dengan range tertentu]
print(df.sort_values(["Runtime"], ascending=[1])) #menampilkan urutan data berdasarkan durasi film terkecil hingga terbesar
print()                                              #[sort data terkecil hingga terbesar]
print(df.loc[50:59,["Title","Genre","Premiere"]]) #hanya menampilkan judul dan genre pada film dalam range baris ke 51 hingga 60 
print()                                #(perhitungan baris dimulai dari 0) [sampel data pada setiap kolom]