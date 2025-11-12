# Efficient Estimation of Word Representations in Vector Space - Paper Summary

**Student Name**: Daryl Nelson  
**Student ID**: 1021215  
**Assignment**: Paper Summary 5  
**Date**: 04/09/2025  
**Word Count**: 268

## Citation
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*.

## Summary

### What is most interesting in the paper?
The area in this paper, what I find most interesting is the performance of the simple Skip-gram paired with RNNLMs model versus RNNLMs, Log-bilinear model and Average LSA similarity when creating embeddings. This demonstrates that more sophisticated techniques do not always result in better performance. It also highlights the intuition required by AI researchers and practitioners when selecting and developing techniques and methodologies to solve or implement solutions as I believe the combination of Skip-gram with RNNLMs was the most critical finding in this paper.  I also appreciated that during the testing of these models the accuracy, time and resource constraints were the main requirements were the main factors when selecting the methodology making the findings realistic and usable in generating word vectors.
### What could the paper have done better?
I believe the authors could have explored more deeply the meaning behind the vector mathematical tests and why these results emerge from the embeddings. I find it remarkable that one can derive related words through these calculations. However, a deeper explanation of why this occurs, along with an evaluation of other embeddings through similar mathematical testing, would have been valuable. I also think the paper could have gone further in examining how these embeddings capture words in a contextual sense. For example, do these embeddings account for situations where words carry different meanings depending on context?### What questions do you have from reading the paper?
### What questions do you have from reading the paper?
I would like to understand how and why vector math works. Is there a simple, explainable, and logical reason behind it? Additionally, I am curious whether other combinations of Skip-gram with different models might outperform the combination explored in this paper.