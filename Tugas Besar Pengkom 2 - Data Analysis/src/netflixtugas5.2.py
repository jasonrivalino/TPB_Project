#statistik data
from numpy.lib.function_base import quantile
import pandas as pd
import numpy as np
from numpy import percentile
df=pd.read_csv("Netflixoriginal.csv")
std=np.std(df) #menghitung standar deviasi pada data numerik yaitu runtime dan IMDb Score
print("Standar Deviasi:")
print(std) 
print()
mean=np.mean(df) #menghitung rata-rata pada data numerik yaitu runtime dan IMDb Score
print("Rata-rata:")
print(mean)
print()
q1,q2,q3,q4,q5=np.percentile(df["Runtime"],[10,25,50,75,90]) #menghitung simpangan kuartil untuk durasi film
print("Simpangan kuartil (Percentile) 10% untuk Runtime:",q1)
print("Simpangan kuartil (Percentile) 25% untuk Runtime:",q2)
print("Simpangan kuartil (Percentile) 50% untuk Runtime:",q3)
print("Simpangan kuartil (Percentile) 75% untuk Runtime:",q4)
print("Simpangan kuartil (Percentile) 90% untuk Runtime:",q5)
print()
min1=(df.min()["Runtime"])
min2=(df.min()["IMDb Score"])
print("Nilai minimum:") #menghitung nilai minimum pada data numerik yaitu runtime dan IMDb Score
print("Waktu film minimum adalah",min1,"menit")
print("IMDb Score minimum adalah",min2)
print()
max1=(df.max()["Runtime"])
max2=(df.max()["IMDb Score"])
print("Nilai maksimum:") #menghitung nilai maksimum pada data numerik yaitu runtime dan IMDb Score
print("Waktu film maksimum adalah",max1,"menit")
print("IMDb Score maksimum adalah",max2)