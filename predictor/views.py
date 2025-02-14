from django.shortcuts import render
import pickle
import pandas as pd

# Load the trained model
try:
    with open("predictor/disease_model.pkl", "rb") as file:
        model = pickle.load(file)
    print("✅ Model Loaded Successfully")
except Exception as e:
    print("❌ Model Loading Failed:", e)

# Load dataset to verify diseases
df = pd.read_csv('predictor/dataset/disease_data.csv')  # Ensure correct path

FEATURE_NAMES = [
    "Fever", "Cough", "Fatigue", "Headache", "Sore Throat", "Runny Nose",
    "Muscle Aches", "Chest Pain", "Nausea", "Diarrhea", "Rash", "Chills",
    "Shortness of Breath", "Joint Pain", "Body Aches", "Swollen Lymph Nodes", "Vomiting"
]

def predict_disease(request):
    if request.method == 'POST':
        symptoms = {feature: int(request.POST.get(feature, 0)) for feature in FEATURE_NAMES}
        symptoms_df = pd.DataFrame([symptoms])

        print("User Symptoms Input:", symptoms_df)

        predicted_disease = model.predict(symptoms_df)[0]
        print("✅ Predicted Disease:", predicted_disease)

        # Handle unknown prediction
        if predicted_disease not in df['Disease'].values:
            predicted_disease = "Unknown Disease"

        return render(request, 'predictor/result.html', {'disease': predicted_disease})

    return render(request, 'predictor/index.html')
