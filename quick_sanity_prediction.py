
import numpy as np

def sanity_check(model, X_test, Y_test):
    probs = model.predict(X_test[:5])
    preds = probs.argmax(axis=1)
    print("Sample prediction: ", preds)
    print("True labels      : ", Y_test[:5])