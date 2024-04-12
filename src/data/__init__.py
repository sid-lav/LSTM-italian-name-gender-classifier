"""
Data processing modules for the name gender classification project.

This package contains modules for:
- Dataset loading and preprocessing
- Data augmentation
- Feature extraction
- Data splitting
"""

from .dataset import NameDataset
from .preprocessing import preprocess_names, normalize_names
from .utils import split_dataset

__all__ = [
    "NameDataset",
    "preprocess_names",
    "normalize_names",
    "split_dataset"
]
