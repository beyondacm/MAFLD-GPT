import csv
import pandas as pd
import numpy as np

features = ['patient_id', 'gender', 'age', 'diastolic_blood_pressure', 'waist circumference', 'body weight index', \
            'γ-glutamyltransferase', 'Direct bilirubin', 'Indirect bilirubin', 'Serum uric acid', 'triglyceride', \
            'HDL cholesterol', 'LDL cholesterol', 'Fasting plasma glucose', 'hemoglobin', 'platelet count', \
            'serum HbA1c']
features_units = ['', '', '', 'mmHg', 'cm', 'kg/m2', \
                  'U/L', 'μmol/L', 'μmol/L', 'umol/L', 'mmol/L', \
                  'mmol/L', 'mmol/L', 'mmol/L', 'g/L', '*109/L', \
                  '%']

def is_not_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None:
        return True 
    try:
        float(element)
        return False 
    except ValueError:
        return True 

# with open('./test_data/test.clean.csv', 'r') as f, \
def generate_prompt(i): 
    src_dir = './test_data_missing/drop' + str(i) + '.csv'
    tgt_dir = './test_data_missing_prompt/drop' + str(i) + '.txt'
    with open(src_dir, 'r') as f, \
        open(tgt_dir, 'w') as fout:
        
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            # if i <= 2:
            #     continue

            feature_values =[]
            patient_id = line[0]
            feature_values.append(('patient id', patient_id))
            # print(patient_id)

            if line[1] == "0":
                patient_gender = "female"
                # f1_value = "female"
            elif line[1] == "1":
                patient_gender = "male"
                # f1_value = "male"
            feature_values.append(('patient gender', patient_gender))

            # feature 2
            patient_age = line[2].strip('岁') 
            # f2_value = line[2].strip('岁') 
            feature_values.append(('patient age', patient_age))
            
            for k in range(3, len(features)):
                if line[k].strip() == "": # or is_not_float(line[k]):
                    f_value = "unknown"
                else:
                    f_value = line[k]
                feature_values.append((features[k], f_value))
            
            # print(feature_values)
            # print(len(features))
            result = line[len(features)]
            # print(result)
            # break

            if patient_gender == 'male':
                patient_placeholder = "his "
            else:
                patient_placeholder = "her "

            prompt = "The patient was " + patient_gender + ', ' \
                     + str(patient_age) + " years old" + ", "  \
            
            for k in range(3, len(features)):
                if str(feature_values[k][1].strip()) != "unknown": 
                    prompt += feature_values[k][0] + ":" + str(feature_values[k][1]) + features_units[k] + ',' 
                else:
                    prompt += feature_values[k][0] + ":" + str(feature_values[k][1]) + ',' 
                    # pass
                # prompt +=  '<' + feature_values[k][0] + ":" + str(feature_values[k][1]) + features_units[k] + '>,' 
            prompt = prompt.strip().rstrip('>,') + '.'
            print(prompt)
            if result == "1":
                prompt = prompt + '\t' + "The patient was diagnosed as fatty liver disease."
            else:
                prompt = prompt + '\t' + "The patient was not diagnosed as fatty liver disease."
            # print(prompt)
            fout.write(prompt + '\n')

for i in range(3, 17): 
    print(i)
    generate_prompt(i) 
    # break
