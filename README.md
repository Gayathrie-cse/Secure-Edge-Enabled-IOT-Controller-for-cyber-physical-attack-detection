Overview
This project presents a Secure Edge-Enabled IoT Controller designed to detect and mitigate cyber-physical attacks in real time using edge computing and anomaly detection techniques. The system continuously monitors sensor data and network activity, processes data locally at the edge, and identifies abnormal behavior such as spoofing, false data injection, replay attacks, and unauthorized access.
By integrating edge intelligence with lightweight machine learning models, the system achieves low-latency threat detection, secure communication, and reliable operation in IoT-based cyber-physical environments.

Features
>Real-time anomaly detection using edge computing
>Monitoring of sensor and network-level data
>Lightweight ML-based threat detection
>Secure communication using MQTT/HTTP with TLS
>Low-latency processing and rapid response
>Real-time dashboards and alert generation
>Detection logs and forensic reporting
>Scalable layered architecture for IoT environments

System Architecture
The system follows a layered architecture consisting of:
>Physical Layer – Sensors and actuators
>Edge Layer – Local processing using ESP32/Raspberry Pi
>Detection Module – ML/rule-based anomaly detection
>Communication Layer – MQTT/HTTP with encryption
>Cloud Layer – Data storage and monitoring
>Application Layer – Dashboard and alert system

Technologies Used
>Python
>ESP32 / Raspberry Pi
>MQTT / HTTP
>Machine Learning (Isolation Forest)
>MongoDB / Firebase
>TLS/SSL Encryption

Performance Highlights
>Detection Accuracy: 96.3%
>False Positive Rate: 2.1%–3.2%
>Detection Latency: 8–12 ms
>End-to-End Response Time: 40–75 ms
>System Uptime: 99.3%

Experimental Results
The system was tested under both normal and simulated attack conditions. Results demonstrate:
>Real-time anomaly detection
>Fast edge-based response
>Secure and stable communication
>Efficient resource utilization on edge devices

Applications
>Industrial Automation
>Smart Infrastructure
>Smart Cities
>Critical System Monitoring
>Cyber-Physical Security Systems

Future Enhancements
>Advanced deep learning-based threat detection
>Federated learning for distributed edge intelligence
>Autonomous threat response and self-healing systems
>Hybrid edge-cloud security framework

Author
>Gayathrie GV

License
>This project is developed for academic and research purposes.
