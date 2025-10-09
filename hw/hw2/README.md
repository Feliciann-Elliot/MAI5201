# MAI 5201 Homework 2: Neural Networks for NLP

## Table of Contents
- [Introduction](#introduction)
- [Part 1: Feedforward Neural Classifier (25 pts)](#part-1-feedforward-neural-classifier-25-pts) - Question 1
- [Part 2: Training Pipeline (20 pts)](#part-2-training-pipeline-20-pts) - Question 2
- [Part 3: Sequence Models (35 pts)](#part-3-sequence-models-35-pts) - Questions 3-4
- [Part 4: Multi-Dataset Evaluation (15 pts)](#part-4-multi-dataset-evaluation-15-pts) - Questions 5-6
- [Grading & Submission](#grading--submission)

## Introduction

Welcome to your second homework for MAI 5201! This assignment moves beyond basic text processing to implement the neural network architectures that power modern NLP systems. You'll build the same types of models used in sentiment analysis, text classification, and language understanding.

**🌟 Why This Matters:**
Neural networks have revolutionized NLP - from basic feedforward classifiers to sophisticated sequence models like LSTMs. The techniques you'll implement here are the building blocks of systems like sentiment analysis APIs, content moderation tools, and text classification services used by millions daily.

**What you'll learn:**
- **Feedforward Networks**: The foundation of deep learning for text classification
- **Training Pipelines**: How to properly train, validate, and evaluate neural networks
- **Sequence Models**: LSTMs and bidirectional architectures for capturing text patterns
- **Real-World Evaluation**: Testing models across multiple datasets and domains

**Real-World Applications You'll Build:**
- Sentiment analysis classifier (like those used by social media platforms)
- LSTM text classifier (powering content categorization systems)
- Multi-dataset evaluation framework (how production ML teams assess model quality)

**Structure:**
1. **Part 1**: Feedforward Neural Classifier (25 pts) - Q1: Basic neural architecture
2. **Part 2**: Training Pipeline (20 pts) - Q2: Complete training and validation system
3. **Part 3**: Sequence Models (35 pts) - Q3-Q4: LSTM and bidirectional LSTM classifiers
4. **Part 4**: Multi-Dataset Evaluation (15 pts) - Q5-Q6: Cross-domain model assessment

**Due Date**: October 14, 2025

This project includes an autograder for you to test your solutions locally:
```bash
python autograder.py
```

Access all starter code and supporting files in the `src` directory: [📁](src/)

---

## Part 1: Feedforward Neural Classifier (25 pts)

Build the foundation of neural text classification - a feedforward network that transforms text into meaningful predictions. This is the same architecture used by early neural sentiment analyzers and still powers many production text classification systems today.

**🎯 What You're Building**: A neural network that takes tokenized text, learns meaningful representations through embedding and hidden layers, and outputs class predictions.

**Why It Matters**: 
- **Production ML**: Many real-world text classifiers use feedforward architectures for their speed and simplicity
- **Foundation Skills**: Understanding feedforward networks is essential before moving to more complex architectures
- **Practical Applications**: Content moderation, spam detection, and basic sentiment analysis

**Real-World Applications**:
- **Email Filtering**: Gmail's spam detection uses similar architectures
- **Content Moderation**: Social media platforms classify harmful content
- **Customer Support**: Automatic ticket routing based on text content
- **E-commerce**: Product review sentiment analysis

### Q1 (25 pts): Feedforward Neural Classifier

**🎯 Architecture Overview**: 
```
Input Text → Tokenization → Embedding Layer → Hidden Layers → Output Layer → Predictions
```

**Key Components You'll Implement**:
- **Embedding Layer**: Convert token IDs to dense vector representations
- **Hidden Layers**: Two fully connected layers with ReLU activation
- **Output Layer**: Final classification layer
- **Forward Pass**: Complete data flow through the network

**Real-World Design Considerations**:
- **Embedding Dimension**: Balance between model expressiveness and computational cost
- **Hidden Layer Size**: Sufficient capacity without overfitting
- **Attention Masking**: Handle variable-length sequences properly
- **Mean Pooling**: Aggregate sequence representations for classification

**Test your implementation:**
```bash
python autograder.py -q q1
```

### Files you'll edit:
- `src/basic_classifier.py`: Your feedforward neural network implementation

### Files you can use:
- `src/data_utils.py`: Text processing and dataset utilities
- `src/autograder.py`: Automated testing system

---

## Part 2: Training Pipeline (20 pts)

Implement a complete training system with proper validation, early stopping, and model management. This represents industry best practices for training neural networks reliably and efficiently.

**🎯 What You're Building**: A production-quality training pipeline that can take any PyTorch model and train it properly with validation monitoring and early stopping.

**Why Training Pipelines Matter**:
- **Reproducibility**: Consistent training procedures across different models and datasets
- **Efficiency**: Proper validation prevents overfitting and reduces training time
- **Production Readiness**: Real ML systems require robust training procedures
- **Debugging**: Good training loops make it easier to diagnose model issues

**Real-World Applications**:
- **Model Development**: Data scientists use similar pipelines for experimentation
- **Production Training**: Automated retraining systems in production ML pipelines
- **Research**: Academic labs use standardized training procedures for fair comparisons
- **MLOps**: Training pipelines integrate with deployment and monitoring systems

### Q2 (20 pts): Training Loop Implementation

**Core Functions You'll Implement**:

**`train_epoch()`**: Single training epoch with gradient updates
- Forward pass through model
- Loss calculation and backpropagation
- Parameter updates with optimizer
- Training metrics tracking

**`validate_epoch()`**: Validation without parameter updates
- Model in evaluation mode
- No gradient computation
- Validation metrics calculation
- Performance monitoring

**`train_model()`**: Complete training pipeline
- Multi-epoch training loop
- Validation after each epoch
- Early stopping implementation
- Best model state management

**Industry Best Practices You'll Learn**:
- **Early Stopping**: Prevent overfitting by monitoring validation loss
- **Model Checkpointing**: Save best model states during training
- **Training History**: Track metrics for analysis and debugging
- **Device Management**: Proper GPU/CPU handling

**Test your implementation:**
```bash
python autograder.py -q q2
```

### Files you'll edit:
- `src/training.py`: Your training pipeline implementation

---

## Part 3: Sequence Models (35 pts)

Move beyond simple feedforward networks to implement LSTM-based models that can capture sequential patterns in text. These models power many real-world NLP applications that require understanding of word order and context.

**🎯 What You're Building**: LSTM and bidirectional LSTM classifiers that can capture temporal dependencies in text sequences.

**Why Sequence Models Matter**:
- **Context Understanding**: Word order and sequence patterns matter for meaning
- **Long-Range Dependencies**: Capture relationships between distant words
- **State-of-the-Art Performance**: LSTMs were the dominant architecture before Transformers
- **Production Use**: Still widely used for many NLP tasks due to efficiency

**Real-World Applications**:
- **Sentiment Analysis**: Understanding negation and context-dependent sentiment
- **Named Entity Recognition**: Identifying entities that span multiple words
- **Text Generation**: Language models and autocomplete systems
- **Document Classification**: Longer documents require sequential processing

### Q3 (15 pts): LSTM Text Classifier

**🎯 Architecture**: Unidirectional LSTM for sequence classification
```
Input → Embedding → LSTM → Final Hidden State → Classifier → Output
```

**Key Components**:
- **LSTM Layer**: Capture sequential patterns and dependencies
- **Hidden State Extraction**: Use final hidden state for classification
- **Sequence Length Handling**: Process variable-length inputs efficiently

### Q4 (20 pts): Bidirectional LSTM Classifier

**🎯 Architecture**: Bidirectional LSTM for enhanced sequence understanding
```
Input → Embedding → Bi-LSTM → Concatenated Hidden States → Classifier → Output
```

**Advanced Features**:
- **Bidirectional Processing**: Information flows both forward and backward
- **State Concatenation**: Combine forward and backward representations
- **Enhanced Context**: Better understanding of word meanings in context

**Bidirectional Advantages**:
- **Complete Context**: Each word sees both past and future context
- **Better Representations**: More informed hidden states
- **Improved Performance**: Typically outperforms unidirectional models

**Test your implementation:**
```bash
python autograder.py -q q3
python autograder.py -q q4
```

### Files you'll edit:
- `src/sequence_models.py`: Your LSTM implementations

---

## Part 4: Multi-Dataset Evaluation (15 pts)

Implement a comprehensive evaluation framework that tests your models across multiple real-world datasets. This simulates how production ML teams assess model quality and generalization.

**🎯 What You're Building**: An evaluation system that loads multiple datasets, runs your trained models, and provides comprehensive performance analysis.

**Why Multi-Dataset Evaluation Matters**:
- **Generalization Assessment**: How well do models perform across different domains?
- **Robustness Testing**: Identify dataset-specific biases and weaknesses
- **Production Readiness**: Real systems must work on diverse inputs
- **Research Standards**: Academic papers typically report results on multiple benchmarks

**Real-World Applications**:
- **Model Selection**: Choose the best architecture for production deployment
- **Domain Transfer**: Understand how models perform when deployed to new domains
- **Quality Assurance**: Comprehensive testing before production release
- **Performance Monitoring**: Track model performance across different user segments

**Datasets You'll Work With**:
- **IMDb Movie Reviews**: Binary sentiment classification (entertainment domain)
- **AG News**: 4-class news categorization (journalism domain)
- Real datasets with 25,000+ samples each via Hugging Face

### Q5-Q6 (15 pts): Multi-Dataset Application and Evaluation

**Core Functionality**:
- **Dataset Loading**: Automatic download and processing of real datasets
- **Model Evaluation**: Run trained models on multiple test sets
- **Performance Analysis**: Comprehensive metrics and domain comparison
- **Results Visualization**: Clear presentation of cross-dataset performance

**Evaluation Metrics**:
- **Accuracy**: Basic classification performance
- **Random Baseline**: Compare against chance performance
- **Domain Analysis**: Understand which domains are easier/harder
- **Improvement Metrics**: Quantify gains over simple baselines

**Test your implementation:**
```bash
python autograder.py -q q5
python autograder.py -q q6
```

### Files you'll edit:
- `src/multi_dataset_eval.py`: Your evaluation framework

---

## Grading & Submission

### Assessment Breakdown

| Component | Points | Description |
|-----------|---------|-------------|
| **Part 1: Feedforward Classifier** | **25** | **Neural network fundamentals** |
| Q1: Basic Neural Architecture | 25 | Embedding layers, hidden layers, forward pass |
| **Part 2: Training Pipeline** | **20** | **Production training systems** |
| Q2: Training Implementation | 20 | Training loops, validation, early stopping |
| **Part 3: Sequence Models** | **35** | **Advanced architectures** |
| Q3: LSTM Classifier | 15 | Unidirectional LSTM implementation |
| Q4: Bidirectional LSTM | 20 | Bidirectional architecture with state concatenation |
| **Part 4: Multi-Dataset Evaluation** | **15** | **Real-world assessment** |
| Q5-Q6: Evaluation Framework | 15 | Cross-dataset testing and analysis |
| **Total Points** | **95** | |

### Autograder Usage

Test your complete solution:
```bash
python autograder.py
```

Test specific questions:
```bash
python autograder.py -q q1
python autograder.py -q q2
# ... etc
```

### Requirements

Install required dependencies:
```bash
pip install -r requirements.txt
```

**Key Dependencies**:
- `torch>=1.9.0`: PyTorch for neural network implementation
- `datasets>=2.0.0`: Hugging Face datasets for real data
- `numpy<2.0`: Numerical computations (version compatibility)
- `tqdm>=4.62.0`: Progress bars for training loops

### Submission Requirements

Your submission should include:
- All modified Python files with your implementations
- Ensure all functions pass the autograder tests
- Clean, well-commented code following Python best practices

**Due Date**: October 14, 2025

---

### Tips for Success

**🚀 Development Strategy**:
1. **Start with Q1**: Build the foundation before moving to complex models
2. **Test Incrementally**: Use the autograder frequently to catch issues early
3. **Understand the Data**: Examine sample inputs and outputs carefully
4. **Handle Edge Cases**: Real datasets have variable lengths and missing data

**🧠 Neural Network Tips**:
- **Gradient Flow**: Ensure your forward pass maintains gradients
- **Device Consistency**: Keep all tensors on the same device (CPU/GPU)
- **Batch Processing**: Handle batch dimensions correctly in all operations
- **Memory Management**: Use proper tensor operations to avoid memory leaks

**🔄 Training Best Practices**:
- **Learning Rates**: Start with standard values (0.001) and adjust if needed
- **Batch Sizes**: 32 is often a good starting point for text classification
- **Early Stopping**: Monitor validation loss to prevent overfitting
- **Reproducibility**: Set random seeds for consistent results

**📊 Evaluation Insights**:
- **Domain Differences**: Some datasets are inherently harder than others
- **Model Comparison**: Compare your architectures fairly on the same data
- **Performance Analysis**: Understand why models perform differently across domains
- **Real-World Considerations**: Consider inference speed vs. accuracy tradeoffs

**🐛 Debugging Strategies**:
- **Shape Errors**: Print tensor shapes to debug dimension mismatches
- **NaN Values**: Check for division by zero or unstable gradients
- **Memory Issues**: Use smaller batch sizes if you run out of memory
- **Training Stagnation**: Verify your gradients are flowing correctly

Remember: Focus on understanding the fundamental concepts of neural text classification. These skills form the foundation for more advanced NLP architectures!

**Good luck!** 🚀