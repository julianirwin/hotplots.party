import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('taco_bell_positivity.txt', header=0, sep='\t')

fig, ax = plt.subplots()
fig.set_dpi(200)
fig.set_size_inches((9.6, 6.6))

for i, (b, a) in enumerate(zip(data['Before'], data['After'])):
    ax.plot((i, i), (b, a), 'k-', lw=2)

ax.plot(data['Before'], 'o', c='#7570b3', label='Before', ms=15)
ax.plot(data['After'], 'o', c='#d95f02', label='After', ms=15)

ax.set_title('Effect of Dorrito Taco on \nLove for Taco Bell')
ax.set_ylabel('Favorability') 

ax.set_xlim(-1, len(data['Before']))
ax.set_ylim(0, 115)

ax.set_xticks(range(len(data['Before'])))
ax.set_xticks(range(len(data['Before'])))
ax.set_xticklabels(data['Panel Member'], rotation='vertical')

ax.legend(loc='best', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/jji/Projects/hotplots/images/mpl_dumbell_dorrito.png')
