import requests
import json
import os 

# Replace with your API key and endpoint
#subscription_key = 'fc24064d3f5746c28e7dbb49a19a2567'

subscription_key = os.environ['OPENAI_API_KEY']
endpoint = 'https://azure-ozguler-techexplorer.openai.azure.com'

# Set headers for the HTTP request
headers = {
    'Content-Type': 'application/json',
    'api-key': subscription_key
}

# Set parameters for the API call
payload = {
    'prompt': 'Once upon a time...',
    'model': 'text-davinci-003',
    'temperature': 0.5,
    'max_tokens': 150,
    'top_p': 1,
    'frequency_penalty': 0,
    'presence_penalty': 0
}
                              
response = requests.post( endpoint + '/openai/deployments/text-davinci-003-ozguler/completions?api-version=2022-12-01', 
                         headers=headers, json=payload)

data = json.loads(response.text)
generated_text = data['choices'][0]['text']
print(generated_text)
