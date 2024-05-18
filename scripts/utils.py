import numpy as np
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Download the NLTK resources (only once)
try:
    _stopwords = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    _stopwords = set(stopwords.words('english'))

_stopwords = set(stopwords.words('english'))

def cohen_d(x, y):
    """Compute Cohen's d effect size for two groups / columns of a DataFrame.
    
    Check out the following link for more information:
    https://en.wikipedia.org/wiki/Effect_size#Cohen's_d

    Args:
        x: The first group / array of data containing the samples
        y: The second group / array of data containing the samples

    Returns:
        The value of Cohen's d effect size
    """
    mean_diff = np.mean(x) - np.mean(y)
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    pooled_std = np.sqrt(((nx-1) * np.std(x, ddof=1) ** 2 + (ny-1) * np.std(y, ddof=1) ** 2) / dof)
    return mean_diff / pooled_std

def preprocess_tweet(tweet):
    """Preprocess a tweet by converting it to lowercase, removing URLs, mentions, and hashtags, and removing non-letters.
    
    Args:
        tweet: A string representing the tweet to be preprocessed
    
    Returns:
        A string representing the preprocessed tweet
    """
    tweet = tweet.lower()
    # Remove URLs, mentions, and hashtags
    tweet = re.sub(r'@\w+|\w+://\S+|(#\S+)', '', tweet)
    # Remove non-letters e.g punctuation, numbers
    tweet = re.sub(r'[^a-zA-Z\s]+', '', tweet) 
    return tweet  

def tokenize(tweet):
    """Tokenize a tweet by splitting it into words.
    
    Args:
        tweet: A string representing the tweet to be tokenized
    
    Returns:
        A list of strings representing the words of the tweet
    """
    tweet = preprocess_tweet(tweet)
    words = tweet.split()
    return words

def stem(word):
    """Stem a word using the Porter Stemmer algorithm.
    
    Args:
        word: A string representing the word to be stemmed
    
    Returns:
        A string representing the stemmed word
    """
    # Implement the Porter Stemmer algorithm
    ps = PorterStemmer()
    return ps.stem(word)

def check_stopword(word):
    """checks if a word is a stopword.
    
    Args:
        word: A string representing the word to be checked
    
    Returns:
        A boolean value indicating whether the word is a stopword
    """
    return word in _stopwords

def cohen_d_spark(df1, df2, col_x, col_y):
    """Compute Cohen's d effect size for two groups / columns of a DataFrame.
    
    Check out the following link for more information:
    https://en.wikipedia.org/wiki/Effect_size#Cohen's_d

    This function is scalable because it uses Spark DataFrames aggregation functions to compute the necessary statistics.

    Args:
        df1: The first group / DataFrame containing the samples
        df2: The second group / DataFrame containing the samples
        col_x: The column name of the first group
        col_y: The column name of the second group

    Returns:
        The value of Cohen's d effect size
    """
    mean_x = df1.agg({col_x: "avg"}).collect()[0][0]
    mean_y = df2.agg({col_y: "avg"}).collect()[0][0]
    mean_diff = mean_x - mean_y
    nx = df1.filter(df1[col_x].isNotNull()).count()
    ny = df2.filter(df2[col_y].isNotNull()).count()
    std_x = df1.agg({col_x: "stddev"}).collect()[0][0]
    std_y = df2.agg({col_y: "stddev"}).collect()[0][0]
    dof = nx + ny - 2
    pooled_std = np.sqrt(((nx-1)*(std_x**2) + (ny-1)*(std_y**2)) / dof)
    return mean_diff / pooled_std
