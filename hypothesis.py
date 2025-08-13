import pandas as pd

def s_algorithm(file_path):
    data = pd.read_csv(file_path) 
    print(data)
    attribute = data.columns[ :-1]
    column = data.columns[-1]
    hypothesis = ['?' for _ in attribute]
    for index,row in data.iterrows():
        if row[column] == 'Yes':
            for i , value in enumerate(row[attribute]):
                if hypothesis[i] == '?' or hypothesis[i] == value:
                    hypothesis[i] = value
                else:
                    hypothesis[i] = '?'
    return hypothesis

file_path = "training_data.csv"
hypothesis = s_algorithm(file_path)
print("The final hypothesis: ",hypothesis)