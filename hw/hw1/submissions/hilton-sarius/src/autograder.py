"""
MAI 5201 - Homework 1: Autograder
Text Feature Extraction and Machine Learning for NLP

This autograder tests student implementations.
Run with: python autograder.py
"""

import sys
import traceback
from typing import List, Tuple, Any

# Import student solutions
try:
    from text_features import extract_bag_of_words, build_vocabulary, text_to_vector
    from feature_engineering import add_ngram_features, compute_tf_idf_features, extract_feature_statistics, build_feature_matrix
    from naive_bayes import calculate_class_priors, calculate_feature_likelihoods, naive_bayes_predict, train_naive_bayes, evaluate_naive_bayes
    from logistic_regression import sigmoid, cross_entropy_loss, compute_gradients, sgd_step, train_logistic_regression, logistic_predict, calculate_accuracy, calculate_precision_recall, confusion_matrix, compare_models, analyze_errors
    from ml_pipeline import MovieReviewClassifier
    STUDENT_CODE_LOADED = True
except ImportError as e:
    print(f"❌ Error importing student code: {e}")
    print("Make sure all required files are in the src directory.")
    STUDENT_CODE_LOADED = False


class HW1Autograder:
    """Autograder for MAI 5201 HW1 - Complete (Q1-Q10)."""
    
    def __init__(self):
        self.total_score = 0
        # Total score: Q1:6 + Q2:8 + Q3:8 + Q4:8 + Q5:8 + Q6:12 + Q7:8 + Q8:8 + Q9:8 + Q10:6 = 80
        self.max_score = 80
        self.test_results = []

    def test_function(self, func_name: str, test_cases: List[Tuple], points: int) -> None:
        """Test a function with given test cases."""
        print(f"\n=== Testing {func_name} ({points} points) ===")
        
        if not STUDENT_CODE_LOADED:
            print(f"❌ Cannot test - student code not loaded")
            self.test_results.append((func_name, 0, points, "Student code not loaded"))
            return
        
        try:
            func = globals()[func_name]
        except KeyError:
            print(f"❌ Function {func_name} not found!")
            self.test_results.append((func_name, 0, points, "Function not implemented"))
            return

        passed = 0
        total = len(test_cases)
        errors = []

        for i, (args, expected) in enumerate(test_cases):
            try:
                if isinstance(args, tuple):
                    result = func(*args)
                else:
                    result = func(args)
                
                if self.compare_results(result, expected):
                    print(f"✅ Test case {i+1}: PASSED")
                    passed += 1
                else:
                    print(f"❌ Test case {i+1}: FAILED")
                    print(f"   Input: {args}")
                    print(f"   Expected: {expected}")
                    print(f"   Got: {result}")
                    errors.append(f"Test case {i+1}: Expected {expected}, got {result}")
                    
            except Exception as e:
                print(f"❌ Test case {i+1}: ERROR - {str(e)}")
                errors.append(f"Test case {i+1}: Exception - {str(e)}")

        score = int((passed / total) * points) if total > 0 else 0
        self.total_score += score
        
        print(f"Score: {score}/{points} ({passed}/{total} test cases passed)")
        self.test_results.append((func_name, score, points, errors))

    def compare_results(self, result: Any, expected: Any) -> bool:
        """Compare results, handling different types appropriately."""
        if expected == "tfidf_result":
            # Special case: TF-IDF results - check structure and non-negativity
            if not isinstance(result, list):
                return False
            if len(result) != 3:  # Should have 3 documents
                return False
            for vec in result:
                if not isinstance(vec, list) or len(vec) != 3:  # Should have 3 features
                    return False
                if not all(isinstance(x, (int, float)) and x >= 0 for x in vec):
                    return False
            return True
        elif expected == "matrix_result":
            # Special case: Feature matrix - check structure
            if not isinstance(result, tuple) or len(result) != 2:
                return False
            matrix, names = result
            if not isinstance(matrix, list) or not isinstance(names, list):
                return False
            if len(matrix) != 1:  # Should have 1 document
                return False
            if len(matrix[0]) != len(names):  # Matrix width should match feature names
                return False
            return True
        elif expected == "nb_prediction_result":
            # Special case: Naive Bayes prediction - check structure
            if not isinstance(result, tuple) or len(result) != 2:
                return False
            pred_class, probs = result
            if not isinstance(pred_class, int) or not isinstance(probs, dict):
                return False
            # Check that probabilities are reasonable
            if probs:
                prob_sum = sum(probs.values())
                if not (0.95 <= prob_sum <= 1.05):  # Allow small floating point errors
                    return False
                if not all(0 <= p <= 1 for p in probs.values()):
                    return False
            return True
        elif expected == "nb_train_result":
            # Special case: Naive Bayes training - check structure
            if not isinstance(result, tuple) or len(result) != 2:
                return False
            priors, likelihoods = result
            if not isinstance(priors, dict) or not isinstance(likelihoods, dict):
                return False
            # Basic structure check - should have same classes
            if set(priors.keys()) != set(likelihoods.keys()):
                return False
            return True
        elif expected == "loss_boundary_result":
            # Special case: Cross-entropy loss boundary - check for valid number
            try:
                import numpy as np
                return (isinstance(result, (int, float, np.number)) and 
                       not np.isnan(result) and not np.isinf(result) and result >= 0)
            except:
                return (isinstance(result, (int, float)) and 
                       result == result and result >= 0)  # Check for NaN and non-negative
        elif expected == "loss_approx_result":
            # Special case: Cross-entropy loss approximate - check range
            try:
                return (isinstance(result, (int, float)) and 
                       0.1 <= result <= 0.2)  # Should be around 0.17
            except:
                return False
        elif expected == "loss_single_result":
            # Special case: Single value loss - check range
            try:
                return (isinstance(result, (int, float)) and 
                       0.008 <= result <= 0.012)  # Should be around 0.010
            except:
                return False
        elif expected == "sigmoid_large_pos":
            # Special case: Sigmoid with large positive input - should be close to 1
            try:
                return (isinstance(result, (int, float)) and 
                       result >= 0.99999)  # Very close to 1
            except:
                return False
        elif expected == "sigmoid_large_neg":
            # Special case: Sigmoid with large negative input - should be close to 0
            try:
                return (isinstance(result, (int, float)) and 
                       result <= 1e-40)  # Very close to 0
            except:
                return False
        elif expected == "gradient_result":
            # Special case: Gradient computation - check approximate values
            try:
                import numpy as np
                if isinstance(result, np.ndarray) and result.shape == (2,):
                    return (abs(result[0] - (-0.16666666666666666)) < 1e-5 and
                           abs(result[1] - (-0.66666666666666674)) < 1e-5)
                elif isinstance(result, (list, tuple)) and len(result) == 2:
                    return (abs(result[0] - (-0.16666666666666666)) < 1e-5 and
                           abs(result[1] - (-0.66666666666666674)) < 1e-5)
                return False
            except:
                # For environments without numpy, check if result has right structure and reasonable values
                if isinstance(result, (list, tuple)) and len(result) == 2:
                    try:
                        return (abs(result[0] - (-0.16666666666666666)) < 1e-4 and
                               abs(result[1] - (-0.66666666666666674)) < 1e-4)
                    except:
                        return False
                return False
        elif expected == "gradient_simple_result":
            # Special case: Simple gradient test - check structure
            try:
                import numpy as np
                return isinstance(result, (list, tuple, np.ndarray)) and len(result) == 2
            except:
                return isinstance(result, (list, tuple)) and len(result) == 2
        elif expected == "gradient_empty_result":
            # Special case: Empty gradient result - should return empty array
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.size == 0
            except:
                return isinstance(result, list) and len(result) == 0
        # Q5 Special cases
        elif expected == "sgd_empty_result":
            # Special case: SGD with empty inputs
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.size == 0
            except:
                return isinstance(result, list) and len(result) == 0
        elif expected == "sgd_basic_result":
            # Special case: Basic SGD test
            try:
                import numpy as np
                expected_vals = [0.095, 0.21]
                if isinstance(result, np.ndarray) and result.shape == (2,):
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                elif isinstance(result, (list, tuple)) and len(result) == 2:
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                return False
            except:
                return False
        elif expected == "sgd_different_result":
            # Special case: Different values SGD test
            try:
                import numpy as np
                expected_vals = [0.9, -0.65]
                if isinstance(result, np.ndarray) and result.shape == (2,):
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                elif isinstance(result, (list, tuple)) and len(result) == 2:
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                return False
            except:
                return False
        elif expected == "sgd_zeros_result":
            # Special case: From zeros SGD test
            try:
                import numpy as np
                expected_vals = [-0.1, -0.2]
                if isinstance(result, np.ndarray) and result.shape == (2,):
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                elif isinstance(result, (list, tuple)) and len(result) == 2:
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                return False
            except:
                return False
        elif expected == "sgd_zero_grad_result":
            # Special case: Zero gradients SGD test
            try:
                import numpy as np
                expected_vals = [1.5, 2.5]
                if isinstance(result, np.ndarray) and result.shape == (2,):
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                elif isinstance(result, (list, tuple)) and len(result) == 2:
                    return (abs(result[0] - expected_vals[0]) < 1e-10 and
                           abs(result[1] - expected_vals[1]) < 1e-10)
                return False
            except:
                return False
        elif expected == "train_simple_result":
            # Special case: Simple training result - check if weights array has right structure
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.shape == (2,)
            except:
                return isinstance(result, (list, tuple)) and len(result) == 2
        elif expected == "train_standard_result":
            # Special case: Standard training result - check weights structure 
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.shape == (2,)
            except:
                return isinstance(result, (list, tuple)) and len(result) == 2
        elif expected == "train_single_result":
            # Special case: Single sample training
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.shape == (2,)
            except:
                return isinstance(result, (list, tuple)) and len(result) == 2
        elif expected == "train_empty_result":
            # Special case: Empty training data
            try:
                import numpy as np
                return isinstance(result, np.ndarray) and result.size == 0
            except:
                return isinstance(result, list) and len(result) == 0
        elif expected == "predict_standard_result":
            # Special case: Standard prediction - check for tuple of (predictions, probabilities)
            if isinstance(result, tuple) and len(result) == 2:
                predictions, probabilities = result
                return (isinstance(predictions, list) and len(predictions) == 2 and
                        isinstance(probabilities, list) and len(probabilities) == 2)
            return False
        elif expected == "predict_zero_weights":
            # Special case: Zero weights prediction - probabilities should be around 0.5
            if isinstance(result, tuple) and len(result) == 2:
                predictions, probabilities = result
                if len(probabilities) == 2:
                    # With zero weights, sigmoid(0) = 0.5, so predictions depend on threshold
                    return all(0.4 <= p <= 0.6 for p in probabilities)
            return False
        elif expected == "predict_different_threshold":
            # Special case: Different threshold prediction
            if isinstance(result, tuple) and len(result) == 2:
                predictions, probabilities = result
                return (isinstance(predictions, list) and len(predictions) == 1 and
                        isinstance(probabilities, list) and len(probabilities) == 1)
            return False
        elif expected == "predict_empty_result":
            # Special case: Empty prediction
            if isinstance(result, tuple) and len(result) == 2:
                predictions, probabilities = result
                return (isinstance(predictions, list) and len(predictions) == 0 and
                        isinstance(probabilities, list) and len(probabilities) == 0)
            return False
        # Q6 Special cases
        elif expected == "accuracy_empty_result":
            # Special case: Empty accuracy calculation
            return result == 0.0
        elif expected == "pr_standard_result":
            # Special case: Standard precision/recall test
            if isinstance(result, tuple) and len(result) == 2:
                precision, recall = result
                # Expected: precision=2/(2+1)=0.667, recall=2/(2+1)=0.667
                return (abs(precision - (2/3)) < 1e-10 and abs(recall - (2/3)) < 1e-10)
            return False
        elif expected == "pr_no_positives":
            # Special case: No positive predictions or labels
            if isinstance(result, tuple) and len(result) == 2:
                precision, recall = result
                return precision == 0.0 and recall == 0.0
            return False
        elif expected == "compare_standard_result":
            # Special case: Standard model comparison
            if isinstance(result, dict) and 'naive_bayes' in result:
                return ('logistic_regression' in result and 'winner' in result and
                        isinstance(result['naive_bayes'], dict) and
                        isinstance(result['logistic_regression'], dict) and
                        isinstance(result['winner'], dict))
            return False
        elif expected == "compare_different_result":
            # Special case: Different performance comparison
            return isinstance(result, dict) and 'winner' in result
        elif expected == "compare_empty_result":
            # Special case: Empty model comparison
            return isinstance(result, dict) and 'winner' in result
        elif expected == "error_analysis_result":
            # Special case: Error analysis with misclassifications
            if isinstance(result, dict):
                required_keys = ['total_errors', 'error_rate', 'false_positives', 'false_negatives', 'error_stats']
                return all(key in result for key in required_keys)
            return False
        elif expected == "error_no_errors_result":
            # Special case: No errors in predictions
            if isinstance(result, dict):
                return (result.get('total_errors') == 0 and 
                       result.get('error_rate') == 0.0)
            return False
        elif expected == "error_empty_result":
            # Special case: Empty error analysis
            return isinstance(result, dict) and 'total_errors' in result
        elif isinstance(expected, dict) and isinstance(result, dict):
            # Handle dictionary comparison with floating point tolerance
            if set(expected.keys()) != set(result.keys()):
                return False
            for key in expected:
                exp_val = expected[key]
                res_val = result[key]
                if isinstance(exp_val, float) and isinstance(res_val, float):
                    if abs(exp_val - res_val) > 1e-10:
                        return False
                elif isinstance(exp_val, list) and isinstance(res_val, list):
                    if len(exp_val) != len(res_val):
                        return False
                    for e, r in zip(exp_val, res_val):
                        if isinstance(e, float) and isinstance(r, float):
                            if abs(e - r) > 1e-10:
                                return False
                        elif e != r:
                            return False
                else:
                    if exp_val != res_val:
                        return False
            return True
        elif isinstance(expected, list) and isinstance(result, list):
            if len(expected) != len(result):
                return False
            # Handle list of dictionaries (for statistics)
            if expected and isinstance(expected[0], dict):
                for exp_dict, res_dict in zip(expected, result):
                    for key in exp_dict:
                        if key not in res_dict:
                            return False
                        # Allow small floating point differences
                        if isinstance(exp_dict[key], float):
                            if abs(exp_dict[key] - res_dict[key]) > 1e-10:
                                return False
                        else:
                            if exp_dict[key] != res_dict[key]:
                                return False
                return True
            return result == expected
        else:
            # Handle floating point tolerance for simple numeric comparisons
            if isinstance(expected, float) and isinstance(result, (int, float)):
                return abs(expected - result) < 1e-10
            return result == expected

    def test_q1(self) -> None:
        """Test Q1: Text Feature Extraction functions."""
        
        # Test extract_bag_of_words (2 points)
        print("\n" + "="*60)
        print("Q1: Text Feature Extraction")
        print("="*60)
        
        bow_test_cases = [
            ("This movie was great! I loved this great movie.", 
             {'this': 2, 'movie': 2, 'was': 1, 'great': 2, 'i': 1, 'loved': 1}),
            ("Bad movie. Really bad!",
             {'bad': 2, 'movie': 1, 'really': 1}),
            ("The BEST movie EVER! Amazing movie.",
             {'the': 1, 'best': 1, 'movie': 2, 'ever': 1, 'amazing': 1}),
            ("", {}),
            ("   ", {})
        ]
        self.test_function("extract_bag_of_words", bow_test_cases, 2)
        
        # Test build_vocabulary (2 points)  
        vocab_test_cases = [
            (["good movie", "bad movie", "great film"],
             {'bad': 0, 'film': 1, 'good': 2, 'great': 3, 'movie': 4}),
            (["I love movies", "movies are fun", "fun times"],
             {'are': 0, 'fun': 1, 'i': 2, 'love': 3, 'movies': 4, 'times': 5}),
            ([], {}),
            (["same same same"], {'same': 0})
        ]
        self.test_function("build_vocabulary", vocab_test_cases, 2)
        
        # Test text_to_vector (2 points)
        vector_test_cases = [
            (("good movie", {"good": 0, "movie": 1, "bad": 2, "great": 3}), [1, 1, 0, 0]),
            (("bad movie great movie", {"good": 0, "movie": 1, "bad": 2, "great": 3}), [0, 2, 1, 1]),
            (("unknown words here", {"good": 0, "movie": 1, "bad": 2}), [0, 0, 0]),
            (("", {"good": 0, "movie": 1, "bad": 2}), [0, 0, 0]),
            (("great great great", {"good": 0, "movie": 1, "bad": 2, "great": 3}), [0, 0, 0, 3])
        ]
        self.test_function("text_to_vector", vector_test_cases, 2)

    def test_q2(self) -> None:
        """Test Q2: Feature Engineering functions."""
        
        print("\n" + "="*60)
        print("Q2: Feature Engineering")
        print("="*60)
        
        # Test add_ngram_features (2 points)
        ngram_test_cases = [
            (["good movie", "bad movie"], 2,
             {'bad': 0, 'bad movie': 1, 'good': 2, 'good movie': 3, 'movie': 4}),
            (["not good"], 2,
             {'good': 0, 'not': 1, 'not good': 2}),
            (["great film ever"], 3,
             {'ever': 0, 'film': 1, 'film ever': 2, 'great': 3, 'great film': 4, 'great film ever': 5}),
            ([], 2, {}),
            ([""], 2, {})
        ]
        
        # Convert to proper test format for test_function
        formatted_ngram_cases = []
        for texts, n, expected in ngram_test_cases:
            formatted_ngram_cases.append(((texts, n), expected))
        
        self.test_function("add_ngram_features", formatted_ngram_cases, 2)
        
        # Test compute_tf_idf_features (2 points)
        # Simplified test cases with expected approximate results
        vocab_simple = {"good": 0, "movie": 1, "bad": 2}
        texts_simple = ["good movie", "bad movie movie", "good good"]
        
        tfidf_test_cases = [
            ((texts_simple, vocab_simple), "tfidf_result"),  # Special marker for TF-IDF
            (([], {}), []),
            (([""], {"word": 0}), [[0.0]])
        ]
        self.test_function("compute_tf_idf_features", tfidf_test_cases, 2)
        
        # Test extract_feature_statistics (2 points)
        stats_test_cases = [
            (["Great movie!"], [{
                'word_count': 2, 'char_count': 10, 'sentence_count': 1,
                'avg_word_length': 5.0, 'vocab_diversity': 1.0,
                'exclamation_count': 1, 'question_count': 0, 'uppercase_ratio': 0.08333333333333333
            }]),
            ([""], [{
                'word_count': 0, 'char_count': 0, 'sentence_count': 0,
                'avg_word_length': 0.0, 'vocab_diversity': 0.0,
                'exclamation_count': 0, 'question_count': 0, 'uppercase_ratio': 0.0
            }])
        ]
        self.test_function("extract_feature_statistics", stats_test_cases, 2)
        
        # Test build_feature_matrix (2 points)  
        config_test_cases = [
            ((["good movie"], {'use_unigrams': True, 'use_bigrams': False, 'use_tfidf': False, 'use_statistics': False}), "matrix_result"),
            (([], {}), ([], []))
        ]
        self.test_function("build_feature_matrix", config_test_cases, 2)

    def test_q3(self) -> None:
        """Test Q3: Naive Bayes functions."""
        
        print("\n" + "="*60)
        print("Q3: Naive Bayes from Scratch")
        print("="*60)
        
        # Test calculate_class_priors (2 points)
        priors_test_cases = [
            ([0, 0, 1, 1, 1], {0: 0.4, 1: 0.6}),
            ([1, 1, 1, 1], {1: 1.0}),
            ([0, 1, 2, 0, 1], {0: 0.4, 1: 0.4, 2: 0.2}),
            ([], {})
        ]
        self.test_function("calculate_class_priors", priors_test_cases, 2)
        
        # Test calculate_feature_likelihoods (3 points)
        vectors = [[1, 0, 2], [0, 1, 1], [2, 0, 0]]
        labels = [1, 0, 1]
        expected_likelihoods = {
            1: [0.5, 0.125, 0.375],  # Class 1: counts [3,0,2] -> smoothed probs
            0: [0.2, 0.4, 0.4]   # Class 0: counts [0,1,1] -> smoothed probs  
        }
        
        likelihood_test_cases = [
            ((vectors, labels), expected_likelihoods),
            (([], []), {}),
            (([[1, 1], [0, 1]], [1, 1]), {1: [0.4, 0.6]})
        ]
        self.test_function("calculate_feature_likelihoods", likelihood_test_cases, 3)
        
        # Test naive_bayes_predict (2 points)
        vector = [1, 0, 1]
        priors = {0: 0.5, 1: 0.5}
        likelihoods = {0: [0.3, 0.4, 0.3], 1: [0.6, 0.2, 0.2]}
        
        predict_test_cases = [
            ((vector, priors, likelihoods), "nb_prediction_result"),  # Special marker
            (([0, 0, 0], {0: 1.0}, {0: [0.5, 0.5, 0.0]}), (0, {0: 1.0})),
            (([], {}, {}), (0, {}))
        ]
        self.test_function("naive_bayes_predict", predict_test_cases, 2)
        
        # Test train_naive_bayes (1 point)
        train_vectors = [[1, 0], [0, 1], [1, 1]]
        train_labels = [0, 1, 1]
        
        train_test_cases = [
            ((train_vectors, train_labels), "nb_train_result"),  # Special marker
            (([], []), ({}, {}))
        ]
        self.test_function("train_naive_bayes", train_test_cases, 1)

    def test_q4(self) -> None:
        """Test Q4: Logistic Regression Core Functions."""
        
        print("\n" + "="*60)
        print("Q4: Logistic Regression Core Functions")
        print("="*60)
        
        # Test sigmoid function (2 points)
        import numpy as np
        sigmoid_test_cases = [
            (0, 0.5),
            (2, 0.8807970779778823),  # approximately
            (-2, 0.11920292202211755),  # approximately
            (100, "sigmoid_large_pos"),  # Should handle large values
            (-100, "sigmoid_large_neg")  # Should handle large negative values
        ]
        self.test_function("sigmoid", sigmoid_test_cases, 2)
        
        # Test cross_entropy_loss (3 points) 
        loss_test_cases = [
            (([1, 0, 1], [0.9, 0.1, 0.8]), "loss_approx_result"),  # Use special marker for approximate
            (([1, 1, 0], [0.5, 0.5, 0.5]), 0.6931471805599453),  # log(2)
            (([1], [0.99]), "loss_single_result"),  # Special marker for single value
            (([0], [0.01]), "loss_single_result"),  # Special marker for single value
            (([1, 0], [1.0, 0.0]), "loss_boundary_result")  # Special marker for boundary case
        ]
        self.test_function("cross_entropy_loss", loss_test_cases, 3)
        
        # Test compute_gradients (3 points)
        X = [[1, 2], [1, 3], [1, 1]]  # Include bias feature
        y = [1, 1, 0]
        weights = [0.0, 0.0]
        
        gradients_test_cases = [
            ((X, y, weights), "gradient_result"),  # Special marker
            (([[1, 1], [1, 0]], [1, 0], [0.0, 0.0]), "gradient_simple_result"),
            (([], [], []), "gradient_empty_result")  # Edge case
        ]
        self.test_function("compute_gradients", gradients_test_cases, 3)

    def test_q5(self) -> None:
        """Test Q5: SGD Implementation (8 points total)."""
        print("\n" + "=" * 60)
        print("Q5: SGD Implementation")
        print("=" * 60)

        # Test sgd_step (3 points)
        sgd_test_cases = [
            (([0.1, 0.2], [0.05, -0.1], 0.1), "sgd_basic_result"),     # Basic test
            (([1.0, -0.5], [0.2, 0.3], 0.5), "sgd_different_result"), # Different values
            (([0.0, 0.0], [0.1, 0.2], 1.0), "sgd_zeros_result"),      # From zeros
            (([1.5, 2.5], [0.0, 0.0], 0.1), "sgd_zero_grad_result"),  # Zero gradients
            (([], [], 0.1), "sgd_empty_result")                       # Edge case
        ]
        self.test_function("sgd_step", sgd_test_cases, 3)

        # Test train_logistic_regression (3 points)
        X_simple = [[1, 1], [1, 0]]  # Simple 2x2 with bias
        y_simple = [1, 0]
        
        train_test_cases = [
            ((X_simple, y_simple, 0.1, 5), "train_simple_result"),    # Basic training
            (([[1, 2], [1, 3], [1, 1]], [1, 1, 0], 0.01, 10), "train_standard_result"),  # Standard case
            (([[1, 0]], [1], 0.1, 1), "train_single_result"),         # Single sample
            (([], [], 0.1, 5), "train_empty_result")                  # Edge case
        ]
        self.test_function("train_logistic_regression", train_test_cases, 3)

        # Test logistic_predict (2 points)
        X_pred = [[1, 2], [1, 1]]
        weights_pred = [0.5, 0.3]
        
        predict_test_cases = [
            ((X_pred, weights_pred, 0.5), "predict_standard_result"),      # Standard prediction
            (([[1, 0], [1, 1]], [0.0, 0.0], 0.5), "predict_zero_weights"), # Zero weights
            (([[1, 1]], [1.0, 1.0], 0.3), "predict_different_threshold"),  # Different threshold
            (([], [], 0.5), "predict_empty_result")                        # Edge case
        ]
        self.test_function("logistic_predict", predict_test_cases, 2)

    def test_q6(self) -> None:
        """Test Q6: Model Evaluation and Comparison (12 points total)."""
        print("\n" + "=" * 60)
        print("Q6: Model Evaluation and Comparison")
        print("=" * 60)

        # Test calculate_accuracy (3 points)
        accuracy_test_cases = [
            (([1, 0, 1, 1, 0], [1, 0, 1, 0, 0]), 0.8),        # 4/5 correct
            (([1, 1, 1], [1, 1, 1]), 1.0),                     # Perfect accuracy
            (([0, 0, 0], [1, 1, 1]), 0.0),                     # Zero accuracy
            (([1, 0], [0, 1]), 0.0),                          # All wrong
            (([], []), "accuracy_empty_result")                # Empty case
        ]
        self.test_function("calculate_accuracy", accuracy_test_cases, 3)

        # Test calculate_precision_recall (3 points)
        pr_test_cases = [
            (([1, 1, 0, 1, 0], [1, 0, 0, 1, 1]), "pr_standard_result"),   # Standard case
            (([1, 1, 1], [1, 1, 1]), (1.0, 1.0)),                         # Perfect P&R
            (([0, 0, 0], [0, 0, 0]), "pr_no_positives"),                   # No positives
            (([1, 1, 1], [0, 0, 0]), (0.0, 0.0)),                         # Zero P&R
            (([], []), (0.0, 0.0))                                        # Empty case
        ]
        self.test_function("calculate_precision_recall", pr_test_cases, 3)

        # Test confusion_matrix (2 points)
        cm_test_cases = [
            (([0, 0, 1, 1], [0, 1, 0, 1]), {'TN': 1, 'FP': 1, 'FN': 1, 'TP': 1}),  # Balanced
            (([1, 1, 1], [1, 1, 1]), {'TN': 0, 'FP': 0, 'FN': 0, 'TP': 3}),        # All TP
            (([0, 0], [0, 0]), {'TN': 2, 'FP': 0, 'FN': 0, 'TP': 0}),              # All TN
            (([], []), {'TN': 0, 'FP': 0, 'FN': 0, 'TP': 0})                       # Empty
        ]
        self.test_function("confusion_matrix", cm_test_cases, 2)

        # Test compare_models (2 points)
        compare_test_cases = [
            (([1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 1]), "compare_standard_result"),  # Standard comparison
            (([1, 1], [0, 0], [1, 0]), "compare_different_result"),                   # Different performance
            (([], [], []), "compare_empty_result")                                    # Empty case
        ]
        self.test_function("compare_models", compare_test_cases, 2)

        # Test analyze_errors (2 points)
        error_test_cases = [
            ((["good movie", "bad film", "great story", "poor plot"], [1, 0, 1, 0], [1, 1, 1, 0]), "error_analysis_result"),
            ((["text1", "text2"], [1, 0], [1, 0]), "error_no_errors_result"),       # No errors
            (([], [], []), "error_empty_result")                                     # Empty case
        ]
        self.test_function("analyze_errors", error_test_cases, 2)

    def test_q7(self) -> None:
        """Test Q7: Basic Pipeline Functionality (8 points)."""
        print("\n" + "=" * 60)
        print("Q7: Basic Pipeline Functionality (8 points)")
        print("=" * 60)
        
        if not STUDENT_CODE_LOADED:
            print("❌ Cannot test Q7 - student code not loaded")
            self.test_results.append(("Q7_Pipeline_Setup", 0, 8, ["Student code not loaded"]))
            return
        
        score = 0
        errors = []
        
        try:
            # Test 1: Pipeline initialization (2 points)
            print("Testing pipeline initialization...")
            classifier = MovieReviewClassifier(data_path="data/reviews.csv", random_state=42)
            if hasattr(classifier, 'random_state') and classifier.random_state == 42:
                print("✅ Pipeline initialization: PASSED")
                score += 2
                self.total_score += 2
            else:
                print("❌ Pipeline initialization: FAILED")
                errors.append("Pipeline initialization failed")
            
            # Test 2: Data loading (2 points)
            print("Testing data loading...")
            texts, labels = classifier.load_data()
            if isinstance(texts, list) and isinstance(labels, list) and len(texts) > 0:
                print("✅ Data loading: PASSED")
                score += 2
                self.total_score += 2
            else:
                print("❌ Data loading: FAILED")
                errors.append("Data loading returned invalid format")
            
            # Test 3: Data splitting (2 points)
            print("Testing train/test split...")
            classifier.split_data(texts, labels, test_size=0.2)
            if (hasattr(classifier, 'texts_train') and hasattr(classifier, 'y_test') and
                len(classifier.texts_train) > 0 and len(classifier.y_test) > 0):
                print("✅ Data splitting: PASSED")
                score += 2
                self.total_score += 2
            else:
                print("❌ Data splitting: FAILED")
                errors.append("Data splitting failed to create train/test sets")
            
            # Test 4: Feature extraction (2 points)
            print("Testing feature extraction...")
            classifier.extract_features('tfidf')
            if (hasattr(classifier, 'X_train') and hasattr(classifier, 'X_test') and
                classifier.X_train is not None and classifier.X_test is not None):
                print("✅ Feature extraction: PASSED")
                score += 2
                self.total_score += 2
            else:
                print("❌ Feature extraction: FAILED")
                errors.append("Feature extraction failed to create feature matrices")
                
        except Exception as e:
            print(f"❌ Q7 test failed: {e}")
            errors.append(f"Exception in Q7: {str(e)}")
        
        self.test_results.append(("Q7_Pipeline_Setup", score, 8, errors))

    def test_q8(self) -> None:
        """Test Q8: Model Training (8 points)."""
        print("\n" + "=" * 60)
        print("Q8: Model Training (8 points)")
        print("=" * 60)
        
        if not STUDENT_CODE_LOADED:
            print("❌ Cannot test Q8 - student code not loaded")
            self.test_results.append(("Q8_Model_Training", 0, 8, ["Student code not loaded"]))
            return
        
        score = 0
        errors = []
        
        try:
            # Set up pipeline
            classifier = MovieReviewClassifier(data_path="data/reviews.csv", random_state=42)
            texts, labels = classifier.load_data()
            classifier.split_data(texts, labels, test_size=0.2)
            classifier.extract_features('tfidf')
            
            # Test 1: Naive Bayes training (4 points)
            print("Testing Naive Bayes training...")
            classifier.train_naive_bayes()
            if hasattr(classifier, 'nb_model') and classifier.nb_model is not None:
                if hasattr(classifier.nb_model, 'predict'):
                    try:
                        predictions = classifier.nb_model.predict(classifier.X_test)
                        if len(predictions) == len(classifier.y_test):
                            print("✅ Naive Bayes training: PASSED")
                            score += 4
                            self.total_score += 4
                        else:
                            print("❌ Naive Bayes training: FAILED (wrong prediction shape)")
                            errors.append("Naive Bayes predictions have wrong shape")
                    except:
                        print("❌ Naive Bayes training: FAILED (prediction error)")
                        errors.append("Naive Bayes model cannot make predictions")
                else:
                    print("❌ Naive Bayes training: FAILED (no predict method)")
                    errors.append("Naive Bayes model has no predict method")
            else:
                print("❌ Naive Bayes training: FAILED (no model)")
                errors.append("Naive Bayes model not created")
            
            # Test 2: Logistic Regression training (4 points)
            print("Testing Logistic Regression training...")
            classifier.train_logistic_regression()
            if hasattr(classifier, 'lr_model') and classifier.lr_model is not None:
                if hasattr(classifier.lr_model, 'predict'):
                    try:
                        predictions = classifier.lr_model.predict(classifier.X_test)
                        if len(predictions) == len(classifier.y_test):
                            print("✅ Logistic Regression training: PASSED")
                            score += 4
                            self.total_score += 4
                        else:
                            print("❌ Logistic Regression training: FAILED (wrong prediction shape)")
                            errors.append("Logistic Regression predictions have wrong shape")
                    except:
                        print("❌ Logistic Regression training: FAILED (prediction error)")
                        errors.append("Logistic Regression model cannot make predictions")
                else:
                    print("❌ Logistic Regression training: FAILED (no predict method)")
                    errors.append("Logistic Regression model has no predict method")
            else:
                print("❌ Logistic Regression training: FAILED (no model)")
                errors.append("Logistic Regression model not created")
                
        except Exception as e:
            print(f"❌ Q8 test failed: {e}")
            errors.append(f"Exception in Q8: {str(e)}")
        
        self.test_results.append(("Q8_Model_Training", score, 8, errors))

    def test_q9(self) -> None:
        """Test Q9: Performance Benchmarks (8 points) - TBD after running solution."""
        print("\n" + "=" * 60)
        print("Q9: Performance Benchmarks (8 points)")
        print("=" * 60)
        
        # Performance thresholds based on solution performance (~82%)
        min_accuracy_threshold = 0.75  # 75% accuracy minimum (achievable)
        min_f1_threshold = 0.75        # 75% F1 score minimum
        
        if not STUDENT_CODE_LOADED:
            print("❌ Cannot test Q9 - student code not loaded")
            self.test_results.append(("Q9_Performance", 0, 8, ["Student code not loaded"]))
            return
        
        score = 0
        errors = []
        
        try:
            # Run complete pipeline
            classifier = MovieReviewClassifier(data_path="data/reviews.csv", random_state=42)
            results = classifier.run_complete_pipeline('tfidf')
            
            if 'naive_bayes_metrics' not in results or 'logistic_regression_metrics' not in results:
                print("❌ Performance test failed: Missing results")
                errors.append("Pipeline did not return proper results")
                self.test_results.append(("Q9_Performance", score, 8, errors))
                return
            
            nb_metrics = results['naive_bayes_metrics']
            lr_metrics = results['logistic_regression_metrics']
            
            # Test 1: Naive Bayes performance (4 points)
            print("Testing Naive Bayes performance...")
            nb_accuracy = nb_metrics.get('accuracy', 0)
            nb_f1 = nb_metrics.get('f1', 0)
            
            points_earned = 0
            if nb_accuracy >= min_accuracy_threshold:
                print(f"✅ NB Accuracy: {nb_accuracy:.3f} >= {min_accuracy_threshold}")
                points_earned += 2
                self.total_score += 2
            else:
                print(f"❌ NB Accuracy: {nb_accuracy:.3f} < {min_accuracy_threshold}")
                errors.append(f"Naive Bayes accuracy {nb_accuracy:.3f} below threshold {min_accuracy_threshold}")
            
            if nb_f1 >= min_f1_threshold:
                print(f"✅ NB F1-Score: {nb_f1:.3f} >= {min_f1_threshold}")
                points_earned += 2
                self.total_score += 2
            else:
                print(f"❌ NB F1-Score: {nb_f1:.3f} < {min_f1_threshold}")
                errors.append(f"Naive Bayes F1 {nb_f1:.3f} below threshold {min_f1_threshold}")
            
            score += points_earned
            print(f"Naive Bayes Performance: {points_earned}/4 points")
            
            # Test 2: Logistic Regression performance (4 points)
            print("Testing Logistic Regression performance...")
            lr_accuracy = lr_metrics.get('accuracy', 0)
            lr_f1 = lr_metrics.get('f1', 0)
            
            points_earned = 0
            if lr_accuracy >= min_accuracy_threshold:
                print(f"✅ LR Accuracy: {lr_accuracy:.3f} >= {min_accuracy_threshold}")
                points_earned += 2
                self.total_score += 2
            else:
                print(f"❌ LR Accuracy: {lr_accuracy:.3f} < {min_accuracy_threshold}")
                errors.append(f"Logistic Regression accuracy {lr_accuracy:.3f} below threshold {min_accuracy_threshold}")
            
            if lr_f1 >= min_f1_threshold:
                print(f"✅ LR F1-Score: {lr_f1:.3f} >= {min_f1_threshold}")
                points_earned += 2
                self.total_score += 2
            else:
                print(f"❌ LR F1-Score: {lr_f1:.3f} < {min_f1_threshold}")
                errors.append(f"Logistic Regression F1 {lr_f1:.3f} below threshold {min_f1_threshold}")
            
            score += points_earned
            print(f"Logistic Regression Performance: {points_earned}/4 points")
                
        except Exception as e:
            print(f"❌ Q9 test failed: {e}")
            errors.append(f"Exception in Q9: {str(e)}")
        
        self.test_results.append(("Q9_Performance", score, 8, errors))

    def test_q10(self) -> None:
        """Test Q10: Pipeline Integration & Comparison (6 points)."""
        print("\n" + "=" * 60)
        print("Q10: Pipeline Integration & Comparison (6 points)")
        print("=" * 60)
        
        if not STUDENT_CODE_LOADED:
            print("❌ Cannot test Q10 - student code not loaded")
            self.test_results.append(("Q10_Integration", 0, 6, ["Student code not loaded"]))
            return
        
        score = 0
        errors = []
        
        try:
            # Test 1: Complete pipeline execution (3 points)
            print("Testing complete pipeline execution...")
            classifier = MovieReviewClassifier(data_path="data/reviews.csv", random_state=42)
            results = classifier.run_complete_pipeline('tfidf')
            
            required_keys = ['naive_bayes_metrics', 'logistic_regression_metrics', 'comparison', 'dataset_info']
            if all(key in results for key in required_keys):
                print("✅ Pipeline execution: PASSED")
                score += 3
                self.total_score += 3
            else:
                missing_keys = [key for key in required_keys if key not in results]
                print(f"❌ Pipeline execution: FAILED (missing keys: {missing_keys})")
                errors.append(f"Pipeline results missing keys: {missing_keys}")
            
            # Test 2: Model comparison functionality (3 points)
            print("Testing model comparison...")
            comparison = results.get('comparison', {})
            if ('naive_bayes' in comparison and 'logistic_regression' in comparison and 
                'winners' in comparison):
                winners = comparison['winners']
                if all(metric in winners for metric in ['accuracy', 'precision', 'recall', 'f1']):
                    print("✅ Model comparison: PASSED")
                    score += 3
                    self.total_score += 3
                else:
                    print("❌ Model comparison: FAILED (missing winner metrics)")
                    errors.append("Model comparison missing winner metrics")
            else:
                print("❌ Model comparison: FAILED (invalid structure)")
                errors.append("Model comparison has invalid structure")
                
        except Exception as e:
            print(f"❌ Q10 test failed: {e}")
            errors.append(f"Exception in Q10: {str(e)}")
        
        self.test_results.append(("Q10_Integration", score, 6, errors))

    def run_all_tests(self) -> None:
        """Run all test cases."""
        print("MAI 5201 - Homework 1 Autograder")
        print("Complete ML Implementation: From Scratch + Libraries")
        print("=" * 60)

        # Test Q1-Q6: From-scratch implementations
        print("\n🚀 PART 1: FROM-SCRATCH IMPLEMENTATIONS (Q1-Q6)")
        print("=" * 60)
        self.test_q1()
        self.test_q2()
        self.test_q3()
        self.test_q4()
        self.test_q5()
        self.test_q6()
        
        # Test Q7-Q10: Library implementations
        print("\n\n🚀 PART 2: LIBRARY IMPLEMENTATIONS (Q7-Q10)")
        print("=" * 60)
        self.test_q7()
        self.test_q8()
        self.test_q9()
        self.test_q10()
        
        # Final summary
        print("\n" + "=" * 60)
        print(f"TOTAL SCORE: {self.total_score}/{self.max_score}")
        print("=" * 60)
        
        if self.total_score == self.max_score:
            print("🎉 Congratulations! All tests passed!")
        elif self.total_score >= self.max_score * 0.8:
            print("👍 Good work! Most tests passed.")
        else:
            print("📝 Some tests failed. Review your implementations.")
        
        # Show detailed results
        if self.test_results:
            print(f"\nDetailed Results:")
            for func_name, score, max_points, errors in self.test_results:
                status = "✅" if score == max_points else "❌"
                print(f"{status} {func_name}: {score}/{max_points}")
                if errors and len(errors) <= 3:
                    for error in errors:
                        print(f"    • {error}")
        
        print(f"\nFinal Grade: {(self.total_score/self.max_score)*100:.1f}%")


def main():
    """Main function to run the autograder."""
    import sys
    
    grader = HW1Autograder()
    
    # Check for command line arguments
    if len(sys.argv) > 2 and sys.argv[1] == "-q":
        question = sys.argv[2].lower()
        if question == "q1":
            grader.test_q1()
            # Print Q1 specific summary
            print(f"\nQ1 SCORE: {grader.total_score}/6")
            if grader.total_score == 6:
                print("🎉 Q1: All tests passed!")
            else:
                print("📝 Q1: Some tests failed. Review your implementations.")
        elif question == "q2":
            grader.test_q2()
            # Print Q2 specific summary
            print(f"\nQ2 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q2: All tests passed!")
            else:
                print("📝 Q2: Some tests failed. Review your implementations.")
        elif question == "q3":
            grader.test_q3()
            # Print Q3 specific summary
            print(f"\nQ3 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q3: All tests passed!")
            else:
                print("📝 Q3: Some tests failed. Review your implementations.")
        elif question == "q4":
            grader.test_q4()
            # Print Q4 specific summary
            print(f"\nQ4 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q4: All tests passed!")
            else:
                print("📝 Q4: Some tests failed. Review your implementations.")
        elif question == "q5":
            grader.test_q5()
            # Print Q5 specific summary
            print(f"\nQ5 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q5: All tests passed!")
            else:
                print("📝 Q5: Some tests failed. Review your implementations.")
        elif question == "q6":
            grader.test_q6()
            # Print Q6 specific summary
            print(f"\nQ6 SCORE: {grader.total_score}/12")
            if grader.total_score == 12:
                print("🎉 Q6: All tests passed!")
            else:
                print("📝 Q6: Some tests failed. Review your implementations.")
        elif question == "q7":
            grader.test_q7()
            # Print Q7 specific summary
            print(f"\nQ7 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q7: All tests passed!")
            else:
                print("📝 Q7: Some tests failed. Review your implementations.")
        elif question == "q8":
            grader.test_q8()
            # Print Q8 specific summary
            print(f"\nQ8 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q8: All tests passed!")
            else:
                print("📝 Q8: Some tests failed. Review your implementations.")
        elif question == "q9":
            grader.test_q9()
            # Print Q9 specific summary
            print(f"\nQ9 SCORE: {grader.total_score}/8")
            if grader.total_score == 8:
                print("🎉 Q9: All tests passed!")
            else:
                print("📝 Q9: Some tests failed. Review your implementations.")
        elif question == "q10":
            grader.test_q10()
            # Print Q10 specific summary
            print(f"\nQ10 SCORE: {grader.total_score}/6")
            if grader.total_score == 6:
                print("🎉 Q10: All tests passed!")
            else:
                print("📝 Q10: Some tests failed. Review your implementations.")
        else:
            print(f"❌ Unknown question: {question}")
            print("Available questions: q1, q2, q3, q4, q5, q6, q7, q8, q9, q10")
            sys.exit(1)
    else:
        # Run all tests (Q1-Q10)
        grader.run_all_tests()


if __name__ == "__main__":
    main()
