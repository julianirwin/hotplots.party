import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set(style='whitegrid', font_scale=1.5)

df = pd.read_csv('car_crashes.csv')

vars = ('total', 'alcohol', 'speeding', 'not_distracted', 'no_previous')
ax = sns.pairplot(data=df, vars=vars)
        
# ax.set_ylabel('%')
# ax.set_title('Where Do Americans Get Their Burritos?')
# ax.set_ylim(0, 45)

plt.show()
