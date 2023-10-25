# app/main.py
import pickle

def classify_text(text, model):
    """Classify text as spam or not."""
    prediction = model.predict([text])
    if prediction == 1:
        return "Spam"
    return "Not Spam"

if __name__ == "__main__":
    with open("../models/spam_model.pkl", "rb") as f:
        model = pickle.load(f)

    sample_text = "Congratulations! You've won a $1000 gift card!"
    print(f"Prediction for '{sample_text}': {classify_text(sample_text, model)}")
