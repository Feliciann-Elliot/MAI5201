# Efficient Estimation of Word Representations in Vector Space - Paper Summary

*Student Name*: [Hilton Sarius]  
*Student ID*: [1006559]  
*Assignment*: Paper Summary 5  
*Date*: [9/8/2025]  
*Word Count*: [159]

## Citation
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.

## Summary
This paper presents the CBOW and Skip-gram, two new neural network architectures that can be used to learn complex word embeddings from huge datasets. Both models record better accuracy as well as better computational efficiency when compared to older models. The models were trained on a 1.6 billion-word corpus in less than a day and the resulting vectors were used to identify semantic and syntactic relationships between words. It was shown that these embeddings provide top notch performance on word similarity tasks and offer a scalable solution for natural language processing.

### What is most interesting in the paper?
I found the part about how applying arithmetic operations vectors resulted in words that are similar. 
“Using a word offset technique where simple algebraic operations are performed on the word vectors, it was shown for example that vector(”King”) - vector(”Man”) + vector(”Woman”) results in a vector that is closest to the vector representation of the word Queen [20].”

### What could the paper have done better?
The paper was well written and not to difficult to digest. However, I believe more work could have been done on the diagrams and tables.

### What questions do you have from reading the paper?
Are there any papers that address how these models can be used or adapted for multiple language embeddings?