import csv
import random

normal_samples = 900
attack_samples = 100

filename = "dataset.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Temperature", "Vibration", "Motor_Current", 
                     "Packet_Rate", "Command_Frequency", "Label"])
    
    for _ in range(normal_samples):
        temperature = random.uniform(40, 70)
        vibration = random.uniform(1, 5)
        motor_current = random.uniform(5, 15)
        packet_rate = random.uniform(100, 300)
        command_frequency = random.uniform(10, 25)
        
        writer.writerow([temperature, vibration, motor_current,
                         packet_rate, command_frequency, "Normal"])
        
    for _ in range(attack_samples):
        temperature = random.uniform(90, 120)
        vibration = random.uniform(8, 15)
        motor_current = random.uniform(20, 35)
        packet_rate = random.uniform(800, 1500)
        command_frequency = random.uniform(80, 150)
        
        writer.writerow([temperature, vibration, motor_current,
                         packet_rate, command_frequency, "Attack"])

print("Dataset generated successfully as dataset.csv")