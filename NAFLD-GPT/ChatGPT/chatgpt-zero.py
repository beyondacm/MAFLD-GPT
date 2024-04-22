import openai
import os
import json
import time
import random

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

keys = []

openai.api_key  = "sk-XXX"


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

target_dir = './16-features-zero/'
start_index = 0 
end_index = 50
eval_results = {} 
with open('./data/data_of_prompt.txt', 'r') as fin:
    for i, line in enumerate(fin):
        if i >= start_index and  i < end_index:
            openai.api_key = random.choice(keys)
            patient_line = line.strip()
            patient_info, patient_result = patient_line.split('\t')
            # print(patient_info)
            # print(patient_result)

            text = patient_info
            prompt = f"""
            I want you to act as AI fatty liver disease classifier. I will provide you with detailed information of a patient, your task is to analysis the detailed information and determine whether the patient has fatty liver disease or not. You will be provided patient information with delimited by triple quotes. \
            \"\"\"{text}\"\"\"
            The output answer should be very strict, you should only output yes or no. Do not explain the result
            """
            try: 
                response = get_completion(prompt)
                print(i, prompt)
                print("predicted:", response)
                print("ground truth:", patient_result)
                key = i
                eval_values = {}
                eval_values['patient_line'] = line
                eval_values['predicted_result'] = response
                if "not" in patient_result:
                    eval_values['gt_result'] = "no" 
                else:
                    eval_values['gt_result'] = "yes" 
                eval_results[key] = eval_values
            except:
                time.sleep(7)

            # if i > 100:
            #     break

with open(target_dir +  'chatgpt_' + str(start_index) + '_' + str(end_index)  + '.json', 'w') as fp:
    json.dump(eval_results, fp)

# print(prompt)
# response = get_completion(prompt)
# print(response)
