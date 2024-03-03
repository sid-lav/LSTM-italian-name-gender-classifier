# Name Gender Classification

A machine learning project that classifies names by gender using LSTM-based neural networks. The project focuses on analyzing and predicting gender from Italian and US names datasets.

## Project Overview

This project implements a deep learning model using PyTorch to classify names by gender. It includes:
- Data preprocessing pipelines for multiple datasets
- LSTM-based neural network architecture
- Comprehensive evaluation metrics and analysis
- Cross-cultural comparison of naming patterns

## Features

- Gender classification using LSTM neural networks
- Support for multiple datasets:
  - Italian names (1999 and 2014)
  - Generated Italian names
  - US names (2000)
- Statistical analysis of name patterns
- Gender-specific accuracy metrics

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── data/                 # Raw datasets
├── generated/            # Generated datasets
├── notebooks/            # Jupyter notebooks for analysis
├── src/                  # Source code
│   ├── data/            # Data processing modules
│   ├── models/          # Model implementations
│   └── utils/           # Utility functions
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Usage

1. Prepare your datasets in the `data/` directory
2. Run data preprocessing:
```bash
python src/data/process_usa_dataset.py
```
3. Train the model using the Jupyter notebook:
```bash
jupyter notebook notebooks/model.ipynb
```

## Results

The model demonstrates varying performance across different datasets:

| Dataset                | Accuracy |
| ---------------------- | -------- |
| Real Italian 1999      | 0.9873   |
| Real Italian 2014      | 0.9524   |
| Generated Italian 1999 | 0.9121   |
| Generated Italian 2014 | 0.8791   |
| Real USA 2000          | 0.7527   |

## Analysis

### Name Length Distribution

The project includes analysis of name length distributions across different datasets, showing significant differences between Italian and US naming patterns.

### Gender-Specific Patterns

Analysis of name endings reveals distinct patterns:
- Female names in Italian datasets typically end in 'a'
- Male names in Italian datasets often end in 'o'
- US names show more varied patterns with less gender-specific endings

### Gender Prediction Performance

The model shows varying performance across different genders:

| Dataset   | Female Accuracy | Male Accuracy |
| --------- | --------------- | ------------- |
| 1999      | 0.9681          | 0.9826        |
| 2014      | 0.9411          | 0.9784        |
| gen_1999  | 0.9076          | 0.9021        |
| gen_2014  | 0.8575          | 0.9045        |
| usa_names | 0.6413          | 0.8547        |

## Data Sources

1. Italian names dataset: [figshare](https://figshare.com/articles/dataset/italian_names_first_5000_xlsx/3839580)
2. US names dataset: [data.world](https://data.world/len/us-first-names-database/workspace/file?filename=SSA_Names_DB.xlsx)

## Requirements

- Python 3.8+
- PyTorch >= 2.0.0
- Matplotlib >= 3.7.0
- Pandas >= 2.0.0
- Scipy >= 1.10.0
- NumPy >= 1.24.0
- Jupyter >= 1.0.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.


Figure 2 - line plot of frequency against name length for all datasets
![[Pasted image 20240331134338.png]]

Figure 3 - chi squared results between all dataset combinations

![[Pasted image 20240331132943.png]]

Figure 4 - 3 most common ending character for each dataset

| Distribution | Gender | 1st Char | 1st %  | 2nd Char | 2nd %  | 3rd Char | 3rd %  |
| ------------ | ------ | -------- | ------ | -------- | ------ | -------- | ------ |
| 1999         | F      | a        | 88.40% | e        | 6.68%  | i        | 1.04%  |
| 1999         | M      | o        | 56.05% | e        | 17.62% | a        | 12.84% |
| 2014         | F      | a        | 80.41% | e        | 11.04% | i        | 1.76%  |
| 2014         | M      | o        | 51.27% | e        | 15.65% | a        | 9.79%  |
| 1999_output  | F      | a        | 87.07% | e        | 6.97%  | n        | 1.25%  |
| 1999_output  | M      | o        | 50.58% | e        | 15.51% | a        | 14.79% |
| 2014_output  | F      | a        | 79.42% | e        | 10.52% | i        | 1.91%  |
| 2014_output  | M      | o        | 46.80% | e        | 14.27% | a        | 10.12% |
| Usa_names    | F      | a        | 37.09% | e        | 18.36% | n        | 13.06% |
| Usa_names    | M      | n        | 34.64% | r        | 9.47%  | s        | 6.80%  |

Figure 5 - gender classifier accuracy male vs female

| Dataset   | Female accuracy | Male accuracy |
| --------- | --------------- | ------------- |
| 1999      | 0.9681          | 0.9826        |
| 2014      | 0.9411          | 0.9784        |
| gen_1999  | 0.9076          | 0.9021        |
| gen_2014  | 0.8575          | 0.9045        |
| usa_names | 0.6413          | 0.8547        |
