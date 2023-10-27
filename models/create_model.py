#pickle module is used to serialize (convert a Python object into a byte stream) 
#and deserialize (convert a byte stream back into a Python object) Python objects. Serialization is useful for saving the state of an object and later restoring it.
import pickle


class DummyModel:
    def predict(self, texts):
        return [1 if "win" in text or "gift" in text else 0 for text in texts]

model = DummyModel()
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)
