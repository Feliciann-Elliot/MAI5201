# Sentiment Classification using Machine Learning - Paper Summary

**Student Name**: Feliciann Elliot  
**Student ID**: 1022055  
**Assignment**: Paper Summary 4  
**Date**: August 28, 2025  
**Word Count**: 312

## Citation
Pang, B., Lee, L., & Vaithyanathan, S. (2002). Thumbs up? Sentiment classification using machine learning techniques. *Proceedings of the ACL-02 Conference on Empirical Methods in Natural Language Processing*, 79-86.

## Summary

### What is most interesting in the paper?
The paper takes on the task of sentiment classification, showing how it is different from regular topic categorization since it looks at the overall opinion (positive or negative) instead of just the subject matter (pp. 1–2). Using IMDb movie reviews, the authors tested standard machine learning methods, Naive Bayes, Maximum Entropy, and Support Vector Machines (SVM) and found that all of them did better than human-picked word lists, which only reached about 58–69% accuracy (pp. 3–4). The study also points out tricky cases like “thwarted expectations,” where a review has lots of positive or negative words but the overall opinion goes the other way, showing the need for analysis that looks at the bigger context (pp. 7–8).

### What could the paper have done better?
The dataset used in the study was only 1,400 reviews, and because Maximum Entropy training was slow, the authors had to limit testing to just three-fold cross-validation (p. 4). Since the experiments focused only on movie reviews, it is not clear how well the results would apply to other domains, especially given that earlier work found movie reviews to be one of the hardest cases (p. 3). The extra features they tried—like negation tagging, bigrams, part-of-speech tags, and word position did not really improve performance much (pp. 6–7). Finally, they chose not to include frequency features in MaxEnt, which made sense for efficiency, but also meant they didn’t explore some other possible approaches (p. 7).

### What questions do you have from reading the paper?
Would the advantage of feature presence generalize to other domains such as product reviews, social media, or political texts? The paper also made the researcher think about how sentiment classification is not the same as topic classification, and why that difference really matters. Since this study was done back in 2002, the researcher would ask, "How well would modern models like transformers, which handle context so much better, perform on the same dataset today"?