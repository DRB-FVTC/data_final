import pandas as pd
import string

file_path = 'material/data/for_tokens.csv'

df = pd.read_csv(file_path)

future_tokens = df[['comfort_food_clean']]

def split_foods(row):
    foods = [food.strip() for food in row.split(',')]
    foods = [food.translate(str.maketrans('', '', string.punctuation)) for food in foods]
    return foods

split_data = future_tokens['comfort_food_clean'].apply(split_foods)

exploded_data = split_data.explode().reset_index(drop=True)

df_split = pd.DataFrame(exploded_data, columns=['comfort_food_clean'])

print(df_split.head())

df_split.to_csv('material/data/tokens.csv', index=False)