# MAI 5201 Homework 1: Machine Learning Fundamentals for NLP

## Table of Contents
- [Introduction](#introduction)
- [Part 1: From-Scratch Implementation (50 pts)](#part-1-from-scratch-implementation-50-pts) - Questions 1-6
- [Part 2: Library Implementation & Comparison (30 pts)](#part-2-library-implementation--comparison-30-pts) - Questions 7-10
- [Grading & Submission](#grading--submission)

## Introduction

Welcome to your second homework for MAI 5201! This assignment bridges the gap between understanding machine learning theory and applying it to real NLP problems. You'll build sentiment analysis systems from scratch and then compare them with industry-standard implementations.

**🌟 Why This Matters:**
Every recommendation system, review platform, and social media feed relies on sentiment analysis. Netflix uses it to understand user reactions, Amazon analyzes product reviews, and Twitter detects harmful content. The algorithms you'll implement here power billion-dollar industries!

**What you'll learn:**
- **Text Feature Engineering**: Transform raw text into numerical representations that machines can understand
- **Naive Bayes**: The probabilistic foundation of spam filters and text classification
- **Logistic Regression**: The building block of modern deep learning (yes, really!)
- **TF-IDF**: The classic algorithm that powered search engines before neural networks
- **ML Pipeline Design**: Industry best practices for building production ML systems

**Real-World Applications You'll Build:**
- **Movie Review Sentiment Analysis**: Classify reviews as positive or negative (like IMDb and Rotten Tomatoes)
- **Feature Engineering Pipeline**: Extract meaningful signals from messy text data
- **Model Comparison Framework**: A/B test different algorithms to find the best performer
- **Production-Ready Classifier**: Compare your from-scratch implementation with scikit-learn

**Structure:**
1. **Part 1**: From-Scratch Implementation (50 pts) - Q1-Q6: Build ML algorithms using only basic Python
2. **Part 2**: Library Implementation & Comparison (30 pts) - Q7-Q10: Use scikit-learn and compare performance

**Dataset**: 25,000 movie reviews from IMDb with balanced positive/negative labels - the same dataset used in foundational NLP research!

**Due Date**: Sept 12 @ 11:59 PM (Guyana Time)

This project includes an autograder for you to test your solutions locally:
```bash
python autograder.py
```

Access all starter code and supporting files in the `src` directory: [📁](src/)

---

## Part 1: From-Scratch Implementation (50 pts)

Understanding machine learning from first principles is crucial for building intuition, debugging models, and innovating new approaches. In this part, you'll implement core ML algorithms using only basic Python, giving you deep insight into how these systems really work.

**📌 Core Philosophy**: Before you use a library, understand what it's doing! This knowledge will make you a better ML engineer, help you debug mysterious model behaviors, and enable you to customize algorithms for your specific needs.

**Real-World Impact**: 
- **Engineering Interviews**: Companies like Google, Facebook, and Netflix ask candidates to implement ML algorithms from scratch
- **Research**: Novel algorithms often start as from-scratch implementations
- **Debugging**: When scikit-learn gives unexpected results, understanding the internals helps you diagnose the issue
- **Performance**: Sometimes custom implementations outperform libraries for specific use cases

**💡 Pro Tips for Success**:
- Start with simple test cases and gradually add complexity
- Use print statements to debug - visualize intermediate results
- Test edge cases: empty inputs, single samples, identical data
- Compare your results with sklearn implementations to verify correctness

### Files you'll edit:
- `src/text_features.py`: Basic text-to-vector conversion (Q1)
- `src/feature_engineering.py`: Advanced feature extraction techniques (Q2)
- `src/naive_bayes.py`: Probabilistic classifier implementation (Q3)
- `src/logistic_regression.py`: Linear classifier with gradient descent (Q4-Q5)

### Files you can use:
- `src/data/reviews.csv`: Movie review dataset (50,000 reviews)
- `src/autograder.py`: Automated testing system

---

### Q1 (6 pts): Text Feature Extraction

**🎯 What You're Building**: The foundation of all NLP systems - converting human language into numerical representations that machine learning algorithms can understand. This is literally the first step in every text classification system ever built!

**Why It's Revolutionary**: Before these techniques, computers couldn't understand text at all. Your bag-of-words implementation is the same core idea used in Google's original search algorithm and early spam filters that saved email from being unusable.

**Real-World Applications**:
- **Search Engines**: Google's PageRank originally used bag-of-words to understand web page content
- **Spam Detection**: Email providers use similar techniques to identify unwanted messages
- **Document Clustering**: Legal firms automatically organize thousands of documents
- **Content Recommendation**: News sites suggest articles based on text similarity

**🧠 The Core Challenge**: Human language is symbolic and contextual, but machine learning requires numbers. How do you convert "This movie is amazing!" into something a computer can process mathematically?

**The Bag-of-Words Revolution**: 
Treat each document as a "bag" of words (ignore order, just count frequencies). It seems oversimplified, but it works surprisingly well for many tasks!

**Example Transformation**:
```
"I love this great movie! This movie is great!"
↓ (your implementation)
{'i': 1, 'love': 1, 'this': 2, 'great': 2, 'movie': 2, 'is': 1}
↓ (with vocabulary: {'great': 0, 'i': 1, 'is': 2, 'love': 3, 'movie': 4, 'this': 5})
[2, 1, 1, 1, 2, 2]  # Vector ready for machine learning!
```

**💡 Implementation Strategy**:
- **extract_bag_of_words**: Convert single text → word frequency dictionary
- **build_vocabulary**: Collect all unique words → assign consistent indices
- **text_to_vector**: Convert text → numerical vector using vocabulary mapping

**In this question, your task is to** implement the three core functions that convert raw text into numerical feature vectors suitable for machine learning algorithms.

**Test your implementation:**
```bash
python autograder.py -q q1
```

**Functions to implement:**

**A. extract_bag_of_words(text: str) → Dict[str, int] (2 pts)**
```python
# Convert single text to word counts
extract_bag_of_words("This movie was great! I loved this great movie.")
# Returns: {'this': 2, 'movie': 2, 'was': 1, 'great': 2, 'i': 1, 'loved': 1}
```

**B. build_vocabulary(texts: List[str]) → Dict[str, int] (2 pts)**
```python
# Create word-to-index mapping from multiple texts
build_vocabulary(["good movie", "bad movie", "great film"])
# Returns: {'bad': 0, 'film': 1, 'good': 2, 'great': 3, 'movie': 4}
```

**C. text_to_vector(text: str, vocab: Dict[str, int]) → List[int] (2 pts)**
```python
# Convert text to numerical vector using vocabulary
vocab = {"good": 0, "movie": 1, "bad": 2, "great": 3}
text_to_vector("good movie", vocab)
# Returns: [1, 1, 0, 0]  # [good=1, movie=1, bad=0, great=0]
```

---

### Q2 (8 pts): Feature Engineering

**🎯 What You're Building**: Advanced text feature extraction that captures context and meaning beyond simple word counts. You're implementing the techniques that made early NLP systems dramatically more accurate!

**Why Advanced Features Matter**: 
Simple bag-of-words misses crucial information:
- "not good" vs "good" - opposite meanings with overlapping words
- "very good" vs "good" - different intensity levels
- Document length, punctuation, and style carry sentiment signals

**Real-World Applications**:
- **TF-IDF**: Powers search engines and document similarity
- **N-gram Features**: Used in Google Translate and text prediction
- **Statistical Features**: Spam filters analyze writing patterns
- **Feature Combination**: Modern systems blend multiple feature types

**🔥 The N-gram Revolution**: 
Moving beyond single words to word sequences:
- **Unigrams**: "not", "good" → can't capture negation
- **Bigrams**: "not good" → captures context!
- **Trigrams**: "not very good" → even richer meaning

**TF-IDF Magic**: 
Term Frequency-Inverse Document Frequency weights words by importance:
- Frequent words in a document get higher weight (TF)
- Words appearing in many documents get lower weight (IDF)
- Result: "movie" gets less weight than "cinematography" in film reviews

**Statistical Features Goldmine**:
Writing style reveals sentiment:
- **Exclamation marks**: "Amazing!!!" vs "okay."
- **Word length**: Complex words suggest thoughtful reviews
- **Vocabulary diversity**: Varied word choice indicates engagement

**💡 Advanced Techniques You'll Master**:
- **N-gram extraction**: Sliding window over word sequences
- **TF-IDF computation**: Mathematical weighting of term importance
- **Statistical analysis**: Document-level features beyond word counts
- **Feature matrix construction**: Flexible pipeline for combining features

**In this question, your task is to** implement advanced feature engineering techniques that capture context, importance, and stylistic patterns in text.

**Test your implementation:**
```bash
python autograder.py -q q2
```

**Functions to implement:**

**A. add_ngram_features(texts: List[str], n: int) → Dict[str, int] (2 pts)**
```python
# Build vocabulary with n-grams up to length n
add_ngram_features(["good movie", "bad movie"], n=2)
# Returns: {'bad': 0, 'bad movie': 1, 'good': 2, 'good movie': 3, 'movie': 4}
```

**B. compute_tf_idf_features(texts: List[str], vocab: Dict[str, int]) → List[List[float]] (2 pts)**
```python
# Compute TF-IDF weighted feature vectors
texts = ["good movie", "bad movie movie", "good good"]
vocab = {"good": 0, "movie": 1, "bad": 2}
compute_tf_idf_features(texts, vocab)
# Returns: TF-IDF weighted vectors for each text
```

**C. extract_feature_statistics(texts: List[str]) → List[Dict] (2 pts)**
```python
# Extract document-level statistical features
extract_feature_statistics(["Great movie!"])
# Returns: [{'word_count': 2, 'char_count': 12, 'exclamation_count': 1, ...}]
```

**D. build_feature_matrix(texts: List[str], config: Dict) → Tuple[List[List], List[str]] (2 pts)**
```python
# Flexible feature extraction pipeline
config = {'use_unigrams': True, 'use_bigrams': True, 'use_tfidf': True}
build_feature_matrix(["good movie"], config)
# Returns: (feature_matrix, feature_names)
```

---

### Q3 (8 pts): Naive Bayes from Scratch

**🎯 What You're Building**: A probabilistic classifier that's mathematically elegant, surprisingly effective, and forms the foundation of countless real-world systems. Despite its "naive" assumption, it often outperforms much more complex models!

**🧠 The Beautiful Mathematics**: 
Naive Bayes applies Bayes' theorem with the "naive" assumption that features are independent:

P(class|document) = P(document|class) × P(class) / P(document)

**Why "Naive" Works**: 
Even though words aren't truly independent ("not" and "good" clearly interact), the assumption often works well in practice. It's like assuming all your features are uncorrelated - mathematically incorrect but practically useful!

**Real-World Applications**:
- **Spam Detection**: Gmail's spam filter is fundamentally Naive Bayes
- **Medical Diagnosis**: Symptom → disease probability calculations  
- **News Classification**: Automatically categorize articles by topic
- **Sentiment Analysis**: The classic approach before deep learning

**🎲 Probabilistic Thinking**:
Instead of hard classifications, Naive Bayes gives you probabilities:
- "This review is 85% likely to be positive"
- "This email is 2% likely to be spam"
- "This symptom suggests 60% chance of condition X"

**⚡ Why It's Still Relevant**:
- **Fast**: Trains and predicts in linear time
- **Robust**: Works well with small datasets
- **Interpretable**: You can see exactly why it made each decision
- **Baseline**: Still the go-to first model for text classification

**💡 Implementation Deep Dive**:
- **Class Priors**: How common is each sentiment in training data?
- **Feature Likelihoods**: How often does each word appear in positive vs negative reviews?
- **Smoothing**: Handle unseen words gracefully (crucial for real-world robustness)
- **Log Probabilities**: Prevent numerical underflow with tiny probability products

**In this question, your task is to** implement a complete Naive Bayes classifier using only basic Python and mathematical operations.

**Test your implementation:**
```bash
python autograder.py -q q3
```

**Functions to implement:**

**A. calculate_class_priors(labels: List[int]) → Dict[int, float] (2 pts)**
```python
# Calculate P(class) for each class
calculate_class_priors([0, 0, 1, 1, 1])
# Returns: {0: 0.4, 1: 0.6}  # 40% negative, 60% positive
```

**B. calculate_feature_likelihoods(vectors: List[List[int]], labels: List[int]) → Dict[int, List[float]] (3 pts)**
```python
# Calculate P(feature|class) with Laplace smoothing
vectors = [[1, 0, 2], [0, 1, 1], [2, 0, 0]]
labels = [1, 0, 1]
calculate_feature_likelihoods(vectors, labels)
# Returns: {0: [likelihood_per_feature], 1: [likelihood_per_feature]}
```

**C. naive_bayes_predict(vector: List[int], priors: Dict, likelihoods: Dict) → Tuple[int, Dict[int, float]] (2 pts)**
```python
# Predict class and return probabilities
vector = [1, 0, 1]
priors = {0: 0.5, 1: 0.5}
likelihoods = {0: [0.3, 0.4, 0.3], 1: [0.6, 0.2, 0.2]}
naive_bayes_predict(vector, priors, likelihoods)
# Returns: (predicted_class, {class: probability})
```

**D. train_naive_bayes(vectors: List[List[int]], labels: List[int]) → Tuple[Dict, Dict] (1 pt)**
```python
# Complete training pipeline
vectors = [[1, 0], [0, 1], [1, 1]]
labels = [0, 1, 1]
train_naive_bayes(vectors, labels)
# Returns: (priors, likelihoods)
```

---

### Q4 (8 pts): Logistic Regression Core Functions

**🎯 What You're Building**: The mathematical foundation of modern machine learning! Logistic regression is the building block of neural networks, and understanding it deeply will make you a better ML practitioner.

**🧠 The Elegant Mathematics**:
Logistic regression uses the sigmoid function to map any real number to a probability between 0 and 1:
- **Sigmoid**: σ(z) = 1/(1 + e^(-z))  
- **Linear combination**: z = w₁x₁ + w₂x₂ + ... + b
- **Prediction**: P(positive) = σ(z)

**Why Logistic > Linear Regression for Classification**:
- Linear regression can predict negative probabilities or values > 1
- Sigmoid ensures outputs are valid probabilities (0-1 range)
- S-shaped curve naturally models decision boundaries

**Real-World Applications**:
- **Medical Diagnosis**: Probability of disease given symptoms
- **Marketing**: Likelihood of customer purchase
- **Finance**: Credit default risk assessment
- **Deep Learning**: Every neuron in a neural network uses sigmoid-like functions

**🎯 The Gradient Descent Journey**:
Finding optimal weights through iterative improvement:
1. **Make prediction** with current weights
2. **Calculate error** using cross-entropy loss
3. **Compute gradients** (direction to improve)
4. **Update weights** in gradient direction
5. **Repeat** until convergence

**💡 Mathematical Intuition**:
- **Cross-entropy loss**: Penalizes confident wrong predictions heavily
- **Gradients**: Tell you how to adjust each weight to reduce loss
- **Learning rate**: Controls step size (too big = overshoot, too small = slow)
- **Convergence**: When gradients become very small

**In this question, your task is to** implement the core mathematical functions that power logistic regression.

**Test your implementation:**
```bash
python autograder.py -q q4
```

**Functions to implement:**

**A. sigmoid(z) → float/array (2 pts)**
```python
# Sigmoid activation function
sigmoid(0)    # Returns: 0.5
sigmoid(2)    # Returns: ~0.881
sigmoid(-2)   # Returns: ~0.119
```

**B. cross_entropy_loss(y_true, y_pred) → float (3 pts)**
```python
# Cross-entropy loss function
y_true = [1, 0, 1]
y_pred = [0.9, 0.1, 0.8]
cross_entropy_loss(y_true, y_pred)
# Returns: average cross-entropy loss
```

**C. compute_gradients(X, y, weights) → List[float] (3 pts)**
```python
# Compute gradients for weight updates
X = [[1, 2], [1, 3], [1, 1]]  # Features with bias
y = [1, 1, 0]                  # Labels
weights = [0.0, 0.0]           # Current weights
compute_gradients(X, y, weights)
# Returns: [grad_bias, grad_feature]
```

---

### Q5 (8 pts): SGD Implementation

**🎯 What You're Building**: Stochastic Gradient Descent - the optimization algorithm that powers virtually all of modern machine learning, from linear models to GPT-4! You're implementing the same core technique used to train billion-parameter models.

**⚡ Why SGD Changed Everything**:
Before SGD, training ML models on large datasets was computationally impossible. SGD makes it feasible by:
- Using small random batches instead of full dataset
- Making frequent small updates instead of rare large ones
- Enabling online learning (update as new data arrives)

**🎯 The SGD Algorithm**:
```
for each training example or mini-batch:
    1. Forward pass: make predictions
    2. Compute loss and gradients  
    3. Update weights: w = w - α * gradient
    4. Repeat until convergence
```

**Real-World Impact**:
- **Deep Learning**: Every neural network uses SGD variants (Adam, RMSprop)
- **Online Systems**: Models update continuously as new data streams in
- **Large Scale ML**: Enables training on datasets with billions of examples
- **A/B Testing**: Models adapt to changing user behavior in real-time

**💡 Key Concepts You'll Master**:
- **Learning Rate**: Balance between convergence speed and stability
- **Weight Updates**: The fundamental step of machine learning
- **Training Loop**: Iterative optimization process
- **Convergence**: When to stop training

**In this question, your task is to** implement the SGD optimization algorithm and complete logistic regression training.

**Test your implementation:**
```bash
python autograder.py -q q5
```

**Functions to implement:**

**A. sgd_step(weights, gradients, learning_rate) → List[float] (3 pts)**
```python
# Single SGD weight update
weights = [0.1, 0.2]
gradients = [0.05, -0.1]  
learning_rate = 0.1
sgd_step(weights, gradients, learning_rate)
# Returns: [0.095, 0.21]  # weights - learning_rate * gradients
```

**B. train_logistic_regression(X, y, learning_rate, epochs) → List[float] (3 pts)**
```python
# Complete training loop
X = [[1, 1], [1, 0]]  # Features with bias
y = [1, 0]            # Labels
weights = train_logistic_regression(X, y, 0.1, 100)
# Returns: trained weights after 100 epochs
```

**C. logistic_predict(X, weights, threshold=0.5) → List[int] (2 pts)**
```python
# Make binary predictions
X = [[1, 2], [1, 1]]
weights = [0.5, 0.3]
logistic_predict(X, weights, 0.5)
# Returns: [1, 1] or [0, 1] depending on sigmoid outputs
```

---

### Q6 (12 pts): Model Evaluation and Comparison

**🎯 What You're Building**: A comprehensive evaluation framework that goes beyond simple accuracy to provide deep insights into model performance. This is how data scientists make informed decisions about which models to deploy in production!

**📊 Why Accuracy Isn't Enough**:
Imagine a disease that affects 1% of the population. A model that always predicts "healthy" gets 99% accuracy but is completely useless! You need:
- **Precision**: Of positive predictions, how many were correct?
- **Recall**: Of actual positives, how many did you catch?
- **F1-Score**: Harmonic mean balancing precision and recall
- **Confusion Matrix**: Complete breakdown of all prediction types

**🎯 The Evaluation Matrix**:
```
Confusion Matrix:
                Predicted
                Neg  Pos
Actual  Neg     TN   FP
        Pos     FN   TP

Metrics:
- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)  
- Recall = TP / (TP + FN)
- F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

**Real-World Decision Making**:
- **Medical Screening**: High recall (catch all cases) vs precision (avoid false alarms)
- **Spam Detection**: Balance between blocking spam and preserving legitimate emails
- **Content Moderation**: Trade-off between removing harmful content and false positives
- **Financial Fraud**: Cost of missing fraud vs cost of blocking legitimate transactions

**🔍 Error Analysis Power**:
Understanding what your model gets wrong is often more valuable than knowing what it gets right:
- Which types of reviews are misclassified?
- Do short reviews perform worse than long ones?  
- Are certain topics particularly challenging?
- How do the two models fail differently?

**💡 Model Comparison Strategy**:
- **Statistical Significance**: Are performance differences meaningful?
- **Error Complementarity**: Do models make different types of mistakes?
- **Ensemble Potential**: Can you combine models for better performance?
- **Deployment Considerations**: Speed, memory, interpretability trade-offs

**In this question, your task is to** implement comprehensive evaluation metrics and model comparison tools.

**Test your implementation:**
```bash
python autograder.py -q q6
```

**Functions to implement:**

**A. calculate_accuracy(y_true, y_pred) → float (3 pts)**
```python
# Basic accuracy calculation
calculate_accuracy([1, 0, 1, 1, 0], [1, 0, 1, 0, 0])
# Returns: 0.8  # 4 out of 5 correct
```

**B. calculate_precision_recall(y_true, y_pred) → Tuple[float, float] (3 pts)**
```python
# Precision and recall calculation
calculate_precision_recall([1, 1, 0, 1, 0], [1, 0, 0, 1, 1])  
# Returns: (precision, recall)
```

**C. confusion_matrix(y_true, y_pred) → Dict[str, int] (2 pts)**
```python
# Generate confusion matrix
confusion_matrix([0, 0, 1, 1], [0, 1, 0, 1])
# Returns: {'TN': 1, 'FP': 1, 'FN': 1, 'TP': 1}
```

**D. compare_models(y_true, pred1, pred2) → Dict (2 pts)**
```python
# Compare two models' performance
compare_models([1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 1])
# Returns: detailed comparison metrics
```

**E. analyze_errors(texts, y_true, y_pred) → Dict (2 pts)**
```python
# Analyze prediction errors
texts = ["good movie", "bad film", "great story", "poor plot"]
y_true = [1, 0, 1, 0]
y_pred = [1, 1, 1, 0]
analyze_errors(texts, y_true, y_pred)
# Returns: error analysis with misclassified examples
```

---

## Part 2: Library Implementation & Comparison (30 pts)

Now that you understand ML algorithms from first principles, let's see how professional data scientists build production systems using industry-standard libraries. You'll use scikit-learn to implement the same classifiers and compare performance with your from-scratch implementations.

**📌 Learning Goals**: 
- Master scikit-learn's ML pipeline patterns
- Compare library vs custom implementation performance
- Build production-ready text classification systems
- Understand when to use libraries vs custom code

**🚀 Professional ML Pipeline**:
This mirrors real-world industry practices:
1. **Data Loading**: Handle large datasets efficiently
2. **Preprocessing**: Clean and prepare text for analysis  
3. **Feature Engineering**: Use optimized TF-IDF and n-grams
4. **Model Training**: Leverage battle-tested implementations
5. **Evaluation**: Generate comprehensive performance reports
6. **Comparison**: Make data-driven model selection decisions

**💼 Industry Reality Check**:
- **Speed**: Scikit-learn is 10-100x faster than pure Python
- **Robustness**: Libraries handle edge cases you might miss
- **Features**: Advanced techniques (regularization, optimization) built-in
- **Maintenance**: Well-tested, documented, and continuously improved

### Files you'll edit:
- `src/ml_pipeline.py`: Complete scikit-learn pipeline implementation (Q7-Q10)

### Dependencies:
```bash
pip install -r requirements.txt
```

---

### Q7 (8 pts): Basic Pipeline Functionality

**🎯 What You're Building**: The foundation of a production ML system - data loading, preprocessing, and feature extraction using industry-standard tools and patterns.

**🏗️ Pipeline Architecture**:
Modern ML systems follow a consistent pattern:
```
Raw Data → Preprocessing → Feature Extraction → Model Training → Evaluation
```

**Real-World Data Challenges**:
- **Scale**: 25,000 reviews (small by industry standards!)
- **Format**: CSV files, text encoding, missing values
- **Memory**: Efficient data structures for large datasets
- **Reproducibility**: Random seeds for consistent results

**💡 Professional Practices You'll Learn**:
- **Object-Oriented Design**: Encapsulate ML pipeline in a class
- **Configuration Management**: Flexible feature extraction options
- **Error Handling**: Graceful failure and informative error messages
- **Documentation**: Clear interfaces and usage examples

**In this question, your task is to** implement the core pipeline infrastructure for loading data, splitting train/test sets, and extracting features.

**Test your implementation:**
```bash
python autograder.py -q q7
```

**Key Components:**

**A. Pipeline Initialization (2 pts)**
- Set up data paths and random seeds
- Initialize scikit-learn components
- Prepare for reproducible experiments

**B. Data Loading (2 pts)**  
- Load movie review dataset
- Parse text and sentiment labels
- Handle data format validation

**C. Train/Test Split (2 pts)**
- 80/20 train/test split
- Stratified sampling for balanced classes
- Store splits for consistent evaluation

**D. Feature Extraction (2 pts)**
- TF-IDF vectorization with scikit-learn
- Configurable n-gram ranges
- Efficient sparse matrix representations

---

### Q8 (8 pts): Model Training

**🎯 What You're Building**: Train both Naive Bayes and Logistic Regression using scikit-learn's optimized implementations and compare them with your from-scratch versions.

**⚡ Library vs From-Scratch Performance**:
Expect dramatic differences:
- **Speed**: 10-100x faster training and prediction
- **Accuracy**: Sophisticated optimizations and regularization
- **Robustness**: Handles edge cases and numerical stability
- **Features**: Advanced options (regularization, solvers, etc.)

**🧠 Model Comparison Insights**:
- **Naive Bayes**: Often surprisingly competitive despite simplicity
- **Logistic Regression**: Usually more accurate but requires more tuning
- **Dataset Size**: Performance differences may vary with data scale
- **Feature Engineering**: Impact of TF-IDF vs simple bag-of-words

**💡 Production Considerations**:
- **Training Time**: Critical for models that retrain frequently
- **Prediction Speed**: Important for real-time applications
- **Memory Usage**: Affects deployment costs and scalability
- **Interpretability**: Balance performance with explainability

**In this question, your task is to** implement scikit-learn model training and make predictions on the test set.

**Test your implementation:**
```bash
python autograder.py -q q8
```

**Key Components:**

**A. Naive Bayes Training (4 pts)**
- Use MultinomialNB with appropriate hyperparameters
- Train on TF-IDF features
- Generate predictions on test set
- Store trained model for evaluation

**B. Logistic Regression Training (4 pts)**
- Use LogisticRegression with proper configuration
- Handle convergence and regularization
- Generate predictions on test set
- Store trained model for evaluation

---

### Q9 (8 pts): Performance Benchmarks

**🎯 What You're Building**: Achieve production-level performance on a real dataset! Your models must meet minimum accuracy thresholds to demonstrate mastery of the techniques.

**🎯 Performance Targets**:
Based on the solution implementation, your models should achieve:
- **Minimum Accuracy**: 75% on test set
- **Minimum F1-Score**: 75% balanced performance
- These are realistic, achievable targets with proper implementation

**📊 Benchmark Context**:
Movie review sentiment analysis results:
- **Random Baseline**: 50% (flip a coin)
- **Simple Bag-of-Words**: ~70-75%
- **TF-IDF + Proper ML**: ~80-85%
- **State-of-the-Art (2024)**: ~95%+ (BERT, GPT)

**🔍 Performance Analysis**:
If your models underperform, check:
- **Feature Engineering**: Are you using TF-IDF properly?
- **Preprocessing**: Text cleaning and normalization
- **Hyperparameters**: Default settings might not be optimal
- **Data Quality**: Are labels correct? Any data leakage?

**💡 Optimization Strategies**:
- **Feature Tuning**: N-gram ranges, vocabulary size, min/max document frequency
- **Model Hyperparameters**: Regularization, solvers, convergence criteria
- **Data Preprocessing**: Stop word removal, stemming, case normalization
- **Ensemble Methods**: Combine multiple models for better performance

**In this question, your task is to** achieve strong performance on the movie review classification task.

**Test your implementation:**
```bash
python autograder.py -q q9
```

**Performance Requirements:**

**A. Naive Bayes Performance (4 pts)**
- Accuracy ≥ 75%
- F1-Score ≥ 75%

**B. Logistic Regression Performance (4 pts)**  
- Accuracy ≥ 75%
- F1-Score ≥ 75%

---

### Q10 (6 pts): Pipeline Integration & Comparison

**🎯 What You're Building**: A complete ML pipeline that orchestrates all components and provides comprehensive model comparison - exactly what you'd build in a professional data science role!

**🔄 Complete Pipeline Flow**:
```
Data Loading → Preprocessing → Feature Engineering → 
Model Training → Evaluation → Comparison → Decision
```

**📊 Comprehensive Evaluation**:
Your pipeline should generate:
- **Individual Model Metrics**: Accuracy, precision, recall, F1 for each model
- **Confusion Matrices**: Detailed error analysis
- **Model Comparison**: Head-to-head performance comparison
- **Winner Selection**: Best model for each metric
- **Dataset Statistics**: Data size, class distribution, feature counts

**💼 Business Impact**:
In production, this analysis drives:
- **Model Selection**: Which algorithm to deploy?
- **Resource Allocation**: Training time vs accuracy trade-offs
- **Performance Monitoring**: Baseline metrics for future comparison
- **Stakeholder Reporting**: Clear, actionable insights

**🎯 Integration Testing**:
Your complete pipeline must:
- Handle the full dataset without errors
- Generate all required metrics
- Compare models fairly
- Provide clear recommendations

**In this question, your task is to** integrate all components into a seamless pipeline that provides comprehensive model evaluation and comparison.

**Test your implementation:**
```bash
python autograder.py -q q10
```

**Key Components:**

**A. Complete Pipeline Execution (3 pts)**
- Orchestrate all pipeline steps
- Handle errors gracefully
- Return comprehensive results dictionary
- Include dataset metadata and statistics

**B. Model Comparison Framework (3 pts)**
- Compare all evaluation metrics
- Identify best model for each metric
- Generate summary statistics
- Provide actionable insights

---

## Grading & Submission

### Assessment Breakdown

| Component | Points | Description |
|-----------|---------|-------------|
| **Part 1: From-Scratch Implementation** | **50** | **Core ML algorithms in pure Python** |
| Q1: Text Feature Extraction | 6 | Bag-of-words, vocabulary, vectorization |
| Q2: Feature Engineering | 8 | N-grams, TF-IDF, statistical features |
| Q3: Naive Bayes from Scratch | 8 | Probabilistic classifier implementation |
| Q4: Logistic Regression Core Functions | 8 | Sigmoid, loss, gradients |
| Q5: SGD Implementation | 8 | Gradient descent optimization |
| Q6: Model Evaluation and Comparison | 12 | Metrics, confusion matrix, error analysis |
| **Part 2: Library Implementation** | **30** | **Professional ML pipeline** |
| Q7: Basic Pipeline Functionality | 8 | Data loading, preprocessing, features |
| Q8: Model Training | 8 | Scikit-learn model implementation |
| Q9: Performance Benchmarks | 8 | Achieve 75%+ accuracy and F1-score |
| Q10: Pipeline Integration & Comparison | 6 | Complete system integration |
| **Total Points** | **80** | |

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

### Dependencies Installation

```bash
pip install -r requirements.txt
```

Required packages:
- numpy>=1.21.0
- scikit-learn>=1.0.0
- pandas>=1.3.0
- matplotlib>=3.5.0

### Performance Expectations

Your implementations should achieve:
- **Part 1 (From-Scratch)**: ~70-75% accuracy (expected given basic implementations)
- **Part 2 (Scikit-learn)**: ~80-85% accuracy (with optimized libraries and features)
- **Speed Comparison**: Library implementations 10-100x faster than from-scratch

### Final Submission

1. **Fork the Repository**: Create a fork of the course repository
2. **Create Your Submission Folder**: Add your work in `submissions/[your-name]/`
3. **Commit Your Changes**: Ensure all changes are committed with detailed messages
4. **Push Your Changes**: Push to your forked repository
5. **Create a Pull Request**: Include detailed description and answers to:
   - Which algorithm performed better and why?
   - How did library performance compare to your from-scratch implementations?
   - What challenges did you encounter with feature engineering?
   - What insights did you gain about the movie review dataset?

### Submission Requirements

Your submission folder should contain:
- All modified Python files (`text_features.py`, `feature_engineering.py`, etc.)
- Performance comparison results/screenshots
- A `README.md` documenting your approach, results, and insights

**Due Date**: Sept 12 @ 11:59 PM (Guyana Time)

---

### Tips for Success

**🚀 Implementation Strategy**:
1. **Start Early**: Machine learning involves experimentation and debugging
2. **Test Incrementally**: Use the autograder frequently to catch issues early
3. **Debug with Small Examples**: Test with simple inputs before full dataset
4. **Compare Outputs**: Verify your from-scratch results match expected behavior
5. **Profile Performance**: Time your implementations vs library versions

**📈 Optimization Mindset**:
- **From-Scratch Goal**: Correctness and understanding over speed
- **Library Goal**: Achieve high performance and learn professional tools
- **Comparison Goal**: Understand trade-offs between custom and library code

**🔍 Debugging Strategies**:
- **Print Intermediate Results**: Visualize data flow through your pipeline
- **Test Edge Cases**: Empty inputs, single samples, identical data
- **Compare with sklearn**: Use library implementations to verify your logic
- **Read Error Messages**: Autograder provides detailed feedback

**📊 Feature Engineering Tips**:
- **Text Preprocessing**: Clean text consistently across pipeline
- **Feature Selection**: More features isn't always better
- **Dimensionality**: Monitor feature matrix size and sparsity
- **Validation**: Always validate feature extraction on known examples

**🎯 Performance Optimization**:
- **Hyperparameter Tuning**: Experiment with different configurations
- **Feature Engineering**: TF-IDF parameters can significantly impact performance
- **Data Quality**: Ensure consistent preprocessing between training and testing
- **Model Selection**: Sometimes simpler models outperform complex ones

**🌟 Beyond the Assignment**:
- **Experiment with Variations**: Try different preprocessing or features
- **Analyze Errors**: Look at misclassified examples to understand model limitations
- **Compare with Baselines**: How much better are ML models than simple heuristics?
- **Research Extensions**: What modern techniques could improve performance?

Remember: The goal is to build intuition for how ML systems work and gain practical experience with both custom implementations and professional tools. Focus on understanding the concepts and making principled engineering decisions!

**Good luck!** 🚀
