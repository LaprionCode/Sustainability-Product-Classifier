import pickle
import os

# Load model components
base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, 'sustainability_model_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(base_path, 'sustainability_model_vectorizer.pkl'), 'rb') as f:
    vectorizer = pickle.load(f)

with open(os.path.join(base_path, 'sustainability_model_preprocessing.pkl'), 'rb') as f:
    preprocess = pickle.load(f)

# Label map (edit based on your actual classes if needed)
label_map = {
    'kemasan_boros': 'kemasan_boros',
    'produk_tidak_tahan_lama': 'produk_tidak_tahan_lama',
    'produk_awet_berkualitas': 'produk_awet_berkualitas',
    'netral': 'netral'
}

def predict_review(text: str):
    cleaned = preprocess([text])
    vec = vectorizer.transform(cleaned)

    prediction = model.predict(vec)[0]

    # Try using real probabilities if available
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(vec)[0]
        confidence = max(proba)
    else:
        # Use decision_function and apply softmax-like transformation
        raw_scores = model.decision_function(vec)
        if len(raw_scores.shape) == 1:
            confidence = 1.0  # binary case fallback
        else:
            from scipy.special import softmax
            probas = softmax(raw_scores[0])  # shape: (n_classes,)
            confidence = max(probas)

    return label_map.get(prediction, "netral"), float(confidence)

