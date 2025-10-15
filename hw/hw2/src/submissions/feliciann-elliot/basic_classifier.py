"""
MAI 5201 - Homework 2: Neural Networks for NLP
Part 1: Basic Neural Text Classification
Q1: Feedforward Neural Classifier (15 pts)

Student Name: Feliciann Elliot
Student ID: 1022055
Date: October 14, 2025

Instructions:
- Implement the FeedforwardClassifier class below
- Use PyTorch nn.Module as your base class
- Include at least 2 hidden layers with ReLU activation
- Support both binary and multi-class classification
- Handle variable-length input sequences through embedding aggregation
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional


class FeedforwardClassifier(nn.Module):
    """
    A feedforward neural network for text classification.
    
    Architecture:
    Input → Embedding → Mean Pooling → Hidden Layers → Output
    
    This network converts variable-length text sequences into fixed-size
    representations and classifies them using feedforward layers.
    """
    
    def __init__(self, vocab_size: int, embedding_dim: int, hidden_dim: int, 
                 num_classes: int, dropout_prob: float = 0.3):
        """
        Initialize the feedforward classifier.
        
        Args:
            vocab_size (int): Size of the vocabulary
            embedding_dim (int): Dimension of word embeddings
            hidden_dim (int): Dimension of hidden layers
            num_classes (int): Number of output classes
            dropout_prob (float): Dropout probability for regularization
        """
        super(FeedforwardClassifier, self).__init__()
        
        # TODO: Initialize embedding layer
        # Hint: Use nn.Embedding(vocab_size, embedding_dim)
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        
        # TODO: Initialize hidden layers
        # Requirement: At least 2 hidden layers with ReLU activation
        # Architecture suggestion:
        # embedding_dim → hidden_dim → hidden_dim → num_classes
        self.hidden1 = nn.Linear(embedding_dim, hidden_dim)
        self.hidden2 = nn.Linear(hidden_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, num_classes)
        
        # TODO: Initialize dropout layer
        # Hint: Use nn.Dropout(dropout_prob)
        self.dropout = nn.Dropout(dropout_prob)
        
        # Store configuration
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.num_classes = num_classes
    
    def forward(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Forward pass through the network.
        
        Args:
            input_ids (torch.Tensor): Input token ids of shape (batch_size, seq_len)
            attention_mask (torch.Tensor, optional): Mask for padding tokens
            
        Returns:
            torch.Tensor: Logits of shape (batch_size, num_classes)
        """
        # TODO: Implement forward pass
        
        # Step 1: Convert input_ids to embeddings
        # Shape: (batch_size, seq_len) → (batch_size, seq_len, embedding_dim)
        embeddings = self.embedding(input_ids)  # Use self.embedding
        
        # Step 2: Aggregate embeddings across sequence length
        # We'll use mean pooling to convert variable-length sequences to fixed-size
        # Shape: (batch_size, seq_len, embedding_dim) → (batch_size, embedding_dim)
        
        if attention_mask is not None:
            # TODO: Use attention mask to ignore padding tokens
            # Hint: Multiply embeddings by attention_mask.unsqueeze(-1)
            # Then divide by the sum of attention_mask for proper averaging
            masked_embeddings = embeddings * attention_mask.unsqueeze(-1)
            pooled = masked_embeddings.sum(dim=1) / attention_mask.sum(dim=1, keepdim=True)
        else:
            # Simple mean pooling without mask
            pooled = torch.mean(embeddings, dim=1)  # Use torch.mean along dimension 1
        
        # Step 3: Pass through hidden layers with ReLU and dropout
        # Shape: (batch_size, embedding_dim) → (batch_size, hidden_dim)
        hidden1_out = self.dropout(F.relu(self.hidden1(pooled)))  # Apply hidden1, then ReLU, then dropout
        
        # Step 4: Second hidden layer
        # Shape: (batch_size, hidden_dim) → (batch_size, hidden_dim)
        hidden2_out = self.dropout(F.relu(self.hidden2(hidden1_out)))  # Apply hidden2, then ReLU, then dropout
        
        # Step 5: Output layer (no activation - we'll use CrossEntropyLoss)
        # Shape: (batch_size, hidden_dim) → (batch_size, num_classes)
        logits = self.output(hidden2_out)  # Apply output layer
        
        return logits


# Example usage and testing
if __name__ == "__main__":
    # Test the classifier with dummy data
    vocab_size = 1000
    embedding_dim = 128
    hidden_dim = 256
    num_classes = 2  # Binary classification
    
    # Create model
    model = FeedforwardClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
    
    # Create dummy input
    batch_size = 4
    seq_len = 20
    input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))
    
    # Forward pass
    with torch.no_grad():
        logits = model(input_ids)
        predictions = torch.argmax(logits, dim=-1)
        
    print(f"Input shape: {input_ids.shape}")
    print(f"Output logits shape: {logits.shape}")
    print(f"Predictions: {predictions}")
    print(f"Model parameters: {sum(p.numel() for p in model.parameters()):,}")