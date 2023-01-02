import pandas

def specific_column(df, col):
    print(df[col].describe())

def all_columns(df):
    print(df.describe())
    print()
    print(df.info())

def print_rows(df, num):
    print(df.head(num))