# Assignment 3: Class-Based n-gram Models of Natural Language

## Paper Information
**Title**: Class-Based n-gram Models of Natural Language  
**Authors**: Peter F. Brown, Peter V. deSouza, Robert L. Mercer, Vincent J. Della Pietra, Jenifer C. Lai (1992)  
**URL**: https://aclanthology.org/J92-4003.pdf  
**Due Date**: August 12, 2025 @ 11:59 PM (GYD)

## Assignment Overview
This is the third paper summary assignment for MAI 5201. You will read the seminal 1992 paper by Brown et al. that introduced class-based n-gram language models, building directly on the n-gram concepts covered in Week 3 of our course. This paper addresses fundamental challenges in statistical language modeling and introduces concepts that remain relevant in modern NLP.

## Historical Context and Significance
This paper tackled one of the core problems in statistical language modeling: data sparsity in n-gram models. Traditional word-based n-gram models suffer from the curse of dimensionality - as vocabulary size grows, the number of possible n-grams grows exponentially, making many sequences unseen in training data. Brown et al. proposed using word classes to create more robust and generalizable language models.

The work was conducted at IBM's T.J. Watson Research Center as part of their influential statistical machine translation project. This paper laid important groundwork for later developments in clustering-based approaches, word representations, and semantic similarity measures that are fundamental to modern NLP systems.

## Key Technical Contributions
- **Class-Based Language Modeling**: Using word classes instead of individual words to build n-gram models
- **Automatic Word Clustering**: Statistical methods for automatically discovering word classes
- **Perplexity Reduction**: Demonstrating improved language model performance through class-based smoothing
- **Mathematical Framework**: Formal treatment of class-based probability estimation
- **Evaluation Methodology**: Rigorous experimental design for comparing language models

## Connection to Course Content
This paper directly extends the n-gram language models covered in Week 3:
- **N-gram Foundation**: Builds upon basic n-gram probability estimation
- **Sparsity Solutions**: Addresses the data sparsity problem inherent in word-based n-grams
- **Smoothing Techniques**: Introduces class-based smoothing as an alternative to traditional methods
- **Bridge to Modern Concepts**: Foreshadows clustering and embedding approaches in contemporary NLP

## Submission Instructions
1. Read the paper thoroughly: https://aclanthology.org/J92-4003.pdf
2. Create a file named `[your-name].md` in the `paper-summaries/assignment-3/submissions` directory
3. Follow the format and requirements specified in the main README
4. Submit via Pull Request by August 12, 2025 @ 11:59 PM (GYD)

## Key Questions to Consider
As you read, think about:
- How do class-based models address the sparsity problem in traditional n-gram models?
- What are the advantages and disadvantages of automatic vs. manual word classification?
- How does the mathematical formulation of class-based probabilities work?
- What clustering algorithms do the authors use, and why are they effective?
- How do the experimental results demonstrate the effectiveness of class-based models?
- What are the computational trade-offs between word-based and class-based models?
- How does this approach relate to modern word embedding and clustering techniques?

## Technical Focus Areas
Pay special attention to:
- **Probability Formulation**: How P(word|class) and P(class|history) are estimated
- **Clustering Methodology**: The iterative algorithm for automatic word classification
- **Evaluation Metrics**: Perplexity comparisons and statistical significance testing
- **Model Interpolation**: Combining class-based and word-based models
- **Computational Complexity**: Time and space considerations for different approaches

## Modern Relevance
Consider how this 1992 paper influenced:
- Word embedding techniques (Word2Vec, GloVe)
- Hierarchical softmax in neural language models
- Clustering-based approaches in modern NLP
- The concept of semantic word classes in contemporary systems
- Statistical foundations underlying current language modeling approaches

## Submission Template
Your markdown file should follow this structure:

```markdown
# Class-Based n-gram Models of Natural Language - Paper Summary

**Student Name**: [Your Full Name]  
**Student ID**: [Your ID]  
**Assignment**: Paper Summary 3  
**Date**: [Submission Date]  
**Word Count**: [Your word count]

## Citation
Brown, P. F., deSouza, P. V., Mercer, R. L., Della Pietra, V. J., & Lai, J. C. (1992). Class-based n-gram models of natural language. *Computational Linguistics*, 18(4), 467-479.

## Summary

### What is most interesting in the paper?
[Your first paragraph here - discuss the class-based approach, automatic clustering innovation, mathematical elegance, connection to modern techniques]

### What could the paper have done better?
[Your second paragraph here - discuss limitations in clustering methods, evaluation scope, computational analysis, or theoretical treatment]

### What questions do you have from reading the paper?
[Your third paragraph here - technical questions about clustering algorithms, theoretical questions about probability estimation, connections to modern approaches]
```

---

**This paper provides crucial foundation for understanding how statistical language modeling evolved beyond simple n-grams. The concepts introduced here - word classes, automatic clustering, and probabilistic frameworks - remain fundamental to modern NLP systems.**
