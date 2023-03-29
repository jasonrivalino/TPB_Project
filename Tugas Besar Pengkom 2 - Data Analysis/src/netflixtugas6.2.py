import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Netflixoriginal.csv")
df2=df["IMDb Score"].value_counts() #whole-part relationships pie chart
df2.plot(kind="pie",title="PIE CHART IMDB SCORE")
plt.show()
print()
df2=(df.loc[(df["Runtime"]<=60)])["Genre"].value_counts() #whole-part relationships pie chart with selection
df2.plot(kind="pie",title="PIE CHART GENRE FILM YANG WAKTUNYA DIBAWAH 60 MENIT")
plt.show()
print()
df.loc[61:80].plot(kind="barh",x="Title",y=["IMDb Score","Runtime"], stacked = True,title="STACKED BAR IMDB SCORE DAN DURASI FILM")
plt.show() #whole-part relationships stacked bar
print()
df.loc[(df["IMDb Score"]<7.5)].plot(kind="scatter", x="Runtime", y="IMDb Score",title="SCATTER PLOT FILM DENGAN RATING DIBAWAH 7.5",color="green")
plt.show() #plotting relationships scatter plot
print()
df.loc[(df["IMDb Score"]>=7.5)].plot(kind="scatter", x="Runtime", y="IMDb Score",title="SCATTER PLOT FILM DENGAN RATING DIATAS ATAU SAMA DENGAN 7.5",color="purple")
plt.show() #plotting relationships scatter plot
print()