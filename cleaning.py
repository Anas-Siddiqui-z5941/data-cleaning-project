import pandas as pd

def load_dataset(file_path):
    return pd.read_csv(file_path)

def handle_missing_values(df):
    for col in df.select_dtypes(include='number'):
        df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(exclude='number'):
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def standardize_formats(df):
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(
            df['date'],
            errors='coerce'
        ).dt.strftime('%Y-%m-%d')
    return df

def fix_data_types(df):
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(
            df['age'],
            errors='coerce'
        ).fillna(0).astype(int)
    return df

def save_cleaned_data(df, output_file_path):
    df.to_csv(output_file_path, index=False)

def main():
    input_file = "data/marketing_campaign.csv"
    output_file = "data/cleaned_data.csv"

    df = load_dataset(input_file)

    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = standardize_formats(df)
    df = fix_data_types(df)

    save_cleaned_data(df, output_file)

if __name__ == "__main__":
    main()