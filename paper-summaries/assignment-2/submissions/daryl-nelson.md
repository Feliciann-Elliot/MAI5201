# Neural Machine Translation with Subword Units - Paper Summary

**Student Name**: Daryl Nelson 
**Student ID**: 1021215  
**Assignment**: Paper Summary 2  
**Date**: 06/08/25
**Word Count**: 230

## Citation
Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 1715-1725.

## Summary

### What is most interesting in the paper?

In this paper, I found the strategy of Byte Pair Encoding the most interesting. This involves breaking rare words into smaller subword units, allowing the model to represent any word. I found this to be quite genius, given that it enabled the NMT model to work with a limited vocabulary while still being able to represent unknown words using these smaller subword units. External research shows this was so significant that it became a standard preprocessing step in models like BERT and GPT

### What could the paper have done better?
This paper clearly shows the improvements of BPE over traditional NMT models. However, I believe it lacks a wider, experiment-based evaluation covering more languages, as well as an analysis of potential gains or losses in performance under different linguistic dynamics. The breakdown of sections was relatively easy to understand, moving through BPE, vocabulary building, preprocessing, NMT architecture, and then the training and evaluation stages.
I thought the paper could have provided more clarity on some implementation details, particularly the algorithm's integration into the training pipeline, and how it affects training. Some methodological choices, such as the comparison baselines and tokenization strategies, could also have been better justified or explained.

### What questions do you have from reading the paper?
In this paper, the focus was on Russian and German, which are described as morphologically rich languages. So a question I had was: Does this approach also work well for languages like Mandarin, which are less morphologically rich?

