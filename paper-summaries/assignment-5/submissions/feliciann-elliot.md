# Efficient Estimation of Word Representations in Vector Space - Paper Summary

**Student Name**: Feliciann Elliot
**Student ID**: 1022055
**Assignment**: Paper Summary 5  
**Date**: September 3, 2025  
**Word Count**: 217

## Citation
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*.

## Summary

### What is most interesting in the paper?
The paper presents a breakthrough in an interesting and efficient approach for learning high-quality word representations (p1-p2). The authors introduce two simplified models which are the Continuous Bag-of-Words (CBOW) and Continuous Skip-gram, which removes the costly non-linear hidden layers used in earlier neural network models (p3-p4). This research demonstrated the possibility to train accurate word vectors on billions of words in under a day (p6). A notable highlight is that these models capture relationships through simple vector math such as solving analogies: King - Man + Woman = Queen (p5).

### What could the paper have done better?
Each word is given only one vector which presents a challenge of handling multiple meanings for one word (p2). The evaluation mainly relies on a custom analogy test set (Table 1, p6), which measures linear relationships well but does not fully reflect performance on other Natural Language Processing activities. Some additional theoretical writing or a context-wise demonstration may have improved the presentation of the research.

### What questions do you have from reading the paper?
Why did the authors choose to look at 4 words before and after a target word in Continuous Bag-of-Words (CBOW)? The researcher is curious to know if other numbers may be suitable or even work better. Additionally, how does the operation of adding and subtracting word vectors such as (king - man + woman = queen) makes sense to the computer system?