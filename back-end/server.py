# Import flask and datetime module for showing date and time
from flask import Flask, render_template, request, jsonify
import numpy as np
import requests, json
from tensorflow.keras.models import load_model
import tensorflow as tf


# Initializing flask app
app = Flask(__name__)

def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

model = tf.keras.models.load_model('model/nn2.h5',custom_objects={'f1_m': f1_m})

# Route for seeing a data
@app.route('/')
def home():
	return render_template("index.html");

@app.route('/predictFunction',methods=['POST'])
def predictFunction():

    # data = request.get_json()
    # features = data['features']

    # # jsonify(feature_name);
 
    # input_data = []
    # for feature_name in features:
    #     input_data.append(request.form[feature_name])
    # input_np = np.array([input_data])
    # prediction = model.predict(input_np)
    # output = {'input_data': input_data, 'prediction': int(prediction[0][0])}
    # return render_template('result.html', output=output)

    # data = request.get_json()
    data = request.get_json()
    feature1 = data['feature1']
    feature2 = data['feature2']
    feature3 = data['feature3']
    
    # Use the input features to make a prediction
    
    return jsonify({'prediction': prediction})
	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
