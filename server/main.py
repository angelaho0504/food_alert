from flask import Flask, jsonify
import pickle
from os.path import abspath, dirname, join

here = dirname(abspath(__file__))
app = Flask(__name__)

with open(join(here, 'data.pkl'), 'rb') as f:
    id_report_mapping,  word_report_ids_mapping = pickle.load(f)


@app.route('/food/<food_name>')
def get_food_info(food_name):
    if food_name in word_report_ids_mapping:
        ids = word_report_ids_mapping[food_name]
        num_of_report = len(ids)
        report_classes = []
        for i in ids:
            report_classes.append(id_report_mapping[i]['classification'])
        num_class_1 = report_classes.count('Class I')
        num_class_2 = report_classes.count('Class II')
        num_class_3 = report_classes.count('Class III')

        return jsonify({
            'num_of_report': num_of_report,
            'overall_score': '5',
            'food_name': food_name,
            'num_class_1': num_class_1,
            'num_class_2': num_class_2,
            'num_class_3': num_class_3,
        })
    else:
        return jsonify({
            'food_name': food_name
        })
