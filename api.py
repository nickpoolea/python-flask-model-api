import numpy as np
from flask import Flask, request, jsonify
import pickle
import sys
from pandas import get_dummies, json_normalize, concat

# load flask
app = Flask(__name__)

# load the model created in model.py
model = pickle.load(open('model.pkl','rb'))

def normalize_data(data):
    species = ['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish']

    input_sp = data['Species'].values[0]

    for s in species:
        if input_sp != s:
            data['Species_' + s] = 0
        else:
            data['Species' + input_sp] = 1
    
    return data

@app.route('/weight',methods=['POST'])
def predict_weght():

    # get JSON from request
    data = json_normalize(request.get_json(force=True))

    data = normalize_data(data)

    print(data, file=sys.stdout)

    species = get_dummies(data, drop_first = True)
    data = data.drop('Species', axis = 1)
    data = concat([data.iloc[:, -1], species], axis = 1)

    prediction = model.predict(np.array(data))   

    return jsonify({'estimatedWeight': prediction[0] })
    
if __name__ == '__main__':
    app.run(port=8081, debug=True)