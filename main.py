import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
helix = pd.read_csv('D:\Slosh AI\Heat Map\helix_parameters.csv')
helix.head()
print(helix.shape)
print(helix.columns)
couple_columns = helix[['Energy','h2', 'h1']]
print(couple_columns.head())
phase_1_2 = couple_columns.groupby(['h1', 'h2']).mean()
phase_1_2.shape
phase_1_2.head(10)
#phase_1_2.pivot(index='h1', columns='h2',values='Energy').head()
plt.figure(figsize=(9,9))
#pivot_table = phase_1_2.pivot('h1', 'h2','Energy')
plt.xlabel('2', size = 15)
plt.ylabel('1', size = 15)
plt.title('Energy from Helix Phase Angles', size = 15)
#sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r');