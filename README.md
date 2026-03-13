# DS4420 Youth Vaping Analysis Project
## Northeastern University Spring 2026
### Professor: Dr. Eric Gerber
### Authors
- Blythe Berlinger
- Sydney Schulz

### Project Overview
The purpose of this project is to analyze youth vaping behavior in the United States, using the National Youth Tobacco Survey (NYTS) from 2021-2023. The goal is to examine how demographic characteristics and social media exposure relate to e-cigarette usage among individuals approximately 9-19 years old. 

We clean and aggregate multiple years of survey data, perform exploratory data analysis, and build machine learning models to predict e-cigarette usage. Our repository contains the data cleaning pipeline, exploratory analysis, and predictive modeling used in the project.

### Research Question
To what extent do demographic characteristics and social media exposure influence youth e-cigarette use, and can machine learning models such as bayesian logistic regression and multilayer perceptrons (MLPs) accurately predict vaping behavior?

### Dataset
The data used comes from the National Youth Tobacco Survey (NYTS). It includes 2021, 2022, and 2023 data.
Key variables include
- age
- sex
- grade
- social media usage
- social media platform
- exposure to e-cigarette related posts
- engagement with vaping-related content
- self-reported e-cigarette use 

The datasets were cleaned and standardized to create a combined dataset across all three years.

### Data Cleaning
Data cleaning involved:
- Standardizing variable names across survey years
- Selecting relevant variables
- Converting categorical responses into consistent formats
- Handling missing values (median imputation because it is robust to skewed distributions)
- Concatenating datasets across years

The final cleaned dataset is saved as: data/cleaned/nyts_2021_2023_clean.csv

### Phase 1 Model (Proof of Concept)
For Phase I, we build a baseline MLP model to predict e-cigarette use using demographic and social media exposure variables.

Steps include:
- Data preprocessing
- Feature selection
- Train/test split
- Model training
- Model evaluation

Some other models we plan to explore:
- Logistic Regression
- Bayesian Logistic Regression

Performance will be evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
