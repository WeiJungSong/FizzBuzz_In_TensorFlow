import numpy as np
import pickle
import os
import training_data_generator as tdg
import tensorflow
import keras

from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.layers import Dropout


def main():
    # read the data from the specific folder
    train, target = tdg.read_from_file()
    train = np.array(train)
    target = to_categorical(np.array(target))

    # establish the model
    model = Sequential()
    model.add(Dense(2000, activation="relu", input_shape = (train.shape[1],)))
    model.add(Dropout(0.1))
    model.add(Dense(4, activation="softmax"))
    
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    #early_stopping_monitor = EarlyStopping(patience = 3)

    model.fit(train, target, batch_size=300, epochs = 100, verbose=1,
                validation_split=0.3)


if __name__ == '__main__':
    main()
