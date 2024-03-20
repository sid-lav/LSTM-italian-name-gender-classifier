"""
Configuration settings for the Name Gender Classification project
"""

# Dataset paths
DATA_DIR = "../data"
GENERATED_DIR = "../generated"

# Model parameters
EMBEDDING_DIM = 128
HIDDEN_DIM = 256
NUM_LAYERS = 2
DROPOUT = 0.3

# Training parameters
BATCH_SIZE = 64
EPOCHS = 50
LEARNING_RATE = 0.001

# Character-level parameters
MAX_NAME_LENGTH = 50
CHAR_VOCAB = "abcdefghijklmnopqrstuvwxyz\'\- "

# Dataset splits
TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1
TEST_SPLIT = 0.1

# Evaluation metrics
METRICS = [
    "accuracy",
    "precision",
    "recall",
    "f1_score"
]
