import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Netflixoriginal.csv")
df.plot(kind="scatter", x="Runtime", y="IMDb Score",title="SCATTER PLOT SEMUA FILM",color="purple")
print(df["IMDb Score"].corr(df["Runtime"]))
plt.show()
print()