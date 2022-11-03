import numpy as np
import pandas as pd
import json
import pickle
import config

class DiabetesPatient():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure =BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin =Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_model(self):
        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_dict = json.load(f)
        with open (config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)



        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_Diabetes\Model\diabetes.json","r") as f:
        #     self.json_dict = json.load(f)
        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_Diabetes\Model\Logistic_Model.pkl","rb") as f:
        #     self.model = pickle.load(f)

    def get_classification_patient(self):
        self.load_model()

        array = np.zeros(len(self.json_dict["column"]))

        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age

        print("Array is :\n",array)

        result = self.model.predict([array])[0]

        result1 = "Diabetic Patient" if result==1 else "Diabetes is absent"
        return result1
        

if __name__ == "__main__":
    Glucose                   = 87.00
    BloodPressure             =  70.000
    SkinThickness             =  35.000
    Insulin                   =  23
    BMI                       =  46.600
    DiabetesPedigreeFunction  =   0.851
    Age                       =  38.000


    

    Obj = DiabetesPatient(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result=Obj.get_classification_patient()
    

  
    
    

