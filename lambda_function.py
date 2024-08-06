import json
import joblib
import pandas as pd

model = joblib.load('/path/to/fraud_detection_model.pkl')

def lambda_handler(event, context):
    transaction_data = json.loads(event['body'])
    df = pd.DataFrame([transaction_data])
    prediction = model.predict(df)
    response = {'fraud_prediction': int(prediction[0])}
    return {'statusCode': 200, 'body': json.dumps(response)}
