import requests
import json

def callRandomMethod():
  print('Hellow world')
  response=requests.get('https://www.random.org/integers/?num=1&min=100&max=100000&col=1&base=10&format=plain&rnd=new')
  data = {
    "body": response.text
  }
  json_data = json.dumps(data)
  print(f"Response => {json_data}")
  return json_data