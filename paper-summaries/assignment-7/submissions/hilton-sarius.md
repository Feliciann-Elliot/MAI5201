# Long Short-Term Memory - Paper Summary

**Student Name**: [Hilton Sarius]  
**Student ID**: [1006559]  
**Assignment**: Paper Summary 7  
**Date**: [10/27/2025]  
**Word Count**: [181]

## Citation
Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735-1780.

## Summary
This paper introduces Long Short-Term Memory (LSTM) AI model to tackle the issue of vanishing and exploding gradient problems that arise when training RNNs. LSTM models use a cell that consists of 3 gates (input, output, and forget). These gates have a value ranging from 0 to 1. With 1 meaning it accepts all of the records and 0 means it accepts none. The architecture facilitates dependencies with lags over 1000 steps. Comparing this to regular RNNs, it is superior with tasks that have lots of noise and long-range temporal data. With the use of Theoretical analysis as well as empirical results, its architectural innovations demonstrate superiority over earlier recurrent models

### What is most interesting in the paper?
Its interesting how the use of the cell that contains the 3 gates resolves the gradient problem. And this elegant solution in essence laid the foundation for modern sequence modeling

### What could the paper have done better?
More measurements and real world data-sets could have been used to validate its generalizability

### What questions do you have from reading the paper?
Why were the specific gating mechanisms—input, output, and forget gates—chosen over alternative designs, and how might different configurations affect memory retention and gradient flow?
