import sys
sys.path.append('../code')

import unittest
from main import classify_text #Import this function from main.p file
import pickle

class TestSpamClassifier(unittest.TestCase):

    def test_classify_text(self):
        with open("../models/spam_model.pkl", "rb") as f:
            model = pickle.load(f)

        self.assertEqual(classify_text("You've won a prize !", model), "Spam") #It will pass text if come spam then pass
        self.assertEqual(classify_text("Hello, how are you?", model), "Not Spam")

if __name__ == "__main__":
    unittest.main()
