## 🏥 AI-Powered Health Monitoring Dashboard

This is a Flask-based web application that provides a simple and intuitive Health Monitoring Dashboard.
It reads simulated health data from a CSV file and displays both the latest health metrics and an interactive chart to visualize health trends over time.

## 🚀 Features
✅ Displays the latest health metrics in real-time (from the dataset)
✅ Interactive chart of Heart Rate and Blood Oxygen (last 100 records)
✅ Clean, user-friendly UI with Chart.js visualizations
✅ Flask backend with pandas for data processing
✅ Ready for integration with AI anomaly detection

## 📁 Project Structure
├── app/
│   ├── app.py               # Main Flask application
│   ├── templates/
│   │   └── index.html        # HTML Template
│   └── static/
│       └── style.css         # CSS Stylesheet
├── data/
│   └── health_data_with_anomalies.csv  # Simulated health data
├── requirements.txt          # Required Python packages
├── .gitignore
├── README.md

## 📊 How It Works

1️⃣ Data Source
The app uses data/health_data_with_anomalies.csv. Example columns:

timestamp

heart_rate

blood_oxygen

activity_level

anomaly

2️⃣ Application Routes

| Route         | Purpose                                    |
| ------------- | ------------------------------------------ |
| `/`           | Displays latest health data in the browser |
| `/chart-data` | Returns JSON for the health metrics chart  |


🎯 Expected Outputs
1️⃣ Latest Health Data (Displayed on Home Page)
When you run the app and visit http://localhost:5000/, you'll see the latest health data from the CSV file:

## Latest Health Data
-------------------
Timestamp: 2025-07-07 23:59:00
Heart Rate: 62 bpm
Blood Oxygen: 98%
Anomaly: Normal
These are dynamically pulled from the last row of your CSV file.

2️⃣ Interactive Health Chart (Displayed Below Latest Data)
An interactive line chart is generated using Chart.js. It visualizes the last 100 records of:

Heart Rate (red line)

Blood Oxygen (blue line)

The X-axis represents timestamps.
The Y-axis shows measurement values (bpm and %).

## 📷 Example of Expected UI Output

[ Page Header: Latest Health Data ]

Timestamp: 2025-07-07 23:59:00
Heart Rate: 62 bpm
Blood Oxygen: 98%
Anomaly: Normal

[ Interactive Line Chart Showing Last 100 Records ]

## ⚙️ Run Locally
1️⃣ Clone the Repository
git clone https://github.com/YourUsername/your-repo.git
cd your-repo/app
2️⃣ Install Requirements
pip install -r ../requirements.txt

3️⃣ Run the App

python app.py

Visit: http://127.0.0.1:5000


## 🛠️ Technologies Used
Flask - Python Web Framework

pandas - Data Processing

Chart.js - Interactive Charts

HTML / CSS / JS - Frontend Design

## Screenshots
 If interested in the working of my projects you can check on the screenshot folder to see all my screenshots..



## 🔮 Future Improvements
Integrate real AI anomaly detection models

Stream live data from wearables via APIs

Host on Azure / AWS / Render / Vercel / Netlify

## 📄 License

This project is open for educational use.
Licensed under MIT or your preferred license.

