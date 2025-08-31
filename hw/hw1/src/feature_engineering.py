"""
MAI 5201 - Homework 1: Machine Learning for NLP
Part 1: From Scratch Implementation
Q2: Feature Engineering (8 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Build on Q1 functions to implement advanced feature engineering
- Use only basic Python and standard string operations
- Run all tests with: python autograder.py
- Run Q1 tests only with: python autograder.py -q q1
- Run Q2 tests only with: python autograder.py -q q2
- Do not modify function signatures
"""

import math
from typing import Dict, List, Tuple, Set
import string, re
from text_features import extract_bag_of_words, build_vocabulary, text_to_vector


def add_ngram_features(texts: List[str], n: int = 2) -> Dict[str, int]:
    """
    Build vocabulary including n-gram features alongside unigrams.
    
    N-grams are sequences of n consecutive words that capture local context
    and word relationships that single words miss. For example:
    - "not good" (bigram) has different meaning than "not" + "good" separately
    - "very good movie" (trigram) provides richer context than individual words
    
    Args:
        texts (List[str]): List of text strings
        n (int): Maximum n-gram size (1=unigrams, 2=bigrams, 3=trigrams, etc.)
    
    Returns:
        Dict[str, int]: Combined vocabulary with unigrams + n-grams, sorted alphabetically
    
    Examples:
        >>> add_ngram_features(["good movie", "bad movie"], n=2)
        {'bad': 0, 'bad movie': 1, 'good': 2, 'good movie': 3, 'movie': 4}
        
        >>> add_ngram_features(["not good"], n=2) 
        {'good': 0, 'not': 1, 'not good': 2}
    
    Implementation Notes:
        - Include all n-grams from 1 to n (unigrams, bigrams, trigrams, etc.)
        - Use extract_bag_of_words for preprocessing individual texts
        - Create n-grams by sliding window over word sequences
        - Combine all features and sort alphabetically for consistent ordering
        - Handle edge cases (empty texts, n=1, texts shorter than n)
    """
    # TODO: Implement n-gram feature extraction
    # Step 1: For each n from 1 to n, extract n-grams from all texts
    # Step 2: Collect all unique n-grams
    # Step 3: Sort and assign indices
    # Step 4: Return combined vocabulary
    
    # For now, return empty dictionary until implemented
    
    grams = set()

    for text in texts:
        words = re.findall(r'\b\w+\b', text.lower())
        length = len(words)
        for size in range(1, n + 1):
            for i in range(length - size + 1):
                ngram = ' '.join(words[i:i + size])
                grams.add(ngram)
    
    sorted_grams = sorted(grams)
    vocab = {gram: idx for idx, gram in enumerate(sorted_grams)}
    
    return vocab


def compute_tf_idf_features(texts: List[str], vocab: Dict[str, int]) -> List[List[float]]:
    """
    Convert texts to TF-IDF weighted feature vectors.
    
    TF-IDF (Term Frequency - Inverse Document Frequency) weights words by:
    - TF: How often a word appears in a document (local importance)
    - IDF: How rare a word is across all documents (global importance)
    
    This gives higher weight to words that are frequent in a document but
    rare across the corpus, which are typically more informative.
    
    Args:
        texts (List[str]): List of text strings to convert
        vocab (Dict[str, int]): Vocabulary mapping words to indices
    
    Returns:
        List[List[float]]: List of TF-IDF vectors, one per text
    
    Examples:
        >>> vocab = {"good": 0, "movie": 1, "bad": 2}
        >>> texts = ["good movie", "bad movie movie"]
        >>> compute_tf_idf_features(texts, vocab)
        [[0.693, 0.0, 0.0], [0.0, 0.0, 0.693]]  # Simplified example
    
    Formulas:
        TF(word, doc) = count(word in doc) / total_words_in_doc
        IDF(word) = log(total_docs / docs_containing_word)
        TF-IDF(word, doc) = TF(word, doc) * IDF(word)
    
    Implementation Notes:
        - Use extract_bag_of_words for word counting
        - Calculate TF for each word in each document
        - Calculate IDF for each word across all documents
        - Multiply TF * IDF for final weights
        - Handle edge cases (empty documents, zero counts)
        - Use natural logarithm (math.log)
    """
    # TODO: Implement TF-IDF feature computation
    # Step 1: Calculate TF for each word in each document
    # Step 2: Calculate IDF for each word across corpus
    # Step 3: Multiply TF * IDF for final vectors
    # Step 4: Return list of TF-IDF vectors
    
    # For now, return empty list until implemented
    
    totalDocs = len(texts)
    if totalDocs == 0 or not vocab:
        return []

    docWordCounts = []
    docLengths = []

    for text in texts:
        word_count = extract_bag_of_words(text)
        docWordCounts.append(word_count)
        docLengths.append(sum(word_count.values()))
    
    docFreq = {word: 0 for word in vocab}
    for wordCount in docWordCounts:
        for word in wordCount:
            if word in vocab:
                docFreq[word] += 1

    idfScores = {
        word: math.log(totalDocs / (docFreq[word] + 1))  # +1 to avoid division by zero
        for word, freq in docFreq.items()
    }

    tf_idf_vectors = []
    for wordCount, length in zip(docWordCounts, docLengths):
        vector = [0.0] * len(vocab)
        if length > 0:
            for word, count in wordCount.items():
                if word in vocab:
                    tf = count / length
                    vector[vocab[word]] = tf * idfScores[word]
        tf_idf_vectors.append(vector)

    return tf_idf_vectors

def extract_feature_statistics(texts: List[str]) -> List[Dict[str, float]]:
    """
    Extract statistical features from texts for machine learning.
    
    Beyond word counts, statistical features capture document-level
    properties that can be highly predictive:
    - Length features: Short vs. long reviews have different patterns
    - Lexical diversity: Vocabulary richness indicates writing style
    - Readability: Sentence complexity affects sentiment expression
    
    Args:
        texts (List[str]): List of text strings
    
    Returns:
        List[Dict[str, float]]: Statistical features for each text
    
    Each dictionary contains:
        - 'word_count': Total number of words
        - 'char_count': Total number of characters (excluding spaces)
        - 'sentence_count': Number of sentences (approximate)
        - 'avg_word_length': Average length of words
        - 'vocab_diversity': Unique words / total words (lexical diversity)
        - 'exclamation_count': Number of exclamation marks
        - 'question_count': Number of question marks
        - 'uppercase_ratio': Proportion of uppercase characters
    
    Examples:
        >>> extract_feature_statistics(["Great movie! Really enjoyed it."])
        [{'word_count': 4, 'char_count': 22, 'sentence_count': 2, 
          'avg_word_length': 5.5, 'vocab_diversity': 1.0,
          'exclamation_count': 1, 'question_count': 0, 'uppercase_ratio': 0.09}]
    
    Implementation Notes:
        - Use extract_bag_of_words for consistent word processing
        - Count sentences by periods, exclamations, questions
        - Calculate character count excluding spaces and punctuation
        - Handle edge cases (empty texts, single words)
        - Vocab diversity = unique_words / total_words (0 if total_words = 0)
    """
    # TODO: Implement statistical feature extraction
    # Step 1: For each text, extract basic counts
    # Step 2: Calculate derived metrics (averages, ratios)
    # Step 3: Handle edge cases
    # Step 4: Return feature dictionaries
    
    # For now, return empty list until implemented
    return []


def build_feature_matrix(texts: List[str], feature_config: Dict[str, bool]) -> Tuple[List[List[float]], List[str]]:
    """
    Build a complete feature matrix combining multiple feature types.
    
    This is the final step that combines everything:
    - Bag-of-words features (from Q1)
    - N-gram features 
    - TF-IDF weighting
    - Statistical features
    
    Real ML systems combine many feature types for best performance.
    
    Args:
        texts (List[str]): List of text strings
        feature_config (Dict[str, bool]): Configuration for which features to include
    
    feature_config keys:
        - 'use_unigrams': Include single words (default: True)
        - 'use_bigrams': Include word pairs (default: True)  
        - 'use_tfidf': Use TF-IDF weighting instead of counts (default: True)
        - 'use_statistics': Include statistical features (default: True)
    
    Returns:
        Tuple[List[List[float]], List[str]]: 
            - Feature matrix (each row = document, each col = feature)
            - Feature names (for interpretability)
    
    Examples:
        >>> config = {'use_unigrams': True, 'use_bigrams': False, 
                      'use_tfidf': False, 'use_statistics': True}
        >>> matrix, names = build_feature_matrix(["good movie"], config)
        >>> len(matrix[0])  # Number of features
        10  # 2 words + 8 statistical features
    
    Implementation Notes:
        - Start with appropriate vocabulary based on n-gram config
        - Apply TF-IDF if requested, otherwise use counts
        - Append statistical features if requested
        - Ensure all vectors have same length
        - Return meaningful feature names for debugging
    """
    # TODO: Implement complete feature matrix construction
    # Step 1: Build vocabulary based on feature_config
    # Step 2: Convert texts to vectors (count or TF-IDF)
    # Step 3: Add statistical features if requested
    # Step 4: Create feature names list
    # Step 5: Return matrix and names
    
    # For now, return empty results until implemented
    return [], []
