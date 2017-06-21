import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#plotstyle
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def ecdf(data):
    """Compute x, y values for an empirical distribution function."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

# # 2. Load in the data sets
# xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
# xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
#
# # 3. Generate ECDFS
# x_high, y_high = ecdf(xa_high)
# x_low, y_low = ecdf(xa_low)
#
# # 4. Plot ECDFs
# plt.plot(x_high, y_high, marker='.', linestyle='none')
# plt.plot(x_low, y_low, marker='.', linestyle='none')
# plt.margins(0.02)
# plt.legend(('high food', 'low food'), loc='lower right')
# plt.xlabel('egg cross sectional area (sq. µm)')
# plt.ylabel('ECDF')
