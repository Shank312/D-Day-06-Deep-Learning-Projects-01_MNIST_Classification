
from tensorflow import keras

def load_mnist():
    return keras.datasets.mnist.load_data()