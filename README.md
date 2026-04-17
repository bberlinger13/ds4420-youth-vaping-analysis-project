# DS4420 Youth Vaping Analysis Project
## Northeastern University Spring 2026
### Professor: Dr. Eric Gerber

### Authors
- Blythe Berlinger
- Sydney Schulz

---

## Project Overview
This project analyzes youth vaping behavior in the United States using the 
National Youth Tobacco Survey (NYTS) from 2021–2023. We examine how demographic 
characteristics and social media exposure relate to e-cigarette use among 
adolescents aged approximately 11–18. We clean and aggregate three years of 
survey data, perform exploratory data analysis, and build two machine learning 
models to predict and interpret e-cigarette use.

**Live App:** https://ds4420-youth-vaping-analysis-project-b4mphtxxscnvyhnohca2vj.streamlit.app/

---

## Research Questions
1. Can social media usage patterns, platform choices, and content creator exposure predict current e-cigarette use among adolescents?
2. Which specific social media behaviors are most credibly associated with e-cigarette use, and with what uncertainty?

---

## Dataset
Data comes from the CDC National Youth Tobacco Survey (NYTS), waves 2021–2023.
These are the first years to include content-specific social media exposure 
questions. Raw data is available at:
https://www.cdc.gov/tobacco/data_statistics/surveys/nyts/

**Key features:**
- Demographics: age, sex, grade
- Social media behavior: overall usage frequency, frequency of seeing/posting/
  interacting with e-cigarette content
- Platform use: Facebook, Instagram, Snapchat, TikTok, Twitter, Reddit, 
  YouTube, Twitch
- Content creator type: real-life contacts, online friends, influencers, 
  brands/sellers, news, public health
- Target variable: current e-cigarette use (binary, from QN9)

**Dataset summary:**
- 12,588 observations across three survey years
- Class balance: 45.3% current users, 54.7% non-users
- Use rates: 40.0% (2021) → 47.2% (2022) → 47.7% (2023)

---

## Data Cleaning
Each year was loaded from its raw CSV, processed to a consistent 24-feature 
schema, and merged into a single dataset. Steps included:
- Standardizing variable names across survey years
- Selecting relevant variables
- Converting multi-select platform/creator questions to binary indicators
- Filling binary columns with 0 for non-selection
- Median imputation for ordinal and demographic columns
- Appending a zero-valued Twitch column to 2021/2022 (not in survey until 2023)

Final cleaned dataset: `data/cleaned/nyts_2021_2023_clean.csv`

---

## Models

### 1. Multilayer Perceptron (Python — manual implementation)
Implemented from scratch using NumPy only (no Scikit-learn or similar).

**Architecture:** 24 → 32 → 16 → 1 (sigmoid output)  
**Activation:** ReLU (hidden layers), Sigmoid (output)  
**Training:** Mini-batch SGD, batch size 64, learning rate 0.001, 600 epochs  
**Initialization:** He initialization  
**Loss:** Binary cross-entropy  

**Results at threshold = 0.3 (selected for public health recall priority):**
- Accuracy: 54.3%
- Precision: 0.499
- Recall: 0.878
- F1: 0.636

### 2. Bayesian Logistic Regression (R — brms)
Implemented in R using the `brms` package with Stan backend.

**Priors:** Normal(0, 0.3) for coefficients, Normal(−2, 0.3) for intercept  
**Chains:** 4 MCMC chains × 2,000 iterations (1,000 warmup)  
**Convergence:** All R-hat = 1.00  
**Bayesian R²:** 0.079 (95% CI: 0.071–0.086)  

**Key findings:**
- Interaction frequency (OR = 1.29), posting frequency (OR = 1.27), and 
  content exposure frequency (OR = 1.21) were all credible positive predictor
- Overall social media usage was not (OR = 0.96)
- Following public health creators had the strongest protective effect 
  (OR = 0.62)
- Female adolescents had 18% higher odds of use (OR = 1.18)

---

## Key Findings
Both models converged on the same core finding: **active engagement with 
e-cigarette content on social media — not overall platform use — is the 
strongest behavioral predictor of adolescent vaping.** Snapchat and TikTok 
were the dominant platforms among current users across all three years. 
E-cigarette use rates were consistent across grade levels (42–48%), suggesting 
prevention efforts should target all grades, not just upperclassmen.

---

## Requirements
See `requirements.txt` for Python dependencies. R dependencies: `brms`, 
`tidybayes`, `ggplot2`, `dplyr`, `here`.
