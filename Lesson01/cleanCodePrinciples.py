# Clean Code Example for AI
from typing import List, Tuple


def preprocess_dataset(raw_data: List[dict],
                       target_column: str = 'label') -> Tuple[List[List[float]], List[int]]:
    """
    Preprocesses raw dataset for machine learning.

    Args:
        raw_data: List of dictionaries containing features and labels
        target_column: Name of the column containing target values

    Returns:
        Tuple of (features, labels) ready for training

    Raises:
        ValueError: If target_column not found in data
    """
    if not raw_data:
        raise ValueError("Dataset cannot be empty")

    # Validate target column exists
    if target_column not in raw_data[0]:
        raise ValueError(f"Target column '{target_column}' not found")

    features = []
    labels = []

    for sample in raw_data:
        # Extract features (all columns except target)
        feature_values = [
            value for key, value in sample.items()
            if key != target_column and isinstance(value, (int, float))
        ]

        # Skip samples with missing features
        if len(feature_values) == 0:
            continue

        features.append(feature_values)
        labels.append(sample[target_column])

    print(f"Processed {len(features)} samples with {len(features[0]) if features else 0} features")
    return features, labels


def normalize_features(features: List[List[float]]) -> List[List[float]]:
    """
    Normalizes features to [0, 1] range using min-max scaling.

    Args:
        features: List of feature vectors

    Returns:
        Normalized feature vectors
    """
    if not features:
        return features

    # Find min and max for each feature dimension
    num_features = len(features[0])
    min_vals = [float('inf')] * num_features
    max_vals = [float('-inf')] * num_features

    for feature_vector in features:
        for i, value in enumerate(feature_vector):
            min_vals[i] = min(min_vals[i], value)
            max_vals[i] = max(max_vals[i], value)

    # Normalize each feature
    normalized = []
    for feature_vector in features:
        normalized_vector = [
            (value - min_vals[i]) / (max_vals[i] - min_vals[i]) if max_vals[i] != min_vals[i] else 0
            for i, value in enumerate(feature_vector)
        ]
        normalized.append(normalized_vector)

    return normalized


# Example usage
sample_data = [
    {'age': 25, 'income': 50000, 'score': 85, 'label': 1},
    {'age': 35, 'income': 75000, 'score': 92, 'label': 0},
    {'age': 45, 'income': 60000, 'score': 78, 'label': 1},
    {'age': 30, 'income': 80000, 'score': 88, 'label': 0}
]

try:
    features, labels = preprocess_dataset(sample_data)
    normalized_features = normalize_features(features)

    print("Original features:", features[0])
    print("Normalized features:", normalized_features[0])
    print("Labels:", labels)

except ValueError as e:
    print(f"Error: {e}")