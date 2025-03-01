import argparse
import json
import logging
import os
import sys

import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", "-p", required=True, help="Path to the file.", type=str)
    parser.add_argument("--n_records", "-n", required=True, help="n records", type=int)
    parser.add_argument("--clazz", "-c", required=False, default=-1, help="class code", type=int)
    args = parser.parse_args()

    file_path = args.file_path  # For example 'SubtaskA/subtaskA_train_multilingual.jsonl'

    if not os.path.exists(file_path):
        logging.error("File doesnt exists: {}".format(file_path))
        raise ValueError("File doesnt exists: {}".format(file_path))

    df = pd.read_json(file_path, lines=True)
    if args.clazz >= 0:
        df = df[df["label"] == args.clazz]
    print(df.head(args.n_records).to_json())


