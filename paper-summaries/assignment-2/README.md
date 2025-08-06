# Assignment 2: Neural Machine Translation with Subword Units

## Paper Information
**Title**: Neural Machine Translation of Rare Words with Subword Units  
**Authors**: Rico Sennrich, Barry Haddow, Alexandra Birch (2016)  
**URL**: https://aclanthology.org/P16-1162.pdf  
**Due Date**: August 6, 2025 @ 11:59 PM (GYD)

## Assignment Overview
This is the second paper summary assignment for MAI 5201. You will read the influential 2016 paper by Sennrich et al. that introduced Byte Pair Encoding (BPE) to neural machine translation and analyze its foundational impact on modern NLP systems.

## Historical Context and Significance
This paper introduced Byte Pair Encoding (BPE) as a solution to the out-of-vocabulary (OOV) problem in neural machine translation. The approach allows models to handle rare and unseen words by breaking them down into smaller subword units. Today, BPE and its variants serve as the foundation for tokenization in virtually all modern large language models, including GPT, LLaMA, Mistral, and others.

The paper addressed a critical limitation of early neural translation systems: their inability to effectively handle words not seen during training. By introducing subword tokenization, the authors enabled models to compositionally understand new words and significantly improved translation quality, especially for morphologically rich languages.

## Key Technical Contributions
- **Subword Tokenization**: Adaptation of BPE compression algorithm for NLP applications
- **OOV Problem Solution**: Method to handle rare and unseen words in neural translation
- **Language Agnostic Approach**: Technique that works across different language families
- **Foundation for Modern Tokenization**: Algorithmic basis for current LLM tokenizers

## Submission Instructions
1. Read the paper thoroughly: https://aclanthology.org/P16-1162.pdf
2. Create a file named `[your-name].md` in the `paper-summaries/assignment-2/submissions` directory
3. Follow the format and requirements specified in the main README
4. Submit via Pull Request by August 6, 2025 @ 11:59 PM (GYD)

## Key Questions to Consider
As you read, think about:
- How does BPE solve the out-of-vocabulary problem in neural translation?
- What are the trade-offs between character-level, word-level, and subword-level tokenization?
- How has this approach influenced modern LLM tokenization strategies?
- What are the computational and linguistic advantages of subword units?
- How do the experimental results demonstrate the effectiveness of BPE?
- What limitations or potential issues does the BPE approach introduce?

## Modern Relevance
Consider how this 2016 paper laid the groundwork for:
- GPT series tokenizers (GPT-2, GPT-3, GPT-4)
- LLaMA and Code Llama tokenization
- Mistral and other modern language models
- Cross-lingual applications and multilingual models
- The current standard in production NLP systems

## Submission Template
Your markdown file should follow this structure:

```markdown
# Neural Machine Translation with Subword Units - Paper Summary

**Student Name**: [Your Full Name]  
**Student ID**: [Your ID]  
**Assignment**: Paper Summary 2  
**Date**: [Submission Date]  
**Word Count**: [Your word count]

## Citation
Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 1715-1725.

## Summary

### What is most interesting in the paper?
[Your first paragraph here - discuss BPE innovation, technical significance, impact on NLP field]

### What could the paper have done better?
[Your second paragraph here - discuss limitations, experimental design, clarity issues]

### What questions do you have from reading the paper?
[Your third paragraph here - technical implementation questions, theoretical considerations, modern applications]
```

---

**This paper represents a foundational moment in NLP history - understanding BPE is crucial for working with any modern language model. Take time to understand both the technical approach and its broader implications for the field.**
