import seaborn as sns
import pandas as pd

dataSet = pd.read_csv('pinguins.csv', sep=';', decimal=',')

dataSet = dataSet.dropna()

especies = {"Pinguim-de-adélia": 1,
            "Pinguim-gentoo": 2,
            "Pinguim-de-barbicha": 3}

ilhas = {"Torgersen": 1,
         "Biscoe": 2,
         "Dream": 3}

sexo = {"macho": 0,
        "fêmea": 1}

dataSet['especie'] = dataSet['especie'].map(especies)
dataSet['ilha'] = dataSet['ilha'].map(ilhas)
dataSet['sexo'] = dataSet['sexo'].map(sexo)

print(dataSet.head())
