import csv
import pandas as pd
import numpy as np

with open('./data-prepared.csv', 'r') as f:
    reader = csv.reader(f)
    data_with_labels = []
    for i, line in enumerate(reader):
        # print('line[{}] = {}'.format(i, line))
        # print(i, line[-1])

        if "脂肪肝" in line[-1]:
            # print(i, line[-1], 1)
            line.append(1)
        else:
            # print(i, line[-1], 0)
            line.append(0)

        if "男" in line[1]:
            line[1] = 1
        else:
            line[1] = 0
        
        line[2] = line[2].strip('岁')
        
        # print(i, line)
        data_with_labels.append(line)

data_with_labels_df = pd.DataFrame(data_with_labels)
data_with_labels_df.replace('', np.nan, inplace=True)
print("before removing:", data_with_labels_df.shape)

# drop rows if NA num > 10
# data_with_labels_df = data_with_labels_df.dropna(thresh=28)
data_with_labels_df = data_with_labels_df.dropna()
print("after removing:", data_with_labels_df.shape)


data_with_labels_df.to_csv('data_with_labels.csv', index=False, header=False)
data_with_labels_df.to_excel("data_with_labels.xlsx", sheet_name='16features', index=False)
