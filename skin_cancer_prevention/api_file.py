import io
import numpy as np
from tensorflow.keras.models import load_model
import pickle
from fastapi import FastAPI, File, UploadFile

from tensorflow.keras.preprocessing.image import img_to_array,load_img
from PIL import Image
from tensorflow.image import resize
from fastapi.responses import HTMLResponse, JSONResponse
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img

app = FastAPI()


@app.get('/')
def root():
    return {'hello': 'world'}

# @app.get('/predict')
# def predict(img):

#     with open('../model/**.keras', 'rb') as file:
#         model = pickle.load(file)
#     img = img_to_array(img)

#     img = img.reshape((-1, 224, 224, 3))
#     prediction = model.predict(img)[0][0]
#     # prediction = model.predict()
#     # to do  convert prediction to skin cancer pred "cancer or no cancer risqk"

#     return {'prediction': str(prediction)}

# @app.post("/predict/")
# async def predict(file: UploadFile = File(...)):
#     # Read the image file
#     contents = await file.read()
#     # image = Image.open(io.BytesIO(contents))
#     img = load_img(contents)

#     img = resize(img, [200,200], method='nearest')
#     img_1 = img_to_array(img_1)
#     # prediction = model.predict(image)[0][0]


#     # Preprocess the image for the model
#     image = np.array(image)
#     if image.shape[2] == 4:  # If the image has an alpha channel, remove it
#         image = image[:, :, :3]
#     # image = np.resize(image, [200,200], method='nearest')
#     # image = np.resize(image, (200,200,3))
#     image = resize(image, [200,200], method='nearest')
#     image = image/255
#     # image = np.expand_dims(image, axis=0)
#     # image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
#     image = img_to_array(image)

#     image = image.reshape((-1, 200, 200, 3))
#     # with open('skin_cancer_prevention/model.pkl', 'rb') as file:
#     #     model = pickle.load(file)
#     model = load_model("skin_cancer_prevention/model_1.keras")
#     # Perform prediction
#     prediction = model.predict(image)[0][0]
#     # decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
#     # return {'prediction': str(prediction)}

#     # # Format the predictions
#     # result = "Predictions:<br>"
#     # for i, (imagenet_id, label, score) in enumerate(prediction):
#     #     result += f"{i + 1}: {label} ({score:.4f})<br>"

#     return HTMLResponse(content=str(prediction))


#     # # Format the predictions
#     # result = "Predictions:<br>"
#     # for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
#     #     result += f"{i + 1}: {label} ({score:.4f})<br>"


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Ensure the uploaded file is a JPEG image
    if file.content_type != "image/jpeg":
        return JSONResponse(status_code=400, content={"message": "Only JPEG images are supported"})

    # Read the image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Preprocess the image for the model
    image = image.resize((224, 224))  # Resize to the expected input size of the model
    image = np.array(image)
    # if image.shape[2] == 4:  # If the image has an alpha channel, remove it
    # #     image = image[:, :, :3]
    # image = image.reshape((-1, 224, 224, 3))
    print(np.shape(image))
    image = preprocess_input(image)  # Adjust as per your model's requirements
    image = img_to_array(image)

    model = load_model("skin_cancer_prevention/model_1.keras")
        # print(np.shape(image))

    # Perform prediction
    predictions = model.predict(image)
    prediction = np.argmax(predictions[0])  # Assuming a classification model

    # Return the prediction as a JSON response
    return JSONResponse(content={"prediction": int(prediction)})
