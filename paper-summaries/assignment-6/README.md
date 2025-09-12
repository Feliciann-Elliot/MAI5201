# Paper Summary Assignment 6: GloVe Word Representations

## Assignment Details

**Paper**: "GloVe: Global Vectors for Word Representation"  
**Authors**: Jeffrey Pennington, Richard Socher, Christopher D. Manning  
**Venue**: Empirical Methods in Natural Language Processing (EMNLP) 2014  
**URL**: https://aclanthology.org/D14-1162/  
**Due Date**: September 11, 2025 @ 11:59 PM (GYD)  

## Paper Overview

This seminal paper introduces Global Vectors (GloVe), a new approach for learning word representations that combines the advantages of global matrix factorization and local context window methods. The work bridges the gap between count-based methods (like LSA) and predictive methods (like word2vec), proposing a model that trains on aggregated global word-word co-occurrence statistics from a corpus.

## Key Contributions

1. **Novel Training Objective**: Introduces a weighted least squares objective that directly incorporates global co-occurrence statistics
2. **Theoretical Foundation**: Provides mathematical justification for the relationship between word meanings and co-occurrence probabilities
3. **Empirical Performance**: Demonstrates superior performance on word analogy, word similarity, and named entity recognition tasks
4. **Computational Efficiency**: Shows faster training compared to word2vec while achieving better performance

## Focus Areas for Your Summary

When writing your summary, consider addressing:

### Technical Innovation
- How does GloVe's training objective differ from word2vec and traditional count-based methods?
- What is the significance of the log-bilinear model and the weighting function?
- How do the authors handle rare word pairs and frequent co-occurrences?

### Experimental Analysis
- What evaluation tasks do the authors use to validate their approach?
- How does performance compare across different vector dimensions and training corpus sizes?
- What insights emerge from the word analogy tasks and qualitative analysis?

### Methodological Considerations
- What are the computational trade-offs between GloVe, word2vec, and traditional methods?
- How sensitive is the model to hyperparameter choices?
- What limitations or potential improvements do you identify?

## Submission Instructions

1. Create a file named `[your-name].md` in the `submissions/` directory
2. Follow the standard paper summary format (see main README)
3. Include proper APA citation for the paper
4. Target length: 200-300 words across three paragraphs

## Discussion Questions

Consider these questions as you read:
- How does GloVe's use of global statistics change our understanding of word representation learning?
- What are the implications of the authors' claim that "ratios of co-occurrence probabilities have the potential for encoding meaning"?
- How might GloVe's approach influence subsequent developments in word embeddings and language models?

---

For questions about this assignment, please contact Dr. Clarke or create an issue in the course repository.
