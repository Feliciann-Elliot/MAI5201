# GloVe: Global Vectors for Word Representation

**Student Name**: Daryl Nelson  
**Student ID**: 1021215
**Assignment**: Paper Summary 6  
**Date**: 9/11/2025  
**Word Count**: 289

## Citation
effrey Pennington, Richard Socher, and Christopher Manning. 2014.

## Summary

### What is most interesting in the paper?
In this paper on GloVe, I find the most interesting aspect is the approach the researchers took when considering ratios of probabilities of co-occurrence words. These ratios can emphasize meaningful differences between words, not just their general frequencies, which more accurately represent meaning. Mathematically, it explains why linear relationships between texture encode semantic analysis, which was left unexplained in the previous paper review on word2vec. The researchers combined the count and prediction approaches, showing that they both use the same underlying co-occurrence information, and they clearly demonstrate the logic behind stating if a word co-occurs much more with, say, word X than word Y, that ratio is large; if less, the ratio is small, and it helps to distinguish word X from Y relative to the initial word
### What could the paper have done better?
While this paper can give significant breakthroughs in the reasoning and meaning differences of words, it is still limited in capturing words with multiple meanings. Its evaluation largely relies on intrinsic tasks like analogies and similarity, which may not fully reflect downstream NLP performance. Despite the detailed explanation of formulas and mathematical training, data methodologies, I found it difficult to grasp certain concepts and the exact reasoning as to why certain design decisions were made. An example of this is the selection of the weighting function and its fractional power.

### What questions do you have from reading the paper?
Some questions that came about from the reading are: How critical is the selection of the weighting function for GloVe, and how significant are the performance differences to the choice? How can GloVe adapt for contextual embeddings? Can it handle polysemy effectively without losing efficiency? Despite being able to explain the meaningful differences between words, why do log co-occurrence ratios produce such robust semantic dimensions, and could this be formalized mathematically?
