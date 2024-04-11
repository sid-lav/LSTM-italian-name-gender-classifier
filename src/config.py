"""
Configuration settings for the Name Gender Classification project

This module contains all configurable parameters for the name gender classification system.
Each parameter is documented with its purpose and default value.
"""

from typing import List

# Dataset paths
DATA_DIR: str = "../data"
"""Path to the directory containing raw datasets"""

GENERATED_DIR: str = "../generated"
"""Path to the directory containing generated datasets"""

# Model architecture parameters
EMBEDDING_DIM: int = 128
"""Dimension of character embeddings"""

HIDDEN_DIM: int = 256
"""Number of hidden units in LSTM layers"""

NUM_LAYERS: int = 2
"""Number of LSTM layers in the network"""

DROPOUT: float = 0.3
"""Dropout rate for regularization"""

# Training parameters
BATCH_SIZE: int = 64
"""Batch size for training"""

EPOCHS: int = 50
"""Number of training epochs"""

LEARNING_RATE: float = 0.001
"""Learning rate for optimizer"""

# Character-level parameters
MAX_NAME_LENGTH: int = 50
"""Maximum length of names in characters"""

CHAR_VOCAB: str = "abcdefghijklmnopqrstuvwxyz\'\- "
"""Allowed characters in names"""

# Dataset splits
TRAIN_SPLIT: float = 0.8
"""Proportion of data for training"""

VAL_SPLIT: float = 0.1
"""Proportion of data for validation"""

TEST_SPLIT: float = 0.1
"""Proportion of data for testing"""

# Evaluation metrics
METRICS: List[str] = [
    "accuracy",
    "precision",
    "recall",
    "f1_score"
]
"""List of evaluation metrics to track during training and evaluation"""
