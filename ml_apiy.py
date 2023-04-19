from fastapi import FastAPI
# all formats of input that our model is going to need 
from pydantic import BaseModel
# load our model
import pickle 
#
import json

app = FastAPI()

# variable we expect 
class model_input(BaseModel):
    
    age : int
    sex : object
    bmi : float
    children : int
    smoker : object
    region : object
    
     
#loading the saved model
insurance_model = pickle.load(open('insurance.sav','rb'))


@app.post('/insurance_prediction')

# create the function which use to user to post his information in url
def insurance_pred(input_parameters : model_input):
    # convert to json
    input_data = input_parameters.json()
    #convert json to dictionary
    input_dictionnary = json.loads(input_data)
    
    # convert dictionary to list
    age = input_dictionnary['age']
    sex = input_dictionnary['sex']
    bmi = input_dictionnary['bmi']
    child = input_dictionnary['children']
    smo = input_dictionnary['smoker']
    reg = input_dictionnary['region']
    
    
    input_list = [age , sex , bmi , child , smo , reg ] 
    
    prediction = insurance_model.predict([input_list])
    
    print(prediction)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    