"""
MAI 5201 - Homework 2: Neural Networks for NLP
Part 1: Basic Neural Text Classification
Q2: Training Loop Implementation (15 pts)

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement the training and validation functions below
- Include proper loss calculation, optimization, and metrics tracking
- Implement early stopping to prevent overfitting
- Support both binary and multi-class classification
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import numpy as np
from typing import Dict, List, Tuple, Optional
from sklearn.metrics import precision_recall_fscore_support
from tqdm import tqdm

def _ensure_vocab_built_from_loader(loader):
    ds = getattr(loader, "dataset", None)
    tok = getattr(ds, "tokenizer", None)
    if tok is None:
        return

    needs_build = False
    if hasattr(tok, "vocab_built"): # Check for vocab_built first, as per SimpleTokenizer
        needs_build = not bool(getattr(tok, "vocab_built", True))
    elif hasattr(tok, "is_built"): # Fallback for other potential tokenizers
        needs_build = not bool(getattr(tok, "is_built", True))
    elif hasattr(tok, "word2id"):
        needs_build = len(getattr(tok, "word2id", {})) == 0

    # Build from raw texts if available
    if needs_build and hasattr(ds, "texts") and ds.texts:
        tok.build_vocab(ds.texts)


def train_epoch(model: nn.Module, train_loader: DataLoader, optimizer: optim.Optimizer, 
                criterion: nn.Module, device: torch.device) -> Tuple[float, float]:
    """
    Train the model for one epoch.
    
    Args:
        model: Neural network model
        train_loader: Training data loader
        optimizer: Optimizer (e.g., Adam)
        criterion: Loss function (e.g., CrossEntropyLoss)
        device: Device to run training on (cpu/cuda)
        
    Returns:
        Tuple[float, float]: Average loss and accuracy for the epoch
    """
    # TODO: Implement training for one epoch
    _ensure_vocab_built_from_loader(train_loader)
   
    # Step 1: Set model to training mode
    model.train()
    
    total_loss = 0.0
    correct_predictions = 0
    total_samples = 0
    
    # Step 2: Iterate through training batches
    for batch in tqdm(train_loader, desc="Training"):
        # TODO: Extract input_ids and labels from batch
        # Batch format: {'input_ids': tensor, 'labels': tensor, 'attention_mask': tensor (optional)}
        input_ids = batch['input_ids'].to(device)
        labels = batch['labels'].to(device)
        attention_mask = batch.get('attention_mask', None)
        if attention_mask is not None:
            attention_mask = attention_mask.to(device)
        
        # Step 3: Zero gradients
        # TODO: Clear gradients from previous iteration
        optimizer.zero_grad()

        # Step 4: Forward pass
        # TODO: Get model predictions
        if attention_mask is not None:
            logits = model(input_ids, attention_mask=attention_mask) # Pass input_ids (and attention_mask if available) to model
        else:
            logits = model(input_ids)

        # Step 5: Calculate loss
        # TODO: Compute loss using criterion
        loss = criterion(logits, labels)
        
        # Step 6: Backward pass
        # TODO: Compute gradients
        loss.backward()

        # Step 7: Update weights
        # TODO: Apply optimizer step
        optimizer.step()

        # Step 8: Track metrics
        total_loss += loss.item()
        
        # Calculate accuracy
        predictions = torch.argmax(logits, dim=-1)
        correct_predictions += (predictions == labels).sum().item()
        total_samples += labels.size(0)
    
    # Calculate average metrics
    avg_loss = total_loss / len(train_loader)
    accuracy = correct_predictions / total_samples
    
    return avg_loss, accuracy


def validate_epoch(model: nn.Module, val_loader: DataLoader, criterion: nn.Module, 
                  device: torch.device) -> Tuple[float, float]:
    """
    Validate the model for one epoch.
    
    Args:
        model: Neural network model
        val_loader: Validation data loader
        criterion: Loss function
        device: Device to run validation on
        
    Returns:
        Tuple[float, float]: Average loss and accuracy for the epoch
    """
    # TODO: Implement validation for one epoch
    _ensure_vocab_built_from_loader(val_loader)
    
    # Step 1: Set model to evaluation mode
    model.eval()
    
    total_loss = 0.0
    correct_predictions = 0
    total_samples = 0
    
    # Step 2: Disable gradient computation for efficiency
    with torch.no_grad():
        for batch in tqdm(val_loader, desc="Validation"):
            # TODO: Extract input_ids and labels from batch
            input_ids = batch['input_ids'].to(device)
            labels = batch['labels'].to(device)
            attention_mask = batch.get('attention_mask', None)
            if attention_mask is not None:
                attention_mask = attention_mask.to(device)
            
            # Step 3: Forward pass (no gradients needed)
            # TODO: Get model predictions
            if attention_mask is not None:
                logits = model(input_ids, attention_mask=attention_mask)
            else:
                logits = model(input_ids)            
            
            # Step 4: Calculate loss
            # TODO: Compute loss
            loss = criterion(logits, labels)
            
            # Step 5: Track metrics
            total_loss += loss.item()
            
            # Calculate accuracy
            predictions = torch.argmax(logits, dim=-1)
            correct_predictions += (predictions == labels).sum().item()
            total_samples += labels.size(0)
    
    # Calculate average metrics
    avg_loss = total_loss / len(val_loader)
    accuracy = correct_predictions / total_samples
    
    return avg_loss, accuracy


def train_model(model: nn.Module, train_loader: DataLoader, val_loader: DataLoader,
                num_epochs: int = 10, learning_rate: float = 0.001, 
                patience: int = 3, device: torch.device = None) -> Dict[str, List[float]]:
    """
    Complete training pipeline with early stopping.
    
    Args:
        model: Neural network model to train
        train_loader: Training data loader
        val_loader: Validation data loader
        num_epochs: Maximum number of epochs to train
        learning_rate: Learning rate for optimizer
        patience: Number of epochs to wait before early stopping
        device: Device to run training on
        
    Returns:
        Dict[str, List[float]]: Training history with losses and accuracies
    """
    # Setup device
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model = model.to(device)
    
    # TODO: Initialize optimizer and loss function
    # Hint: Use Adam optimizer and CrossEntropyLoss
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  # torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()  # nn.CrossEntropyLoss()
    
    # Initialize tracking variables
    history = {
        'train_loss': [],
        'train_accuracy': [],
        'val_loss': [],
        'val_accuracy': []
    }
    
    best_val_loss = float('inf')
    patience_counter = 0
    best_model_state = None
    
    print(f"Training on device: {device}")
    print(f"Model has {sum(p.numel() for p in model.parameters()):,} parameters")
    
    # Training loop
    for epoch in range(num_epochs):
        print(f"\nEpoch {epoch + 1}/{num_epochs}")
        print("-" * 50)
        
        # Train for one epoch
        train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion, device)
        
        # Validate for one epoch
        val_loss, val_acc = validate_epoch(model, val_loader, criterion, device)
        
        # Update history
        history['train_loss'].append(train_loss)
        history['train_accuracy'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_accuracy'].append(val_acc)
        
        # Print epoch results
        print(f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}")
        print(f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        # TODO: Implement early stopping logic
        # Check if validation loss improved
        if val_loss < best_val_loss:
            # TODO: Update best validation loss and save model state
            best_val_loss = val_loss
            patience_counter = 0
            best_model_state = model.state_dict()  # Save model.state_dict()
            print(f"✓ New best validation loss: {val_loss:.4f}")
        else:
            # TODO: Increment patience counter
            patience_counter += 1
            print(f"No improvement. Patience: {patience_counter}/{patience}")
        
        # TODO: Check if we should stop early
        if patience_counter >= patience:
            print(f"\nEarly stopping after {epoch + 1} epochs!")
            break
    
    # TODO: Load best model state
    if best_model_state is not None:
        pass  # model.load_state_dict(best_model_state)
        print("Loaded best model from training")
    
    return history


def evaluate_model(model: nn.Module, test_loader: DataLoader, 
                  device: torch.device = None) -> Dict[str, float]:
    """
    Evaluate the trained model on test data.
    
    Args:
        model: Trained neural network model
        test_loader: Test data loader
        device: Device to run evaluation on
        
    Returns:
        Dict[str, float]: Evaluation metrics
    """
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model = model.to(device)
    model.eval()
    
    all_predictions = []
    all_labels = []
    
    # TODO: Implement model evaluation
    with torch.no_grad():
        for batch in tqdm(test_loader, desc="Evaluating"):
            # TODO: Extract inputs and labels
            input_ids = batch['input_ids'].to(device)
            labels = batch['labels'].to(device)
            attention_mask = batch.get('attention_mask', None)
            if attention_mask is not None:
                attention_mask = attention_mask.to(device)
            
            # TODO: Get predictions
            if attention_mask is not None:
                logits = model(input_ids, attention_mask=attention_mask)  # model forward pass
            else:
                logits = model(input_ids)
            
            predictions = torch.argmax(logits, dim=-1)  # torch.argmax(logits, dim=-1)
            
            # Store for metrics calculation
            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    # Calculate metrics
    all_predictions = np.array(all_predictions)
    all_labels = np.array(all_labels)
    
    accuracy = (all_predictions == all_labels).mean()
    
    # TODO: Add more metrics (precision, recall, F1)
    # Hint: You can use sklearn.metrics for additional metrics
    precision, recall, f1, _ = precision_recall_fscore_support(all_labels, all_predictions, average='weighted')
        
    metrics = {
        'accuracy': accuracy,
        'num_samples': len(all_labels),
        'num_correct': (all_predictions == all_labels).sum()
    }
    
    return metrics


# Example usage and testing
if __name__ == "__main__":
    # This would normally use real data loaders
    print("Training utilities ready!")
    print("Import this module and use train_model() function")
    print("Example:")
    print("history = train_model(model, train_loader, val_loader, num_epochs=10)")