import json 
import os
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix


with open('./16-features-missing/drop3_0_100.json') as json_file:
    result = json.load(json_file)  

# result = {}
# json_files = os.listdir('./16-features-removed/')
# for json_file in json_files:
#     print(json_file)
#     with open('./16-features-removed/' + json_file) as fin:
#         current_result = json.load(fin)
#         result.update(current_result)

print(type(result), len(result))

prediction_result = []
gt_result = []
for k, v in result.items():
    # print(k)
    # print(v)
    # print(v['predicted_result'])
    if 'yes'in v['predicted_result'].lower():
        prediction_result.append(1)
    else:
        prediction_result.append(0)

    if v['gt_result'] == 'yes':
        gt_result.append(1)
    else:
        gt_result.append(0)

print(prediction_result)
print(gt_result)

assert len(prediction_result) == len(gt_result)
print("0-50 Evaluation result:")
print("precision score:", precision_score(gt_result, prediction_result))
print("recall score:", recall_score(gt_result, prediction_result))
print("acc score:", accuracy_score(gt_result, prediction_result))
print("f1 score:", f1_score(gt_result, prediction_result))

