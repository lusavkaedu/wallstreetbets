## r/Wallstreetbets: Precise Forecasters
=========================

## Project Overview

### Problem Statement and Background

We all face an increasing information overload. Signal to noise ratio is very low.  This is especially relevant in financial markets, where difference of opinions is very high, as it should be.  

It is sensible to attempt to utilise the machine language processing techniques to improve information filtering for market participants. 

This project is an attempt to capture investment recommendations expressed on social media networks and use machine learning and text processing tools to separate signal from the noise. 

This analysis would help me to identify social media accounts with a history of accurate investment advice while sidelining those with poor timing in their market actions. Such a filtration system will enable a focused consideration of only those voices with a credible track record in investment decisions.

**Objective of the Project**

I want to explore how machine learning (ML) and natural language processing (NLP) techniques can be used to ease the task of identifying and ranking “smart” social media accounts (the “Precise Forecasters”).  
The goal of this project  is to scrutinize historical posts on financially-oriented subreddits like r/Wallstreetbets and r/gme, decode sentiments and topics, and translate them into definitive market actions—buy or sell signals. Public accounts on these subreddits will be treated as "financial advisors," their market recommendations subject to subsequent scoring.

**Potential Business Value**
•	This project aspires to elevate the decision-making capabilities of investors, particularly the small retail investors without the AI resources of larger institutions.
•	Amidst the social network clamor lies wisdom. Isolating the insightful from the mundane could vastly benefit investors of all stripes.
Project Impact
•	Aids investors in distinguishing between insightful investment leads and misguided ones.
•	Facilitates the creation of a real-time trading strategy.
•	Holds the promise to enhance the efficiency of capital markets, a sphere with multi-trillion-dollar implications, fostering a more affluent society.

To build this filtering system I needed to answer a few key questions:

1.  What is the subject of discussion on social networks (which stocks are being debated)?
2.  What is the sentiment on the market participants, are they bullish or bearish? 
3.  If I were to follow sentiment expressed by a specific social account, and buy when this account is bullish and sell when this account is bearish, what my financial performance would be? 

### Datasets

For my analysis I chose the following datasets:

1.	Reddit posts dataset collected by a user Leukipp and hosted on Kaggle. https://www.kaggle.com/datasets/leukipp/reddit-finance-data.  This dataset has 1.5 million of posts from 2021 on finance related topics posted on Reddit, the social media platform. Unlike many other similar datasets use for analysing investor sentiment, the dataset I chose has information on the posters’ account names. This allowed me to group the results by author. 
2.	Labelled dataset: with a bit of effort, I found a small r/wallstreetbears subreddit dataset that has been labelled by researchers from the University of Texas at San Antonio. The dataset can be downloaded from here: https://zenodo.org/records/5851847#.YeOvhPML8E  and the research paper that accompanied it is available here: https://arxiv.org/abs/2203.08694 (March 2022). 

The labelled dataset is quite small, only 5000 rows and it was labelled by humans with respect to two features: a) expressed an intent to buy Gamestock (GME) shares (‘Intent”) and 2) expressed support towards wallstreetbets anti-establishment movement in general (“Support”).  I was mostly interested in the first field, an intent to buy a financial instrument, so I made this as my target variable. The labelled dataset had 5 categories for expressing varied degrees of intent: yes (20%), no (3%), maybe (7%), unclear (65%), and informational post (6%).  I am mostly interested in capturing definitive bullish/bearish stance, and the fact that only 3% of the small dataset expressed clearly negative intent is unfortunate. Only 100 observations are labelled “no” for “Intent”, and this is normally not sufficient to build a robust predictive model using ML techniques. 

### Project orgainsation

The project is organised into the following notebooks:

01. Reddit Data Loading and EDA.  
02_A. Labelled dataset text cleaning.
02_B. Reddit text cleaning.
03_A. Labelled dataset modelling.

### Steps performed to date
    
1. Clean the text   
2. Sentiment Extraction (VADER) 
3. Vectorisation. Pre-processing    
4. Logistic Regression  

### Next Steps 
    
5. Portfolio of buys and sells  
6. Back testing financial performance    
7. Refine Entity Resolution, Dependency, Part Of Speech etc. for each post  
8. Instead of vectorise, try embeddings - word2vec  
9. Report, video and presentation  

### 1. Data Loading and EDA

The dataset was generally clean, but some data cleaning was still necessary.  Specifically, 5.6% of duplicate or repetitive rows were eliminated.  

Additionally, I converted the date into proper data type, eliminated several unnecessary columns, and created several new calculated fields, with information on word count for text fields, and popularity rankings of various posts. 

An important observation derived from early EDA was that the dataset is extremely imbalanced, with only 0.1% of accounts gaining all the attention (likes, comments, reposts), and only 20 top days comprising nearly 40% of all the posts. However, this imbalance is not an obstacle for text analysis and sentiment extraction. 

The encouraging result of the initial EDA is that top 150 accounts posted sufficient number of times (100-700 times in 2021) to be able to identify buy and sell signals throughout the year.

Additional challenge identified during the EDA stage is that the text of posts is full of slang and emojis. I will need to do a lot of work preparing the text for machine processing.

#### Data Dictionary: 



### Walkthrough Demo

...
...
...

### Project Flowchart

 

### Project Organization

...
...
...

* `data` 
    - raw dataset copy on Google Drive folder:
 https://drive.google.com/drive/folders/1kC-QpEKzTDOs9Y8r7qSyabGHVHa1gIZx?usp=sharing

    - labelled dataset used for modelling:
https://zenodo.org/records/5851847#.YeOvhPML8E

    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - contains all final notebooks involved in the project

* `reports`
    - contains final report which summarises the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `environment.yml`
    - Conda environment specification

* `Makefile`
    - Automation script for the project

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

### Dataset

...
...
...

### Credits & References

...
...
...

--------



