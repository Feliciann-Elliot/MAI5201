# n-gram Models Summary

**Student Name**: [Hilton Sarius]  
**Student ID**: [1006559]  
**Assignment**: Paper Summary 3
**Date**: [8/12/2025]  
**Word Count**: [289]

## Summary
This paper explores the improvement of traditional n-gram language models using word groups derived using statistical methods. Complexity is reduced and prediction accuracy improved with this approach. Words are assigned to classes based on how they appear in the text. And the authors show how the classes can be syntactic or semantic. The application of this method includes speech recognition, machine translation, and spelling check.

### What is most interesting in the paper?
I like the section that speaks about predictive text and defining how that works in n-gram models using conditional probability. I believe it’s an elegantly beautiful way to document, mathematically, the idea that we can predict the likelihood of a word being the next word based on what words came before it.

I also liked the TGIF example the author give in the section about word classes – it was a needle of humor found in a haystack of science.
The section on frequent words used in office correspondence was also interesting- It helped to put things in perspective.
Another interesting section was this:
“The class {that tha theat} is interesting because although tha and theat are not English words, the computer has discovered that in our data each of them is most often a mistyped that” (Peter F. Brown et al. 1992)
With n-gram models, the system was able to pick up on something we as humans would have taken a very long time to identify.
I liked the distinction made between sticky and semantic sticky whereby one only looks at whether they are close together vs looking at whether one comes after the other.

### What could the paper have done better?
I got lost with the mathematical notation getting integrated into the text as the paper progressed. Compared to the ELIZA paper, this one was not as easily digestible.

### What questions do you have from reading the paper?
The paper ended with the hope that we would eventually be able to improve the 3-gram language models with the help of classes described in the paper. I wonder what other work has been published that talks about actual success.

## References
(Peter F. Brown et all (1992)). Class-Based n-gram Models of Natural Language Peter F. Brown" Peter V. deSouza* Robert L. Mercer* IBM T. J. Watson Research Center