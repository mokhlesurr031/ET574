import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader as pdr

df = pd.read_csv('https://raw.githubusercontent.com/mokhlesurr031/ET574/master/content/sitka_weather_2018_simple.csv')
df.index = df['DATE']
ax = df['PRCP'].plot(figsize = (15,8))
ax.set_xlabel("Date")
ax.set_ylabel("Precipitation (in.)")
plt.show()