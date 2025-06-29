from flask import Flask, render_template, request, jsonify
from model import predict_review

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    label, confidence = predict_review(text)
    return jsonify({
        'label': label,
        'confidence': round(confidence * 100, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
