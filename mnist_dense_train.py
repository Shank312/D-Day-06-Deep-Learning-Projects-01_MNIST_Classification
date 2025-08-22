
from folders import SAVE_DIR, MODEL_PATH
from load_data import load_mnist
from preprocess import preprocess
from build_model import build_model
from compile import compile_model
from train import train_model
from evaluate import evaluate_model
from save_model import save_model
from quick_sanity_prediction import sanity_check

# 1) Load data
(X_train, Y_train), (X_test, Y_test) = load_mnist()

# 2) Preprocess 
X_train, X_test = preprocess(X_train, X_test)

# 3) Build + compile
model = build_model()
model = compile_model(model)

# 4) Train
history = train_model(model, X_train, Y_train)

# 5) Evaluate
test_loss, test_acc = evaluate_model(model, X_test, Y_test)
print(f"Test accuracy: {test_acc:.4f}, Test loss: {test_loss:.4f}")

# 6) Save
save_model(model, MODEL_PATH)

# 7) Sanity check
sanity_check(model, X_test, Y_test)