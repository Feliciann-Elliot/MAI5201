# Assignment 6: GloVe: Global Vectors for Word Representation

## Paper Information
**Title**: GloVe: Global Vectors for Word Representation  
**Authors**: Jeffrey Pennington, Richard Socher, Christopher D. Manning (2014)  
**URL**: https://aclanthology.org/D14-1162/  
**Due Date**: September 11, 2025 @ 11:59 PM (GYD)

## Assignment Overview
This is the sixth paper summary assignment for MAI 5201. You will read the influential 2014 GloVe paper by Pennington et al. that bridges the gap between count-based and predictive methods for learning word representations. This paper builds directly on the Word2Vec foundations covered in Assignment 5 and connects to Week 6's coverage of vector semantics and distributional methods.

## Historical Context and Significance
GloVe emerged at a time when the field was divided between two paradigms: global matrix factorization methods (like LSA) that captured global corpus statistics but performed poorly on analogies, and local context window methods (like Word2Vec) that performed well on analogies but didn't explicitly utilize global statistics. The Stanford team recognized that both approaches had complementary strengths and developed GloVe to combine the best of both worlds.

The paper's impact was significant: GloVe became one of the most widely used word embedding methods, often outperforming Word2Vec on various tasks while providing a more interpretable training objective. The work also influenced subsequent research into how global and local information can be combined in representation learning, principles that continue to inform modern approaches.

## Key Technical Contributions
- **Log-bilinear Model**: A weighted least squares objective that directly incorporates global co-occurrence statistics
- **Co-occurrence Matrix Factorization**: Explicit use of global word-word co-occurrence information from the entire corpus
- **Weighted Training Objective**: A sophisticated weighting function that handles frequent and rare co-occurrences appropriately
- **Theoretical Foundation**: Mathematical justification for why ratios of co-occurrence probabilities encode meaning
- **Empirical Performance**: Superior results on word analogy tasks compared to existing methods
- **Computational Efficiency**: Faster convergence than Word2Vec while achieving better performance

## Direct Connection to Course Content
This paper extends Week 6's vector semantics coverage by:
- **Combining Approaches**: Merging global matrix factorization with local context prediction methods
- **Co-occurrence Statistics**: Explicitly modeling word-word co-occurrence patterns from distributional semantics
- **Vector Arithmetic**: Demonstrating that semantic relationships emerge from the training objective's mathematical structure
- **Evaluation Methods**: Using word analogy tasks and similarity benchmarks to validate representation quality
- **Computational Trade-offs**: Balancing statistical coverage with computational efficiency

## Key Questions to Consider
As you read, think about:
- How does GloVe's training objective differ fundamentally from Word2Vec's prediction-based approach?
- Why do ratios of co-occurrence probabilities have the potential for encoding semantic relationships?
- What role does the weighting function play in handling different frequency ranges?
- How do the authors justify their specific choice of log-bilinear model?
- What are the computational advantages of training on co-occurrence statistics versus individual context windows?
- How does GloVe handle rare words and frequent words differently?
- What makes GloVe's approach more interpretable than Word2Vec's?

## Technical Focus Areas
Pay special attention to:
- **Mathematical Foundation**: The derivation of the training objective from co-occurrence probability ratios
- **Weighting Function**: How the f(X_ij) function balances frequent and rare co-occurrences
- **Model Architecture**: The log-bilinear structure and parameter sharing
- **Training Process**: How global co-occurrence matrices are constructed and factorized
- **Hyperparameter Sensitivity**: The impact of vector dimensions, context window size, and other parameters
- **Evaluation Methodology**: Comparison across multiple benchmarks and tasks

## Theoretical Foundations
Consider the underlying principles:
- **Global vs. Local Information**: How corpus-wide statistics complement local context information
- **Matrix Factorization**: The connection to traditional dimensionality reduction techniques
- **Probabilistic Interpretation**: How co-occurrence probabilities relate to semantic similarity
- **Optimization Theory**: The weighted least squares objective and its convergence properties
- **Information Theory**: What information is captured by different aspects of the model

## Modern Impact and Legacy
Reflect on how this 2014 paper influenced:
- **Hybrid Approaches**: Combining different types of information in representation learning
- **Pre-training Methods**: The importance of leveraging global corpus statistics
- **Evaluation Standards**: Establishing comprehensive benchmarks for word embeddings
- **Theoretical Understanding**: Providing mathematical foundations for why embeddings work
- **Practical Applications**: Widespread adoption in NLP pipelines and downstream tasks

## Critical Analysis Points
When writing your summary, consider:
- **Innovations**: The elegant combination of global and local information
- **Limitations**: Static representations, computational requirements for large vocabularies
- **Evaluation**: Strengths and potential biases in the chosen evaluation tasks
- **Theoretical Claims**: How well the mathematical theory matches empirical performance
- **Comparison Fairness**: Whether comparisons with Word2Vec and other methods are equitable

## Submission Instructions
1. Read the paper thoroughly: https://aclanthology.org/D14-1162/
2. Create a file named `[your-name].md` in the `paper-summaries/assignment-6/submissions` directory
3. Follow the format and requirements specified in the main README
4. Submit via Pull Request by September 11, 2025 @ 11:59 PM (GYD)

## Submission Template
Your markdown file should follow this structure:

```markdown
# GloVe: Global Vectors for Word Representation - Paper Summary

**Student Name**: [Your Full Name]  
**Student ID**: [Your ID]  
**Assignment**: Paper Summary 6  
**Date**: [Submission Date]  
**Word Count**: [Your word count]

## Citation
Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)* (pp. 1532-1543).

## Summary

### What is most interesting in the paper?
[Your first paragraph here - discuss the bridge between global and local methods, the mathematical elegance of the training objective, or the theoretical insights about co-occurrence ratios]

### What could the paper have done better?
[Your second paragraph here - discuss limitations in handling polysemy, potential biases in evaluation, theoretical gaps, or computational considerations]

### What questions do you have from reading the paper?
[Your third paragraph here - technical questions about the weighting function design, theoretical questions about why the approach works, or questions about extensions and improvements]
```

---

**This paper elegantly bridges two major paradigms in word representation learning and provides both theoretical insights and practical improvements that influenced the field's development toward modern embedding methods.**
