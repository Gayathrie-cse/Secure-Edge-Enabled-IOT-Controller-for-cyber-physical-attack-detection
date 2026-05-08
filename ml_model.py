import pandas as pd
from sklearn.ensemble import IsolationForest


data = pd.read_csv("dataset.csv")


features = data[["Temperature", "Vibration", "Motor_Current", 
                 "Packet_Rate", "Command_Frequency"]]


model = IsolationForest(contamination=0.1, random_state=42)
model.fit(features)


def predict_anomaly(input_data):
    prediction = model.predict([input_data])
    
    if prediction[0] == -1:
        return "Anomaly Detected"
    else:
        return "Normal"