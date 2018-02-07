
#Importing Library
import scipy.stats
import numpy as np
import statistics
import pandas as pd
import matplotlib as plt
#Importing dataset
dataset = pd.read_csv('forest5.csv')
meanloc =dataset.iloc[:, 1].values
#MEAN with numpy
meanelevation=np.mean(meanloc)
print(meanelevation)
#MEAN with statistics
meanselevation=statistics.mean(meanloc)
print(meanselevation)
#MEDIAN from numpy
medianelevation=np.median(meanloc)
print(medianelevation)
#MEDIAN from statistics
medianselevation=statistics.median(meanloc)
print(medianselevation)
#MODE with scipy
modeelevation=scipy.stats.mode(meanloc)
print(modeelevation)
#MODE with numpy
modeselevation=statistics.mode(meanloc)
print(modeselevation)
#best way to get statistics detail of individual variable
from scipy import stats
print(stats.describe(meanloc))

# creaing plots
import seaborn as sns
sns.set()
import matplotlib.pyplot as plpt
plpt.hist(meanloc)
plt.show()
