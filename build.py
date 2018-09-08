import json
import pickle


with open('./data/food-enforcement-0001-of-0001.json') as f:
    all_strings = f.read()
    data = json.loads(all_strings)

num_of_reports = len(data['results'])
id_report_mapping = dict(zip(range(num_of_reports), data['results']))
# generate dictonary mapping word (should be a food) to report id
word_report_ids_mapping = {}
for i, report in enumerate(data['results']):
    words = report['product_description'].lower().split(' ')
    for w in words:
        if w in word_report_ids_mapping:
            word_report_ids_mapping[w].append(i)
        else:
            word_report_ids_mapping[w] = [i]

with open('./server/data.pkl', 'wb') as out_f:
    pickle.dump([id_report_mapping,  word_report_ids_mapping], out_f)
