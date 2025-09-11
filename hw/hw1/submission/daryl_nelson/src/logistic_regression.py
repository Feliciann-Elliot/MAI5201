"""
MAI 5201 - Homework 1, Question 4
Logistic Regression Core Functions

Implement the fundamental components of logistic regression:
sigmoid activation, cross-entropy loss, and gradient computation.

Your Name: [Your Name Here]
"""

import numpy as np
from typing import List, Tuple


def sigmoid(z):
    """
    Compute the sigmoid activation function.
    
    The sigmoid function maps any real number to a value between 0 and 1,
    making it perfect for binary classification probabilities.
    
    Formula: σ(z) = 1 / (1 + e^(-z))
    
    Args:
        z: Input value(s) - can be a single number, list, or numpy array
    
    Returns:
        float or numpy array: Sigmoid of input(s), values between 0 and 1
    
    Example:
        >>> sigmoid(0)
        0.5
        >>> sigmoid([0, 2, -2])
        [0.5, 0.88, 0.12] (approximately)
    """
    # TODO: Implement sigmoid function
    # Hint: Use np.exp() and handle potential overflow with np.clip()

    z_np_array = np.array(z, dtype=np.float64)

    z_np_array = np.clip(z_np_array, -500, 500)

    sigmoid_arr = 1 / (1 + np.exp(-z_np_array))

    if np.isscalar(z):
        return float(sigmoid_arr)
    return sigmoid_arr


def cross_entropy_loss(y_true, y_pred):
    """
    Compute the cross-entropy loss for binary classification.
    
    Cross-entropy loss penalizes confident wrong predictions more heavily
    than uncertain predictions, making it ideal for probabilistic models.
    
    Formula: L = -[y*log(p) + (1-y)*log(1-p)]
    
    Args:
        y_true: True binary labels (0 or 1) - list or numpy array
        y_pred: Predicted probabilities (0 to 1) - list or numpy array
    
    Returns:
        float: Average cross-entropy loss across all samples
    
    Example:
        >>> y_true = [1, 0, 1]
        >>> y_pred = [0.9, 0.1, 0.8]
        >>> cross_entropy_loss(y_true, y_pred)
        0.174 (approximately)
    """
    # TODO: Implement cross-entropy loss
    # Hints: 
    # - Use np.log() for logarithm
    # - Add small epsilon (1e-15) to prevent log(0)
    # - Return the mean loss across all samples
    y_true = np.array(y_true, dtype=np.float64)
    y_pred = np.array(y_pred, dtype=np.float64)


    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    return float(np.mean(loss))


def compute_gradients(X, y, weights):
    """
    Compute gradients for logistic regression using the chain rule.
    
    This is the core of gradient descent - computing how much to adjust
    each weight to minimize the loss function.
    
    The gradient formula comes from differentiating cross-entropy loss
    with respect to weights: ∇w = X^T * (predictions - y_true) / m
    
    Args:
        X: Feature matrix, shape (n_samples, n_features) - list of lists or numpy array
        y: True binary labels, shape (n_samples,) - list or numpy array  
        weights: Current weight vector, shape (n_features,) - list or numpy array
    
    Returns:
        numpy array: Gradients for each weight, shape (n_features,)
    
    Example:
        >>> X = [[1, 2], [1, 3], [1, 1]]  # Include bias feature (1s)
        >>> y = [1, 1, 0]
        >>> weights = [0.0, 0.0]
        >>> compute_gradients(X, y, weights)
        array([0.167, 0.333]) (approximately)
    """
    # TODO: Implement gradient computation
    # Steps:
    # 1. Convert inputs to numpy arrays
    # 2. Compute predictions using sigmoid(X @ weights)
    # 3. Compute error = predictions - y_true
    # 4. Compute gradients = X.T @ error / n_samples
    # 5. Return gradients as numpy array
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    if X.size == 0 or y.size == 0:
        return np.zeros_like(weights)

    weights = np.array(weights, dtype=np.float64)

    z = X @ weights
    predictions = sigmoid(z)

    error = predictions - y

    n_samples = X.shape[0]
    gradients = (X.T @ error) / n_samples

    return gradients


def sgd_step(weights, gradients, learning_rate):
    """
    Perform a single SGD (Stochastic Gradient Descent) update step.
    
    SGD is the optimization algorithm that powers most machine learning.
    This function updates weights by moving them in the opposite direction
    of the gradients, scaled by the learning rate.
    
    Formula: weights_new = weights_old - learning_rate * gradients
    
    Args:
        weights: Current weight vector - list or numpy array
        gradients: Gradient vector from compute_gradients() - list or numpy array  
        learning_rate: Step size for the update - float
    
    Returns:
        numpy array: Updated weight vector
    
    Example:
        >>> weights = [0.1, 0.2]
        >>> gradients = [0.05, -0.1] 
        >>> learning_rate = 0.1
        >>> sgd_step(weights, gradients, learning_rate)
        array([0.095, 0.21])  # weights - lr * gradients
    """
    # TODO: Implement SGD step
    # Hints:
    # 1. Convert inputs to numpy arrays
    # 2. Apply the SGD update formula
    # 3. Return updated weights as numpy array
    weights = np.array(weights, dtype=np.float64)
    gradients = np.array(gradients, dtype=np.float64)
    updated_weights = weights - learning_rate * gradients

    return updated_weights


def train_logistic_regression(X, y, learning_rate=0.01, epochs=100):
    """
    Train a logistic regression model using gradient descent.
    
    This combines all the core functions to implement the full training loop.
    Each epoch, we compute gradients and use SGD to update weights.
    
    Args:
        X: Feature matrix, shape (n_samples, n_features) - list of lists or numpy array
        y: True binary labels, shape (n_samples,) - list or numpy array
        learning_rate: Step size for gradient descent - float
        epochs: Number of training iterations - int
    
    Returns:
        numpy array: Trained weight vector, shape (n_features,)
    
    Example:
        >>> X = [[1, 2], [1, 3], [1, 1]]  # Include bias feature
        >>> y = [1, 1, 0]
        >>> weights = train_logistic_regression(X, y, learning_rate=0.1, epochs=10)
        >>> len(weights)
        2
    """
    # TODO: Implement training loop
    # Steps:
    # 1. Convert inputs to numpy arrays
    # 2. Initialize weights to zeros (shape should match number of features)
    # 3. For each epoch:
    #    - Compute gradients using compute_gradients()
    #    - Update weights using sgd_step()
    # 4. Return final weights

    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    if X.size == 0 or y.size == 0:
        return np.zeros(X.shape[1] if X.ndim > 1 else 0)

    n_features = X.shape[1]
    weights = np.zeros(n_features, dtype=np.float64)

    for epoch in range(epochs):
        gradients = compute_gradients(X, y, weights)
        weights = sgd_step(weights, gradients, learning_rate)

    return weights


def logistic_predict(X, weights, threshold=0.5):
    """
    Make predictions using trained logistic regression model.
    
    This function uses the sigmoid function to compute probabilities,
    then applies a threshold to make binary predictions.
    
    Args:
        X: Feature matrix for prediction, shape (n_samples, n_features)
        weights: Trained weight vector, shape (n_features,)
        threshold: Decision threshold, typically 0.5 - float
    
    Returns:
        tuple: (predictions, probabilities)
            - predictions: Binary predictions (0 or 1) - list
            - probabilities: Predicted probabilities (0 to 1) - list
    
    Example:
        >>> X = [[1, 2], [1, 1]]  # Two samples with bias
        >>> weights = [0.5, 0.3] # Trained weights
        >>> predictions, probabilities = logistic_predict(X, weights)
        >>> len(predictions) == len(probabilities) == 2
        True
    """
    # TODO: Implement prediction
    # Steps:
    # 1. Convert inputs to numpy arrays
    # 2. Compute z = X @ weights (matrix multiplication)
    # 3. Compute probabilities using sigmoid(z)
    # 4. Apply threshold: predictions = probabilities >= threshold
    # 5. Convert to lists and return both predictions and probabilities
    X = np.array(X, dtype=np.float64)
    weights = np.array(weights, dtype=np.float64)

    if X.size == 0 or weights.size == 0:
        return [], []

    z = X @ weights
    probabilities = sigmoid(z)
    predictions = (probabilities >= threshold).astype(int)

    return predictions.tolist(), probabilities.tolist()


def calculate_accuracy(y_true, y_pred):
    """
    Calculate classification accuracy.
    
    Accuracy is the most intuitive performance measure - it's simply 
    the ratio of correctly predicted observations to total observations.
    
    Formula: accuracy = (correct predictions) / (total predictions)
    
    Args:
        y_true: True binary labels - list or numpy array
        y_pred: Predicted binary labels - list or numpy array
    
    Returns:
        float: Accuracy score between 0.0 and 1.0
    
    Example:
        >>> y_true = [1, 0, 1, 1, 0]
        >>> y_pred = [1, 0, 1, 0, 0] 
        >>> calculate_accuracy(y_true, y_pred)
        0.8  # 4 out of 5 correct
    """
    # TODO: Implement accuracy calculation
    # Hints:
    # 1. Convert to numpy arrays for easier comparison
    # 2. Count correct predictions: sum(y_true == y_pred)
    # 3. Divide by total predictions: len(y_true)
    # 4. Handle empty inputs
    return 0.0


def calculate_precision_recall(y_true, y_pred):
    """
    Calculate precision and recall for binary classification.
    
    Precision answers: "Of all positive predictions, how many were correct?"
    Recall answers: "Of all actual positives, how many did we find?"
    
    Formulas:
    - Precision = True Positives / (True Positives + False Positives)
    - Recall = True Positives / (True Positives + False Negatives)
    
    Args:
        y_true: True binary labels - list or numpy array
        y_pred: Predicted binary labels - list or numpy array
    
    Returns:
        tuple: (precision, recall) as floats
    
    Example:
        >>> y_true = [1, 1, 0, 1, 0]
        >>> y_pred = [1, 0, 0, 1, 1]  
        >>> precision, recall = calculate_precision_recall(y_true, y_pred)
        >>> precision  # 2 TP / (2 TP + 1 FP) = 0.667
        >>> recall     # 2 TP / (2 TP + 1 FN) = 0.667
    """
    # TODO: Implement precision and recall
    # Steps:
    # 1. Convert to numpy arrays
    # 2. Calculate True Positives: sum((y_true == 1) & (y_pred == 1))
    # 3. Calculate False Positives: sum((y_true == 0) & (y_pred == 1))
    # 4. Calculate False Negatives: sum((y_true == 1) & (y_pred == 0))
    # 5. Calculate precision and recall using formulas
    # 6. Handle edge cases (division by zero)
    return (0.0, 0.0)


def confusion_matrix(y_true, y_pred):
    """
    Generate a confusion matrix for binary classification.
    
    A confusion matrix shows the complete picture of classification performance:
    - True Negatives (TN): Correctly predicted negative
    - False Positives (FP): Incorrectly predicted positive  
    - False Negatives (FN): Incorrectly predicted negative
    - True Positives (TP): Correctly predicted positive
    
    Matrix format:
                Predicted
              0 (neg)  1 (pos)
    Actual 0   TN       FP
           1   FN       TP
    
    Args:
        y_true: True binary labels - list or numpy array
        y_pred: Predicted binary labels - list or numpy array
    
    Returns:
        dict: Confusion matrix with keys 'TN', 'FP', 'FN', 'TP'
    
    Example:
        >>> y_true = [0, 0, 1, 1]
        >>> y_pred = [0, 1, 0, 1]
        >>> confusion_matrix(y_true, y_pred)
        {'TN': 1, 'FP': 1, 'FN': 1, 'TP': 1}
    """
    # TODO: Implement confusion matrix calculation
    # Steps:
    # 1. Convert to numpy arrays
    # 2. Calculate each quadrant:
    #    - TN = sum((y_true == 0) & (y_pred == 0))
    #    - FP = sum((y_true == 0) & (y_pred == 1))
    #    - FN = sum((y_true == 1) & (y_pred == 0))
    #    - TP = sum((y_true == 1) & (y_pred == 1))
    # 3. Return as dictionary
    return {'TN': 0, 'FP': 0, 'FN': 0, 'TP': 0}


def compare_models(nb_preds, lr_preds, y_true):
    """
    Compare Naive Bayes and Logistic Regression models.
    
    This function provides a comprehensive comparison of the two models
    you implemented in Q3 and Q5, showing which performs better on
    different metrics.
    
    Args:
        nb_preds: Naive Bayes predictions - list or numpy array
        lr_preds: Logistic Regression predictions - list or numpy array  
        y_true: True binary labels - list or numpy array
    
    Returns:
        dict: Comparison results with accuracy, precision, recall for both models
        
        Format:
        {
            'naive_bayes': {'accuracy': float, 'precision': float, 'recall': float},
            'logistic_regression': {'accuracy': float, 'precision': float, 'recall': float},
            'winner': {'accuracy': str, 'precision': str, 'recall': str}  # 'nb' or 'lr'
        }
    
    Example:
        >>> nb_preds = [1, 0, 1, 0]
        >>> lr_preds = [1, 1, 1, 0] 
        >>> y_true = [1, 0, 1, 1]
        >>> compare_models(nb_preds, lr_preds, y_true)
        {'naive_bayes': {'accuracy': 0.75, ...}, 'logistic_regression': {...}, 'winner': {...}}
    """
    # TODO: Implement model comparison
    # Steps:
    # 1. Calculate accuracy, precision, recall for Naive Bayes
    # 2. Calculate accuracy, precision, recall for Logistic Regression
    # 3. Determine winner for each metric
    # 4. Return structured comparison dictionary
    return {
        'naive_bayes': {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0},
        'logistic_regression': {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0},
        'winner': {'accuracy': 'tie', 'precision': 'tie', 'recall': 'tie'}
    }


def analyze_errors(texts, y_true, y_pred):
    """
    Analyze misclassified examples to understand model weaknesses.
    
    This function helps you understand what types of texts your model
    struggles with, which is crucial for improving model performance.
    
    Args:
        texts: Original text samples - list of strings
        y_true: True binary labels - list or numpy array
        y_pred: Predicted binary labels - list or numpy array
    
    Returns:
        dict: Error analysis with misclassified examples and statistics
        
        Format:
        {
            'total_errors': int,
            'error_rate': float,
            'false_positives': list,  # Texts wrongly predicted as positive
            'false_negatives': list,  # Texts wrongly predicted as negative
            'error_stats': {
                'avg_length_errors': float,
                'avg_length_correct': float
            }
        }
    
    Example:
        >>> texts = ["good movie", "bad film", "great story", "poor plot"]
        >>> y_true = [1, 0, 1, 0]
        >>> y_pred = [1, 1, 1, 0]  # "bad film" misclassified as positive
        >>> analyze_errors(texts, y_true, y_pred)
        {'total_errors': 1, 'error_rate': 0.25, 'false_positives': ["bad film"], ...}
    """
    # TODO: Implement error analysis
    # Steps:
    # 1. Find indices of misclassified examples
    # 2. Separate into false positives and false negatives
    # 3. Calculate error statistics (length analysis, etc.)
    # 4. Return structured analysis
    return {
        'total_errors': 0,
        'error_rate': 0.0,
        'false_positives': [],
        'false_negatives': [],
        'error_stats': {
            'avg_length_errors': 0.0,
            'avg_length_correct': 0.0
        }
    }
