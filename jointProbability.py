import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

data = pd.read_csv('data.csv',header=None,names=['x','y'])
print(data)
sns.jointplot(data).plot_joint(sns.scatterplot)
plt.show()