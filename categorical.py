import pandas as pd

def getCategoricalColumns(data):
    return data.select_dtypes(include=['object']).columns

def oneHotEncoding(data, columns):
    return pd.get_dummies(data, columns=columns)
