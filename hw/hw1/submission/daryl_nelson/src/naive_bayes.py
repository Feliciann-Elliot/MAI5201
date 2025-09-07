"""
MAI 5201 - Homework 1: Machine Learning for NLP
Part 1: From Scratch Implementation
Q3: Naive Bayes from Scratch (8 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement Naive Bayes classifier using only basic Python and math operations
- Use the feature vectors from Q1/Q2 as input to these functions
- Run all tests with: python autograder.py
- Run Q3 tests only with: python autograder.py -q q3
- Do not modify function signatures
"""

from typing import Dict, List, Tuple
import math
from collections import defaultdict, Counter


def calculate_class_priors(labels: List[int]) -> Dict[int, float]:
    """
    Calculate the prior probabilities P(class) for each class.
    
    The prior probability represents how common each class is in the training data.
    For binary sentiment classification:
    - P(positive) = number of positive reviews / total reviews
    - P(negative) = number of negative reviews / total reviews
    
    Args:
        labels (List[int]): List of class labels (0 for negative, 1 for positive)
    
    Returns:
        Dict[int, float]: Dictionary mapping class labels to their prior probabilities
    
    Examples:
        >>> calculate_class_priors([0, 0, 1, 1, 1])
        {0: 0.4, 1: 0.6}  # 40% negative, 60% positive
        
        >>> calculate_class_priors([1, 1, 1, 1])
        {1: 1.0}  # 100% positive (edge case)
    
    Implementation Notes:
        - Handle empty input gracefully
        - Ensure probabilities sum to 1.0
        - Use precise division (not integer division)
        - Return probabilities as floats
    """
    # TODO: Implement class prior calculation
    # Step 1: Count occurrences of each class
    # Step 2: Calculate total number of examples
    # Step 3: Compute probability for each class
    # Step 4: Return dictionary mapping class -> probability
    
    # For now, return empty dictionary until implemented
    return {}


def calculate_feature_likelihoods(vectors: List[List[float]], labels: List[int]) -> Dict[int, List[float]]:
    """
    Calculate feature likelihoods P(feature|class) for Naive Bayes.
    
    For each class and each feature position, calculate the probability that
    a document of that class will have that feature value. This uses the
    "multinomial" variant of Naive Bayes suitable for text classification.
    
    Args:
        vectors (List[List[float]]): Feature vectors (from Q1/Q2 feature extraction)
        labels (List[int]): Corresponding class labels
    
    Returns:
        Dict[int, List[float]]: For each class, list of feature probabilities
                               where each position corresponds to a feature
    
    Formula for Multinomial Naive Bayes:
        P(feature_i | class) = (count of feature_i in class + alpha) / 
                              (total feature count in class + alpha * vocab_size)
        
        Where alpha = 1 (Laplace smoothing) prevents zero probabilities
    
    Examples:
        >>> vectors = [[1, 0, 2], [0, 1, 1], [2, 0, 0]]
        >>> labels = [1, 0, 1]
        >>> calculate_feature_likelihoods(vectors, labels)
        {0: [0.2, 0.6, 0.2], 1: [0.5, 0.0, 0.5]}
        # Class 0: feature counts [0,1,1] -> probabilities after smoothing
        # Class 1: feature counts [3,0,2] -> probabilities after smoothing
    
    Implementation Notes:
        - Apply Laplace smoothing (alpha=1) to avoid zero probabilities
        - Handle multiple classes (not just binary)
        - Ensure probabilities for each class sum to 1.0
        - Use float division for precision
        - Handle empty classes gracefully
    """
    # TODO: Implement feature likelihood calculation
    # Step 1: Group vectors by class labels
    # Step 2: For each class, sum feature counts across all documents
    # Step 3: Apply Laplace smoothing (add 1 to each count)
    # Step 4: Normalize to get probabilities
    # Step 5: Return dictionary mapping class -> feature probabilities
    
    # For now, return empty dictionary until implemented
    return {}


def naive_bayes_predict(vector: List[float], priors: Dict[int, float], 
                       likelihoods: Dict[int, List[float]]) -> Tuple[int, Dict[int, float]]:
    """
    Make a prediction using Naive Bayes classification.
    
    Uses Bayes' theorem to calculate the probability of each class given
    the feature vector, then returns the most likely class.
    
    Args:
        vector (List[float]): Feature vector to classify
        priors (Dict[int, float]): Class prior probabilities from calculate_class_priors
        likelihoods (Dict[int, List[float]]): Feature likelihoods from calculate_feature_likelihoods
    
    Returns:
        Tuple[int, Dict[int, float]]: (predicted_class, class_probabilities)
            - predicted_class: The class with highest probability
            - class_probabilities: Probability of each class given the input
    
    Formula (Bayes' Theorem):
        P(class | features) ∝ P(class) * ∏ P(feature_i | class)^count_i
        
        Where count_i is the value of feature_i in the input vector
    
    Examples:
        >>> vector = [1, 0, 1]
        >>> priors = {0: 0.5, 1: 0.5}
        >>> likelihoods = {0: [0.3, 0.4, 0.3], 1: [0.6, 0.2, 0.2]}
        >>> naive_bayes_predict(vector, priors, likelihoods)
        (1, {0: 0.33, 1: 0.67})  # Class 1 is more likely
    
    Implementation Notes:
        - Work in log space to prevent numerical underflow
        - Use log(P(class)) + Σ count_i * log(P(feature_i | class))
        - Convert back to probabilities for final result
        - Handle zero feature values (they contribute 0 to log sum)
        - Normalize final probabilities to sum to 1.0
    """
    # TODO: Implement Naive Bayes prediction
    # Step 1: For each class, calculate log-probability
    #         log P(class|features) = log P(class) + Σ count_i * log P(feature_i|class)
    # Step 2: Convert log-probabilities back to regular probabilities
    # Step 3: Normalize probabilities to sum to 1.0
    # Step 4: Find class with highest probability
    # Step 5: Return (predicted_class, all_probabilities)
    
    # For now, return dummy values until implemented
    return 0, {}


def train_naive_bayes(vectors: List[List[float]], labels: List[int]) -> Tuple[Dict[int, float], Dict[int, List[float]]]:
    """
    Train a complete Naive Bayes classifier.
    
    This is a convenience function that combines the prior and likelihood
    calculations into a single training step.
    
    Args:
        vectors (List[List[float]]): Training feature vectors
        labels (List[int]): Training labels
    
    Returns:
        Tuple[Dict[int, float], Dict[int, List[float]]]: (priors, likelihoods)
            - priors: Class prior probabilities
            - likelihoods: Feature likelihoods for each class
    
    Examples:
        >>> vectors = [[1, 0], [0, 1], [1, 1]]
        >>> labels = [0, 1, 1]
        >>> priors, likelihoods = train_naive_bayes(vectors, labels)
        >>> priors
        {0: 0.33, 1: 0.67}
        >>> likelihoods
        {0: [0.67, 0.33], 1: [0.4, 0.6]}
    
    Implementation Notes:
        - This function should call your other implemented functions
        - Validate that vectors and labels have same length
        - Handle edge cases (empty data, single class, etc.)
    """
    # TODO: Implement complete training pipeline
    # Step 1: Validate input (same length vectors and labels)
    # Step 2: Calculate class priors using calculate_class_priors
    # Step 3: Calculate feature likelihoods using calculate_feature_likelihoods
    # Step 4: Return both components
    
    # For now, return empty results until implemented
    return {}, {}


def evaluate_naive_bayes(vectors: List[List[float]], labels: List[int], 
                        priors: Dict[int, float], likelihoods: Dict[int, List[float]]) -> Dict[str, float]:
    """
    Evaluate Naive Bayes classifier on a dataset.
    
    Args:
        vectors (List[List[float]]): Feature vectors to classify
        labels (List[int]): True labels
        priors (Dict[int, float]): Trained class priors
        likelihoods (Dict[int, List[float]]): Trained feature likelihoods
    
    Returns:
        Dict[str, float]: Evaluation metrics
            - 'accuracy': Overall classification accuracy
            - 'precision': Precision for positive class (class 1)
            - 'recall': Recall for positive class (class 1)
            - 'f1': F1-score for positive class (class 1)
    
    Implementation Notes:
        - Use naive_bayes_predict for each vector
        - Calculate standard classification metrics
        - Handle edge cases (perfect classification, etc.)
    """
    # TODO: Implement evaluation metrics
    # Step 1: Make predictions for all vectors
    # Step 2: Calculate accuracy, precision, recall, F1
    # Step 3: Return metrics dictionary
    
    # For now, return dummy metrics until implemented
    return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0}
