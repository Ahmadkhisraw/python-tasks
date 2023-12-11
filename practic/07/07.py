import pandas as pd

def get_books_df(keyword, df):
    filtered_books = df[df['title'].str.lower().str.contains(keyword.lower())]
    return filtered_books.values.tolist()

def get_totals_df(df):
    df['total_price'] = df['quantity'] * df['price']
    return df[['isbn', 'total_price']].values.tolist()

def get_totals_with_threshold_df(df, threshold, increase_value):
    df['total_price'] = df['quantity'] * df['price']
    df.loc[df['total_price'] < threshold, 'total_price'] += increase_value
    return df[['isbn', 'total_price']].values.tolist()

if __name__ == '__main__':
    df = pd.read_csv("data.csv", sep='|', skipinitialspace=True)

    python_books_df = get_books_df('python', df)
    print("Книги с ключевым словом 'python':")
    print(python_books_df)

    totals_df = get_totals_df(df)
    print("\nОбщие суммы по книгам:")
    print(totals_df)

    threshold = 500
    increase_value = 100
    totals_with_threshold_df = get_totals_with_threshold_df(df, threshold, increase_value)
    print("\nОбщие суммы с учетом порога и увеличения:")
    print(totals_with_threshold_df)
