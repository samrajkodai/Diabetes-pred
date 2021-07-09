import pickle

def prediction(Age,Gender_Female,Gender_Male,Polyuria_No,Polyuria_Yes,Polydipsia_No,Polydipsia_Yes,suddenweightloss_No,suddenweightloss_Yes,weakness_No,weakness_Yes,Polyphagia_No,Polyphagia_Yes,visualblurring_No,visualblurring_Yes,Itching_No,Itching_Yes,Irritability_No,Irritability_Yes,delayedhealing_No,delayedhealing_Yes,musclestiffness_No,musclestiffness_Yes):
  x=[[Age,Gender_Female,Gender_Male,Polyuria_No,Polyuria_Yes,Polydipsia_No,Polydipsia_Yes,suddenweightloss_No,suddenweightloss_Yes,weakness_No,weakness_Yes,Polyphagia_No,Polyphagia_Yes,visualblurring_No,visualblurring_Yes,Itching_No,Itching_Yes,Irritability_No,Irritability_Yes,delayedhealing_No,delayedhealing_Yes,musclestiffness_No,musclestiffness_Yes]]
  cl=pickle.load(open('classifierk.pkl','rb'))
  pred=cl.predict(x)
  if pred==1:
      return "The Result is 'Positive' You need to consider a Good Doctor Take Care Of Your Health"
  else:
      return "You Get a 'Negative' Result !!!!!! Thank You For Visiting"