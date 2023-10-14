import pickle


model_file = 'model1.bin'

dv_file = 'dv.bin'


with open(model_file, 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print ('get_credit_probability ',float(y_pred))
