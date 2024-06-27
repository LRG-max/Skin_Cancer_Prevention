import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

import cv2
from tensorflow.keras.models import load_model

from tensorflow.image import resize


def read_image(contents):

    nparr = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray
    return(image)


def format_image(image):
    image = cv2.resize(image,(224, 224))  # Resize to the expected input size of the model

    image = img_to_array(image)
    image = image.reshape((-1, 224, 224, 3))
    return image

def predict_risk(image,model_path):
    model = load_model(model_path)

    prediction = model.predict(image)[0][0]
    return prediction
