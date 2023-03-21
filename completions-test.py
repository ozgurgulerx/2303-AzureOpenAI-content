import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + apiKey}

data = json.dumps({ "prompt":"Once upon a time", "max_tokens":15 })
url = 'https://api.openai.com/v1/engines/davinci/completions'
result = requests.post(url,headers=headers,data=data)
 