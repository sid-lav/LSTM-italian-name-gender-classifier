#### Introduction (10%)

In this assignment, I will be expanding on the work I completed for assignment 2, which involved using datasets of Italian names from the years 1999 and 2014 to train a model that generates new names based on the training data. For this assignment, I will instead focus on creating a model that classifies names by gender using the same datasets.

The gender classification model will be trained on the 1999 dataset, which includes both male and female names. Once trained, the model will be used to predict the gender of names from the following 5 datasets.
###### Test sets
1. Italian names from 1999
2. Italian names from 2014
3. Generated Italian names based on the 1999 dataset
4. Generated Italian names based on the 2014 dataset
5. Given names from the United States in the year 2000

The inclusion of the 1999 Italian names dataset, on which the model is trained, will serve as a frame of reference for evaluating the model's performance. Additionally, the U.S. given names dataset from 2000 has been included to assess the model's ability to classify names from a different context.

In Italy, the law requires a child's name to match their gender, with few exceptions for unisex names like "Andrea" and "Gianmaria". Italian naming conventions also follow a pattern where names ending in "a" are typically feminine, and those ending in "o" are masculine. These norms suggest that the gender classification model should perform well on Italian name datasets. I would expect the model's accuracy may be lower for U.S. given names, as naming conventions in the United States do not follow the same strict gender-based patterns, and may contain more unisex names or less gender-specific endings. As such, I would expect the accuracy from highest to lowest to be the same as the order given above.
#### Material and methods (20%)

The gender predictor model is implemented using PyTorch and consists of an embedding layer, an LSTM layer, and a fully connected layer. The input data is preprocessed by converting gender labels to binary labels and splitting the data into training and testing sets. The model architecture includes an embedding layer to convert input character indices to dense vectors, an LSTM layer to capture sequential patterns, and a fully connected layer to map the LSTM hidden state to the output gender classes. The loss function is CrossEntropyLoss and adam is the optimizer.

The US dataset featured a list of names with the frequency and gender in separate columns. I made a small script (make_usa_dataset.py) to generate a new csv file that has each name printed its frequency number of times, with the second column being the associated gender. I made all the datasets of length 400000 as this was approximately the size of the original Italian datasets, while the US dataset was in the millions and the generated could be any length.

#### Results (40%)

After training the model on 1999 Italian names, I obtained the results shown in (Figure 1). The accuracy decreased gradually from the 1999 Italian names dataset to the U.S. given names from 2000, which is consistent with my expectations. As the datasets become more dissimilar to the training set, the model's performance declines.

To better understand the differences between the datasets, I visualised the distribution of name lengths and their frequencies for each dataset (Figure 2). I then conducted chi-squared tests to compare the distributions (Figure 3). All comparisons revealed significant differences, with p-values ranging from 3.0e-3 to 2.0e-98, except for two cases: the comparison between the real 1999 and 2014 datasets (χ2 = 0.56, p = 0.45) and the comparison between the generated 1999 and 2014 datasets (χ2 = 0.012, p = 0.91). While I expected to find differences between the real 1999 and 2014 datasets, I anticipated that the generated data would either be significantly different from all other datasets or show no difference between the generated data and its corresponding real data.

I hypothesise that the similarity between the two generated datasets, despite their dissimilarity to their equivalent real datasets, may be a quirk of the model used in assignment 2. The model might have a more substantial influence on the distribution of name lengths than the actual training data, as such I might expect to find similar distributions when generating on completely different training data.

Furthermore, I investigated the final letter of the names in each dataset. I discovered that the proportion of female names ending in "a" was much higher on average than male names ending in "o" (Figure 4). Based on this finding, I modified the model to output its accuracy in predicting male versus female names separately (Figure 5). I suspected that names terminating in "a" would be a good predictor of increased accuracy for female names. However, the results suggested the opposite, the only dataset with higher accuracy for female names was gen_1999 with a negligible difference (0.907 vs 0.902). While the other Italian datasets had 0.02-0.05 higher in accuracy for males, and the dataset for U.S. names having a massive increase (0.64 vs 0.85). After checking the predictions were not reversed, I suspect the differences could be attributed to less variance in morthology of male names.
#### Sources, Dependencies and Figures

###### Sources
1.  https://figshare.com/articles/dataset/italian_names_first_5000_xlsx/3839580
2. https://data.world/len/us-first-names-database/workspace/file?filename=SSA_Names_DB.xlsx 
###### Dependencies
- torch
- matplotlib
- pandas
- scipy
###### Figures

Figure 1 - gender classifier accuracy on all datasets

| Dataset                | accuracy |
| ---------------------- | -------- |
| Real Italian 1999      | 0.9873   |
| Real Italian 2014      | 0.9524   |
| Generated Italian 1999 | 0.9121   |
| Generated Italian 2014 | 0.8791   |
| Real USA 2000          | 0.7527   |


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
