"""
MAI 5201 - Homework 2: Neural Networks for NLP
Data Loading and Preprocessing Utilities

This module provides functions to load and preprocess datasets for neural network training.
Students can use these utilities as-is or modify them as needed.
"""

import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
import re
from collections import Counter

# Import Hugging Face datasets for real datasets
try:
    from datasets import load_dataset
    DATASETS_AVAILABLE = True
    print("Hugging Face datasets available - will load real data")
except ImportError:
    print("Warning: Hugging Face datasets not available. Using synthetic data.")
    DATASETS_AVAILABLE = False


class TextDataset(Dataset):
    """
    Dataset class for text classification tasks.
    """
    
    def __init__(self, texts: List[str], labels: List[int], tokenizer, max_length: int = 512):
        """
        Initialize the dataset.
        
        Args:
            texts: List of text strings
            labels: List of integer labels
            tokenizer: Tokenizer function that converts text to token ids
            max_length: Maximum sequence length
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        
        # Tokenize text
        token_ids = self.tokenizer(text)
        
        # Truncate or pad to max_length
        if len(token_ids) > self.max_length:
            token_ids = token_ids[:self.max_length]
        else:
            # Pad with zeros (assuming 0 is padding token)
            token_ids = token_ids + [0] * (self.max_length - len(token_ids))
        
        return {
            'input_ids': torch.tensor(token_ids, dtype=torch.long),
            'labels': torch.tensor(label, dtype=torch.long),
            'attention_mask': torch.tensor([1 if t != 0 else 0 for t in token_ids], dtype=torch.long)
        }


class SimpleTokenizer:
    """
    Simple word-level tokenizer for text preprocessing.
    """
    
    def __init__(self, vocab_size: int = 10000):
        self.vocab_size = vocab_size
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_built = False
    
    def build_vocab(self, texts: List[str]):
        """Build vocabulary from a list of texts."""
        # Tokenize all texts and count word frequencies
        all_words = []
        for text in texts:
            words = self.preprocess_text(text).split()
            all_words.extend(words)
        
        # Count word frequencies
        word_counts = Counter(all_words)
        
        # Select most frequent words
        most_common = word_counts.most_common(self.vocab_size - 2)  # Reserve space for special tokens
        
        # Build vocabulary
        self.word_to_id = {'<PAD>': 0, '<UNK>': 1}
        self.id_to_word = {0: '<PAD>', 1: '<UNK>'}
        
        for i, (word, count) in enumerate(most_common):
            word_id = i + 2
            self.word_to_id[word] = word_id
            self.id_to_word[word_id] = word
        
        self.vocab_built = True
        print(f"Built vocabulary with {len(self.word_to_id)} words")
    
    def preprocess_text(self, text: str) -> str:
        """Basic text preprocessing."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Simple tokenization (split on whitespace and punctuation)
        text = re.sub(r'[^\w\s]', ' ', text)
        
        return text.strip()
    
    def __call__(self, text: str) -> List[int]:
        """Convert text to list of token IDs."""
        if not self.vocab_built:
            raise ValueError("Vocabulary not built. Call build_vocab() first.")
        
        words = self.preprocess_text(text).split()
        token_ids = []
        
        for word in words:
            if word in self.word_to_id:
                token_ids.append(self.word_to_id[word])
            else:
                token_ids.append(self.word_to_id['<UNK>'])  # Unknown word
        
        return token_ids
    
    def decode(self, token_ids: List[int]) -> str:
        """Convert token IDs back to text."""
        words = []
        for token_id in token_ids:
            if token_id in self.id_to_word:
                word = self.id_to_word[token_id]
                if word not in ['<PAD>', '<UNK>']:
                    words.append(word)
        return ' '.join(words)


def load_imdb_dataset(data_path: str = None, max_samples: int = None) -> Tuple[List[str], List[int], List[str], List[int]]:
    """
    Load IMDb movie review dataset using Hugging Face datasets.
    
    Args:
        data_path: Unused (kept for compatibility)
        max_samples: Maximum number of samples per split (for testing)
    
    Returns:
        Tuple of (train_texts, train_labels, test_texts, test_labels)
    """
    print("Loading IMDb dataset...")
    
    if not DATASETS_AVAILABLE:
        # Fallback to synthetic data if datasets not available
        return _load_synthetic_imdb(max_samples)
    
    try:
        # Load real IMDB dataset from Hugging Face
        dataset = load_dataset("imdb")
        
        # Extract train and test splits
        train_split = dataset['train']
        test_split = dataset['test']
        
        # Convert to lists
        train_texts = train_split['text']
        train_labels = train_split['label']  # Already 0/1 (0=negative, 1=positive)
        
        test_texts = test_split['text']
        test_labels = test_split['label']
        
        # Limit samples if requested
        if max_samples:
            train_texts = train_texts[:max_samples]
            train_labels = train_labels[:max_samples]
            test_texts = test_texts[:max_samples]
            test_labels = test_labels[:max_samples]
        
        print(f"Loaded {len(train_texts)} training samples, {len(test_texts)} test samples")
        print("Labels: 0=negative, 1=positive")
        return train_texts, train_labels, test_texts, test_labels
        
    except Exception as e:
        print(f"Error loading real IMDB dataset: {e}")
        print("Falling back to synthetic data...")
        return _load_synthetic_imdb(max_samples)


def _load_synthetic_imdb(max_samples: int = None) -> Tuple[List[str], List[int], List[str], List[int]]:
    """Fallback synthetic IMDB data for when torchtext is not available."""
    # Dummy data for demonstration
    train_texts = [
        "This movie was absolutely fantastic! Great acting and storyline.",
        "Terrible film. Boring and predictable plot.",
        "Amazing cinematography and excellent direction. Highly recommended!",
        "Waste of time. Poor acting and weak script.",
        "One of the best movies I've ever seen. Brilliant!",
        "Disappointing. Expected much more from this director."
    ] * 100  # Repeat to create larger dataset
    
    train_labels = [1, 0, 1, 0, 1, 0] * 100  # 1 = positive, 0 = negative
    
    test_texts = train_texts[:200]  # Use subset for testing
    test_labels = train_labels[:200]
    
    if max_samples:
        train_texts = train_texts[:max_samples]
        train_labels = train_labels[:max_samples]
        test_texts = test_texts[:min(max_samples, len(test_texts))]
        test_labels = test_labels[:min(max_samples, len(test_labels))]
    
    print(f"Loaded {len(train_texts)} training samples, {len(test_texts)} test samples")
    return train_texts, train_labels, test_texts, test_labels


def load_ag_news_dataset(data_path: str = None, max_samples: int = None) -> Tuple[List[str], List[int], List[str], List[int]]:
    """
    Load AG News dataset (4-class news categorization) using Hugging Face datasets.
    
    Args:
        data_path: Unused (kept for compatibility)
        max_samples: Maximum number of samples per split (for testing)
    
    Returns:
        Tuple of (train_texts, train_labels, test_texts, test_labels)
    """
    print("Loading AG News dataset...")
    
    if not DATASETS_AVAILABLE:
        return _load_synthetic_ag_news(max_samples)
    
    try:
        # Load real AG_NEWS dataset from Hugging Face
        dataset = load_dataset("ag_news")
        
        # Extract train and test splits
        train_split = dataset['train']
        test_split = dataset['test']
        
        # Convert to lists
        train_texts = train_split['text']
        train_labels = train_split['label']  # Already 0-3 (0=World, 1=Sports, 2=Business, 3=Sci/Tech)
        
        test_texts = test_split['text']
        test_labels = test_split['label']
        
        # Limit samples if requested
        if max_samples:
            train_texts = train_texts[:max_samples]
            train_labels = train_labels[:max_samples]
            test_texts = test_texts[:max_samples]
            test_labels = test_labels[:max_samples]
        
        # Class mapping
        class_names = ["World", "Sports", "Business", "Sci/Tech"]
        
        print(f"Loaded {len(train_texts)} training samples, {len(test_texts)} test samples")
        print(f"Classes: {class_names}")
        return train_texts, train_labels, test_texts, test_labels
        
    except Exception as e:
        print(f"Error loading real AG News dataset: {e}")
        print("Falling back to synthetic data...")
        return _load_synthetic_ag_news(max_samples)


def _load_synthetic_ag_news(max_samples: int = None) -> Tuple[List[str], List[int], List[str], List[int]]:
    """Fallback synthetic AG News data for when torchtext is not available."""
    # Dummy data for demonstration
    class_names = ["World", "Sports", "Business", "Sci/Tech"]
    
    train_texts = [
        "International summit discusses climate change policies.",  # World
        "Basketball team wins championship in overtime victory.",   # Sports
        "Stock market reaches new highs amid economic recovery.",   # Business
        "Scientists discover new method for quantum computing.",    # Sci/Tech
        "Political tensions rise between neighboring countries.",   # World
        "Football season begins with exciting opening games.",      # Sports
        "Company reports record profits in quarterly earnings.",    # Business
        "Breakthrough in artificial intelligence research announced." # Sci/Tech
    ] * 50
    
    train_labels = [0, 1, 2, 3, 0, 1, 2, 3] * 50  # 0=World, 1=Sports, 2=Business, 3=Sci/Tech
    
    test_texts = train_texts[:100]
    test_labels = train_labels[:100]
    
    if max_samples:
        train_texts = train_texts[:max_samples]
        train_labels = train_labels[:max_samples]
        test_texts = test_texts[:min(max_samples, len(test_texts))]
        test_labels = test_labels[:min(max_samples, len(test_labels))]
    
    print(f"Loaded {len(train_texts)} training samples, {len(test_texts)} test samples")
    print(f"Classes: {class_names}")
    return train_texts, train_labels, test_texts, test_labels


def create_data_loaders(train_texts: List[str], train_labels: List[int],
                       val_texts: List[str], val_labels: List[int],
                       tokenizer, batch_size: int = 32, max_length: int = 512) -> Tuple[DataLoader, DataLoader]:
    """
    Create PyTorch DataLoaders for training and validation.
    
    Args:
        train_texts: Training text samples
        train_labels: Training labels
        val_texts: Validation text samples
        val_labels: Validation labels
        tokenizer: Tokenizer function
        batch_size: Batch size for DataLoader
        max_length: Maximum sequence length
        
    Returns:
        Tuple of (train_loader, val_loader)
    """
    # Create datasets
    train_dataset = TextDataset(train_texts, train_labels, tokenizer, max_length)
    val_dataset = TextDataset(val_texts, val_labels, tokenizer, max_length)
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader


def calculate_random_baseline(labels: List[int]) -> float:
    """
    Calculate random baseline accuracy for a dataset.
    
    Args:
        labels: List of integer labels
        
    Returns:
        Random baseline accuracy
    """
    unique_labels = list(set(labels))
    num_classes = len(unique_labels)
    random_accuracy = 1.0 / num_classes
    
    print(f"Random baseline accuracy: {random_accuracy:.4f} ({random_accuracy*100:.2f}%)")
    return random_accuracy


def print_dataset_stats(texts: List[str], labels: List[int], dataset_name: str = "Dataset"):
    """
    Print statistics about a dataset.
    
    Args:
        texts: List of text samples
        labels: List of labels
        dataset_name: Name of the dataset for printing
    """
    print(f"\n{dataset_name} Statistics:")
    print(f"Number of samples: {len(texts)}")
    print(f"Number of classes: {len(set(labels))}")
    
    # Text length statistics
    text_lengths = [len(text.split()) for text in texts]
    print(f"Average text length: {np.mean(text_lengths):.1f} words")
    print(f"Min text length: {min(text_lengths)} words")
    print(f"Max text length: {max(text_lengths)} words")
    
    # Class distribution
    label_counts = Counter(labels)
    print("Class distribution:")
    for label, count in sorted(label_counts.items()):
        percentage = count / len(labels) * 100
        print(f"  Class {label}: {count} samples ({percentage:.1f}%)")
    
    # Random baseline
    calculate_random_baseline(labels)


# Example usage
if __name__ == "__main__":
    # Load sample dataset
    train_texts, train_labels, test_texts, test_labels = load_imdb_dataset()
    
    # Print statistics
    print_dataset_stats(train_texts, train_labels, "IMDb Training")
    
    # Create tokenizer and build vocabulary
    tokenizer = SimpleTokenizer(vocab_size=5000)
    tokenizer.build_vocab(train_texts)
    
    # Test tokenization
    sample_text = "This is a great movie!"
    token_ids = tokenizer(sample_text)
    decoded_text = tokenizer.decode(token_ids)
    
    print(f"\nTokenization example:")
    print(f"Original: {sample_text}")
    print(f"Token IDs: {token_ids}")
    print(f"Decoded: {decoded_text}")
    
    # Create data loaders
    train_loader, val_loader = create_data_loaders(
        train_texts[:400], train_labels[:400],
        train_texts[400:500], train_labels[400:500],
        tokenizer, batch_size=16
    )
    
    print(f"\nData loaders created:")
    print(f"Training batches: {len(train_loader)}")
    print(f"Validation batches: {len(val_loader)}")
    
    # Test a batch
    for batch in train_loader:
        print(f"Batch input shape: {batch['input_ids'].shape}")
        print(f"Batch labels shape: {batch['labels'].shape}")
        break