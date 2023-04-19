

import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    
    'age' : 181 ,
    'sex' : 'male' , 
    'bmi' : 33.77 ,
    'children' : 1 , 
    'smoker' : 'no' ,
    'region' : 'southeast' ,

}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print (response.text )














































