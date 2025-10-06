import json 
import os
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix

result = {}
with open('./eval_results.json', 'r') as fin:
    result = json.load(fin)

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

    # if v['gt_result'].lower() == 'yes':
    #     gt_result.append(1)
    # else:
    #     gt_result.append(0)
with open('./test.csv', 'r') as fin:
    for i, line in enumerate(fin):
        gt_label = int(line.strip().split(',')[-1])
        gt_result.append(gt_label)

print(prediction_result)
print(gt_result)

assert len(prediction_result) == len(gt_result)
print("Evaluation result:")
print("precision score:", precision_score(gt_result, prediction_result))
print("recall score:", recall_score(gt_result, prediction_result))
print("acc score:", accuracy_score(gt_result, prediction_result))
print("f1 score:", f1_score(gt_result, prediction_result))

with open('./MAFLD-GPT-result.txt', 'w') as fout:
    print(*prediction_result, sep=',', file=fout)

with open('./gt-result.txt', 'w') as fout:
    print(*gt_result, sep=',', file=fout)


