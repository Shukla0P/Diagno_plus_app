from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact, Cirrhosis
from home import cirrhosis_pred,brain_tumor_pred,Hpred
# Create your views here.
global cirr_pred_output
def index(request):
    return render(request,'index.html')
def testcase1(request):
    return HttpResponse("theek chal ria hai \nNext line bhi ho ria hai")
def contacts(request):
    if request.method == "POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        phone1=request.POST.get('phone')
        context1=request.POST.get('context')
        contact=Contact(name=name1,email=email1,phone=phone1,context=context1,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def links(request):
    return render(request,'links.html')
def cirrhosis(request):
    return render(request,'cirrhosis.html')
def tumor(request):
    prediction=brain_tumor_pred.filepath()
    if prediction=="Glioma Tumor":
        return render(request,'btreport.html')
    elif prediction=="Meningioma Tumor":
        return render(request,'btreport2.html')
    elif prediction=="Pituitary Tumor":
        return render(request,'btreport3.html')
    else:
        return render(request,'btreport4.html') #no tumor
    
def hdisease2(request):
    if request.method=="POST":
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        CP=request.POST.get('CP')
        RBP=request.POST.get('resting_bp')
        cholesterol=request.POST.get('cholesterol')
        FBS=request.POST.get('FBS')
        Recg=request.POST.get('Recg')
        max_hr=request.POST.get('max_hr')
        angina=request.POST.get('angina')
        ST_depp=request.POST.get('STdep')
        ST_slope=request.POST.get('STslope')
        MV=request.POST.get('MV')
        thal=request.POST.get('thalassemia')
        #test=[age,sex,CP,RBP,cholesterol,FBS,Recg,max_hr,angina,ST_depp,ST_slope,MV,thal]
        #print(test)
        prediction_output=Hpred.hpred(age,sex,CP,RBP,cholesterol,FBS,Recg,max_hr,angina,ST_depp,ST_slope,MV,thal)
        if prediction_output==1:
            return render(request,'HpredYes.html')
        elif prediction_output==0:
            return render(request,'HpredNo.html')
        
def hdisease(request):
    return render(request,'heart_disease.html')
        
def cirr(request):
    if request.method == "POST":
        drug1=request.POST.get('drug')
        ascites1=request.POST.get('ascites')
        hepatomegaly1=request.POST.get('hepatomegaly')
        spiders1=request.POST.get('spiders')
        edema1=request.POST.get('edema')
        bilirubin1=request.POST.get('bilirubin')
        cholesterol1=request.POST.get('cholesterol')
        albumin1=request.POST.get('albumin')
        copper1=request.POST.get('copper')
        alk_phos1=request.POST.get('alk_phos')
        sgot1=request.POST.get('sgot')
        triglycerides1=request.POST.get('triglycerides')
        platelets1=request.POST.get('platelets')
        prothrombin1=request.POST.get('prothrombin')
        
        prediction_output=cirrhosis_pred.predict(drug1,ascites1,hepatomegaly1,spiders1,edema1,bilirubin1,cholesterol1,albumin1,copper1,
                               alk_phos1,sgot1,triglycerides1,platelets1,prothrombin1)
        if prediction_output==1:
            return render(request,'cirrhosisYes.html')
        elif prediction_output==0:
            return render(request,'cirrhosisNo.html')
def btumor(request):
    if request.method=="POST":
        img=request.FILES.get('btumor')
        print("img is : ",img)
        prediction_output=brain_tumor_pred.pred(img)
        print(prediction_output)
        