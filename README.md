## r/Wallstreetbets: Precise Forecasters
=========================

This was my Capstone project for the BrainStation Bootcamp in London in 2023. It focuses on analyzing the sentiment of financial discussions on the Reddit platform, specifically within the WallStreetBets subreddit. The goal was to identify and understand investment sentiment expressed in various investment related discussions and, in turn, gain insights into the financial opinions and behaviors of the community members.

### Problem Statement and Background

We all face an increasing information overload. Signal to noise ratio is very low.  This is especially relevant in financial markets, where difference of opinions is very high. On the same day, investors are bombarded by various opinions - some of them argue a stock is a BUY, some others argue it is a SELL. 

This project is an attempt to capture investment recommendations expressed on social media networks by various accounts and use machine learning and text processing tools to separate signal from the noise.  I am trying to identify social media accounts with a history of accurate investment advice/predictions while sidelining those with poor timing in their market actions. Such a filtration system will enable a focused consideration of only those voices with a credible track record in investment decisions.

My goal was to scrutinize historical posts on financially-oriented subreddits like r/Wallstreetbets and r/gme, decode sentiments and topics, and translate them into definitive "recommendations" issued by the authors — the buy or sell signals. Public accounts on these subreddits will be treated as "financial advisors," their market recommendations subject to subsequent scoring.

**Potential Business Value**
•	This project aims to develop tools that will help to filter noise from signal for investors.  The tools will help to  distinguish between insightful investment leads and misguided ones.
•	The filtering system potentially can also be used for the creation of a real-time trading strategy.

To build this filtering system I needed to answer a few key questions:

1.  What is the subject of discussion on social networks (which stocks are being debated)? Topic identification. 
2.  What is the sentiment on the market participants, are they bullish or bearish? Sentiment detection. 
3.  If I were to follow sentiment expressed by a specific social account, and buy when this account is bullish and sell when this account is bearish, what my financial performance would be? Backtesting trades. 

### Datasets

For my analysis I chose the following datasets:

1.	Reddit posts dataset collected by a user Leukipp and hosted on Kaggle. https://www.kaggle.com/datasets/leukipp/reddit-finance-data.  This dataset has 1.5 million of posts from 2021 on finance related topics posted on Reddit, the social media platform. Unlike many other similar datasets use for analysing investor sentiment, the dataset I chose has information on the posters’ account names. This allowed me to group the results by author. 

2.	Labelled dataset: with a bit of effort, I found a small r/wallstreetbears subreddit dataset that has been labelled by researchers from the University of Texas at San Antonio. The dataset can be downloaded from here: https://zenodo.org/records/5851847#.YeOvhPML8E  and the research paper that accompanied it is available here: https://arxiv.org/abs/2203.08694 (March 2022). The labelled dataset is quite small, only 5000 rows and it was labelled by humans with respect to two features: a) expressed an intent to buy Gamestock (GME) shares (‘Intent”) and 2) expressed support towards wallstreetbets anti-establishment movement in general (“Support”).

    - raw dataset copy on Google Drive folder:
 https://drive.google.com/drive/folders/1kC-QpEKzTDOs9Y8r7qSyabGHVHa1gIZx?usp=sharing

    - labelled dataset used for modelling:
https://zenodo.org/records/5851847#.YeOvhPML8E


### Steps performed to date
    
1. EDA of both datasets.
2. Cleaning the text.
3. Bag of words approach: Vectorisation. Pre-processing.
4. Modelling using the vectorised text. 
5. Application of the models trained on the labelled data towards unseen data. 

## Next Steps

1. Building predictive models that focus on sentence-level embeddings, comparing their performance to traditional Bag of Words (BoW) models.

2. Performing back testing of financial predictions made by WallStreetBets authors/accounts in 2021 to evaluate their financial skills and accuracy.

3. Conducting a clustering analysis of actively posting authors, using additional feature engineering to rate posts based on language complexity, readability, and other factors. This will help identify accounts worth following for financial insights. 

## Project Organization

The project comprises several notebooks, each with a specific focus and objective:

### Notebook 1 - Labelled Dataset - EDA and Cleaning

This notebook explores a labelled dataset of Reddit comments collected from the WallStreetBets subreddit in early 2021. The dataset focuses on identifying the intent to buy or not to buy securities expressed by various authors. It includes information about the authors, their comments, and labels indicating intent.

### Notebook 2 - Negative Labels Upsampling using OpenAI API

In this notebook, the author addresses the issue of imbalanced labels in the dataset, with a significant shortage of negatively labeled comments. To overcome this, OpenAI's GPT models are used to generate additional negative labels for upsampling.

### Notebook 3A - Labelled Dataset - "Bag of Words" Modelling - Yes and No only

This notebook focuses on modeling the upsampled labelled dataset using binary encoding strategies for the target variable "Intent." Various classification models and encoding combinations are explored, ultimately settling on two primary encoding strategies for modeling.

### Notebook 3B - Labelled Dataset - "Bag of Words" Modelling - Relevant and Irrelevant

This notebook explores an alternate encoding strategy, differentiating between "relevant" and "irrelevant" classes within the labelled dataset. The results of this encoding strategy are analyzed, and the significance of various word tokens is examined.

### Notebook 4 - Reddit Dataset - EDA and Data Cleaning

This notebook shifts attention to a larger dataset of unlabelled Reddit posts on financial topics throughout 2021. Extensive exploratory data analysis (EDA) and data cleaning are performed to prepare this dataset for various machine learning techniques and experiments.

### Notebook 5 - Reddit Dataset - BOW Models Applied to the Reddit Dataset Sample

In this notebook, logistic regression models trained on the labelled data are applied to the unlabelled Reddit dataset. The models predict the relevance and sentiment (bullish or bearish) of posts, allowing for analysis of overall community sentiment trends and the identification of influential authors.

#### Data Dictionary: 



### Walkthrough Demo

...


### Project Flowchart

 


* `data` 
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - contains all final notebooks involved in the project

* `reports`
    - contains final report which summarises the project

* `references`
    - contains papers / tutorials used in the project

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `environment.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license


### Credits & References

The white paper from the University of Texas in San Antonio that was a good starting point in my analysis.  This papers explains the labelled dataset in detail.  
https://arxiv.org/abs/2203.08694

Predicting $GME Stock Price Movement Using Sentiment from Reddit r/wallstreetbets
https://aclanthology.org/2021.finnlp-1.4.pdf
The white paper from the university of ILlinois in Chicago. This was an interesting paper that explains the approach to using BERT and Word2Vec embeddings for the WallStreetBets messages analysis.   
