import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader as pdr

df = pd.read_csv('https://raw.githubusercontent.com/mokhlesurr031/ET574/master/content/nyc_temps.csv')
df.index = df['DATE']
df['TMAX'].plot(figsize = (15,8), color='red')
ax = df['TMIN'].plot(figsize = (15,8))
ax.set_xlabel("Dates")
ax.set_ylabel("Temparature (F)")
plt.show()
