
from fastapi import FastAPI, File, UploadFile

from fastapi.responses import JSONResponse

from scripts.utils import read_image,format_image,predict_risk
app = FastAPI()


@app.get('/')
def root():

    return {'hello': 'world'}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Ensure the uploaded file is a JPEG image
#    if file.content_type != "image/jpeg":
#        return JSONResponse(status_code=400, content={"message": "Only JPEG images are supported"})

    # Read the image file
    contents = await file.read()

    image = read_image(contents)

    image = format_image(image)

    prediction = predict_risk(image,"skin_cancer_prevention/modelvgg16.h5")#model.keras

    # Return the prediction as a JSON response
    return JSONResponse(content={"prediction": float(prediction)})
