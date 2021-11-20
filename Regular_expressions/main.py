# читаем адресную книгу в формате CSV в список contacts_list
import pandas as pd

data = pd.read_csv('phonebook_raw.csv')
print(data)

