# Research Paper Presentations - MAI 5201

This directory contains the framework for student research paper presentations. Each student will select and present one research paper from the approved paper bank, delivering a comprehensive 30-minute presentation that demonstrates deep understanding of the paper's contributions, methodology, and significance to the field of NLP.

## Assignment Overview

Research paper presentations are a critical component of MAI 5201, designed to:
- Develop expertise in a specific area of NLP research
- Practice professional presentation skills
- Foster critical analysis and evaluation abilities
- Encourage peer learning and academic discourse
- Build confidence in explaining complex technical concepts

Each student will select one paper from the approved paper bank, conduct thorough analysis, and deliver a professional-quality presentation to the class.

## Presentation Schedule

| Week | Date Range | Focus Area | Number of Presentations |
|------|------------|------------|------------------------|
| **Week 9** | Sep 9-11, 2025 | Transformers & Attention | 1 presentation |
| **Week 11** | Sep 23-25, 2025 | Pre-trained Language Models | 1 presentation |
| **Week 13** | Oct 7-9, 2025 | Advanced Techniques & Scaling | 1 presentation |

## Paper Selection Process

### Step 1: Paper Selection Deadline
**Due: August 28, 2025 @ 11:59 PM (GYD)**

1. Review the [Paper Bank](#approved-paper-bank) below
2. Select your **first choice** and **second choice** papers
3. Create a file named `[your-name]-selection.md` in the `paper-selections/` directory
4. Submit via Pull Request following the template provided

### Step 2: Assignment Confirmation
- Instructor will assign papers based on preferences and balance across weeks
- Students will be notified of their assigned paper by August 30, 2025
- No two students will present the same paper

## Approved Paper Bank

### Foundational Word Representations
1. **GloVe: Global Vectors for Word Representation** (Pennington et al., 2014)
   - **URL**: https://aclanthology.org/D14-1162.pdf
   - **Focus**: Global matrix factorization approach to word embeddings
   - **Key Topics**: Distributional semantics, word analogies, embedding evaluation

### Neural Architecture Foundations
2. **Long Short-Term Memory** (Hochreiter & Schmidhuber, 1997)
   - **URL**: https://deeplearning.cs.cmu.edu/S23/document/readings/LSTM.pdf
   - **Focus**: LSTM architecture for sequence modeling
   - **Key Topics**: Vanishing gradients, gating mechanisms, sequence memory

3. **Deep Contextualized Word Representations (ELMo)** (Peters et al., 2018)
   - **URL**: https://arxiv.org/abs/1802.05365
   - **Focus**: Context-dependent word embeddings using bidirectional LSTMs
   - **Key Topics**: Contextualized embeddings, transfer learning, polysemy

### Transformer Revolution
4. **Attention is All You Need** (Vaswani et al., 2017)
   - **URL**: https://arxiv.org/abs/1706.03762
   - **Focus**: Transformer architecture and self-attention mechanisms
   - **Key Topics**: Attention mechanisms, parallelization, sequence-to-sequence learning

5. **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** (Devlin et al., 2019)
   - **URL**: https://arxiv.org/pdf/1810.04805
   - **Focus**: Bidirectional encoder representations for language understanding
   - **Key Topics**: Masked language modeling, pre-training/fine-tuning paradigm

### Large Language Models Era
6. **Language Models are Few-Shot Learners** (Brown et al., 2020)
   - **URL**: https://arxiv.org/abs/2005.14165
   - **Focus**: GPT-3 and emergent abilities of large-scale language models
   - **Key Topics**: In-context learning, scaling effects, few-shot performance

7. **Scaling Laws for Neural Language Models** (Kaplan et al., 2020)
   - **URL**: https://arxiv.org/abs/2001.08361
   - **Focus**: Mathematical relationships between model size, data, and performance
   - **Key Topics**: Power law scaling, compute-optimal training, model architecture choices

### Advanced Training & Alignment
8. **Training Language Models to Follow Instructions with Human Feedback** (Ouyang et al., 2022)
   - **URL**: https://arxiv.org/abs/2203.02155
   - **Focus**: InstructGPT and reinforcement learning from human feedback (RLHF)
   - **Key Topics**: Human preference learning, instruction following, AI alignment

9. **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer** (Raffel et al., 2020)
   - **URL**: https://arxiv.org/pdf/1910.10683
   - **Focus**: T5 model and text-to-text unified framework
   - **Key Topics**: Transfer learning, multi-task learning, text generation

## Presentation Requirements

### Format & Duration
- **Length**: 30 minutes total (25 minutes presentation + 5 minutes Q&A)
- **Format**: Live presentation via Zoom
- **Materials**: PDF slides required for submission

### Content Requirements
Your presentation must address:

#### 1. Introduction & Motivation (5-7 minutes)
- Research problem and motivation
- Historical context and related work
- Paper's significance in NLP development

#### 2. Technical Content (15-18 minutes)
- **Methodology**: Detailed explanation of the approach
- **Architecture/Algorithm**: Key technical innovations
- **Experimental Setup**: Datasets, baselines, evaluation metrics
- **Results**: Main findings and their interpretation

#### 3. Critical Analysis (5-7 minutes)
- **Strengths**: What the paper does well
- **Limitations**: Methodological or conceptual weaknesses
- **Impact**: Influence on subsequent research and applications
- **Future Directions**: Potential improvements or extensions

#### 4. Discussion & Q&A (5 minutes)
- Field questions from instructor and peers
- Demonstrate deep understanding through responses

### Technical Depth Expectations
- Explain mathematical formulations clearly
- Provide intuitive explanations for complex concepts
- Include relevant diagrams, examples, and visualizations
- Connect to concepts covered in class
- Discuss computational complexity and efficiency considerations

## Submission Requirements

### Step 1: Paper Selection (Due: August 28, 2025)
Submit paper selection via Pull Request:

**File**: `paper-selections/[your-name]-selection.md`

```markdown
# Research Paper Presentation Selection

**Student Name**: [Your Full Name]
**Student ID**: [Your ID]
**Date**: [Submission Date]

## Paper Selections

### First Choice
**Title**: [Paper Title]
**Authors**: [Authors]
**Year**: [Year]
**Reason for Selection**: [2-3 sentences explaining your interest in this paper]

### Second Choice
**Title**: [Paper Title]
**Authors**: [Authors]
**Year**: [Year]
**Reason for Selection**: [2-3 sentences explaining your interest in this paper]

## Presentation Preferences
**Preferred Week(s)**: [Week 9, 11, and/or 13]
**Conflicts/Constraints**: [Any scheduling conflicts]
```

### Step 2: Slide Submission (Due: 24 hours before presentation)
Submit presentation slides via Pull Request:

**File**: `submissions/[your-name]-[paper-short-name]-slides.pdf`

**Pull Request Requirements**:
- **Title**: `Research Paper Presentation: [Paper Title] - [Your Name]`
- **Description**: Brief summary of your main insights and key points
- **File Format**: PDF only (PowerPoint, Keynote, or LaTeX Beamer)
- **File Size**: Maximum 50MB

## Assessment Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Content Knowledge** | 40% | Understanding of paper's technical content, methodology, and contributions |
| **Presentation Skills** | 25% | Clarity, organization, timing, visual aids, engagement |
| **Critical Analysis** | 20% | Evaluation of strengths, limitations, and broader impact |
| **Technical Communication** | 10% | Ability to explain complex concepts clearly |
| **Q&A Response** | 5% | Quality of responses to questions and discussion participation |

### Evaluation Rubric

#### Excellent (A: 90-100%)
- Demonstrates comprehensive understanding of all technical details
- Presentation is engaging, well-structured, and professionally delivered
- Provides insightful critical analysis and connects to broader NLP context
- Handles all questions confidently with detailed, accurate responses

#### Proficient (B: 80-89%)
- Shows solid understanding of main concepts with minor gaps
- Presentation is clear and organized with good visual support
- Provides reasonable critical analysis with some insights
- Handles most questions well with generally accurate responses

#### Developing (C: 70-79%)
- Demonstrates basic understanding but misses some important details
- Presentation lacks polish or has organizational issues
- Limited critical analysis or superficial treatment of limitations
- Struggles with some questions or provides incomplete answers

#### Inadequate (F: <70%)
- Significant gaps in understanding of key concepts
- Poor presentation delivery or organization
- Lacks meaningful critical analysis
- Unable to handle basic questions about the paper

## Git Workflow for Submissions

### Paper Selection Submission
```bash
# 1. Create branch for paper selection
git checkout -b paper-selection-[your-name]

# 2. Create your selection file
# Edit: paper-selections/[your-name]-selection.md

# 3. Commit and push
git add paper-selections/[your-name]-selection.md
git commit -m "Add paper selection - [Your Name]"
git push origin paper-selection-[your-name]

# 4. Create Pull Request on GitHub
```

### Presentation Slides Submission
```bash
# 1. Create branch for presentation slides
git checkout -b presentation-[paper-short-name]-[your-name]

# 2. Add your PDF slides
git add submissions/[your-name]-[paper-short-name]-slides.pdf
git commit -m "Add [Paper Title] presentation slides - [Your Name]"
git push origin presentation-[paper-short-name]-[your-name]

# 3. Create Pull Request on GitHub
```

## Presentation Tips & Best Practices

### Content Organization
- Start with a compelling motivation - why should the audience care?
- Use the "inverted triangle" structure: broad context → specific contributions → detailed methods
- Include concrete examples and intuitive explanations
- Allocate time proportionally to the paper's emphasis

### Visual Design
- Use consistent formatting and professional templates
- Include clear diagrams and illustrations
- Avoid text-heavy slides - use bullet points and visuals
- Ensure readability in online presentation format

### Technical Communication
- Define all technical terms and notation
- Build complexity gradually - don't jump to advanced concepts
- Use analogies and examples to explain difficult concepts
- Practice explaining the paper to someone outside the field

### Engagement Strategies
- Ask rhetorical questions to maintain audience attention
- Use interactive elements when appropriate
- Prepare for common questions in advance
- Connect the paper to current events or applications

## Timeline Summary

| Date | Deliverable | Action Required |
|------|-------------|-----------------|
| **Aug 28, 2025** | Paper Selection | Submit selection via PR |
| **Aug 30, 2025** | Assignment Notification | Receive assigned paper |
| **Week 9 (Sep 9-11)** | Presentations Block 1 | Present if assigned |
| **Week 11 (Sep 23-25)** | Presentations Block 2 | Present if assigned |
| **Week 13 (Oct 7-9)** | Presentations Block 3 | Present if assigned |

---

*This assignment is designed to deepen your expertise in a specific area of NLP research while developing professional presentation skills that will serve you throughout your career in AI and technology.*
