import pandas as pd

data_df = pd.read_csv('cities.csv')

data_df.to_html('data_raw.html')