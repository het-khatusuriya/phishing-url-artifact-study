from flask import Flask, request, jsonify
import joblib
import pandas as pd
import sys
from pathlib import Path

# Add path to feature_extractor
sys.path.append(str(Path(__file__).parent))

from feature_extractor import extract_features

app = Flask(__name__)

# Load model
try:
    model = joblib.load('weighted_soft_voting_ensemble.joblib')
    print("✅ Model loaded successfully!")
except:
    print("❌ Model file not found! Make sure weighted_soft_voting_ensemble.joblib is in the same folder")

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/api/predict', methods=['POST'])
def predict_url():
    try:
        url = request.json.get('url')
        
        # Extract features
        features = extract_features(url)
        features_df = pd.DataFrame([features])
        
        # Predict
        prediction = model.predict(features_df)[0]
        probability = model.predict_proba(features_df)[0]
        
        result = {
            'url': url,
            'prediction': 'Phishing' if prediction == 1 else 'Legitimate',
            'confidence': float(probability[prediction] * 100)
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)