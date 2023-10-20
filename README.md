
## r/Wallstreetbets: Precise Forecasters
=========================

## Project Overview

### Problem Statement and Background

We all face an increasing information overload. Signal to noise ratio is very low.  This is especially relevant in financial markets, where difference of opinions is very high, as it should be.  

It is sensible to attempt to utilise the machine language processing techniques to improve information filtering for market participants. 

This project is an attempt to capture investment sentiment expressed on social media networks and use machine learning and text processing tools to separate signal from noise. 

This analysis would help me to identify those accounts that were right in the past, and those who were spectacularly wrong – those who were buying and selling at exactly the wrong times.  This information will help me to disregard the noise and only focus on the opinions of those accounts that have a good past investment track record.   

### Data Collection 

To build this filtering system I needed to answer a few key questions:

1.	What is the subject of discussion on social networks (which stocks are being debated)?
2.	What is the sentiment on the market participants, are they bullish or bearish? 
3.	If I were to follow sentiment expressed by a specific social account, and buy when this account is bullish and sell when this account is bearish, what my financial performance would be? 

For my analysis I chose a dataset collected by a user Leukipp and hosted on Kaggle.  This dataset has 1.5 millions of posts from 2021 on finance related topics posted on Reddit, the social media platform.  

Unlike many other similar datasets use for analysing investor sentiment, the dataset has information on the posters’ account names. This will allow me to group the results by author. 

### Data Cleaning and EDA

The dataset was generally clean, but some data cleaning was still necessary.  Specifically, 5.6% of duplicate or repetitive rows were eliminated.  

Additionally, I converted the date into proper data type, eliminated several unnecessary columns, and created several new calculated fields, with information on word count for text fields, and popularity rankings of various posts. 

An important observation derived from early EDA was that the dataset is extremely imbalanced, with only 0.1% of accounts gaining all the attention (likes, comments, reposts), and only 20 top days comprising nearly 40% of all the posts. However, this imbalance is not an obstacle for text analysis and sentiment extraction. 

The encouraging result of the initial EDA is that top 150 accounts posted sufficient number of times (100-700 times in 2021) to be able to identify buy and sell signals throughout the year.

Additional challenge identified during the EDA stage is that the text of posts is full of slang and emojis. I will need to do a lot of work preparing the text for machine processing.


### Walkthrough Demo

...
...
...

### Project Flowchart

...
...
...

### Project Organization

...
...
...

* `data` 
    - raw dataset copy on Google Drive folder:
 https://drive.google.com/drive/folders/1kC-QpEKzTDOs9Y8r7qSyabGHVHa1gIZx?usp=sharing

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
