import pandas as pd
import numpy as np

def generate_random_data(num_samples=100):
  """
  Generates a sample dataset with symptoms and diseases.

  Args:
    num_samples: The number of samples to generate.

  Returns:
    pandas.DataFrame: A DataFrame containing the generated data.
  """

  data = []
  symptoms = ['Fever', 'Cough', 'Fatigue', 'Headache', 'Sore Throat', 'Runny Nose', 
              'Muscle Aches', 'Chest Pain', 'Nausea', 'Diarrhea', 'Rash', 'Chills', 
              'Shortness of Breath', 'Joint Pain', 'Body Aches', 'Swollen Lymph Nodes', 
              'Vomiting'] 
  diseases = ['Flu', 'Cold', 'Covid-19', 'Malaria', 'Pneumonia', 'Bronchitis', 
              'Measles', 'Arthritis', 'Influenza', 'Rubella', 'Mononucleosis', 
              'Gastroenteritis', 'COPD', 'Other', "Can't Predict"] 

  for _ in range(num_samples):
    sample = {}
    for symptom in symptoms:
      sample[symptom] = np.random.randint(0, 2)  # 0: No, 1: Yes

    # Assign a disease based on simplified rules 
    if sample['Fever'] and sample['Cough'] and sample['Fatigue']:
        sample['Disease'] = 'Flu'
    elif sample['Cough'] and sample['Runny Nose'] and sample['Sore Throat']:
        sample['Disease'] = 'Cold'
    elif sample['Fever'] and sample['Headache'] and sample['Muscle Aches']:
        sample['Disease'] = 'Flu' 
    elif sample['Fever'] and sample['Fatigue'] and sample['Diarrhea']:
        sample['Disease'] = 'Malaria' 
    elif sample['Fever'] and sample['Cough'] and sample['Chest Pain']:
        sample['Disease'] = 'Pneumonia' 
    elif sample['Cough'] and sample['Shortness of Breath']: 
        sample['Disease'] = 'Bronchitis'
    elif sample['Fever'] and sample['Rash']:
        sample['Disease'] = 'Measles'
    elif sample['Fatigue'] and sample['Joint Pain']:
        sample['Disease'] = 'Arthritis' 
    elif sample['Fever'] and sample['Chills'] and sample['Body Aches']: 
        sample['Disease'] = 'Influenza' 
    elif sample['Fever'] and sample['Rash'] and sample['Joint Pain']: 
        sample['Disease'] = 'Rubella' 
    elif sample['Fatigue'] and sample['Swollen Lymph Nodes']: 
        sample['Disease'] = 'Mononucleosis' 
    elif sample['Fever'] and sample['Diarrhea'] and sample['Vomiting']: 
        sample['Disease'] = 'Gastroenteritis' 
    elif sample['Cough'] and sample['Chest Pain'] and sample['Shortness of Breath']: 
        sample['Disease'] = 'COPD' 
    else:
        sample['Disease'] = "Can't Predict" 

    data.append(sample)

  return pd.DataFrame(data)

# Generate the dataset
df = generate_random_data(10000) 

# Print the first 5 rows
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('disease_data.csv', index=False) 


# Save the dataset to a CSV file
df.to_csv('disease_dataset.csv', index=False)
