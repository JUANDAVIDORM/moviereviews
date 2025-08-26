import pandas as pd
import json 

# Leer el archivo CSV
df = pd.read_csv('movies_initial.csv')

#guardar el dataframe como json
df.to_json('movies.json', orient='records')

with open('movies.json', 'r') as file:
   movies = json.load(file)

for i in range(100):
   movie= movies[i]
print(movie)  # Aquí se imprime la información de la película
break 