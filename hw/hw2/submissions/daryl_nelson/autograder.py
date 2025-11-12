"""
MAI 5201 - Homework 2: Neural Networks for NLP
Basic Autograder for Testing Implementations

This autograder provides basic tests to verify your implementations work correctly.
Students should use this to check their code before submission.

Usage:
    python autograder.py          # Run all tests
    python autograder.py -q q1    # Run specific question tests
"""

import sys
import os
# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import torch
import torch.nn as nn
import numpy as np
from typing import Dict, Any


class HW2Autograder:
    """Basic autograder for HW2 implementations."""
    
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        self.verbose = True
    
    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(message)
    
    def test_assert(self, condition: bool, test_name: str, points: int = 1):
        """Assert a test condition and track results."""
        self.total_tests += 1
        if condition:
            self.passed_tests += 1
            self.log(f"✓ {test_name} ({points} pts)")
            return points
        else:
            self.log(f"✗ {test_name} (0/{points} pts)")
            return 0
    
    def test_q1_feedforward_classifier(self) -> int:
        """Test Q1: Feedforward Neural Classifier implementation."""
        self.log("\n" + "="*50)
        self.log("Testing Q1: Feedforward Neural Classifier")
        self.log("="*50)
        
        total_points = 0
        
        try:
            from src.basic_classifier import FeedforwardClassifier
            
            # Test 1: Model has properly initialized embedding layer (not None)
            vocab_size, embedding_dim, hidden_dim, num_classes = 1000, 128, 256, 2
            model = FeedforwardClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
            
            has_embedding = (hasattr(model, 'embedding') and 
                           model.embedding is not None and 
                           isinstance(model.embedding, nn.Embedding))
            total_points += self.test_assert(has_embedding, "Has embedding layer (not None)")
            
            # Test 2: Model has properly initialized hidden layers (not None)
            has_hidden1 = (hasattr(model, 'hidden1') and 
                          model.hidden1 is not None and 
                          isinstance(model.hidden1, nn.Linear))
            has_hidden2 = (hasattr(model, 'hidden2') and 
                          model.hidden2 is not None and 
                          isinstance(model.hidden2, nn.Linear))
            has_output = (hasattr(model, 'output') and 
                         model.output is not None and 
                         isinstance(model.output, nn.Linear))
            
            total_points += self.test_assert(has_hidden1 and has_hidden2 and has_output, 
                                           "Has properly initialized hidden layers (not None)")
            
            # Test 3: Forward pass actually works (produces valid output)
            batch_size, seq_len = 4, 20
            dummy_input = torch.randint(0, vocab_size, (batch_size, seq_len))
            
            try:
                output = model(dummy_input)
                if output is None:
                    total_points += self.test_assert(False, "Forward pass returns None - not implemented")
                else:
                    correct_shape = output.shape == (batch_size, num_classes)
                    has_gradients = output.requires_grad
                    contains_numbers = not torch.isnan(output).any() and not torch.isinf(output).any()
                    
                    if correct_shape and has_gradients and contains_numbers:
                        total_points += self.test_assert(True, "Forward pass produces valid output")
                    else:
                        total_points += self.test_assert(False, f"Forward pass issues: shape={output.shape}, grad={has_gradients}, finite={contains_numbers}")
                        
            except Exception as e:
                self.log(f"Forward pass failed: {e}")
                total_points += self.test_assert(False, "Forward pass works without errors")
            
            # Test 4: Model actually has parameters (layers are implemented)
            param_count = sum(p.numel() for p in model.parameters())
            reasonable_params = param_count > 10000  # Must have real parameters
            total_points += self.test_assert(reasonable_params, f"Has actual parameters: {param_count:,}")
            
            # Test 5: Model can handle different input sizes
            try:
                different_input = torch.randint(0, vocab_size, (2, 15))  # Different batch/seq size
                output2 = model(different_input)
                handles_different_sizes = output2 is not None and output2.shape[0] == 2
                total_points += self.test_assert(handles_different_sizes, "Handles variable input sizes")
            except Exception as e:
                self.log(f"Variable size handling failed: {e}")
                total_points += self.test_assert(False, "Handles variable input sizes")
            
        except ImportError as e:
            self.log(f"Could not import FeedforwardClassifier: {e}")
            # No points for just importing - must have working implementation
            total_points += self.test_assert(False, "Cannot test - import failed")
        except Exception as e:
            self.log(f"Unexpected error testing Q1: {e}")
            total_points += self.test_assert(False, "Q1 implementation works without errors")
        
        self.log(f"\nQ1 Score: {total_points}/5 points")
        return total_points
    
    def test_q2_training_functions(self) -> int:
        """Test Q2: Training Loop Implementation."""
        self.log("\n" + "="*50)
        self.log("Testing Q2: Training Loop Implementation")
        self.log("="*50)
        
        total_points = 0
        
        try:
            from src.training import train_epoch, validate_epoch, train_model, evaluate_model
            from src.basic_classifier import FeedforwardClassifier
            from src.data_utils import TextDataset, SimpleTokenizer
            
            # Create a minimal working model for testing
            model = FeedforwardClassifier(100, 32, 64, 2)
            
            # Create minimal test data
            texts = ["good movie", "bad film", "great show", "terrible acting"] * 5
            labels = [1, 0, 1, 0] * 5
            tokenizer = SimpleTokenizer(vocab_size=100)
            
            # Test 1: train_epoch actually trains (reduces loss or updates parameters)
            try:
                # Get initial parameters
                initial_params = [p.clone() for p in model.parameters()]
                
                # Create minimal training data
                train_dataset = TextDataset(texts, labels, tokenizer, max_length=10)
                train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4)
                
                optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
                criterion = nn.CrossEntropyLoss()
                device = torch.device('cpu')
                
                # Run one training epoch
                loss, acc = train_epoch(model, train_loader, optimizer, criterion, device)
                
                # Check if parameters actually changed (training occurred)
                params_changed = any(not torch.equal(p1, p2) for p1, p2 in 
                                   zip(initial_params, model.parameters()))
                
                # Check if function returns valid loss and accuracy
                valid_output = (isinstance(loss, float) and isinstance(acc, float) and 
                              0 <= acc <= 1 and loss >= 0)
                
                if params_changed and valid_output:
                    total_points += self.test_assert(True, "train_epoch actually trains model")
                else:
                    total_points += self.test_assert(False, f"train_epoch issues: params_changed={params_changed}, valid_output={valid_output}")
                    
            except Exception as e:
                self.log(f"train_epoch failed: {e}")
                total_points += self.test_assert(False, "train_epoch works")
            
            # Test 2: validate_epoch works without training (no parameter updates)
            try:
                initial_params = [p.clone() for p in model.parameters()]
                
                val_dataset = TextDataset(texts[:8], labels[:8], tokenizer, max_length=10)
                val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=4)
                
                loss, acc = validate_epoch(model, val_loader, criterion, device)
                
                # Parameters should NOT change during validation
                params_unchanged = all(torch.equal(p1, p2) for p1, p2 in 
                                     zip(initial_params, model.parameters()))
                
                valid_output = (isinstance(loss, float) and isinstance(acc, float) and 
                              0 <= acc <= 1 and loss >= 0)
                
                if params_unchanged and valid_output:
                    total_points += self.test_assert(True, "validate_epoch works without training")
                else:
                    total_points += self.test_assert(False, f"validate_epoch issues: params_unchanged={params_unchanged}, valid_output={valid_output}")
                    
            except Exception as e:
                self.log(f"validate_epoch failed: {e}")
                total_points += self.test_assert(False, "validate_epoch works")
            
            # Test 3: train_model runs complete training pipeline
            try:
                fresh_model = FeedforwardClassifier(100, 32, 64, 2)
                
                history = train_model(fresh_model, train_loader, val_loader, 
                                    num_epochs=2, learning_rate=0.001)
                
                # Check if returns training history
                valid_history = (isinstance(history, dict) and 
                               'train_loss' in history and 'val_loss' in history)
                
                if valid_history and len(history['train_loss']) > 0:
                    total_points += self.test_assert(True, "train_model returns valid training history")
                else:
                    total_points += self.test_assert(False, "train_model does not return valid history")
                    
            except Exception as e:
                self.log(f"train_model failed: {e}")
                total_points += self.test_assert(False, "train_model works")
            
            # Test 4: Functions handle edge cases properly
            try:
                # Test with very small dataset
                tiny_dataset = TextDataset(texts[:2], labels[:2], tokenizer, max_length=10)
                tiny_loader = torch.utils.data.DataLoader(tiny_dataset, batch_size=1)
                
                loss, acc = validate_epoch(model, tiny_loader, criterion, device)
                handles_small_data = isinstance(loss, float) and isinstance(acc, float)
                
                total_points += self.test_assert(handles_small_data, "Functions handle small datasets")
                
            except Exception as e:
                self.log(f"Edge case handling failed: {e}")
                total_points += self.test_assert(False, "Functions handle edge cases")
                
        except ImportError as e:
            self.log(f"Could not import training functions: {e}")
            # No points for imports - need working implementations
            for i in range(4):
                total_points += self.test_assert(False, "Cannot test - import failed")
        except Exception as e:
            self.log(f"Unexpected error testing Q2: {e}")
            total_points += self.test_assert(False, "Q2 implementation works without errors")
        
        self.log(f"\nQ2 Score: {total_points}/4 points")
        return total_points
    
    def test_q3_q4_sequence_models(self) -> int:
        """Test Q3-Q4: LSTM and Bidirectional LSTM Classifiers."""
        self.log("\n" + "="*50)
        self.log("Testing Q3-Q4: Sequence Models")
        self.log("="*50)
        
        total_points = 0
        
        try:
            from src.sequence_models import LSTMClassifier, BidirectionalLSTMClassifier
            
            # Test Q3: LSTM Classifier - must actually work, not just exist
            vocab_size, embedding_dim, hidden_dim, num_classes = 1000, 128, 256, 2
            
            try:
                lstm_model = LSTMClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
                
                # Check that LSTM layers are actually initialized (not None)
                has_lstm = (hasattr(lstm_model, 'lstm') and 
                           lstm_model.lstm is not None and 
                           hasattr(lstm_model.lstm, 'forward'))
                
                has_embedding = (hasattr(lstm_model, 'embedding') and 
                               lstm_model.embedding is not None)
                
                if not (has_lstm and has_embedding):
                    total_points += self.test_assert(False, "LSTM model missing essential layers")
                else:
                    # Test LSTM forward pass actually works
                    batch_size, seq_len = 4, 20
                    dummy_input = torch.randint(0, vocab_size, (batch_size, seq_len))
                    
                    lstm_output = lstm_model(dummy_input)
                    
                    if lstm_output is None:
                        total_points += self.test_assert(False, "LSTM forward pass returns None")
                    else:
                        correct_lstm_shape = lstm_output.shape == (batch_size, num_classes)
                        has_gradients = lstm_output.requires_grad
                        is_finite = not torch.isnan(lstm_output).any() and not torch.isinf(lstm_output).any()
                        
                        if correct_lstm_shape and has_gradients and is_finite:
                            total_points += self.test_assert(True, "LSTM forward pass works")
                        else:
                            total_points += self.test_assert(False, f"LSTM issues: shape={lstm_output.shape}, grad={has_gradients}, finite={is_finite}")
                            
            except Exception as e:
                self.log(f"LSTM forward pass failed: {e}")
                total_points += self.test_assert(False, "LSTM forward pass works")
            
            # Test Q4: Bidirectional LSTM Classifier - must actually work
            try:
                bilstm_model = BidirectionalLSTMClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
                
                # Check that BiLSTM layers are actually initialized
                has_bilstm = (hasattr(bilstm_model, 'lstm') and 
                             bilstm_model.lstm is not None and 
                             hasattr(bilstm_model.lstm, 'forward'))
                
                has_embedding = (hasattr(bilstm_model, 'embedding') and 
                               bilstm_model.embedding is not None)
                
                if not (has_bilstm and has_embedding):
                    total_points += self.test_assert(False, "BiLSTM model missing essential layers")
                else:
                    # Test BiLSTM forward pass
                    batch_size, seq_len = 4, 20
                    dummy_input = torch.randint(0, vocab_size, (batch_size, seq_len))
                    bilstm_output = bilstm_model(dummy_input)
                    
                    if bilstm_output is None:
                        total_points += self.test_assert(False, "BiLSTM forward pass returns None")
                    else:
                        correct_bilstm_shape = bilstm_output.shape == (batch_size, num_classes)
                        has_gradients = bilstm_output.requires_grad
                        is_finite = not torch.isnan(bilstm_output).any() and not torch.isinf(bilstm_output).any()
                        
                        if correct_bilstm_shape and has_gradients and is_finite:
                            total_points += self.test_assert(True, "BiLSTM forward pass works")
                        else:
                            total_points += self.test_assert(False, f"BiLSTM issues: shape={bilstm_output.shape}, grad={has_gradients}, finite={is_finite}")
                            
            except Exception as e:
                self.log(f"BiLSTM forward pass failed: {e}")
                total_points += self.test_assert(False, "BiLSTM forward pass works")
            
            # Test parameter comparison - BiLSTM should have more parameters than LSTM
            try:
                lstm_params = sum(p.numel() for p in lstm_model.parameters())
                bilstm_params = sum(p.numel() for p in bilstm_model.parameters())
                
                # Both should have substantial parameters (not 0)
                both_have_params = lstm_params > 10000 and bilstm_params > 10000
                bilstm_has_more = bilstm_params > lstm_params
                
                if both_have_params and bilstm_has_more:
                    total_points += self.test_assert(True, f"BiLSTM has more parameters ({bilstm_params:,} vs {lstm_params:,})")
                else:
                    total_points += self.test_assert(False, f"Parameter issue: LSTM={lstm_params:,}, BiLSTM={bilstm_params:,}")
                    
            except Exception as e:
                self.log(f"Parameter comparison failed: {e}")
                total_points += self.test_assert(False, "Parameter comparison works")
            
            # Test sequence length handling
            try:
                # Test with different sequence lengths
                short_input = torch.randint(0, vocab_size, (2, 5))
                long_input = torch.randint(0, vocab_size, (2, 50))
                
                lstm_short = lstm_model(short_input)
                lstm_long = lstm_model(long_input)
                
                handles_variable_length = (lstm_short is not None and lstm_long is not None and
                                         lstm_short.shape[0] == 2 and lstm_long.shape[0] == 2)
                
                total_points += self.test_assert(handles_variable_length, "Models handle variable sequence lengths")
                
            except Exception as e:
                self.log(f"Variable length handling failed: {e}")
                total_points += self.test_assert(False, "Variable length handling works")
                
        except ImportError as e:
            self.log(f"Could not import sequence models: {e}")
            # No points for just importing - need working implementations
            for i in range(5):
                total_points += self.test_assert(False, "Cannot test - import failed")
        except Exception as e:
            self.log(f"Unexpected error testing Q3-Q4: {e}")
            total_points += self.test_assert(False, "Q3-Q4 implementation works without errors")
        
        self.log(f"\nQ3-Q4 Score: {total_points}/5 points")
        return total_points
    
    def test_q5_q6_multi_dataset(self) -> int:
        """Test Q5-Q6: Multi-Dataset Evaluation."""
        self.log("\n" + "="*50)
        self.log("Testing Q5-Q6: Multi-Dataset Evaluation")
        self.log("="*50)
        
        total_points = 0
        
        try:
            from src.multi_dataset_eval import MultiDatasetEvaluator, run_complete_evaluation
            
            # Test 1: Evaluator actually works, not just imports
            try:
                evaluator = MultiDatasetEvaluator()
                
                # Test that it can actually load datasets (not just return empty dict)
                datasets = evaluator.load_all_datasets()
                
                if not isinstance(datasets, dict) or len(datasets) == 0:
                    total_points += self.test_assert(False, "Evaluator does not load actual datasets")
                else:
                    # Check that datasets have actual data
                    has_real_data = all(
                        isinstance(data, dict) and 
                        'train_texts' in data and 
                        len(data['train_texts']) > 0
                        for data in datasets.values()
                    )
                    
                    if has_real_data:
                        total_points += self.test_assert(True, f"Successfully loads datasets: {list(datasets.keys())}")
                    else:
                        total_points += self.test_assert(False, "Datasets loaded but contain no real data")
                        
            except Exception as e:
                self.log(f"MultiDatasetEvaluator failed: {e}")
                total_points += self.test_assert(False, "MultiDatasetEvaluator works")
            
            # Test 2: Can actually evaluate a model (not just return None)
            try:
                from src.basic_classifier import FeedforwardClassifier
                
                # Create a simple model for testing
                test_model = FeedforwardClassifier(100, 32, 64, 2)
                
                # Test evaluation functionality
                results = evaluator.evaluate_model_on_all_datasets(test_model)
                
                if results is None or not isinstance(results, dict):
                    total_points += self.test_assert(False, "Model evaluation returns None or invalid format")
                else:
                    # Check that results contain actual metrics
                    has_metrics = any(
                        isinstance(result, dict) and 'accuracy' in result
                        for result in results.values()
                    )
                    
                    if has_metrics:
                        total_points += self.test_assert(True, "Model evaluation produces valid results")
                    else:
                        total_points += self.test_assert(False, "Model evaluation missing metrics")
                        
            except Exception as e:
                self.log(f"Model evaluation failed: {e}")
                total_points += self.test_assert(False, "Model evaluation works")
            
            # Test 3: Complete evaluation pipeline works
            try:
                # Test that the complete evaluation function actually works
                complete_results = run_complete_evaluation()
                
                if complete_results is None or not isinstance(complete_results, dict):
                    total_points += self.test_assert(False, "Complete evaluation returns None or invalid format")
                else:
                    # Check that it ran multiple models and datasets
                    has_multiple_results = len(complete_results) > 1
                    has_valid_structure = all(
                        isinstance(v, dict) for v in complete_results.values()
                    )
                    
                    if has_multiple_results and has_valid_structure:
                        total_points += self.test_assert(True, "Complete evaluation pipeline works")
                    else:
                        total_points += self.test_assert(False, "Complete evaluation pipeline incomplete")
                        
            except Exception as e:
                self.log(f"Complete evaluation failed: {e}")
                total_points += self.test_assert(False, "Complete evaluation works")
                
        except ImportError as e:
            self.log(f"Could not import multi-dataset evaluation: {e}")
            # No points for just importing - need working implementations
            for i in range(3):
                total_points += self.test_assert(False, "Cannot test - import failed")
        except Exception as e:
            self.log(f"Unexpected error testing Q5-Q6: {e}")
            total_points += self.test_assert(False, "Q5-Q6 implementation works without errors")
        
        self.log(f"\nQ5-Q6 Score: {total_points}/3 points")
        return total_points
    
    def test_data_utilities(self) -> int:
        """Test data loading and preprocessing utilities."""
        self.log("\n" + "="*50)
        self.log("Testing Data Utilities")
        self.log("="*50)
        
        total_points = 0
        
        try:
            from src.data_utils import (SimpleTokenizer, TextDataset, load_imdb_dataset,
                                      create_data_loaders, calculate_random_baseline)
            
            # Test 1: Tokenizer actually works (not just exists)
            try:
                tokenizer = SimpleTokenizer(vocab_size=1000)
                sample_texts = ["This is a test", "Another test sentence"]
                tokenizer.build_vocab(sample_texts)
                
                # Test tokenization produces valid output
                token_ids = tokenizer("This is a test")
                
                valid_tokenization = (isinstance(token_ids, list) and 
                                    len(token_ids) > 0 and 
                                    all(isinstance(tid, int) for tid in token_ids))
                
                total_points += self.test_assert(valid_tokenization, "Tokenizer produces valid token IDs")
                
            except Exception as e:
                self.log(f"Tokenizer failed: {e}")
                total_points += self.test_assert(False, "Tokenizer works")
            
            # Test 2: Dataset loading actually loads real data
            try:
                train_texts, train_labels, test_texts, test_labels = load_imdb_dataset()
                
                # Check that we get actual data, not empty lists
                has_real_data = (len(train_texts) > 50 and len(train_labels) > 50 and 
                               len(test_texts) > 10 and len(test_labels) > 10)
                
                # Check data format is correct
                valid_format = (isinstance(train_texts[0], str) and 
                              isinstance(train_labels[0], int) and
                              len(train_texts) == len(train_labels))
                
                if has_real_data and valid_format:
                    total_points += self.test_assert(True, f"Successfully loads real dataset: {len(train_texts)} train, {len(test_texts)} test samples")
                else:
                    total_points += self.test_assert(False, f"Dataset loading issues: real_data={has_real_data}, valid_format={valid_format}")
                    
            except Exception as e:
                self.log(f"Dataset loading failed: {e}")
                total_points += self.test_assert(False, "Dataset loading works")
            
        except ImportError as e:
            self.log(f"Could not import data utilities: {e}")
            # No points for just importing - need working implementations
            for i in range(2):
                total_points += self.test_assert(False, "Cannot test - import failed")
        except Exception as e:
            self.log(f"Unexpected error testing data utilities: {e}")
            total_points += self.test_assert(False, "Data utilities work without errors")
        
        self.log(f"\nData Utilities Score: {total_points}/2 points")
        return total_points
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run all autograder tests."""
        self.log("MAI 5201 - HW2 Autograder")
        self.log("Neural Networks for NLP")
        self.log("="*50)
        
        # Run individual question tests
        q1_score = self.test_q1_feedforward_classifier()
        q2_score = self.test_q2_training_functions()
        q3_q4_score = self.test_q3_q4_sequence_models()
        q5_q6_score = self.test_q5_q6_multi_dataset()
        data_score = self.test_data_utilities()
        
        total_score = q1_score + q2_score + q3_q4_score + q5_q6_score + data_score
        max_score = 5 + 4 + 5 + 3 + 2  # Adjust based on actual point distribution
        
        # Final summary
        self.log("\n" + "="*50)
        self.log("FINAL SUMMARY")
        self.log("="*50)
        self.log(f"Q1 (Feedforward Classifier): {q1_score}/5 points")
        self.log(f"Q2 (Training Functions): {q2_score}/4 points") 
        self.log(f"Q3-Q4 (Sequence Models): {q3_q4_score}/5 points")
        self.log(f"Q5-Q6 (Multi-Dataset): {q5_q6_score}/3 points")
        self.log(f"Data Utilities: {data_score}/2 points")
        self.log("-" * 30)
        self.log(f"TOTAL: {total_score}/{max_score} points ({total_score/max_score*100:.1f}%)")
        self.log(f"Tests Passed: {self.passed_tests}/{self.total_tests}")
        
        return {
            'total_score': total_score,
            'max_score': max_score,
            'percentage': total_score/max_score*100,
            'tests_passed': self.passed_tests,
            'total_tests': self.total_tests,
            'breakdown': {
                'q1': q1_score,
                'q2': q2_score,
                'q3_q4': q3_q4_score,
                'q5_q6': q5_q6_score,
                'data_utils': data_score
            }
        }
    
    def run_specific_test(self, question: str):
        """Run tests for a specific question."""
        question = question.lower()
        
        if question == 'q1':
            return self.test_q1_feedforward_classifier()
        elif question == 'q2':
            return self.test_q2_training_functions()
        elif question in ['q3', 'q4']:
            return self.test_q3_q4_sequence_models()
        elif question in ['q5', 'q6']:
            return self.test_q5_q6_multi_dataset()
        elif question == 'data':
            return self.test_data_utilities()
        else:
            self.log(f"Unknown question: {question}")
            self.log("Available tests: q1, q2, q3, q4, q5, q6, data")
            return 0


def main():
    """Main function to run autograder."""
    autograder = HW2Autograder()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '-q' and len(sys.argv) > 2:
            # Run specific question
            question = sys.argv[2]
            autograder.run_specific_test(question)
        else:
            print("Usage: python autograder.py [-q question_number]")
            print("Example: python autograder.py -q q1")
    else:
        # Run all tests
        results = autograder.run_all_tests()


if __name__ == "__main__":
    main()