import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def clean_data(df):
    print("Columns:", df.columns)

    # Convert to numeric safely
    cols = ['Price', 'Bedroom', 'Bathroom', 'Area', 'RentEstimate']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove bad rows
    df = df[df['Price'] >= 10000]

    df = df.dropna(subset=['Bedroom', 'Bathroom', 'Area', 'RentEstimate'])

    return df


def train_model():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    data_path = os.path.join(BASE_DIR, 'data', 'House_listings_dataset.csv')
    model_path = os.path.join(BASE_DIR, 'data', 'rent_model.pkl')

    df = pd.read_csv(data_path)

    df_clean = clean_data(df)

    features = ['Price', 'Bedroom', 'Bathroom', 'Area']
    target = 'RentEstimate'

    X = df_clean[features]
    y = df_clean[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Model trained. MAE: {mae:.2f}")

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")

    return model


if __name__ == "__main__":
    train_model()