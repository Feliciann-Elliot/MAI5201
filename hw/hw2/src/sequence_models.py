"""
MAI 5201 - Homework 2: Neural Networks for NLP
Part 2: Sequence Models
Q3-Q4: LSTM and Bidirectional LSTM Classifiers (35 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement LSTM and Bidirectional LSTM classifiers below
- Handle variable-length sequences properly
- Use final hidden state or max/mean pooling for classification
- Compare unidirectional vs bidirectional performance
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple


class LSTMClassifier(nn.Module):
    """
    LSTM-based text classifier that processes sequences to capture temporal dependencies.
    
    Architecture:
    Input → Embedding → LSTM → Final Hidden State → Classifier → Output
    """
    
    def __init__(self, vocab_size: int, embedding_dim: int, hidden_dim: int,
                 num_classes: int, num_layers: int = 1, dropout_prob: float = 0.3):
        """
        Initialize the LSTM classifier.
        
        Args:
            vocab_size (int): Size of vocabulary
            embedding_dim (int): Dimension of word embeddings
            hidden_dim (int): Dimension of LSTM hidden state
            num_classes (int): Number of output classes
            num_layers (int): Number of LSTM layers
            dropout_prob (float): Dropout probability
        """
        super(LSTMClassifier, self).__init__()
        
        # TODO: Initialize embedding layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim)  # nn.Embedding(vocab_size, embedding_dim)
        
        # TODO: Initialize LSTM layer
        # Hint: Use nn.LSTM with batch_first=True for easier handling
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers, 
                            batch_first=True, dropout=dropout_prob if num_layers > 1 else 0)  # nn.LSTM(embedding_dim, hidden_dim, num_layers, 
                         #          batch_first=True, dropout=dropout_prob if num_layers > 1 else 0)
        
        # TODO: Initialize dropout layer
        self.dropout = nn.Dropout(dropout_prob)  # nn.Dropout(dropout_prob)
        
        # TODO: Initialize classifier layer
        # Maps from LSTM hidden dimension to number of classes
        self.classifier = nn.Linear(hidden_dim, num_classes)  # nn.Linear(hidden_dim, num_classes)
        
        # Store configuration
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.num_classes = num_classes
    
    def forward(self, input_ids: torch.Tensor, lengths: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Forward pass through LSTM classifier.
        
        Args:
            input_ids (torch.Tensor): Input sequences of shape (batch_size, seq_len)
            lengths (torch.Tensor, optional): Actual lengths of sequences for packing
            
        Returns:
            torch.Tensor: Logits of shape (batch_size, num_classes)
        """
        batch_size = input_ids.size(0)
        
        # TODO: Step 1 - Convert input to embeddings
        # Shape: (batch_size, seq_len) → (batch_size, seq_len, embedding_dim)
        embeddings = self.embedding(input_ids)  # self.embedding(input_ids)
        
        # TODO: Step 2 - Process with LSTM
        # For efficiency with variable lengths, you can use pack_padded_sequence
        if lengths is not None:
            # Optional: Pack padded sequences for efficiency
            # This handles variable-length sequences more efficiently
            # packed_embeddings = nn.utils.rnn.pack_padded_sequence(
            #     embeddings, lengths, batch_first=True, enforce_sorted=False)
            # lstm_output, (hidden, cell) = self.lstm(packed_embeddings)
            # lstm_output, _ = nn.utils.rnn.pad_packed_sequence(lstm_output, batch_first=True)
            
            # For simplicity, just use regular LSTM processing
            lstm_output, (hidden, cell) = self.lstm(embeddings)  # self.lstm(embeddings)
        else:
            # Regular LSTM processing
            # Shape: (batch_size, seq_len, embedding_dim) → (batch_size, seq_len, hidden_dim)
            lstm_output, (hidden, cell) = self.lstm(embeddings)  # self.lstm(embeddings)
        
        # TODO: Step 3 - Extract sequence representation
        # Option 1: Use final hidden state
        # Shape: (num_layers, batch_size, hidden_dim) → (batch_size, hidden_dim)
        final_hidden = hidden[-1]  # hidden[-1]  # Take last layer's hidden state
        
        # Option 2: Use max pooling over sequence (alternative approach)
        # pooled, _ = torch.max(lstm_output, dim=1)  # Max over sequence length
        
        # Option 3: Use mean pooling over sequence (alternative approach)
        # if lengths is not None:
        #     # Mask out padding positions
        #     mask = torch.arange(lstm_output.size(1)).expand(batch_size, -1) < lengths.unsqueeze(1)
        #     masked_output = lstm_output * mask.unsqueeze(-1).float()
        #     pooled = masked_output.sum(dim=1) / lengths.unsqueeze(-1).float()
        # else:
        #     pooled = lstm_output.mean(dim=1)
        
        # TODO: Step 4 - Apply dropout
        representation = self.dropout(final_hidden)  # self.dropout(final_hidden)
        
        # TODO: Step 5 - Classify
        # Shape: (batch_size, hidden_dim) → (batch_size, num_classes)
        logits = self.classifier(representation)  # self.classifier(representation)
        
        return logits


class BidirectionalLSTMClassifier(nn.Module):
    """
    Bidirectional LSTM classifier that processes sequences in both directions.
    
    Architecture:
    Input → Embedding → Bi-LSTM → Concatenated Hidden State → Classifier → Output
    """
    
    def __init__(self, vocab_size: int, embedding_dim: int, hidden_dim: int,
                 num_classes: int, num_layers: int = 1, dropout_prob: float = 0.3):
        """
        Initialize the bidirectional LSTM classifier.
        
        Args:
            vocab_size (int): Size of vocabulary
            embedding_dim (int): Dimension of word embeddings
            hidden_dim (int): Dimension of LSTM hidden state (per direction)
            num_classes (int): Number of output classes
            num_layers (int): Number of LSTM layers
            dropout_prob (float): Dropout probability
        """
        super(BidirectionalLSTMClassifier, self).__init__()
        
        # TODO: Initialize embedding layer
        self.embedding = None  # nn.Embedding(vocab_size, embedding_dim)
        
        # TODO: Initialize bidirectional LSTM
        # Key difference: Set bidirectional=True
        # Note: Output hidden dimension will be 2 * hidden_dim (forward + backward)
        self.lstm = None  # nn.LSTM(embedding_dim, hidden_dim, num_layers,
                         #          batch_first=True, bidirectional=True,
                         #          dropout=dropout_prob if num_layers > 1 else 0)
        
        # TODO: Initialize dropout layer
        self.dropout = None  # nn.Dropout(dropout_prob)
        
        # TODO: Initialize classifier layer
        # Important: Input dimension is 2 * hidden_dim due to bidirectionality
        self.classifier = None  # nn.Linear(2 * hidden_dim, num_classes)
        
        # Store configuration
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.num_classes = num_classes
    
    def forward(self, input_ids: torch.Tensor, lengths: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        Forward pass through bidirectional LSTM classifier.
        
        Args:
            input_ids (torch.Tensor): Input sequences of shape (batch_size, seq_len)
            lengths (torch.Tensor, optional): Actual lengths of sequences
            
        Returns:
            torch.Tensor: Logits of shape (batch_size, num_classes)
        """
        batch_size = input_ids.size(0)
        
        # TODO: Step 1 - Convert input to embeddings
        # Shape: (batch_size, seq_len) → (batch_size, seq_len, embedding_dim)
        embeddings = None  # self.embedding(input_ids)
        
        # TODO: Step 2 - Process with bidirectional LSTM
        # Shape: (batch_size, seq_len, embedding_dim) → (batch_size, seq_len, 2 * hidden_dim)
        lstm_output, (hidden, cell) = None  # self.lstm(embeddings)
        
        # TODO: Step 3 - Extract bidirectional representation
        # The hidden state shape is (num_layers * 2, batch_size, hidden_dim)
        # We want to concatenate forward and backward final hidden states
        
        # Forward direction hidden state (last layer)
        forward_hidden = None  # hidden[-2]  # Second to last (forward direction)
        # Backward direction hidden state (last layer)  
        backward_hidden = None  # hidden[-1]  # Last (backward direction)
        
        # Concatenate forward and backward hidden states
        # Shape: (batch_size, 2 * hidden_dim)
        final_hidden = None  # torch.cat([forward_hidden, backward_hidden], dim=1)
        
        # Alternative approach: Use max/mean pooling over the bidirectional output
        # pooled, _ = torch.max(lstm_output, dim=1)  # Max pooling
        # pooled = lstm_output.mean(dim=1)  # Mean pooling
        
        # TODO: Step 4 - Apply dropout
        representation = None  # self.dropout(final_hidden)
        
        # TODO: Step 5 - Classify
        # Shape: (batch_size, 2 * hidden_dim) → (batch_size, num_classes)
        logits = None  # self.classifier(representation)
        
        return logits


# Utility function to compare models
def compare_lstm_models(vocab_size: int, embedding_dim: int, hidden_dim: int, num_classes: int):
    """
    Compare unidirectional vs bidirectional LSTM models.
    
    Returns information about model architectures and parameter counts.
    """
    # Create both models
    lstm_model = LSTMClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
    bilstm_model = BidirectionalLSTMClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)
    
    # Count parameters
    lstm_params = sum(p.numel() for p in lstm_model.parameters())
    bilstm_params = sum(p.numel() for p in bilstm_model.parameters())
    
    print("Model Comparison:")
    print(f"LSTM Parameters: {lstm_params:,}")
    print(f"Bidirectional LSTM Parameters: {bilstm_params:,}")
    print(f"Parameter Increase: {bilstm_params / lstm_params:.2f}x")
    
    # Test with dummy input
    batch_size, seq_len = 4, 20
    dummy_input = torch.randint(0, vocab_size, (batch_size, seq_len))
    
    with torch.no_grad():
        lstm_output = lstm_model(dummy_input)
        bilstm_output = bilstm_model(dummy_input)
    
    print(f"\nOutput shapes:")
    print(f"LSTM: {lstm_output.shape}")
    print(f"Bidirectional LSTM: {bilstm_output.shape}")
    
    return lstm_model, bilstm_model


# Example usage and testing
if __name__ == "__main__":
    # Test the LSTM classifiers
    vocab_size = 1000
    embedding_dim = 128
    hidden_dim = 256
    num_classes = 2
    
    print("Testing LSTM Classifiers...")
    compare_lstm_models(vocab_size, embedding_dim, hidden_dim, num_classes)