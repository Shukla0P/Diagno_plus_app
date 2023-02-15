import pickle
import numpy as np
from django.shortcuts import render
from home import urls

pickled_model = pickle.load(open(r"/home/shukla-op/django_tutorial/hello/log_model.pkl", 'rb'))

def predict(drug1,ascites1,hepatomegaly1,spiders1,edema1,bilirubin1,cholesterol1,albumin1,copper1,
                               alk_phos1,sgot1,triglycerides1,platelets1,prothrombin1):
    predin=[drug1,ascites1,hepatomegaly1,spiders1,edema1,bilirubin1,cholesterol1,albumin1,copper1,
                               alk_phos1,sgot1,triglycerides1,platelets1,prothrombin1]
    predin=[predin]
    predin=np.array(predin)
    #print(predin.shape)
    prediction=pickled_model.predict(predin)
    print(prediction)
    
    return prediction
   
