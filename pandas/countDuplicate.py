import pandas as pd

# read the csv file as dataframe
df = pd.read_csv(r'D:\Downloads\chrome\shopee\new_contacts.csv')

data = (
    df.groupby(df.columns.tolist())
    .size()
    .rename("count")
    .to_frame().reset_index()
)

# exports the dataframe as csv file.
data.to_csv(r'D:\Downloads\chrome\shopee\sorted_contacts.csv', index=None)
