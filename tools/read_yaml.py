import os

import yaml

from config import base_url


def read_yaml(filename):
    # 获取数据文件流
    with open(base_url + os.sep + "data" + os.sep + filename,"r",encoding="utf-8") as f:

        # 遍历values
        arr = []
        # 调用方法解析 文件流
        for data in yaml.safe_load(f).values():
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    print(read_yaml("login_yaml"))
