#!/usr/bin/env python
# -*- coding:utf8 -*

import json


def load_json(filepath: str):
    """Load a JSON file.

    :param:
        filepath
            Filepath of the file to be loaded.

    """

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    A = load_json("../examples/sample.json")
    print(A)
