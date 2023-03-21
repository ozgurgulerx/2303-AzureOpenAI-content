import requests
import json

# Replace with your API key and endpoint
subscription_key = '087d52f070f14cb584a3c55c59928902'
endpoint = 'https://openai-ozguler.openai.azure.com/'

# Set headers for the HTTP request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + subscription_key
}

# Set parameters for the API call
payload = {
    'prompt': 'What is the capital of France?',
    'model': 'text-davinci-003',
    'temperature': 0.5,
    'max_tokens': 50,
    'top_p': 1,
    'frequency_penalty': 0,
    'presence_penalty': 0
}

# Call the OpenAI API using the requests library
#response = requests.post(endpoint + '/completions', headers=headers, json=payload)
response = requests.post(endpoint + '/v1/engines/text-davinci-003/completions', headers=headers, json=payload)

# Parse the response and print the generated text
data = json.loads(response.text)
#generated_text = data['choices'][0]['text']
#print(generated_text)
print(data)