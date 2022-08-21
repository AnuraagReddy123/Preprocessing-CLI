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
    print(', '.join(df.columns))
    print()

    # Ask for target variable
    target = ''

    while True:
        target = input('Which is the target variable (-1 to exit): ')
        if target != '-1':
            if target not in df.columns:
                print('Enter a column name from the list of columns')
            break
        else:
            exit()

    print()

    print('Tasks (Preprocessing)')
    print()
    print('1. Data Description')
    print('2. Handling NULL values')
    print('3. Encoding Categorical Data')
    print('4. Feature scaling of the dataset')
    print('5. Download the modified dataset')
    print()

    resp = 0
    while True:
        try:
            resp = int(input('What do you want to do? (-1 to exit): '))
            assert resp in [-1, 1, 2, 3, 4, 5]
            break
        except:
            print('Enter a valid digit from the above')

    if resp == -1:
        exit()

