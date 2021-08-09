import pandas as pd
data = pd.read_excel('123.xlsx','sheet1',index_col=0)
data.to_csv('data.csv',encoding='utf-8')