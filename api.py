from fastapi import FastAPI
import pickle
from pydantic import BaseModel

with open('model.pickle','rb') as file:
    model = pickle.load(file)

class Data(BaseModel):
    email: str

app = FastAPI()

@app.get('/')
def greet():
    return {'msg':'Welcome'}

@app.post('/predict')
def predict(item:Data):
    y_pred = model.predict([item.email])
    return{'label' : y_pred[0]}