"""
MAI 5201 - Homework 2: Neural Networks for NLP
Part 3: Multi-Dataset Application and Evaluation
Q5-Q6: Apply models to multiple datasets and analyze results (15 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Apply your best model from Parts 1-2 to multiple datasets
- Compare performance across different text domains
- Analyze what makes some datasets easier/harder for neural networks
- Provide insights about model generalization
"""

import os
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Any
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from data_utils import (load_imdb_dataset, load_ag_news_dataset, 
                       create_data_loaders, print_dataset_stats, 
                       calculate_random_baseline, SimpleTokenizer)
from training import evaluate_model


class MultiDatasetEvaluator:
    """
    Evaluate neural network models across multiple text classification datasets.
    """
    
    def __init__(self):
        self.results = {}
        self.datasets_info = {}
    
    def load_all_datasets(self) -> Dict[str, Tuple[List[str], List[int]]]:
        """
        Load all available datasets for evaluation.
        
        Returns:
            Dictionary mapping dataset names to (texts, labels) tuples
        """
        datasets = {}
        
        # TODO: Load IMDb dataset
        print("Loading datasets...")
        
        # IMDb Movie Reviews (Binary Sentiment)
        try:
            train_texts, train_labels, test_texts, test_labels = load_imdb_dataset()
            # datasets['imdb'] = (test_texts, test_labels)  # Use test set for evaluation
            datasets['imdb'] = {
                'train_texts': test_texts,
                'train_labels': test_labels,
                'test_texts': test_texts,
                'test_labels': test_labels
            }

            self.datasets_info['imdb'] = {
                'name': 'IMDb Movie Reviews',
                'domain': 'Entertainment/Opinion',
                'task': 'Binary Sentiment Classification',
                'classes': ['Negative', 'Positive']
            }
        except Exception as e:
            print(f"Could not load IMDb dataset: {e}")
        
        # TODO: Load AG News dataset
        # AG News (4-class Topic Classification)
        try:
            train_texts, train_labels, test_texts, test_labels = load_ag_news_dataset()
            # datasets['ag_news'] = (test_texts, test_labels)
            datasets['ag_news'] = {
                'train_texts': test_texts,
                'train_labels': test_labels,
                'test_texts': test_texts,
                'test_labels': test_labels
            }
            self.datasets_info['ag_news'] = {
                'name': 'AG News',
                'domain': 'News/Journalism', 
                'task': '4-Class Topic Classification',
                'classes': ['World', 'Sports', 'Business', 'Sci/Tech']
            }
        except Exception as e:
            print(f"Could not load AG News dataset: {e}")
        
        # TODO: Add more datasets as needed
        # You can add Yelp Reviews, 20 Newsgroups, etc.
        
        return datasets

    def evaluate_model_on_all_datasets(self, model: nn.Module, tokenizer=None, device: torch.device = None) -> Dict[
        str, Dict]:
        """
        Convenience wrapper used by tests: evaluates `model` on all datasets and returns results.
        If tokenizer is not provided, tries to instantiate SimpleTokenizer from data_utils.
        """
        if device is None:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        if tokenizer is None:
            try:
                from data_utils import SimpleTokenizer
                tokenizer = SimpleTokenizer()
            except Exception:
                raise ValueError(
                    "No tokenizer provided and SimpleTokenizer could not be imported. Please pass a tokenizer.")

        return self.run_multi_dataset_evaluation(model, tokenizer, device)

    def evaluate_on_dataset(self, model: nn.Module, dataset_name: str,
                            texts: list[str], labels: list,
                            tokenizer, device: torch.device) -> dict:
        """
        Evaluate a model on a single dataset, adapting the classifier if needed
        and fixing label indexing to avoid CUDA errors.

        Args:
            model: Trained neural network model
            dataset_name: Name of the dataset
            texts: Text samples
            labels: Ground truth labels
            tokenizer: Tokenizer for preprocessing
            device: Device for computation

        Returns:
            Dictionary containing evaluation results
        """
        import numpy as np
        import torch
        import torch.nn as nn
        from torch.utils.data import DataLoader
        from sequence_models import BidirectionalLSTMClassifier
        from data_utils import TextDataset

        print(f"\nEvaluating on {dataset_name}...")

        # Enable deterministic CUDA errors for debugging
        if device.type == 'cuda':
            import os
            os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

        # Build vocabulary
        tokenizer.build_vocab(texts)

        # ---------------------
        # Ensure labels are integers starting from 0
        # ---------------------
        if isinstance(labels[0], str):
            unique_labels = sorted(list(set(labels)))
            label_map = {label: idx for idx, label in enumerate(unique_labels)}
            labels = [label_map[l] for l in labels]
        else:
            unique_labels = sorted(list(set(labels)))
            label_map = {l: l for l in unique_labels}
            labels = list(labels)

        # Shift labels to start from 0 if needed
        min_label = min(labels)
        if min_label != 0:
            print(f"Shifting labels by {min_label} to start from 0")
            labels = [l - min_label for l in labels]

        num_classes_dataset = len(set(labels))
        print(f"Labels min/max after shift: {min(labels)} {max(labels)} Num classes: {num_classes_dataset}")

        # ---------------------
        # Resize embedding layer if needed
        # ---------------------
        # Try to infer vocab size from tokenizer attributes or methods
        vocab_size = None
        if hasattr(tokenizer, "word2idx"):
            vocab_size = len(tokenizer.word2idx)
        elif hasattr(tokenizer, "vocab"):
            vocab_size = len(tokenizer.vocab)
        elif hasattr(tokenizer, "get_vocab_size"):
            vocab_size = tokenizer.get_vocab_size()
        elif hasattr(tokenizer, "vocab_size"):
            vocab_size = tokenizer.vocab_size
        else:
            # Try to infer from __call__ or __getitem__ on a dummy string
            try:
                tokens = tokenizer("dummy string")
                vocab_size = max(tokens) + 1 if tokens else 0
            except Exception:
                raise AttributeError("SimpleTokenizer has no recognizable vocab attribute or method.")

        if hasattr(model, "embedding") and getattr(model.embedding, "num_embeddings", None) != vocab_size:
            print(f"Resizing embedding layer: {getattr(model.embedding, 'num_embeddings', None)} → {vocab_size}")
            old_embedding = model.embedding
            embedding_dim = old_embedding.embedding_dim
            new_embedding = nn.Embedding(vocab_size, embedding_dim)
            # Optionally copy weights for overlapping indices
            num_to_copy = min(old_embedding.num_embeddings, vocab_size)
            with torch.no_grad():
                new_embedding.weight[:num_to_copy] = old_embedding.weight[:num_to_copy]
            model.embedding = new_embedding
            model.embedding.to(device)

        # ---------------------
        # Adapt model classifier if needed
        # ---------------------
        if hasattr(model, 'num_classes') and model.num_classes != num_classes_dataset:
            print(f"Adapting classifier: {model.num_classes} → {num_classes_dataset}")
            if hasattr(model, 'hidden_dim'):
                model.output = nn.Linear(model.hidden_dim, num_classes_dataset)
                model.output.apply(lambda m: m.reset_parameters() if hasattr(m, "reset_parameters") else None)
            elif hasattr(model, "classifier"):
                # For BiLSTM etc.
                out_features = 2 * model.hidden_dim if hasattr(model, "hidden_dim") else model.classifier.in_features
                model.classifier = nn.Linear(out_features, num_classes_dataset)
                model.classifier.apply(lambda m: m.reset_parameters() if hasattr(m, "reset_parameters") else None)
            model.num_classes = num_classes_dataset
            # Move model to device after changing layers
            model.to(device)

        # Always move model to device (in case not already)
        model.to(device)

        # ---------------------
        # Create dataset and loader
        # ---------------------
        eval_dataset = TextDataset(texts, labels, tokenizer, max_length=512)
        eval_loader = DataLoader(eval_dataset, batch_size=32, shuffle=False)

        # ---------------------
        # Evaluate model
        # ---------------------
        try:
            results = evaluate_model(model, eval_loader, device)

            # Collect predictions and labels
            model.eval()
            all_predictions = []
            all_labels = []

            with torch.no_grad():
                for batch in eval_loader:
                    input_ids = batch['input_ids'].to(device)
                    batch_labels = batch['labels'].to(device).long()  # Ensure long
                    attention_mask = batch.get('attention_mask', None)
                    if attention_mask is not None:
                        attention_mask = attention_mask.to(device)

                    logits = model(input_ids, attention_mask) if attention_mask is not None else model(input_ids)
                    predictions = torch.argmax(logits, dim=-1)

                    all_predictions.extend(predictions.cpu().numpy())
                    all_labels.extend(batch_labels.cpu().numpy())

            # Convert to arrays
            all_predictions = np.array(all_predictions)
            all_labels = np.array(all_labels)

            # Metrics
            num_classes = len(set(all_labels))
            random_baseline = 1.0 / num_classes
            improvement = results['accuracy'] - random_baseline
            improvement_factor = results['accuracy'] / random_baseline

            detailed_results = {
                'accuracy': results['accuracy'],
                'num_samples': len(all_labels),
                'num_classes': num_classes,
                'random_baseline': random_baseline,
                'improvement_over_random': improvement,
                'improvement_factor': improvement_factor,
                'predictions': all_predictions,
                'true_labels': all_labels,
                'dataset_info': self.datasets_info.get(dataset_name, {})
            }

            print(f"Accuracy: {results['accuracy']:.4f}")
            print(f"Random Baseline: {random_baseline:.4f}")
            print(f"Improvement: +{improvement:.4f} ({improvement_factor:.2f}x better)")

            return detailed_results

        except RuntimeError as e:
            print(f"Error evaluating {dataset_name}: {e}")
            if 'device-side assert' in str(e):
                print("→ CUDA device-side assert triggered. Check labels and number of classes.")
            return {'error': str(e)}

    def run_multi_dataset_evaluation(self, model: nn.Module, tokenizer,
                                   device: torch.device) -> Dict[str, Dict]:
        """
        Evaluate model on all available datasets.

        Args:
            model: Trained neural network model
            tokenizer: Tokenizer for preprocessing
            device: Device for computation

        Returns:
            Dictionary mapping dataset names to evaluation results
        """
        # TODO: Load all datasets
        datasets = self.load_all_datasets()
        # TODO: Evaluate on each dataset
        all_results = {}

        for dataset_name, data in datasets.items():
            try:
                texts = data['test_texts']
                labels = data['test_labels']

                results = self.evaluate_on_dataset(
                    model, dataset_name, texts, labels, tokenizer, device
                )
                all_results[dataset_name] = results
                self.results[dataset_name] = results
            except Exception as e:
                print(f"Error evaluating {dataset_name}: {e}")
                continue

        return all_results
    
    def generate_performance_summary(self) -> pd.DataFrame:
        """
        Generate a summary table of performance across all datasets.
        
        Returns:
            DataFrame with performance metrics for each dataset
        """
        # TODO: Create summary table
        summary_data = []
        
        for dataset_name, results in self.results.items():
            dataset_info = results['dataset_info']
            summary_data.append({
                'Dataset': dataset_info.get('name', dataset_name),
                'Domain': dataset_info.get('domain', 'Unknown'),
                'Task': dataset_info.get('task', 'Classification'),
                'Num Classes': results['num_classes'],
                'Num Samples': results['num_samples'],
                'Accuracy': results['accuracy'],
                'Random Baseline': results['random_baseline'],
                'Improvement': results['improvement_over_random'],
                'Improvement Factor': results['improvement_factor']
            })
        
        df = pd.DataFrame(summary_data)
        
        # Sort by accuracy (best performing first)
        df = df.sort_values('Accuracy', ascending=False)
        
        return df
    
    def analyze_performance_patterns(self) -> Dict[str, Any]:
        """
        Analyze patterns in model performance across datasets.
        
        Returns:
            Dictionary containing analysis insights
        """
        if not self.results:
            return {"error": "No evaluation results available"}
        
        # TODO: Calculate statistics across datasets
        accuracies = [r['accuracy'] for r in self.results.values()]
        improvements = [r['improvement_over_random'] for r in self.results.values()]
        
        analysis = {
            'num_datasets': len(self.results),
            'mean_accuracy': np.mean(accuracies),
            'std_accuracy': np.std(accuracies),
            'min_accuracy': min(accuracies),
            'max_accuracy': max(accuracies),
            'mean_improvement': np.mean(improvements),
            'best_dataset': max(self.results.keys(), key=lambda k: self.results[k]['accuracy']),
            'worst_dataset': min(self.results.keys(), key=lambda k: self.results[k]['accuracy']),
        }
        
        # TODO: Identify patterns
        # Which types of datasets are easier/harder?
        domain_performance = {}
        for dataset_name, results in self.results.items():
            domain = results['dataset_info'].get('domain', 'Unknown')
            if domain not in domain_performance:
                domain_performance[domain] = []
            domain_performance[domain].append(results['accuracy'])
        
        analysis['domain_performance'] = {
            domain: np.mean(accuracies) 
            for domain, accuracies in domain_performance.items()
        }
        
        return analysis
    
    def plot_performance_comparison(self, save_path: str = None):
        """
        Create visualizations comparing performance across datasets.
        
        Args:
            save_path: Optional path to save the plot
        """
        if not self.results:
            print("No results to plot")
            return
        
        # TODO: Create performance comparison plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot 1: Accuracy vs Random Baseline
        dataset_names = []
        accuracies = []
        baselines = []
        
        for dataset_name, results in self.results.items():
            dataset_names.append(results['dataset_info'].get('name', dataset_name))
            accuracies.append(results['accuracy'])
            baselines.append(results['random_baseline'])
        
        x = np.arange(len(dataset_names))
        width = 0.35
        
        ax1.bar(x - width/2, accuracies, width, label='Model Accuracy', alpha=0.8)
        ax1.bar(x + width/2, baselines, width, label='Random Baseline', alpha=0.8)
        ax1.set_xlabel('Dataset')
        ax1.set_ylabel('Accuracy')
        ax1.set_title('Model vs Random Baseline Performance')
        ax1.set_xticks(x)
        ax1.set_xticklabels(dataset_names, rotation=45, ha='right')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Improvement Factor
        improvements = [results['improvement_factor'] for results in self.results.values()]
        
        ax2.bar(dataset_names, improvements, alpha=0.8, color='green')
        ax2.set_xlabel('Dataset')
        ax2.set_ylabel('Improvement Factor (Model/Random)')
        ax2.set_title('How Much Better Than Random?')
        ax2.set_xticklabels(dataset_names, rotation=45, ha='right')
        ax2.grid(True, alpha=0.3)
        ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Random Baseline')
        ax2.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()


def run_complete_evaluation(model: nn.Module, tokenizer, device: torch.device = None) -> Dict[str, Any]:
    """
    Run complete multi-dataset evaluation and analysis.
    
    Args:
        model: Trained neural network model
        tokenizer: Tokenizer for preprocessing
        device: Device for computation
        
    Returns:
        Complete evaluation results and analysis
    """
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # TODO: Initialize evaluator and run evaluation
    evaluator = MultiDatasetEvaluator()
    
    print("Starting multi-dataset evaluation...")
    results = evaluator.run_multi_dataset_evaluation(model, tokenizer, device)
    
    # TODO: Generate summary and analysis
    print("\n" + "="*50)
    print("PERFORMANCE SUMMARY")
    print("="*50)
    
    summary_df = evaluator.generate_performance_summary()
    print(summary_df.to_string(index=False))
    
    print("\n" + "="*50)
    print("PERFORMANCE ANALYSIS")
    print("="*50)
    
    analysis = evaluator.analyze_performance_patterns()
    
    print(f"Overall Statistics:")
    print(f"  Mean Accuracy: {analysis['mean_accuracy']:.4f} ± {analysis['std_accuracy']:.4f}")
    print(f"  Best Dataset: {analysis['best_dataset']}")
    print(f"  Worst Dataset: {analysis['worst_dataset']}")
    print(f"  Mean Improvement over Random: {analysis['mean_improvement']:.4f}")
    
    print(f"\nDomain Performance:")
    for domain, avg_acc in analysis['domain_performance'].items():
        print(f"  {domain}: {avg_acc:.4f}")
    
    # TODO: Create visualizations
    evaluator.plot_performance_comparison()
    
    return {
        'detailed_results': results,
        'summary': summary_df,
        'analysis': analysis,
        'evaluator': evaluator
    }


# Example usage and testing
if __name__ == "__main__":
    print("Multi-dataset evaluation module ready!")
    print("Usage:")
    print("1. Train your best model from Parts 1-2")
    print("2. Create a tokenizer and build vocabulary")
    print("3. Call: run_complete_evaluation(model, tokenizer)")
    print("\nExample:")
    print("results = run_complete_evaluation(best_model, tokenizer)")
    print("This will evaluate your model on all available datasets and provide comprehensive analysis.")