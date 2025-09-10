# Machine Learning Project 1 - Credit Card Fraud Prediction
For this project, I developed a random forest classifier built to detect fraudulent credit card transactions. I obtained a simulated dataset from Kaggle, which I used to develop features, train and test the model. The dataset was very imbalanced with very few cases of fraud. This prompted me to use undersampling to see if I could improve the model's ability to detect cases of fraud.
### Chosen Machine Learning Method
I chose to use a random forest classifier for this project. 
### Feature Engineering
I developed several features for this project.
### Results
The results were compelling, with a precision of 0.95 and a recall of 0.73 for the original model. After performing undersampling, the model achieved a precision of 0.14 and a recall of 0.96. This means that without undersampling, the model detected less cases of fraud, but had fewer false positives. The model with undersampling however, detected a much larger proportion of fraudulent credit card transactions, but had way more false positives. 
It would be advisable to explore more machine learining alternatives, such XGBoost. This would potentially yield improved model performance. Additionally, the performance of one model over the other depends on the business needs. For instance, if it is crucial to detect as much fraud as possible, then the second model would be preferred. 