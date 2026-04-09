# Estate Empire

Estate Empire is a modular Python board game inspired by Monopoly, built with Pygame for UI rendering and a clean separation between game logic, data systems, and machine learning.

## Project Structure

- `models/` - core game entities like `Player`, `Property`, `Tile`, and `Board`
- `engine/` - game flow controllers: `GameEngine`, `TurnManager`
- `systems/` - gameplay systems such as economy, CPU decision-making, card deck, and ML model training
- `ui/` - Pygame rendering and input handling
- `data/` - dataset loader and saved ML model artifacts
- `utils/` - helper utilities like dice rolling
- `test/` - unit tests and validation code

## Features

- Turn-based board game for 2–8 players
- Property purchasing and rent mechanics
- Tax and card tiles with event handling
- CPU opponents with difficulty-based heuristics
- ML-driven rent prediction using housing dataset features
- Clean separation of UI and game logic

## Getting Started

### Prerequisites

- Python 3.10+ or newer
- `pygame`
- `pandas`
- `scikit-learn`

Install dependencies using pip:

```bash
pip install pygame pandas scikit-learn
```

### Run the game

From the project root:

```bash
python main.py
```

### Train the rent model

The ML model is trained offline and saved as `data/rent_model.pkl`.

```bash
python systems/ml_model.py
```

### Load properties from dataset

The game board loads properties from `data/House_listings_dataset.csv` using `data/dataset_loader.py`. Missing `RentEstimate` values are predicted via the saved model.

## Notes

- The game logic is intentionally kept separate from the UI layer.
- Property values are scaled before use: `price = Price // 1000`, `rent = predicted_rent // 10`.
- Use `main.py` to launch the game, and `systems/ml_model.py` for offline model training.

## License

This project is provided under the terms and conditions of the MIT License.
