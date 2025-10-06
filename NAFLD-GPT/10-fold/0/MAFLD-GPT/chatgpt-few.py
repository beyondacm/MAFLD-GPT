import openai
import os
import json
import time
import random

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

keys = [# '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'
        # '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', \
        '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', \
        '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', \
        # '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', \
        # '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', \
        # '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', \
        # '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', \
        # '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'
        ]

# openai.api_key  = "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"
# openai.api_key  = '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'
openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create( \
            model = model, \
            messages=messages, \
            temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

start_index = 600 
end_index = 700 
tgt_dir = './16-features-10shot/'
eval_results = {} 
with open('./data/data_of_prompt.txt', 'r') as fin:
    for i, line in enumerate(fin):
        if i >= start_index and  i < end_index:
            patient_line = line.strip()
            patient_info, patient_result = patient_line.split('\t')
            # print(patient_info)
            # print(patient_result)

            text = patient_info
            
            messages = [\
            {'role':'system', 'content':'I want you to act as AI fatty liver disease classifier. I will provide you with detailed information of a patient, including medical measurements represented as ``feature:value`` pairs. Your task is to analyze the detailed information and determine whether the patient has fatty liver disease or not. You should only output yes or no.'},\
            # Case 1
            {'role':'user', 'content':'The patient was male, 57 years old, diastolic_blood_pressure:72mmHg,waist circumference:85cm,body weight index:24.94kg/m2,γ-glutamyltransferase:17U/L,Direct bilirubin:5μmol/L,Indirect bilirubin:10μmol/L,Serum uric acid:360umol/L,triglyceride:0.62mmol/L,HDL cholesterol:1.23mmol/L,LDL cholesterol:1.94mmol/L,Fasting plasma glucose:4.86mmol/L,hemoglobin:164g/L,platelet count:137*109/L,serum HbA1c:6.8%.'}, \
            {'role':'assistant', 'content':'Yes'},\
            # Case 2
            {'role':'user', 'content':'The patient was male, 47 years old, diastolic_blood_pressure:90mmHg,waist circumference:86cm,body weight index:25.05kg/m2,γ-glutamyltransferase:421U/L,Direct bilirubin:5μmol/L,Indirect bilirubin:10μmol/L,Serum uric acid:377umol/L,triglyceride:2.21mmol/L,HDL cholesterol:1.35mmol/L,LDL cholesterol:2.26mmol/L,Fasting plasma glucose:5.62mmol/L,hemoglobin:176g/L,platelet count:312*109/L,serum HbA1c:6.5%.'}, \
            {'role':'assistant', 'content':'No'},\
            # Case 3
            {'role':'user', 'content':'The patient was female, 46 years old, diastolic_blood_pressure:104mmHg,waist circumference:76cm,body weight index:24.02kg/m2,γ-glutamyltransferase:16U/L,Direct bilirubin:3μmol/L,Indirect bilirubin:8μmol/L,Serum uric acid:271umol/L,triglyceride:1.01mmol/L,HDL cholesterol:1.74mmol/L,LDL cholesterol:1.87mmol/L,Fasting plasma glucose:4.66mmol/L,hemoglobin:151g/L,platelet count:206*109/L,serum HbA1c:6.5%.'},\
            {'role':'assistant', 'content':'Yes'},\
            # Case 4
            {'role':'user', 'content':'The patient was female, 67 years old, diastolic_blood_pressure:83mmHg,waist circumference:100cm,body weight index:29.17kg/m2,γ-glutamyltransferase:23U/L,Direct bilirubin:3μmol/L,Indirect bilirubin:7μmol/L,Serum uric acid:436umol/L,triglyceride:1.06mmol/L,HDL cholesterol:1.57mmol/L,LDL cholesterol:2.36mmol/L,Fasting plasma glucose:4.85mmol/L,hemoglobin:135g/L,platelet count:184*109/L,serum HbA1c:7.0%.'},\
            {'role':'assistant', 'content':'No'},\
            # Case 5
            {'role':'user', 'content':'The patient was male, 39 years old, diastolic_blood_pressure:85mmHg,waist circumference:85cm,body weight index:24.43kg/m2,γ-glutamyltransferase:21U/L,Direct bilirubin:5μmol/L,Indirect bilirubin:12μmol/L,Serum uric acid:312umol/L,triglyceride:2.0mmol/L,HDL cholesterol:1.23mmol/L,LDL cholesterol:3.93mmol/L,Fasting plasma glucose:5.12mmol/L,hemoglobin:162g/L,platelet count:284*109/L,serum HbA1c:6.6%.'},\
            {'role':'assistant', 'content':'Yes'},\
            # Case 6:
            {'role':'user', 'content':'The patient was female, 56 years old, diastolic_blood_pressure:75mmHg,waist circumference:78cm,body weight index:22.09kg/m2,γ-glutamyltransferase:19U/L,Direct bilirubin:2μmol/L,Indirect bilirubin:6μmol/L,Serum uric acid:199umol/L,triglyceride:1.21mmol/L,HDL cholesterol:1.31mmol/L,LDL cholesterol:3.02mmol/L,Fasting plasma glucose:4.85mmol/L,hemoglobin:147g/L,platelet count:268*109/L,serum HbA1c:7.1%.'},\
            {'role':'assistant', 'content':'No'},\
            # Case 7:
            {'role':'user', 'content':'The patient was male, 62 years old, diastolic_blood_pressure:96mmHg,waist circumference:88cm,body weight index:26.64kg/m2,γ-glutamyltransferase:59U/L,Direct bilirubin:5μmol/L,Indirect bilirubin:12μmol/L,Serum uric acid:432umol/L,triglyceride:1.94mmol/L,HDL cholesterol:1.43mmol/L,LDL cholesterol:3.45mmol/L,Fasting plasma glucose:4.82mmol/L,hemoglobin:144g/L,platelet count:328*109/L,serum HbA1c:8.2%.'},\
            {'role':'assistant', 'content':'Yes'}, \
            # Case 8:
            {'role':'user', 'content':'The patient was male, 45 years old, diastolic_blood_pressure:72mmHg,waist circumference:70cm,body weight index:18.61kg/m2,γ-glutamyltransferase:22U/L,Direct bilirubin:4μmol/L,Indirect bilirubin:9μmol/L,Serum uric acid:408umol/L,triglyceride:1.03mmol/L,HDL cholesterol:1.93mmol/L,LDL cholesterol:3.2mmol/L,Fasting plasma glucose:4.96mmol/L,hemoglobin:158g/L,platelet count:268*109/L,serum HbA1c:6.5%.'},\
            {'role':'assistant', 'content':'No'}, \
            # Case 9:
            {'role':'user', 'content':'The patient was male, 51 years old, diastolic_blood_pressure:91mmHg,waist circumference:91cm,body weight index:25.07kg/m2,γ-glutamyltransferase:15U/L,Direct bilirubin:5μmol/L,Indirect bilirubin:11μmol/L,Serum uric acid:245umol/L,triglyceride:0.67mmol/L,HDL cholesterol:1.19mmol/L,LDL cholesterol:2.65mmol/L,Fasting plasma glucose:4.98mmol/L,hemoglobin:152g/L,platelet count:161*109/L,serum HbA1c:7.0%.'},\
            {'role':'assistant', 'content':'Yes'},\
            # Case 10:
            {'role':'user', 'content':'The patient was female, 49 years old, diastolic_blood_pressure:68mmHg,waist circumference:77cm,body weight index:22.91kg/m2,γ-glutamyltransferase:14U/L,Direct bilirubin:3μmol/L,Indirect bilirubin:8μmol/L,Serum uric acid:211umol/L,triglyceride:1.38mmol/L,HDL cholesterol:1.27mmol/L,LDL cholesterol:2.89mmol/L,Fasting plasma glucose:4.32mmol/L,hemoglobin:119g/L,platelet count:240*109/L,serum HbA1c:6.6%.'},\
            {'role':'assistant', 'content':'No'}
            ]

            messages.append({'role':'user', 'content':text})
            # print(i)
            # print(messages)
            try:
                response = get_completion_from_messages(messages, temperature=0)
                # print(i, prompt)
                # response = get_completion(prompt)
                print("predicted:", response)
                print("ground truth:", patient_result)
                key = i
                eval_values = {}
                eval_values['patient_line'] = line
                eval_values['predicted_result'] = response
                if "no" in patient_result.lower():
                    eval_values['gt_result'] = "no" 
                else:
                    eval_values['gt_result'] = "yes" 
                eval_results[key] = eval_values
            except:
                # openai.api_key  = random.choice(keys) 
                openai.api_key = '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'
                time.sleep(7)

            # if i > 100:
            #     break

with open(tgt_dir + 'chatgpt_' + str(start_index) + '_' + str(end_index)  + '.json', 'w') as fp:
    json.dump(eval_results, fp)

# print(prompt)
# response = get_completion(prompt)
# print(response)
