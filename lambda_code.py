import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = "linear-learner-2021-11-21-04-43-37-731"
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    print(payload)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)
    pred = int(result['predictions'][0]['score'])
    predicted_label = 'Yes!! Customer is likely to purchase long-term plan' if pred == 1 else 'No. Customer is not likely to purchase long-term plan'
    
    return predicted_label
