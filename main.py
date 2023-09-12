import joblib
import pandas as pd
from fastapi import FastAPI
from schema import Input


app = FastAPI()
model = joblib.load("ml/model.pkl")
vectorizer = joblib.load("ml/vectorizer.pkl")


@app.post("/api/v1/predict")
def get_prediction(body: Input):
    test = vectorizer.transform(pd.Series(body.input))
    probability = round(model.predict_proba(test)[0][1],2)
    is_spam = True if probability > 0.3 else False
    return {"isSpam":is_spam, "spamProbability": probability}