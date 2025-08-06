## Feliciann Elliot, 1022055
### MAI5201 - Natural Language Processing
### Assignment #2
### University of Guyana
---

## Paper Summary

## Neural Machine Translation of Rare Words with Subword Units


### What is most interesting in the paper?
The paper by Sennrich, Haddow, and Birch (2016) addresses a critical challenge in neural machine translation (NMT) that translates rare and out-of-vocabulary (OOV) words. The authors propose using Byte Pair Encoding (BPE) which is a technique that break words into smaller, reusable units. This technique is particularly useful because it enables productive translation whereby the system can translate compound words like German "Abwasserbehandlungsanlage" by understanding its components. This enables cross-alphabet transliteration for names like "Barack Obama" into Russian Cyrillic.

### What could the paper have done better?
While innovative, the paper has limitations. The experimental scope appears limited since it focuses primarily on European language pairs (English-German and English-Russian) without exploring how BPE performs across diverse languages. The authors also note that their vocabulary size selection is arbitrary, which presents an opportunity for an adaptive approach (pp. 6–7). Despite this gap, the paper’s contribution shows that subword units simplify OOV translation has had a lasting impact that influence modern tokenization strategies in models like GPT and LLaMA (pp. 8–9).

### What questions do you have from reading the paper?
Given that this 2016 work became the foundation for modern language model tokenization, I'm curious how the original BPE design choices have evolved. What modifications are necessary to handle code tokenization in models like Code Llama. While the authors chose BPE merge operations somewhat arbitrarily, how do companies like OpenAI or Meta now determine vocabulary sizes for models serving millions of users across Large Language Model tasks?

## References
Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 1715–1725. Berlin, Germany: Association for Computational Linguistics. https://doi.org/10.18653/v1/P16-1162
