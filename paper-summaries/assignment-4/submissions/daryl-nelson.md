**Student Name**: Daryl Nelson  
**Student ID**: 1021215  
**Assignment**: Paper Summary 4  
**Date**: 28/08/2025  
**Word Count**: 204 

## Citation
Pang, B., Lee, L., & Vaithyanathan, S. (2002). Thumbs up? Sentiment classification using machine learning techniques. *Proceedings of the ACL-02 Conference on Empirical Methods in Natural Language Processing*, 79-86.

## Summary

### What is most interesting in the paper?
What I find most interesting about this paper is the authors treating sentiment analysis as a machine learning problem, when trying to distinguishing between positive and negative sentiment. I like how the authors experimented with Naive Bayes, Maximum Entropy, etc and found the best results coming from unigrams combined with SVMs. The design of the study was carefully controlled balancing reviewer bias and ensuring robust experimental conditions. This approach and methodology set the standard for future work in sentiment analysis.

### What could the paper have done better?
I believe some limitations in this paper included the dataset being relatively small, with only 2,000 IMDB reviews. There were also only two labels positive or negative. Since the method also uses the bag of words features there are still more laguage concepts to take into consideration like sentence structure, sarcasm, or the subtle contrasts in tone that can change sentiment. Even when the authors experiment with bigrams and tagging negations, they find only minor improvements, which suggests the need for more advanced models. 

### What questions do you have from reading the paper?
This raises several important questions for future research. Could adding features like parts of speech or sentence structure improve sentiment predictions? How adaptable are these methods when applied to other types of text in other domains and with more labels?