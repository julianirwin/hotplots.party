import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set(style='whitegrid', font_scale=1.5)

data = {
    'Chipotle': 0.4,
    'Qdoba': 0.3,
    'Local Chain': 0.1, 
    'Taco Bell': 0.2}
restaurants, pcs = list(data.keys()), list(data.values())

y = 100 * np.array(pcs)
x = np.arange(len(y))
width = 0.4

ax = sns.barplot(restaurants, y)
        
ax.set_ylabel('%')
ax.set_title('Where Do Americans Get Their Burritos?')
ax.set_ylim(0, 45)

plt.show()
