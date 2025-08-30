"""
MAI 5201 - Homework 1: Machine Learning for NLP
Part 1: From Scratch Implementation
Q1: Text Feature Extraction (6 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement the three functions below for text feature extraction
- Use only basic Python and standard string operations
- Run all tests with: python autograder.py
- Run Q1 tests only with: python autograder.py -q q1
- Do not modify function signatures
"""

from typing import Dict, List
import re
from collections import defaultdict
import string


def extract_bag_of_words(text: str) -> Dict[str, int]:
    """
    Convert a single text string into a bag-of-words representation.
    
    A bag-of-words represents text as a dictionary where:
    - Keys are unique words (lowercased)
    - Values are the count of how many times each word appears
    
    Args:
        text (str): Input text string
    
    Returns:
        Dict[str, int]: Dictionary mapping words to their counts
    
    Examples:
        >>> extract_bag_of_words("This movie was great! I loved this great movie.")
        {'this': 2, 'movie': 2, 'was': 1, 'great': 2, 'i': 1, 'loved': 1}
        
        >>> extract_bag_of_words("Bad movie. Really bad!")
        {'bad': 2, 'movie': 1, 'really': 1}
    
    Implementation Notes:
        - Convert text to lowercase
        - Remove punctuation (hint: use string.punctuation)
        - Split on whitespace
        - Count word frequencies
        - Handle empty strings gracefully
    """
    # TODO: Implement bag-of-words extraction
    # Step 1: Convert to lowercase
    # Step 2: Remove punctuation 
    # Step 3: Split into words
    # Step 4: Count word frequencies
    # Step 5: Return dictionary
    
    # For now, return empty dictionary until implemented
    sentence = text.lower()
    words = re.findall(r'\b\w+\b', sentence)

    vocab = defaultdict(int)        
    for word in words:
        vocab[word] += 1
    sorted_vocab = dict(sorted(vocab.items()))
    
    return sorted_vocab


def build_vocabulary(texts: List[str]) -> Dict[str, int]:
    """
    Create a word-to-index mapping from a list of texts.
    
    This creates a vocabulary where each unique word gets assigned
    a unique integer index. This is essential for converting text
    to numerical feature vectors.
    
    Args:
        texts (List[str]): List of text strings to build vocabulary from
    
    Returns:
        Dict[str, int]: Dictionary mapping words to unique indices
    
    Examples:
        >>> build_vocabulary(["good movie", "bad movie", "great film"])
        {'bad': 0, 'film': 1, 'good': 2, 'great': 3, 'movie': 4}
        
        >>> build_vocabulary(["I love movies", "movies are fun"])
        {'are': 0, 'fun': 1, 'i': 2, 'love': 3, 'movies': 4}
    
    Implementation Notes:
        - Use extract_bag_of_words to process each text
        - Collect all unique words across all texts
        - Assign indices in consistent order (sorted alphabetically)
        - Handle empty input gracefully
    """
    # TODO: Implement vocabulary building
    # Step 1: Extract all words from all texts
    # Step 2: Get unique words
    # Step 3: Sort words for consistent ordering
    # Step 4: Assign indices
    # Step 5: Return word-to-index dictionary
    
    # For now, return empty dictionary until implemented
    return {}


def text_to_vector(text: str, vocab: Dict[str, int]) -> List[int]:
    """
    Convert a text string to a feature vector using the given vocabulary.
    
    This creates a numerical representation of text where each position
    corresponds to a word in the vocabulary, and the value is the count
    of that word in the text.
    
    Args:
        text (str): Input text string to convert
        vocab (Dict[str, int]): Vocabulary mapping words to indices
    
    Returns:
        List[int]: Feature vector where index i contains count of vocab word i
    
    Examples:
        >>> vocab = {"good": 0, "movie": 1, "bad": 2}
        >>> text_to_vector("good movie", vocab)
        [1, 1, 0]
        
        >>> text_to_vector("bad movie great movie", vocab)
        [0, 2, 1]
        
        >>> text_to_vector("unknown words", vocab)  # words not in vocab
        [0, 0, 0]
    
    Implementation Notes:
        - Use extract_bag_of_words to get word counts
        - Initialize vector with zeros for all vocabulary words
        - Fill in counts for words that appear in both text and vocab
        - Ignore words that don't appear in vocabulary
        - Return vector of length equal to vocabulary size
    """
    # TODO: Implement text-to-vector conversion
    # Step 1: Get bag-of-words representation of text
    # Step 2: Initialize vector of zeros (length = vocab size)
    # Step 3: Fill vector with word counts from vocab
    # Step 4: Return feature vector
    
    # For now, return empty list until implemented
    return []
