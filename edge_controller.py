import serial
import time
import random
import matplotlib.pyplot as plt
from anomaly_detection import detect_anomaly
from ml_model import predict_anomaly

print("Starting Secure Edge IoT Controller...\n")

SECURE_TOKEN = "SECURE123"
input_token = "SECURE123"

if input_token != SECURE_TOKEN:
    print("Unauthorized Access! System Stopped.")
    exit()

# Connect to ESP32
ser = serial.Serial('/dev/cu.usbserial-0001', 115200)

# Graph setup
plt.ion()
temps = []

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        print("Raw Data:", line)

        if "Temperature:" in line:
            temperature = float(line.split(":")[1])

            # 😈 ATTACK SIMULATION (random spikes)
            if random.randint(1, 10) > 7:
                print("⚠️ Simulated Attack Triggered!")
                temperature += random.uniform(10, 20)

            # Dummy values (for now)
            vibration = 1.0
            motor_current = 5.0
            packet_rate = 100
            command_frequency = 10

            # Rule-based detection
            rule_result = detect_anomaly(
                temperature,
                vibration,
                motor_current,
                packet_rate,
                command_frequency
            )

            # ML detection
            input_data = [temperature, vibration, motor_current, packet_rate, command_frequency]
            ml_result = predict_anomaly(input_data)

            # Attack classification
            attack_type = "None"
            if "Temperature" in rule_result or "Vibration" in rule_result:
                attack_type = "PHYSICAL ATTACK"
            elif "Packet" in rule_result or "Command" in rule_result:
                attack_type = "CYBER ATTACK"

            # Final decision
            if "Attack" in rule_result and ml_result == "Anomaly Detected":
                final_decision = "ATTACK CONFIRMED"
            elif "Attack" in rule_result or ml_result == "Anomaly Detected":
                final_decision = "SUSPICIOUS ACTIVITY"
            else:
                final_decision = "SYSTEM SAFE"

            print("====== EDGE IoT CONTROLLER STATUS ======")
            print(f"Temperature: {temperature:.2f} °C")
            print(f"Vibration: {vibration:.2f} mm/s")
            print(f"Motor Current: {motor_current:.2f} A")
            print(f"Packet Rate: {packet_rate:.2f} packets/sec")
            print(f"Command Frequency: {command_frequency:.2f} per min")

            print(f"Rule-Based Result: {rule_result}")
            print(f"ML-Based Result: {ml_result}")
            print(f"Attack Type: {attack_type}")
            print(f"Final Decision: {final_decision}")
            print("========================================\n")

            # 📊 GRAPH UPDATE
            temps.append(temperature)
            if len(temps) > 20:
                temps.pop(0)

            plt.clf()
            plt.plot(temps)
            plt.title("Real-Time Temperature Monitoring")
            plt.xlabel("Time")
            plt.ylabel("Temperature (°C)")
            plt.pause(0.01)

        time.sleep(0.5)

    except Exception as e:
        print("Error:", e)