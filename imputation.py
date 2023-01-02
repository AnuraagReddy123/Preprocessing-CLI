def removeColumns(data, columns):
    return data.drop(columns, axis=1)

def impute(data, column, method):
    if method == 'mean':
        data[column].fillna(data[column].mean(), inplace=True)
    elif method == 'median':
        data[column].fillna(data[column].median(), inplace=True)
    elif method == 'mode':
        data[column].fillna(data[column].mode()[0], inplace=True)
    else:
        print('Invalid method')
        return