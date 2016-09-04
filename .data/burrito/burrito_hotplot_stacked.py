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
ax = df.plot.barh(stacked=True, legend=False)

f = ax.get_figure()
f.set_dpi(200)
f.set_size_inches((4.80, 3.30))
ax.set_ylim((-0.5, 2.0))

# ax.legend(loc='best', fontsize=12, bbox_to_anchor=(1.2, 0.5))
ax.legend(loc='best', fontsize=9, ncol=2)

plt.title('American Burrito Sources \nNow and Then', fontsize=16)
plt.ylabel('Year')
plt.tight_layout()
# plt.show()
plt.savefig('/Users/jji/Desktop/out.png')

