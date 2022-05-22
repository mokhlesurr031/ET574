import matplotlib.pyplot as plt
import numpy as np

lifetime_earning_by_educational_background = {"Less than high school":1.13, "High school graduate":1.54, "Some college":1.76, "Bachelor's degree":2.43, "Graduate degree":3.07}
degrees = list(lifetime_earning_by_educational_background.keys())
earning = list(lifetime_earning_by_educational_background.values())
x = np.array(degrees)
y = np.array(earning)

plt.barh(x, y)
plt.show()