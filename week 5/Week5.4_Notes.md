## Serving the churn model with Flask
- To make a prediction we need to first load the previous saved model and use a prediction function in a special route.
  - To load the previous saved model we use the code below:
  - ```python
    import pickle
    
    with open('churn-model.bin', 'rb') as f_in:
      dv, model = pickle.load(f_in)
    ```
  - We had earlier to predict a value for a customer. So we need a function like below:
  - ```python
    def predict_single(customer, dv, model):
      X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
      y_pred = model.predict_proba(X)[:, 1]
      return y_pred[0]
    ```
   - At last we make the final function used for creating the web service.
   - ```python
     @app.route('/predict', methods=['POST'])  ## in order to send the customer information we need to post its data.
     def predict():
     customer = request.get_json()  ## web services work best with json frame, So after the user post its data in json format we need to access the body of json.

     prediction = predict_single(customer, dv, model)
     churn = prediction >= 0.5
     
     result = {
         'churn_probability': float(prediction), ## we need to cast numpy float type to python native float type
         'churn': bool(churn),  ## same as the line above, casting the value using bool method
     }

     return jsonify(result)  ## send back the data in json format to the user
     ```
   - Finally run the code. To see the result we can't use a simple request in web browser, because we are expecting a `POST` request in our app. We can run the code below to **post** customer data as `json` and see the response
   - ```python     
     ## a new customer informations
     customer = {
       'customerid': '8879-zkjof',
       'gender': 'female',
       'seniorcitizen': 0,
       'partner': 'no',
       'dependents': 'no',
       'tenure': 41,
       'phoneservice': 'yes',
       'multiplelines': 'no',
       'internetservice': 'dsl',
       'onlinesecurity': 'yes',
       'onlinebackup': 'no',
       'deviceprotection': 'yes',
       'techsupport': 'yes',
       'streamingtv': 'yes',
       'streamingmovies': 'yes',
       'contract': 'one_year',
       'paperlessbilling': 'yes',
       'paymentmethod': 'bank_transfer_(automatic)',
       'monthlycharges': 79.85,
       'totalcharges': 3320.75
     }
     import requests ## to use the POST method we use a library named requests
     url = 'http://localhost:9696/predict' ## this is the route we made for prediction
     response = requests.post(url, json=customer) ## post the customer information in json format
     result = response.json() ## get the server response
     print(result)
     ```
 - Until here we saw how we made a simple web server that predicts the churn value for every user. When you run your app you will see a warning that it is not a WGSI server and not suitable for production environmnets. To fix this issue and run this as a production server there are plenty of ways available. 
   - One way to create a WSGI server is to use gunicorn. To install it use the command ```pip install gunicorn```, And to run the WGSI server you can simply run it with the   command ```gunicorn --bind 0.0.0.0:9696 churn:app```. Note that in __churn:app__ the name churn is the name we set for our the file containing the code ```app = Flask('churn')```(for example: churn.py), You may need to change it to whatever you named your Flask app file.  
