import pickle
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {'hello': 'world'}

# @app.get('/predict')
# def predict():

#     with open('../model/**.pkl', 'rb') as file:
#         model = pickle.load(file)

#     prediction = model.predict()
#     # to do  convert prediction to skin cancer pred "cancer or no cancer risqk"

#     return {'prediction': str(prediction)}
