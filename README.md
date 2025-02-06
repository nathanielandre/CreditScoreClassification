# Credit Score Classification
### This project aims to develop a machine learning model to categorize individuals into credit score brackets (Good, Standard, Poor), enhancing the loan approval process and improving risk assessment. The model utilizes various classification techniques and provides a reliable solution for smarter lending decisions.

[View the presentation as PDF](CreditScoreClassification.pdf)


## Dataset Source
```
The dataset is taken from kaggle.

Credit score classification
by ROHAN PARIS
```
<a href="https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data?select=train.csv">DATASET LINK</a>

## BACKGORUND
Assumed role :
Data Scientist working at Global Finance Company.

## Assumed background :
The management wants to create an intelligent system to categorize individuals into credit score brackets to help the company make smarter, faster, and more profitable decisions.

## PROBLEM
The company I currently work for still relies on a manual process to assess and categorize individuals into credit score brackets. This process is time-consuming, error-prone, and inconsistent, leading to inefficient decision-making, higher operational costs, and delays in offering personalized financial products.

To solve the problem, the company's management asked me as a data scientist to create a machine learning model that could automatically categorize individuals into credit score brackets. The goal was to create a model that accurately and efficiently classifies individuals based on their creditworthiness, reducing manual effort and increasing the speed and accuracy of credit scoring. By implementing this automated solution, companies will be able to make smarter, faster, and more profitable decisions while ensuring compliance with regulatory standards and improving customer satisfaction.

## GOALS
The goal is to develop a machine learning model that categorizes individuals into credit score brackets (Good, Standard, and Poor), helping the company make more informed lending decisions.

## JUSTIFICATION
Credit scores play a critical role in evaluating a customer's creditworthiness, allowing financial companies to assess risk, and set appropriate loan regulations. Customers with good credit scores are considered low-risk and typically receive better financial terms, while those with poor credit scores are viewed as high-risk, often facing higher interest rates or loan rejections.

Categorizing customers based on their credit scores enables lenders to make faster, data-driven decisions, improving efficiency and ensuring more personalized financial offerings. However, the traditional manual process of categorizing customers into credit score brackets is time-consuming and prone to human error and inconsistency, leading to inefficiencies and higher operational costs.

By automating this process with a machine learning model, the company can significantly enhance the accuracy, speed, and scalability of credit score classification.

<a href="https://fastercapital.com/topics/the-role-of-credit-scores-in-creditworthiness-evaluation.html">JUSTIFICATION 1</a><br><br>
<a href="https://riskseal.io/blog/what-is-alternative-credit-scoring-and-how-does-it-differ-from-the-traditional#toc-why-financial-inclusion-needs-alternative-data-beyond-the-traditional">JUSTIFICATION 2</a><br><br>
<a href="https://www.brex.com/resources/what-is-business-credit-score">JUSTIFICATION 3</a>

## USAGE
Loan Approval and Risk Assessment
The machine learning model helps the company evaluate the risk of lending to individuals by categorizing them based on their credit scores.

Interest Rates
Individuals with higher credit scores get better loan terms, while those with lower scores are seen as riskier and may face higher interest rates.

Personalized Financial Offerings
The model lets the company offer customized financial products, like loans or credit cards, with terms based on each customer's credit score. Higher scores lead to better offers, while lower scores may require higher rates or extra security.

Profitability
By categorizing customers, the company can manage its portfolio more effectively. They can focus on offering high-value services to customers with good credit, while also managing the risk associated with those who have poor credit.

## Techniques Used
- Exploratory Data Analysis (EDA): Conducted an analysis of the dataset to understand distributions, correlations, and potential issues in the data.
- Data Cleaning & Preprocessing: Cleaned missing values, handled outliers, and encoded categorical variables for use in machine learning models.
- Modeling: Evaluated six different machine learning algorithms:
    - K-Nearest Neighbors (KNN)
    - Support Vector Classifier (SVC)
    - Decision Tree
    - Random Forest
    - ADABOOST
    - XGBoost (Best Performer)
 
## Model Performance
After testing multiple models, XGBoost outperformed the others with the best accuracy and generalization capability. With fine-tuned hyperparameters, the model was optimized for higher precision and recall, achieving robust results for the task of classifying individuals into the credit score brackets (Good, Standard, Poor).
 
## DEPLOYMENT
Model deployed on Hugging face. Deployment file can be found in deployment folder.

<a href="https://huggingface.co/spaces/eldzilla/BankCreditScoreClassification">HuggingFace Link</a>
