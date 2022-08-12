import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d1 = pd.read_excel('frequencies_atropine central.xlsx')
d2 = pd.read_excel('frequencies_atropine cmp central.xlsx')
# d1 = pd.read_excel('frequencies_atropine cmp epithelial.xlsx')
# d2 = pd.read_excel('frequencies_atropine epithelial.xlsx')

plt.hist(d1['size'], range=(0, 40), bins=20, label='Atropine Central', density=True, alpha=0.8, color='red')
plt.hist(d2['size'], range=(0, 40), bins=20, label='Atropine + CMP Central', density=True, alpha=0.8, color='green')
plt.legend(loc='upper right')
plt.show()

plt.hist(d1['size'], range=(40, 1500), bins=20, label='Atropine Central', density=True, alpha=0.8, color='red')
plt.hist(d2['size'], range=(40, 1500), bins=20, label='Atropine + CMP Central', density=True, alpha=0.8, color='green')
plt.legend(loc='upper right')
plt.show()

plt.hist(d1['size'], range=(1500, 14000), bins=10, label='Atropine Central', density=True, alpha=0.5)
plt.hist(d2['size'], range=(1500, 14000), bins=10, label='Atropine + CMP Central', density=True, alpha=0.5)
plt.legend(loc='upper right')
plt.show()

# bins = list(np.arange(0, 15000, 1000))
# counts_d1 = []
# counts_d2 = []
#
# for i in range(len(bins)):
#     for n in d1:
#         if n<bins[i+1]:
#