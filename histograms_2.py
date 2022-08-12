import pandas as pd
import numpy as np

df = pd.read_excel('frq_data.xlsx', converters={'area frequencies': list})

s1=df['area frequencies'][0]

dict = {}

for i in range(df.shape[0]):
    dict[f'key_{i}'] = df['area frequencies'][i]
print(dict)
# print(dict)
# df = pd.concat({k: pd.Series(v) for k, v in dict.items()}, axis=1)
# df.to_excel('j.xlsx')

your_dict = {
    'key1': [10, 100.1, 0.98, 1.2],
    'key2': [72.5],
    'key3': [1, 5.2, 71.2, 9, 10.11, 12.21, 65, 7]
}

print(pd.concat({k: pd.Series(v) for k, v in your_dict.items()}, axis=1))
