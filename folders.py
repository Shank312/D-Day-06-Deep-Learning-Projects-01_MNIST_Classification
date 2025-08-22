
import os

# Windows absolute path
SAVE_DIR = r"D:\Day 06\Deep Learning Projects\01_MNIST_Classification"

# Create the folder if it does not exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Path for saving the model file
MODEL_PATH = os.path.join(SAVE_DIR, "mnist_dense_model.h5")

print("Model will be saved at: ", MODEL_PATH)