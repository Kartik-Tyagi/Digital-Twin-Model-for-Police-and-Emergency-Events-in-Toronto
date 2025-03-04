import pandas as pd



file_path = "./2021 PRofile Fire incident.xlsx"
data = pd.read_excel(file_path)
print(data)

'''
Step 1: Combine Data
Step 2: Feature Separation - Categorical Features and Numerical Features
Step 3: Divide into training, validation, and test data
Step 4: Divide into data and labels
'''
