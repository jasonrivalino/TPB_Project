import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Netflixoriginal.csv")
df.loc[15:29].plot(kind="barh",x="Title",y="Runtime",title="DURASI FILM",color="red")
plt.show() #comparing categories horizontal bar chart
df.loc[(df["IMDb Score"]>8)].plot(kind="barh",x="Title",y="IMDb Score",title="FILM DENGAN IMDB SCORE LEBIH DARI 8",color="gray")
plt.show() #comparing categories horizontal bar chart
print()
df[["IMDb Score"]].plot(kind="hist",bins=[7,7.25,7.5,7.75,8,8.25,8.5,8.75,9],rwidth=0.8,title="HISTOGRAM RANGE IMDB SCORE") 
plt.show() #comparing categories histogram
print()
df.loc[(df["Runtime"]<=25)].plot(kind="line",x="IMDb Score",y=["Runtime"],title="LINE CHART RATING FILM DENGAN WAKTU KURANG DARI 25 MENIT",color="black") 
plt.show() #showing over times line chart
print()
df.loc[(df["Runtime"]>=135)].plot(kind="area",x="IMDb Score",y=["Runtime"],title="AREA CHART RATING FILM DENGAN WAKTU LEBIH DARI 135 MENIT",color="orange")
plt.show() #showing over times area chart
print()