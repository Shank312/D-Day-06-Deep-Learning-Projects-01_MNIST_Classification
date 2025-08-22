
def evaluate_model(model, X_test, Y_test):
    return model.evaluate(X_test, Y_test, verbose=0)
