import os
import csv
import pandas as pd

def get_train_ids():
    '''
        get train_ids
    '''
    train_ids = {} 
    with open('./train_data/train.clean.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            # print(line.split())
            # print(type(line), line)
            patient_id = int(line[1][0])
            # train_ids.append(patient_id)
            train_ids[patient_id] = 1
            # break
    return train_ids 


def get_test_ids():
    '''
        get test_ids
    '''
    test_ids = {} 
    with open('./test_data/test.clean.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            # print(line.split())
            # print(type(line), line)
            patient_id = int(line[1][0])
            test_ids[patient_id] = 1
            # break
    return test_ids 

def get_removed_ids():
    '''
        get test_ids
    '''
    test_ids = {} 
    with open('./test_data/removed.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            # print(line.split())
            # print(type(line), line)
            patient_id = int(line[1][0])
            test_ids[patient_id] = 1
            # break
    return test_ids 



def get_train_excels():
    '''
    '''
    train_excels = []
    with open('./data_with_labels.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            if line[0] == 0:
                train_excels.append(line[1])
                continue
            patient_id = int(line[1][0])
            if patient_id in train_ids: 
                # print(line)
                # print(patient_id)
                train_excels.append(line[1])
            # break
    return train_excels


def get_test_excels():
    '''
    '''
    test_excels = []
    with open('./data_with_labels.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            if line[0] == 0:
                test_excels.append(line[1])
                continue
            patient_id = int(line[1][0])
            if patient_id in test_ids: 
                # print(line)
                # print(patient_id)
                test_excels.append(line[1])
            # break
    return test_excels

def get_valid_excels():
    '''
    '''
    test_excels = []
    with open('./data_with_labels.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            if line[0] == 0:
                test_excels.append(line[1])
                continue
            patient_id = int(line[1][0])
            if patient_id in valid_ids: 
                # print(line)
                # print(patient_id)
                test_excels.append(line[1])
            # break
    return test_excels



def get_removed_excels():
    '''
    '''
    test_excels = []
    with open('./data_with_labels.csv', 'r') as fin:
        reader = csv.reader(fin)
        for line in enumerate(reader):
            if line[0] == 0:
                test_excels.append(line[1])
                continue
            patient_id = int(line[1][0])
            if patient_id in removed_ids: 
                # print(line)
                # print(patient_id)
                test_excels.append(line[1])
            # break
    return test_excels



train_ids = list(get_train_ids().keys())
valid_ids = train_ids[5956:]
train_ids = train_ids[0:5956]
print(len(train_ids))
# print(train_ids)
train_excels = get_train_excels()
print(len(train_excels))
# print(train_excels)
df = pd.DataFrame(train_excels)
print(df.shape)
df.to_excel("./output_excels/train.xlsx")


valid_excels = get_valid_excels()
print(len(valid_excels))
df = pd.DataFrame(valid_excels)
print(df.shape)
df.to_excel("./output_excels/valid.xlsx")


test_ids = get_test_ids()
print(len(test_ids))
test_excels = get_test_excels()
print(len(test_excels))
# print(test_excels)
df = pd.DataFrame(test_excels)
print(df.shape)
df.to_excel("./output_excels/test.xlsx")


removed_ids =  get_removed_ids()
print(len(removed_ids))
removed_excels = get_removed_excels()
print(len(removed_excels))
df = pd.DataFrame(removed_excels)
print(df.shape)
df.to_excel("./output_excels/removed.xlsx")





