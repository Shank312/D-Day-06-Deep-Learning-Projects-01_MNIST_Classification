
# Import Keras (high-level API for building and training models) from Tensorflow
from tensorflow import keras

# Define a function that compiles a given model
def compile_model(model):
    # Configure the model for training using compile()
    model.compile(
        # Optimizer: Adam (adaptive learning optimizer) with learning rate = 0.001
        optimizer = keras.optimizers.Adam(learning_rate=1e-3),

        # Loss function: sparse categorical crossentropy
        # -> Used for multi-class classification when labels are integers (not one-hot encoded)
        loss="sparse_categorical_crossentropy",

        # Metrics: Track accuracy while training/testing (for reporting only, not optimization)
        metrics = ["accuracy"]
    )

    # Return the compiled model so it can be trained
    return model