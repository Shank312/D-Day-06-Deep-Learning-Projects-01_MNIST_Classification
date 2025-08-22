
from tensorflow import keras
from tensorflow.keras import layers

# Function to build a simple feedforward neural network model
def build_model():
    model = keras.Sequential([                    # Sequential model: stack layers one after another
        layers.Input(shape=(784,)),               # Input layer: accepts flattened 28x28 images (784 features)
        layers.Dense(128, activation="relu"),     # Hidden layer: 128 neurons with ReLU activation
        layers.Dense(10, activation="softmax")    # Output layer: 10 classes for probabilities

    ])

    return model                                  # Return the built model