import matplotlib.pyplot as plt
import numpy as np

data = {
    'Chipotle': 0.4,
    'Qdoba': 0.3,
    'Local Chain': 0.1, 
    'Taco Bell': 0.2}
restaurants, pcs = list(data.keys()), list(data.values())

y = 100 * np.array(pcs)
x = np.arange(len(y))
width = 0.4

fig, ax = plt.subplots()
ax.set_ylabel('%')
ax.set_title('Where Do Americans Get Their Burritos?', y=1.06)
ax.set_xticks(x + width/2)
ax.set_xticklabels(restaurants)
ax.set_xlim(-width/2.0, 4.0 - width)
ax.set_ylim(0, 45)

ax.bar(x, y, width)

plt.tight_layout()
plt.show()
