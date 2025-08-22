
import numpy as np

def preprocess(X_train, X_test):
    X_train = X_train.reshape((-1, 28*28)).astype("float32")/255.0
    X_test = X_test.reshape((-1, 28*28)).astype("float32")/255.0
    
    return X_train, X_test