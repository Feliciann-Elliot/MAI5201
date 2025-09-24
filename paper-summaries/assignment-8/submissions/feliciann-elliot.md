**Student Name**: Feliciann Elliot
**Student ID**: 1022055
**Assignment**: Paper Summary 8  
**Date**: September 23, 2025
**Word Count**: 244

## Citation
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... & Amodei, D. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33, 1877-1901.

## Summary

### What is most interesting in the paper?
The most compelling aspect of this paper is its demonstration that scaling up language models can unlock powerful few-shot learning capabilities, moving away from the need for task-specific fine-tuning. GPT-3, with 175 billion parameters, is shown to perform diverse tasks such as translation, question answering, and arithmetic without gradient updates, using only a handful of examples provided in context. This “in-context learning” becomes markedly stronger as model size increases, and the authors argue that it more closely mirrors human learning, where brief instructions or limited demonstrations often suffice. The work highlights a shift toward more general and adaptable AI systems that are not constrained by the constant demand for large labeled datasets.

### What could the paper have done better?
While groundbreaking, the paper could have provided a more balanced treatment of its limitations. Its discussion of broader societal impacts is relatively brief, touching mainly on misuse, bias, and energy costs. A deeper exploration of issues such as harmful bias in outputs related to gender, race, or religion would have strengthened the analysis.

### What questions do you have from reading the paper?
Reading this paper raises several important questions for future research. On a technical level, the precise mechanism behind in-context learning remains ambiguous. Does the model genuinely learn new skills "from scratch" at inference time, or does it merely recognize tasks it has implicitly seen during pre-training? Additionally, the ethical implications of deploying such powerful models warrant further exploration. How can we ensure that these models are used responsibly, and what frameworks should be in place to mitigate potential harms?
