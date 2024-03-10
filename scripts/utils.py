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
