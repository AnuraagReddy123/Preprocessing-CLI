import numpy as np

def minMaxScalerColumn(data, column):
    min = np.min(data[column])
    max = np.max(data[column])
    data[column] = (data[column] - min) / (max - min)
    return data

def minMaxScaler(data):
    for column in data.columns:
        min = np.min(data[column])
        max = np.max(data[column])
        data[column] = (data[column] - min) / (max - min)
    return data

def standardScalerColumn(data, column):
    mean = np.mean(data[column])
    std = np.std(data[column])
    data[column] = (data[column] - mean) / std
    return data

def standardScaler(data):
    for column in data.columns:
        mean = np.mean(data[column])
        std = np.std(data[column])
        data[column] = (data[column] - mean) / std
    return data