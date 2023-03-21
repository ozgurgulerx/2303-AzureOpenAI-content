import os
import openai
import requests
openai.organization = "org-F9jpIz0OFOHLboY1melcGb6I"
openai.api_key = "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"
openai.Model.list()
headers = { 'Authorization':'Bearer ' + openai.api_key }
result = requests.get('https://api.openai.com/v1/engines' ,headers=headers)
print(result.json())








