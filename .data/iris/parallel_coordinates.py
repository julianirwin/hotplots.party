import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates

data = pandas.read_csv(r'iris.csv', sep=',')
parallel_coordinates(data, 'Name')
# plt.show()

