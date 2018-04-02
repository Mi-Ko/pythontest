import json
import urllib.request as request


api_url="https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%20523920%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

with request.urlopen(api_url) as response:
    txt = response.read()
    js=json.loads(txt)   
    condition=js['query']['results']['channel']['item']['condition']
    
print("====================================")
print("Pogoda w Warszawie:",condition['text'],condition['temp']+"°C")
print("====================================") 