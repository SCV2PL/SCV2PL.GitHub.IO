import pandas as pd
from db_management import populate_table


S7DAVRDLR14D_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid=1388511953&single=true&output=csv")
populate_table(table_name="S7DAVRDLR14D", df=S7DAVRDLR14D_df)
