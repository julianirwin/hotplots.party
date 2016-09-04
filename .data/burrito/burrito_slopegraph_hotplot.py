import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    '2016': {
        'Chipotle': 0.4,
        'Qdoba': 0.3,
        'Local Chain': 0.1, 
        'Taco Bell': 0.2},
    '2003': {
        'Chipotle': 0.15,
        'Qdoba': 0.15,
        'Local Chain': 0.3, 
        'Taco Bell': 0.4}
}

df = pd.DataFrame(data).T

x = (2003, 2016)
chipotle = (0.15, 0.4)
qdoba = (0.15, 0.3)
local = (0.3, 0.1)
taco = (0.4, 0.2)

fig, ax = plt.subplots()

fig.set_dpi(200)
fig.set_size_inches(4.8, 3.3)

plotkws = {'lw': 3}

ax.plot(x, chipotle, 'o-', label='Chipotle')
ax.plot(x, qdoba, 'o-', label='Qdoba')
ax.plot(x, local, 'o-', label='Local Chain')
ax.plot(x, taco, 'o-', label='Taco Bell')

ax.set_xlabel('Year')
ax.set_xticks((2003, 2016))
ax.set_yticks((0.0, 0.1, 0.2, 0.3, 0.4))
ax.set_xlim((2001, 2026))
ax.set_ylim((0.0, 0.45))
ax.set_title('American Burrito Sources\n Now and Then', fontsize=12)

ax.legend(loc='center right', fontsize=9)

plt.tight_layout()
plt.savefig('/Users/jji/Desktop/out.png')
# plt.show()
