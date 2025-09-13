"""
MAI 5201 - Homework 1, Part 2
Library Implementation: Scikit-Learn ML Pipeline

In Part 1, you implemented machine learning algorithms from scratch to understand
the underlying mathematics and principles. Now in Part 2, you'll use scikit-learn
to build the same classifiers, comparing library performance with your custom implementations.

This demonstrates the power of well-optimized libraries while reinforcing your
understanding of the machine learning pipeline.

Your Name: Feliciann Elliot
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from typing import Tuple, Dict, Any
import json


class MovieReviewClassifier:
    """
    Complete movie review sentiment classification pipeline using scikit-learn.
    
    This class encapsulates the entire machine learning workflow:
    1. Data loading and preprocessing
    2. Train/test split (80/20)
    3. Feature extraction (bag-of-words and TF-IDF)
    4. Model training (Naive Bayes and Logistic Regression)
    5. Evaluation and comparison
    
    The goal is to achieve good performance on the test set using library implementations.
    """
    
    def __init__(self, data_path: str = None, random_state: int = 42):
        """
        Initialize the classifier pipeline.
        
        Args:
            data_path: Path to the movie reviews dataset
            random_state: Random seed for reproducibility
        """
        self.random_state = random_state
        self.data_path = data_path
        
        # Data storage
        self.X_train = None
        self.X_test = None 
        self.y_train = None
        self.y_test = None
        self.texts_train = None
        self.texts_test = None
        
        # Feature extractors
        self.count_vectorizer = None
        self.tfidf_vectorizer = None
        
        # Models
        self.nb_model = None
        self.lr_model = None
        
        # Results storage
        self.results = {}
    
    def load_data(self) -> Tuple[list, list]:
        """Load the movie reviews dataset."""
        if self.data_path and self.data_path.endswith('.csv'):
            # Load real dataset
            df = pd.read_csv(self.data_path)
            texts = df['review'].tolist()
            # Convert sentiment strings to numeric labels
            labels = [1 if sentiment == 'positive' else 0 for sentiment in df['sentiment'].tolist()]
            return texts, labels
        else:
            # TODO: Load data from CSV file
            # The CSV has columns 'review' and 'sentiment'
            # Convert 'positive' -> 1, 'negative' -> 0
            
            # Sample data for testing (remove when implementing)
            sample_texts = [
                "This movie was great! I loved it.",
                "Terrible film. Don't waste your time.",
                "Amazing story and great acting.",
                "Boring and predictable plot."
            ]
            sample_labels = [1, 0, 1, 0]  # 1=positive, 0=negative
            return sample_texts, sample_labels
    
    def split_data(self, texts: list, labels: list, test_size: float = 0.2) -> None:
        """
        Split data into training and testing sets.
        
        Args:
            texts: List of text samples
            labels: List of corresponding labels
            test_size: Fraction of data to use for testing (default 0.2 = 20%)
        """
        # TODO: Implement train/test split using sklearn.model_selection.train_test_split
        # Store results in self.texts_train, self.texts_test, self.y_train, self.y_test
        # Use self.random_state for reproducibility
        
        # Placeholder implementation
        split_idx = int(len(texts) * (1 - test_size))
        self.texts_train = texts[:split_idx]
        self.texts_test = texts[split_idx:]
        self.y_train = labels[:split_idx]
        self.y_test = labels[split_idx:]
        
        print(f"Data split: {len(self.texts_train)} train, {len(self.texts_test)} test samples")
    
    def extract_features(self, feature_type: str = 'count') -> None:
        """
        Extract features from text using scikit-learn vectorizers.
        
        Args:
            feature_type: Type of features to extract
                - 'count': Bag-of-words (CountVectorizer)  
                - 'tfidf': TF-IDF weighted features (TfidfVectorizer)
        """
        if feature_type == 'count':
            # TODO: Implement bag-of-words feature extraction
            # 1. Initialize CountVectorizer with appropriate parameters
            # 2. Fit on training texts and transform both train/test
            # 3. Store results in self.X_train, self.X_test
            
            # Placeholder
            self.count_vectorizer = CountVectorizer(
                lowercase=True,
                stop_words='english',
                max_features=10000,
                ngram_range=(1, 2)
            )
            train_texts = getattr(self, 'train_texts', getattr(self, 'X_train_text', getattr(self, 'train_X', self.X_train)))
            test_texts = getattr(self, 'test_texts', getattr(self, 'X_test_text', getattr(self, 'test_X', self.X_test)))

            self.X_train = self.count_vectorizer.fit_transform(self.texts_train)
            self.X_test = self.count_vectorizer.transform(self.texts_test)
            
            
        elif feature_type == 'tfidf':
            # TODO: Implement TF-IDF feature extraction
            # 1. Initialize TfidfVectorizer with appropriate parameters
            # 2. Fit on training texts and transform both train/test  
            # 3. Store results in self.X_train, self.X_test
            
            # Placeholder
            self.tfidf_vectorizer = TfidfVectorizer(
                lowercase=True,
                stop_words='english',
                max_features=10000,
                ngram_range=(1, 2)
            )
            
            self.X_train = self.tfidf_vectorizer.fit_transform(self.texts_train)
            self.X_test = self.tfidf_vectorizer.transform(self.texts_test)
            
        else:
            raise ValueError(f"Unknown feature type: {feature_type}")
    
    def train_naive_bayes(self) -> None:
        """
        Train a Naive Bayes classifier using scikit-learn.
        
        Use MultinomialNB which is appropriate for text classification
        with count/frequency features.
        """
        # TODO: Implement Naive Bayes training
        # 1. Initialize MultinomialNB classifier
        # 2. Fit on self.X_train and self.y_train
        # 3. Store trained model in self.nb_model
        
        self.nb_model = MultinomialNB()
        # self.nb_model.fit(self.X_train, self.y_train)
    
    def train_logistic_regression(self) -> None:
        """
        Train a Logistic Regression classifier using scikit-learn.
        
        Use appropriate parameters for text classification.
        """
        # TODO: Implement Logistic Regression training
        # 1. Initialize LogisticRegression with random_state=self.random_state
        # 2. Consider using max_iter parameter for convergence
        # 3. Fit on self.X_train and self.y_train
        # 4. Store trained model in self.lr_model
        
        self.lr_model = LogisticRegression(random_state=self.random_state)
        # self.lr_model.fit(self.X_train, self.y_train)
    
    def evaluate_model(self, model, model_name: str) -> Dict[str, float]:
        """
        Evaluate a trained model on the test set.
        
        Args:
            model: Trained scikit-learn model
            model_name: Name for storing results
            
        Returns:
            dict: Evaluation metrics (accuracy, precision, recall, f1)
        """
        # TODO: Implement model evaluation
        # 1. Make predictions on self.X_test
        # 2. Calculate accuracy using accuracy_score
        # 3. Calculate precision, recall, F1 using precision_recall_fscore_support
        # 4. Return metrics dictionary
        
        # Placeholder implementation
        predictions = [0] * len(self.y_test)  # Dummy predictions
        
        accuracy = accuracy_score(self.y_test, predictions)
        precision, recall, f1, _ = precision_recall_fscore_support(
            self.y_test, predictions, average='binary'
        )
        
        metrics = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }
        
        self.results[model_name] = metrics
        return metrics
    
    def compare_models(self) -> Dict[str, Any]:
        """
        Compare the performance of Naive Bayes and Logistic Regression.
        
        Returns:
            dict: Comprehensive comparison including metrics and winner analysis
        """
        if 'naive_bayes' not in self.results or 'logistic_regression' not in self.results:
            return {'error': 'Both models must be trained and evaluated first'}
        
        nb_results = self.results['naive_bayes']
        lr_results = self.results['logistic_regression']
        
        # Determine winners for each metric
        comparison = {
            'naive_bayes': nb_results,
            'logistic_regression': lr_results,
            'winners': {
                'accuracy': 'nb' if nb_results['accuracy'] > lr_results['accuracy'] 
                           else 'lr' if lr_results['accuracy'] > nb_results['accuracy'] 
                           else 'tie',
                'precision': 'nb' if nb_results['precision'] > lr_results['precision']
                            else 'lr' if lr_results['precision'] > nb_results['precision'] 
                            else 'tie',
                'recall': 'nb' if nb_results['recall'] > lr_results['recall']
                         else 'lr' if lr_results['recall'] > nb_results['recall'] 
                         else 'tie',
                'f1': 'nb' if nb_results['f1'] > lr_results['f1']
                     else 'lr' if lr_results['f1'] > nb_results['f1'] 
                     else 'tie'
            }
        }
        
        return comparison
    
    def run_complete_pipeline(self, feature_type: str = 'tfidf') -> Dict[str, Any]:
        """
        Run the complete machine learning pipeline.
        
        Args:
            feature_type: 'count' for bag-of-words, 'tfidf' for TF-IDF features
            
        Returns:
            dict: Complete results including individual model performance and comparison
        """
        print("🚀 Starting Movie Review Classification Pipeline")
        print("=" * 60)
        
        # Step 1: Load data
        print("📂 Loading movie reviews dataset...")
        texts, labels = self.load_data()
        print(f"   Loaded {len(texts)} reviews")
        
        # Step 2: Split data
        print("✂️  Splitting data (80% train, 20% test)...")
        self.split_data(texts, labels)
        
        # Step 3: Extract features
        print(f"🔧 Extracting {feature_type} features...")
        self.extract_features(feature_type)
        print(f"   Feature matrix shape: {getattr(self.X_train, 'shape', 'Not implemented')}")
        
        # Step 4: Train models
        print("🧠 Training Naive Bayes classifier...")
        self.train_naive_bayes()
        
        print("🧠 Training Logistic Regression classifier...")
        self.train_logistic_regression()
        
        # Step 5: Evaluate models
        print("📊 Evaluating models on test set...")
        nb_metrics = self.evaluate_model(self.nb_model, 'naive_bayes')
        lr_metrics = self.evaluate_model(self.lr_model, 'logistic_regression')
        
        print(f"   Naive Bayes Test Accuracy: {nb_metrics['accuracy']:.3f}")
        print(f"   Logistic Regression Test Accuracy: {lr_metrics['accuracy']:.3f}")
        
        # Step 6: Compare models
        print("🔍 Comparing model performance...")
        comparison = self.compare_models()
        
        print("✅ Pipeline complete!")
        print("=" * 60)
        
        return {
            'naive_bayes_metrics': nb_metrics,
            'logistic_regression_metrics': lr_metrics,
            'comparison': comparison,
            'feature_type': feature_type,
            'dataset_info': {
                'train_size': len(self.y_train),
                'test_size': len(self.y_test),
                'feature_dim': getattr(self.X_train, 'shape', (0, 0))[1] if hasattr(self.X_train, 'shape') else 0
            }
        }


# Main execution for testing
if __name__ == "__main__":
    # Create classifier instance
    classifier = MovieReviewClassifier()
    
    # Run complete pipeline
    results = classifier.run_complete_pipeline(feature_type='tfidf')
    
    # Print results summary
    print("\n📋 Results Summary:")
    print("-" * 40)
    nb_acc = results['naive_bayes_metrics']['accuracy']
    lr_acc = results['logistic_regression_metrics']['accuracy']
    print(f"Naive Bayes Accuracy: {nb_acc:.3f}")
    print(f"Logistic Regression Accuracy: {lr_acc:.3f}")
    print(f"Best Model: {'Naive Bayes' if nb_acc > lr_acc else 'Logistic Regression' if lr_acc > nb_acc else 'Tie'}")
