# 🌱 Sustainability Product Classifier

A web-based NLP application for classifying **Indonesian product reviews** based on their relevance to sustainability (aligned with [SDG 12](https://en.wikipedia.org/wiki/Sustainable_Development_Goal_12): Responsible Consumption and Production).

This app uses a machine learning model (TF-IDF + Linear SVC) to classify reviews into 4 categories:

- 🔴 **Kemasan Boros** — Excessive or wasteful packaging  
- 🟠 **Produk Tidak Tahan Lama** — Low durability / short-lived  
- 🟢 **Produk Awet & Berkualitas** — High quality and durable  
- ⚪ **Netral** — No clear sustainability concern  

---

## 📁 Project Structure

```
sustainability-app/
│
├── app.py                           # Flask server
├── model.py                         # Preprocessing, vectorizer, model loading
├── sustainability_model_model.pkl          # Trained Linear SVC model
├── sustainability_model_vectorizer.pkl     # TF-IDF vectorizer
├── sustainability_model_preprocessing.pkl  # Text cleaner/preprocessor
│
├── templates/
│   └── index.html                   # Beautiful front-end UI (custom styled)
│
└── static/
    └── (optional styles or assets)
```

---

## 🚀 Live Demo

🧪 Not deployed online yet. Run locally by following instructions below.

---

## 🔧 Installation

### ✅ Requirements

- Python 3.8+
- pip
- virtualenv (recommended)

### 🔌 Install dependencies

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/sustainability-app.git
cd sustainability-app
```

2. **Install required packages:**

```bash
pip install -r requirements.txt
```

> **Sample `requirements.txt`:**
> ```
> Flask
> scikit-learn
> scipy
> joblib
> ```

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

---

## ✨ Features

- ✍️ Input a review and get immediate classification
- 📊 Shows prediction label + animated confidence bar
- 🧠 Powered by real ML model (TF-IDF + SVC)
- 💡 Shows examples for each class
- 🌐 Beautiful frontend with full responsiveness

---

## 📚 Inside the ML Model

- Vectorizer: **TF-IDF** (`sustainability_model_vectorizer.pkl`)  
- Classifier: **Linear SVC**  
- Calibrated: ✅ Confidence simulated with softmax fallback  
- Preprocessing includes:
  - Lowercasing
  - Cleaning stopwords, punctuation, etc. (`sustainability_model_preprocessing.pkl`)

---

## 🧪 Testing

Use any of the example reviews provided on the UI, or try your own in Indonesian:

```
Barang bagus, tahan lama dan berkualitas tinggi. Recommended!
Kemasan terlalu banyak plastik, boros banget packaging nya
Produk cepat rusak, tidak awet, mengecewakan
```

---


## 📝 License

This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👤 Author

Made by **[Not me]** – feel free to connect or contribute!
