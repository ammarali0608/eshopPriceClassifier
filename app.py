from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route("/predict",methods = ["POST"])
def predict():
    features = request.form.values()
    float_features = []


    for i in features:
        float_features.append(float(i))


    features = [np.array(float_features)]
    pred = model.predict(features)
    if pred == 1:
        return render_template('index.html', prediction_text="The Price is Best")
    else:
        return render_template('index.html', prediction_text="The website is higher than average. Think before buy")


if __name__ == '__main__':
    app.run()
