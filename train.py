
def train_model(model, X_train, Y_train):

    # Call the built-in 'fit' method of the model to start training
    return model.fit(
        X_train,                 # Training input data
        Y_train,                 # Training labels

        validation_split = 0.1,  # Use 10% of the training data as validation set (automatically split off)

        epochs=5,                # Number of times the model sees the *entire dataset*

        batch_size = 64,         # Number of samples per gradient update (mini-batch)

        verbose = 2              # Training log display mode: 0 = silent, 1 = progress bar, 2 = one line per epoch


    ) 