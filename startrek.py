import pandas as pd

startrek = pd.read_csv ('data\TNG.csv', encoding = 'latin-1')

startrek.info()
startrek['Released'] = pd.to_datetime (startrek['Released'])

startrek.describe()
startrek.describe(include = ['object'])
startrek.info()


tng = startrek.drop(columns = ['Unnamed: 0', 'productionnumber', 'type', 'text', 'speechdescription', 'imdbID' ])
#test = startrek.drop('Unnamed: 0', axis= 1)
tng.head(2)

startrek['imdbRating'].plot()
startrek.imdbRating.describe()
startrek.plot.scatter(x = 'imdbRating', y = 'Season')
startrek.plot.scatter(x = 'imdbRating', y = 'Episode')

startrek.to_excel ('data\startrek.xlsx', sheet_name = 'Next Generation', index = False)
