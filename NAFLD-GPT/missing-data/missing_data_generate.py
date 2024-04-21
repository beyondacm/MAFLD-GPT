import csv
import pandas as pd
import numpy as np
import random

# random.seed(42)

test_data_df = pd.read_csv('./test.clean.csv', header=None)
print(test_data_df.shape)

for i in range(3, test_data_df.shape[1]-1):
    missing_data_df = test_data_df.sample(n=100, random_state=1)
    # Replace the nth column value with the new_value
    nth_column_index = i
    missing_data_df.iloc[:, nth_column_index] = "unknown" 
    print(missing_data_df.shape)
    print(missing_data_df)
    missing_data_df.to_csv('./test_data_missing/drop' + str(nth_column_index) + '.csv', header=False, index=False) 

nomissing_data_df = test_data_df.sample(n=100, random_state=13)
nomissing_data_df.to_csv('./test_data_missing/nomissing_data.csv', header=False, index=False) 

