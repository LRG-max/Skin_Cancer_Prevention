import pickle
from fastapi import FastAPI

from tensorflow.keras.preprocessing.image import img_to_array

app = FastAPI()

@app.get('/')
def root():
    return {'hello': 'world'}

@app.get('/predict')
def predict(img):

    with open('../model/**.keras', 'rb') as file:
        model = pickle.load(file)
    img = img_to_array(img)

    img = img.reshape((-1, 224, 224, 3))
    prediction = model.predict(img)[0][0]
    # prediction = model.predict()
    # to do  convert prediction to skin cancer pred "cancer or no cancer risqk"

    return {'prediction': str(prediction)}
