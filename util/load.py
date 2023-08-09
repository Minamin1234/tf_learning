import os
import numpy as np
import argparse
import random
import math
import glob

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("target_path", help="npzファイルが含まれているフォルダパス")
    args = argp.parse_args()
    TARGET = args.target_path
    files = glob.glob(os.path.join(TARGET, "*.npz"))
    for f in files:
        _data = np.load(f, allow_pickle=True)
        for k in _data:
            print(k)
            print(len(_data[k]))
            pass
    pass