import seaborn as sns
import pandas as pd

pinguins = sns.load_dataset('penguins')

print(pinguins.head(4))
print("--------------")
pinguins = pinguins.dropna()
print(pinguins.head(4))