import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model2.bin'

dv_file = 'dv.bin'


with open(model_file, 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)


app = Flask('predictflask')

@app.route('/predictflask', methods=['POST'])
def predictflask():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'credit_getting_probability': float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

#This is a development server. install and use "gunicorn" for deployment server.
#pip install gunicorn
#gunicorn --bind 0.0.0.0:9696 predict:app