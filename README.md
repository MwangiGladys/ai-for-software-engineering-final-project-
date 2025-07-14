## 📊 Health Data Monitoring Dashboard (Flask + Chart.js)
## Overview
This project is a simple health monitoring dashboard built with Flask and Chart.js.
It reads health-related CSV data (heart rate, temperature, etc.) and provides:
✅ Latest health metrics
✅ Interactive charts for recent trends

## 🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript, Chart.js

Data: CSV (Simulated health data)

## 📁 Project Structure
/Ai Main project/
│
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│
├── data/
│   └── health_data_with_anomalies.csv
│
├── requirements.txt
├── .gitignore
├── README.md

## 🚀 How to Run Locally
1️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

2️⃣ Install Required Packages
pip install -r requirements.txt

3️⃣ Run the Flask App
python app/app.py

4️⃣ Access the App
Go to your browser:
http://127.0.0.1:5000/

## 🔧 Required Files
health_data_with_anomalies.csv:
CSV file containing columns like:
timestamp, heart_rate, temperature, anomaly

## requirements.txt:
flask
pandas
gunicorn

## 💡 Key Features
Displays latest health record (timestamp, heart rate, temperature, anomaly status).

Interactive Chart.js graphs for heart rate and temperature trends (last 100 records).

Clean UI styled with custom CSS.

## 🌐 Deployment (Suggested: Render.com)
Deploy on Render using:
Build Command: pip install -r requirements.txt
Start Command: gunicorn app.app:app

## 📸 Screenshot Example


## ⚖️ License
MIT License - Feel free to use, modify, and share.

