import os
import numpy as np
import argparse
import random
import math
import glob
import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models

def predict(_model_path: str, _test_path: str, _save_path: str):
    _model: models.Model = models.load_model(_model_path)
    _test_files = glob.glob(os.path.join(_test_path, "*.npz"))
    print("--Predicts--")
    for f in _test_files:
        _test_data = np.load(f, allow_pickle=True)
        _test_features = _test_data["features"]
        _test_values = _test_data["values"]
        _preds = _model.predict(_test_features)
        _result_name = os.path.basename(f).split(".")[0] + "_result.txt"
        np.savetxt(os.path.join(_save_path, _result_name),
                   _preds)
        print(f"Data: {f}")
        for i in range(len(_test_features)):
            print(f"Params: {_test_features[i]}")
            print(f"Answer: {_test_values[i]}, Predict: {_preds[i][0]}")
            print("")
            pass
    pass

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--model_path", default="log/")
    argp.add_argument("--test_path", default="target/")
    argp.add_argument("--save_path", default="target/result/")
    args = argp.parse_args()
    MODEL = args.model_path
    TEST = args.test_path
    SAVE = args.save_path
    predict(MODEL, TEST, SAVE)
    pass