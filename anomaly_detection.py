def detect_anomaly(temperature, vibration, motor_current, packet_rate, command_frequency):
    
    if temperature > 85:
        return "Attack Detected - Temperature Spike"
    
    if vibration > 7:
        return "Attack Detected - Abnormal Vibration"
    
    if motor_current > 18:
        return "Attack Detected - Motor Overload"
    
    if packet_rate > 700:
        return "Attack Detected - Possible DDoS"
    
    if command_frequency > 60:
        return "Attack Detected - Command Injection"
    
    return "Normal"