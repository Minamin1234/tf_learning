import os
import numpy as np
import argparse
import random
import math
import tqdm

def generate_data():
    _p1 = random.uniform(1.0, 50.0)
    _p2 = random.uniform(0.5, 10.0)
    _p3 = random.uniform(1.0, 2.0)
    _p4 = random.uniform(10.0, random.uniform(20.0, 100.0))
    _p5 = random.uniform(0.0, 1.0)
    _p6 = random.uniform(32.0, 512.0)
    _value = ((_p1 + _p2) / (_p3 * _p4)) + (_p5 * math.log2(_p6))
    _datas = [
        _p1, _p2, _p3, _p4, _p5, _p6
    ]
    return _datas, _value

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--out_path", help="出力先フォルダパス", default="../train/train_data")
    argp.add_argument("--datas", help="生成個数", default=50000)
    argp.add_argument("--name", help="ファイル名", default="train_data")
    args = argp.parse_args()
    OUT = args.out_path
    DATAS = int(args.datas)
    NAME_FILE = "train_data"
    _datas = []
    _values = []
    for i in tqdm.tqdm(range(DATAS)):
        _data, _data_value = generate_data()
        _datas.append(_data)
        _values.append(_data_value)
        pass
    _datas = np.array(_datas)
    np.savez_compressed(os.path.join(OUT, f"{NAME_FILE}.npz"),
                        features=_datas,
                        values=_values)
    pass