import requests
import json

# Replace with your API key and endpoint
subscription_key = 'fc24064d3f5746c28e7dbb49a19a2567'
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

# Call the OpenAI API using the requests library
#result_engines = requests.get(endpoint + '/v1/engines' , headers=headers)
#print(result_engines.json())
                              
response = requests.post( endpoint + '/openai/deployments/text-davinci-003-ozguler/completions?api-version=2022-12-01', headers=headers, json=payload)
#response = requests.post(endpoint + '/v1/engines/text-davinci-003/completions', headers=headers, json=payload)

#POST https://{your-resource-name}.openai.azure.com/openai/deployments/{deployment-id}/completions?api-version={api-version}

# Parse the response and print the generated text
data = json.loads(response.text)
generated_text = data['choices'][0]['text']
print(generated_text)
