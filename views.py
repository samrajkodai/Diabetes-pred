from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request,'index.html')

def symptoms(request):
    return render(request,'symptoms.html')

def welcome(request):
    return render(request,'home.html')



def result(request):
    Age=request.GET['Age']
    Gender_Male=request.GET['Gender_Male']
    if (Gender_Male=='Male'):
        Gender_Male=1
        Gender_Female=0
    else:
        Gender_Male=0
        Gender_Female=1

    Polyuria_Yes=request.GET['Polyuria_Yes']
    if Polyuria_Yes=='Yes':
        Polyuria_Yes=1
        Polyuria_No=0
    else:
        Polyuria_Yes=0
        Polyuria_No=1

    Polydipsia_Yes=request.GET['Polydipsia_Yes']
    if Polydipsia_Yes=='Yes':
       Polydipsia_Yes=1
       Polydipsia_No=0
    else:
        Polydipsia_Yes=0
        Polydipsia_No=1

    suddenweightloss_Yes=request.GET['suddenweightloss_Yes']
    if suddenweightloss_Yes=='Yes':
        suddenweightloss_Yes=1
        suddenweightloss_No=0
    else:
        suddenweightloss_Yes=1
        suddenweightloss_No=0

    weakness_Yes=request.GET['weakness_Yes']
    if weakness_Yes=='Yes':
        weakness_Yes=1
        weakness_No=0
    else:
        weakness_Yes=1
        weakness_No=0


    Polyphagia_Yes=request.GET['Polyphagia_Yes']
    if Polyphagia_Yes=='Yes':
        Polyphagia_Yes=1
        Polyphagia_No=0
    else:
        Polyphagia_Yes=0
        Polyphagia_No=1

    visualblurring_Yes=request.GET['visualblurring_Yes']
    if visualblurring_Yes=='yes':
        visualblurring_Yes=1
        visualblurring_No=0
    else:
        visualblurring_Yes=0
        visualblurring_No=1
    
    Itching_Yes=request.GET['Itching_Yes']
    if Itching_Yes=='Yes':
        Itching_Yes=1
        Itching_No=0
    else:
        Itching_Yes=0
        Itching_No=1
        

    Irritability_Yes=request.GET['Irritability_Yes']

    if Irritability_Yes=='Yes':
        Irritability_Yes=1
        Irritability_No=0
    else:
        Irritability_Yes=0
        Irritability_No=1
        

    delayedhealing_Yes=request.GET['delayedhealing_Yes']
    if delayedhealing_Yes=='Yes':
        delayedhealing_Yes=1
        delayedhealing_No=0
    else:
         delayedhealing_Yes=0
         delayedhealing_No=1


    musclestiffness_Yes=request.GET['musclestiffness_Yes']
    if musclestiffness_Yes=='Yes':
        musclestiffness_Yes=1
        musclestiffness_No=0
    else:
        musclestiffness_Yes=0
        musclestiffness_No=1

    predict=ml_predict.prediction(Age,Gender_Female,Gender_Male,Polyuria_No,Polyuria_Yes,Polydipsia_No,Polydipsia_Yes,suddenweightloss_No,suddenweightloss_Yes,weakness_No,weakness_Yes,Polyphagia_No,Polyphagia_Yes,visualblurring_No,visualblurring_Yes,Itching_No,Itching_Yes,Irritability_No,Irritability_Yes,delayedhealing_No,delayedhealing_Yes,musclestiffness_No,musclestiffness_Yes)

    
    return render(request,'result.html',{'predict':predict})