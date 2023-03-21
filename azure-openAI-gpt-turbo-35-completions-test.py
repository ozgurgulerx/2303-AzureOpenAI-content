import requests
import json
import os 


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
    'model': 'gpt-35-turbo',
    'temperature': 0.5,
    'max_tokens': 150,
    'top_p': 1,
    'frequency_penalty': 0,
    'presence_penalty': 0
}
                              
response = requests.post( endpoint + '/openai/deployments/gpt-35-turbo-ozguler/completions?api-version=2022-12-01', 
                         headers=headers, json=payload)

data = json.loads(response.text)
generated_text = data['choices'][0]['text']
print(generated_text)
