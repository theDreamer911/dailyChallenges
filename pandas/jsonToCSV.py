import pandas as pd
# Change to JSON file
df = pd.read_json(r'D:\Downloads\chrome\shopee\contacts.json')
df.to_csv(r'D:\Downloads\chrome\shopee\new_contacts.csv',
          index=None)  # Change to CSV file
