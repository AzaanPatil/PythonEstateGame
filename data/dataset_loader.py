import pandas as pd
import pickle
from models.property import Property


def load_model(model_path='data/rent_model.pkl'):
    """
    Load the trained machine learning model.

    Args:
        model_path (str): Path to the pickled model file.

    Returns:
        The loaded model.
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model


def load_properties(path='data/House_listings_dataset.csv', model_path='data/rent_model.pkl'):
    """
    Load properties from the dataset, using ML predictions for missing rent estimates.

    Args:
        path (str): Path to the CSV dataset.
        model_path (str): Path to the trained model.

    Returns:
        list: List of Property objects.
    """
    df = pd.read_csv(path)
    model = load_model(model_path)
    properties = []

    for _, row in df.iterrows():
        # Get rent: use existing RentEstimate if available, else predict
        if pd.notna(row['RentEstimate']):
            rent = row['RentEstimate']
        else:
            # Predict using features: Price, Bedroom, Bathroom, Area
            features = [[row['Price'], row['Bedroom'], row['Bathroom'], row['Area']]]
            rent = model.predict(features)[0]

        # Scale values as per requirements
        price_scaled = int(row['Price'] // 1000)
        rent_scaled = int(rent // 10)

        properties.append(Property(
            row['City'],
            price_scaled,
            rent_scaled
        ))

    return properties