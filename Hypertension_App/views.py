from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
     if request.method == "POST":
          print("Accepting Inputs")

          age = request.POST['age']
          sex = request.POST['gender']
          chest_pain_type = request.POST['chestPainType']
          resting_blood_pressure = request.POST['bloodPressure']
          cholestoral = request.POST['cholestoral']
          rest_ecg = request.POST['restEcg']
          max_heart_rate = request.POST['MaxheartRate']
          exercise_induced_angina = request.POST['exerciseInducedAngina']

          print("Inputs Accepted")


          result = getResult(age,sex,chest_pain_type,resting_blood_pressure,cholestoral,rest_ecg,max_heart_rate,exercise_induced_angina)
          print("Return Completed")


          if result == "YES Hypertensation":  
               return render(request,'result.html')

          else:
               messages.success(request, "Dont Worry!!! You Don't have Hypertension") 
               return redirect('/index')


     else:
          return render(request,'index.html')



def result(request):
     return render(request, 'result.html')














def getResult(age,sex,chest_pain_type,resting_blood_pressure,cholestoral,rest_ecg,Max_heart_rate,exercise_induced_angina):
     print("getResult Called")
     import pandas as pd
     from sklearn.model_selection import train_test_split
     from sklearn.ensemble import RandomForestClassifier

     # Load the dataset
     print("Loading Dataset")

     data = pd.read_csv("static/csv/HeartDiseaseTrain-Test.csv")

     # Prepare the data
     X = data.drop("target", axis=1)
     y = data["target"]

     # Convert string categories to numerical values using one-hot encoding
     categorical_cols = ["sex", "chest_pain_type", "rest_ecg", "exercise_induced_angina"]
     X_encoded = pd.get_dummies(X, columns=categorical_cols)

     # Split the data into training and testing sets
     X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

     # Train the model
     print("Training Started")

     model = RandomForestClassifier()
     model.fit(X_train, y_train)

     print("Training Ended")


     # Create a DataFrame with user input
     user_input = pd.DataFrame({
     "age": [age],
     "sex": [sex],
     "chest_pain_type": [chest_pain_type],
     "resting_blood_pressure": [resting_blood_pressure],
     "cholestoral": [cholestoral],
     "rest_ecg": [rest_ecg],
     "Max_heart_rate": [Max_heart_rate],
     "exercise_induced_angina": [exercise_induced_angina]
     })

     print("Training Encoding")


     # Encode the user input using the same one-hot encoding
     user_input_encoded = pd.get_dummies(user_input, columns=categorical_cols)

     # Reindex the user input to match the encoded columns
     user_input_encoded = user_input_encoded.reindex(columns=X_encoded.columns, fill_value=0)

     # Make a prediction

     print("Predicting............")

     prediction = model.predict(user_input_encoded)

     print("Returning")

     return(prediction[0])

