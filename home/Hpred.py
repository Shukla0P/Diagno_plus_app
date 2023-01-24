import pickle
import numpy as np
pickled_model = pickle.load(open(r"D:\django_tutorial\hello\hmodel.pkl", 'rb'))

def hpred(age,sex,CP,RBP,cholesterol,FBS,Recg,max_hr,angina,ST_depp,ST_slope,MV,thal):
    hpred=[age,sex,CP,RBP,cholesterol,FBS,Recg,max_hr,angina,ST_depp,ST_slope,MV,thal]
    hpred=[hpred]
    hpred=np.array(hpred)
    print(hpred.shape)
    prediction=pickled_model.predict(hpred)
    print(prediction)
    return prediction
