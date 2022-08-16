from fileinput import filename
import pyfiglet
import argparse
import os
import numpy as np
import pandas as pd

join = os.path.join


def isValidFile(file):
    assert os.path.exists(join(os.getcwd(), file)) and file[-3:] == 'csv'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A tool for all your preprocessing needs!')
    parser.add_argument('--file', type=str, required=True,
                        help='Pass your csv file')
    args = parser.parse_args()

    # Check if file exists
    try:
        isValidFile(args.file)
    except:
        print("File does not exist. Enter a file with csv format")
        exit()

    print(pyfiglet.figlet_format("Dataset Preprocessing!!"))

    # Read file
    df = pd.read_csv(args.file)
    print('Columns present in the given dataset: ')
    for col in df.columns:
        print(col, end=', ')
