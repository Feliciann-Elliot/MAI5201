# BPE Paper Summary

**Student Name**: [Hilton Sarius]  
**Student ID**: [1006559]  
**Assignment**: Paper Summary 2
**Date**: [8/8/2025]  
**Word Count**: [213]

## Summary
This paper speaks about a neural machine translation (NMT) method that more efficiently handles rare and out-of-vocabulary words. The method encodes sequences of sub-words using the byte pair encoding (BPE) technique. BPE enables systems to handle words or phrases that are not found in the training data and improves (Englis to German and English to Russian) translations, with BLEU score gains a much as 1.3. “… the subword ensembles outperform the WDict baseline by 0.3–1.3 BLEU and 0.6–2 CHRF3”  (Rico Sennrich and Barry Haddow and Alexandra Birch (2016)). The method demonstrates robustness and generalization as it handles not just names but also compounds and other complex words.

### What is most interesting in the paper?
I found the section that describes the process of data compression using BPE most interesting. It is an elegant solution to the problem of storage issues.

### What could the paper have done better?
I believe the comparisons with the different methods could have been more powerful if they had used a graph or even conditional formatting in the table. I do not believe readers will immediately be able to see that BPE is better. Overall the analysis that followed was good. But they could have made a better opening visual to clearly show that BPE is better before diving into the details

### What questions do you have from reading the paper?
How would this BPE model scale across different languages?

## References
Rico Sennrich and Barry Haddow and Alexandra Birch (2016). Neural Machine Translation of Rare Words with Subword Units Rico Sennrich and Barry Haddow and Alexandra Birch School of Informatics, University of Edinburgh {rico.sennrich,a.birch}@ed.ac.uk, bhaddow@inf.ed.ac.uk