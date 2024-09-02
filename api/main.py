# Data Handling
import logging
import pickle
import pandas as pd
import json
from pydantic import BaseModel

# Server

from fastapi import FastAPI


app = FastAPI()

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='sample.log')

# Initialize files
clf = pickle.load(open('model/model.pickle', 'rb'))
pre_processor = pickle.load(open('model/preprocessor.pickle', 'rb'))

class Data(BaseModel):
    Gender: list
    Age: list
    AnnualSalary: list
        
        
@app.post("/predict")
def predict(data: Data):
    try:
        # Extract data in correct order
        input = data.model_dump()

        # create the data frame
        to_predict = pd.DataFrame(input)

        # Apply preprocessing
        encoded_features = pre_processor.transform(to_predict)
        
        # Create and return prediction
        prediction = clf.predict(encoded_features)

        return json.dumps(prediction.tolist())
    
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}
