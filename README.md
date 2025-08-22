# MNIST Digit Classification with Dense Neural Network

This project implements a simple **Dense (Fully Connected) Neural Network** to classify handwritten digits from the MNIST dataset using **TensorFlow** and **Keras**.

---

## 📂 Project Structure

01_MNIST_Classification/
│
├── build_model.py # Builds the Keras Dense model
├── compile.py # Compiles the model with optimizer and loss
├── evaluate.py # Evaluates the model on test data
├── folders.py # Contains paths and folder setup
├── load_data.py # Loads the MNIST dataset
├── mnist_dense_train.py # Main training script
├── preprocess.py # Preprocesses the MNIST images
├── quick_sanity_prediction.py# Quick test predictions for sanity check
├── save_model.py # Saves trained model
├── train.py # Training loop
├── mnist_dense_model.h5 # Saved model file
└── pycache/ # Python cache files


---

## 🧠 Requirements

- Python 3.10+
- TensorFlow 2.13+
- NumPy
- Keras (comes with TensorFlow)

Install dependencies using pip:

```bash
pip install tensorflow numpy

🚀 How to Run

Clone the repository:

git clone https://github.com/Shank312/D-Day-06-Deep-Learning-Projects-01_MNIST_Classification.git
cd 01_MNIST_Classification

Run the training script:
python mnist_dense_train.py

This will:

Load and preprocess MNIST data

Build, compile, and train the Dense Neural Network

Evaluate the model on the test set

Save the trained model

Run a quick sanity check prediction


📊 Model Performance

Training Accuracy (last epoch): ~98%

Validation Accuracy: ~97.7%

Test Accuracy: ~97.4%

Sample prediction output:
Sample prediction:  [7 2 1 0 4]
True labels      :  [7 2 1 0 4]

💾 Saving the Model

Model is saved as: mnist_dense_model.h5 (HDF5 format)

Recommended for future use: Keras native .keras format


⚡ Notes

.pyc files are generated automatically and can be ignored.

For production, consider adding a .gitignore to exclude *.pyc and model files.


📖 References

TensorFlow MNIST Tutorial

Keras Dense Layer Documentation
