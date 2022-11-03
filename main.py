from Model.utils import DiabetesPatient
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")

@app.route("/Patient_Status",methods=["POST"])
def get_classification():
    Glucose = int(request.form.get('Glucose'))
    BloodPressure = int(request.form.get('BloodPressure'))
    SkinThickness = int(request.form.get('SkinThickness'))
    Insulin = int(request.form.get('Insulin'))
    BMI = float(request.form.get('BMI'))
    DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
    Age = int(request.form.get('Age'))

    print("Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age\n",Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)


    Obj = DiabetesPatient(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result1=Obj.get_classification_patient()
    

    return render_template("index.html",prediction=result1)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port =config.PORT_NUMBER, debug=True)
    

