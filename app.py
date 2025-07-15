from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Correct path to the CSV relative to app.py
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'health_data_with_anomalies.csv'))

@app.route('/')
def home():
    df = pd.read_csv(DATA_PATH)
    latest = df.iloc[-1].to_dict()
    return render_template('index.html', data=latest)

@app.route('/chart-data')
def chart_data():
    df = pd.read_csv(DATA_PATH)
    latest_records = df.tail(100)

    timestamps = latest_records['timestamp'].tolist()
    heart_rate = latest_records['heart_rate'].tolist()
    blood_oxygen = latest_records['blood_oxygen'].tolist()

    return jsonify({
        'timestamps': timestamps,
        'heart_rate': heart_rate,
        'blood_oxygen': blood_oxygen
    })

if __name__ == '__main__':
    app.run(debug=True)
