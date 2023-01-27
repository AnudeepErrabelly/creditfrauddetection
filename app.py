from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
import os from pml
import app
port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("forest.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [float(x) for x in request.form.values()]  # written float at int place here
    final = [np.array(int_features)]
    prediction = model.predict(final)
    #output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if prediction == 1:
        return render_template('forest.html',pred='fraud transaction')
        #,pred = 'Your Transaction  might be a fraud one.\nProbability of  txn being fraud is {}'.format( output), bhai = "bank see u have alert"
    else:
        return render_template('forest.html',pred='Safe transaction')
    #, pred = 'Your Transaction  might be a safer one.\n Probability of fire occuring is {}'.format(output), bhai = "Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

