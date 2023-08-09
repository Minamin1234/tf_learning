import os
import numpy as np
import argparse
import random
import math
import glob
import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models

def get_model(n):
    input = layers.Input(shape= n)
    d = layers.Dense(units=16, activation="relu")(input)
    d = layers.Dense(units=32, activation="relu")(d)
    d = layers.Dense(units=32, activation="relu")(d)
    output = layers.Dense(units=1, activation="linear")(d)

    _model = models.Model(inputs=input, outputs=output)
    _model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=5e-3),
        loss="mse"
    )
    return _model

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--train_path", default="train/train_data")
    argp.add_argument("--val_path", default="train/val_data")
    argp.add_argument("--test_path", default="train/test_data")
    argp.add_argument("--model_path", default="log/")
    args = argp.parse_args()
    TRAIN_PATH = args.train_path
    VAL_PATH = args.val_path
    TEST_PATH = args.test_path
    MODEL_PATH = args.model_path
    _train = np.load(
        glob.glob(os.path.join(TRAIN_PATH, "*.npz"))[0],
        allow_pickle=True
    )
    _val = np.load(
        glob.glob(os.path.join(VAL_PATH, "*.npz"))[0],
        allow_pickle=True
    )
    _test = np.load(
        glob.glob(os.path.join(TEST_PATH, "*npz"))[0],
        allow_pickle=True
    )

    _train_datas = _train["features"]
    _train_values = _train["values"]
    _val_datas = _val["features"]
    _val_values = _val["values"]
    _test_datas = _test["features"]
    _test_values = _test["values"]
    print(len(_train_datas))
    _model = get_model(len(_train_datas[0]))
    _model.fit(
        _train_datas, _train_values,
        validation_data=(_val_datas, _val_values),
        epochs=200,
        use_multiprocessing=True
    )
    preds = _model.predict(_test_datas)
    _model.save(MODEL_PATH)
    #print(preds)
    #print(_test_values)
    pass