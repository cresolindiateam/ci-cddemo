# dummy_model.py
import pickle

class DummyModel:
    def predict(self, texts):
        return [1 if "win" in text or "gift" in text else 0 for text in texts]
        #if words "win" or "gift" are present it is "spam" (returns 1). 
        #Otherwise, it classifies it as "not spam" (returns 0).

model = DummyModel()
with open("models/spam_model.pkl", "wb") as f:
    pickle.dump(model, f)
