from django.shortcuts import render
import tensorflow as tf
import numpy as np

# Create your views here.


def index(request):
    return render(request, 'index.html')


def model(data):
    model = tf.keras.models.load_model("regression/models/predict.keras")
    prediction = model.predict(data)
    return prediction

def predict(request):
    if(request.method == 'POST'):
        test_features = [int(request.POST.get(x)) for x in list(request.POST.keys())[1:]]
        prediction = model(np.array([test_features]))
    return render(request, 'index.html', {'prediction': prediction[0,0]})
