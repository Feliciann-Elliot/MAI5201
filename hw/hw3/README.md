# MAI 5201 Homework 3: Hands-On with Large Language Models

## Table of Contents
- [Introduction](#introduction)
- [Course Overview](#course-overview)
- [Chapter Requirements](#chapter-requirements)
- [Setup Instructions](#setup-instructions)
- [Submission Requirements](#submission-requirements)
- [Grading Rubric](#grading-rubric)
- [Getting Help](#getting-help)

## Introduction

Welcome to your last homework for MAI 5201! This assignment takes a hands-on approach to learning Large Language Models by working through the industry-standard **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter0/1?fw=pt)**. You'll gain practical experience with the same tools and techniques used by AI engineers and researchers worldwide.

**🌟 Why This Matters:**
The Hugging Face ecosystem has become the de facto standard for working with LLMs in industry and research. By completing this course, you'll:
- Master the tools used by leading AI companies and research labs
- Build hands-on experience with state-of-the-art language models
- Learn industry best practices for model fine-tuning, evaluation, and deployment
- Develop practical skills that directly translate to real-world NLP projects

**What you'll accomplish:**
- **Practical LLM Skills**: Work with pre-trained models, fine-tune them for specific tasks, and evaluate their performance
- **Industry Tools**: Master the Hugging Face ecosystem (Transformers, Datasets, Tokenizers, Hub)
- **Real-World Applications**: Implement solutions for text classification, language modeling, and other NLP tasks
- **Professional Portfolio**: Build a collection of working notebooks demonstrating LLM expertise

**Structure:**
You'll complete **8 chapters** from the Hugging Face course, documenting your learning journey with completed notebooks and result screenshots.

**Due Date**: October 28, 2025

---

## Course Overview

You will work through the **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter0/1?fw=pt)**, completing the following chapters:

### 📚 Required Chapters

| Chapter | Title | Focus Area | Key Learning Outcomes |
|---------|-------|------------|----------------------|
| **1** | [Introduction](https://huggingface.co/learn/llm-course/chapter1/1?fw=pt) | Transformers & LLMs | Understanding modern NLP, transformer architecture, LLM capabilities |
| **2** | [Using Transformers](https://huggingface.co/learn/llm-course/chapter2/1?fw=pt) | Core Library Usage | Pipelines, models, tokenizers, hands-on implementation |
| **3** | [Fine-tuning Models](https://huggingface.co/learn/llm-course/chapter3/1?fw=pt) | Model Training | Custom training loops, Trainer API, evaluation metrics |
| **4** | [Sharing Models](https://huggingface.co/learn/llm-course/chapter4/1?fw=pt) | Model Hub & Deployment | Version control for ML, model sharing, collaboration |
| **5** | [Datasets Library](https://huggingface.co/learn/llm-course/chapter5/1?fw=pt) | Data Processing | Loading, processing, and managing large-scale datasets |
| **6** | [Tokenizers Library](https://huggingface.co/learn/llm-course/chapter6/1?fw=pt) | Text Processing | Building custom tokenizers, subword algorithms |
| **7** | [Main NLP Tasks](https://huggingface.co/learn/llm-course/chapter7/1?fw=pt) | Task Implementation | Token classification, summarization, Q&A, language modeling |
| **11** | [Transfer Learning](https://huggingface.co/learn/llm-course/chapter11/1?fw=pt) | Advanced Techniques | Pre-trained model adaptation, domain transfer |

---

## Chapter Requirements

For each chapter, you must complete **ALL sections** and their associated notebooks. Here's what to expect:

### 📋 Per-Chapter Checklist

For **each of the 8 required chapters**, you need to:

✅ **Complete all section notebooks** in the chapter  
✅ **Run all code cells** successfully  
✅ **Take screenshots** of key results (see requirements below)  
✅ **Download/save your completed notebooks**  
✅ **Complete any end-of-chapter quizzes or exercises**  

### 📸 Screenshot Requirements

For each chapter, capture screenshots showing:

1. **Chapter completion** - Final section or summary showing you've finished
2. **Key results** - At least 3 screenshots per chapter of interesting outputs, model predictions, training curves, or evaluation metrics
3. **Personal notebook environment** - Show your Colab/local environment with completed notebooks

**Screenshot Naming Convention:**
```
screenshots/
├── chapter1/
│   ├── ch1_completion.png
│   ├── ch1_result1_pipeline_demo.png
│   ├── ch1_result2_model_output.png
│   └── ch1_result3_tokenizer_example.png
├── chapter2/
│   ├── ch2_completion.png
│   ├── ch2_result1_fine_tuning.png
│   └── ...
```

---

## Setup Instructions

### Option 1: Google Colab (Recommended)
1. Go to the [Hugging Face Course](https://huggingface.co/learn/llm-course/chapter0/1?fw=pt)
2. For each chapter section, click the "Google Colab" button
3. Work through notebooks directly in Colab
4. Save completed notebooks to your Google Drive
5. Download notebooks as `.ipynb` files for submission

### Option 2: Local Environment
1. Set up Python environment with required packages:
   ```bash
   pip install transformers datasets tokenizers accelerate
   pip install torch torchvision torchaudio  # or tensorflow
   pip install jupyter notebook
   ```
2. Clone or download notebook files from [huggingface/notebooks](https://github.com/huggingface/notebooks)
3. Run notebooks locally in Jupyter

---

## Submission Requirements

### 📁 Submission Structure

Submit your work via **Pull Request** to the course repository with the following structure in your submissions folder:

```
hw/
└── hw3/
    └── submissions/
        └── [your-name]/
            ├── README.md                          # Your personal reflection (see below)
            ├── notebooks/
            │   ├── chapter1/
            │   │   ├── section1.ipynb
            │   │   ├── section2.ipynb
            │   │   └── ...
            │   ├── chapter2/
            │   ├── chapter3/
            │   ├── chapter4/
            │   ├── chapter5/
            │   ├── chapter6/
            │   ├── chapter7/
            │   └── chapter11/
            └── screenshots/
                ├── chapter1/
                │   ├── ch1_completion.png
                │   ├── ch1_result1_[description].png
                │   ├── ch1_result2_[description].png
                │   └── ch1_result3_[description].png
                ├── chapter2/
                ├── chapter3/
                ├── chapter4/
                ├── chapter5/
                ├── chapter6/
                ├── chapter7/
                └── chapter11/
```

### 📝 Personal Reflection README

Include a `README.md` file in your submission root with:

```markdown
# HW3: Hugging Face Course Completion - [Your Name]

## Course Progress Summary
- **Completion Date**: [Date]
- **Total Time Spent**: [Approximate hours]
- **Chapters Completed**: 1, 2, 3, 4, 5, 6, 7, 11

## Key Learnings
Write 2-3 paragraphs about:
- Most valuable concepts you learned
- How this connects to our MAI 5201 course content
- Practical applications you can now implement

## Technical Highlights
For each chapter, write 1-2 sentences about:
- **Chapter 1**: [Your key takeaway]
- **Chapter 2**: [Your key takeaway]
- **Chapter 3**: [Your key takeaway]
- **Chapter 4**: [Your key takeaway]
- **Chapter 5**: [Your key takeaway]
- **Chapter 6**: [Your key takeaway]
- **Chapter 7**: [Your key takeaway]
- **Chapter 11**: [Your key takeaway]

## Challenges & Solutions
- What was most challenging?
- How did you overcome difficulties?
- What would you do differently?

## Future Applications
How will you apply these skills in:
- Your final course project?
- Future NLP work?
- Professional development?
```

---

## Grading Rubric

**Total Points: 100**

| Component | Points | Criteria |
|-----------|--------|----------|
| **Notebook Completion** | 60 | All notebooks complete with executed cells (7.5 pts per chapter) |
| **Screenshots & Documentation** | 20 | Clear screenshots showing results and completion (2.5 pts per chapter) |
| **Personal Reflection** | 15 | Thoughtful analysis of learning experience and connections to course |
| **Organization & Submission** | 5 | Proper file structure, naming conventions, complete submission |

### Detailed Scoring:

**Notebook Completion (60 points)**
- **Excellent (7-7.5 pts/chapter)**: All cells executed, outputs visible, modifications/experiments attempted
- **Good (5.5-6.5 pts/chapter)**: Most cells executed, minor issues with outputs
- **Satisfactory (4-5 pts/chapter)**: Basic completion, some cells not run or errors present
- **Needs Improvement (0-3.5 pts/chapter)**: Incomplete, significant errors, minimal effort

**Screenshots & Documentation (20 points)**
- **Excellent (2.5 pts/chapter)**: Clear, relevant screenshots with descriptive filenames
- **Good (2 pts/chapter)**: Screenshots present but may lack clarity or relevance
- **Satisfactory (1.5 pts/chapter)**: Minimal screenshots, basic documentation
- **Needs Improvement (0-1 pts/chapter)**: Missing or poor-quality screenshots

**Personal Reflection (15 points)**
- **Excellent (13-15 pts)**: Deep insights, clear connections to course, specific examples
- **Good (10-12 pts)**: Good reflection with some connections to course material
- **Satisfactory (7-9 pts)**: Basic reflection, minimal connections
- **Needs Improvement (0-6 pts)**: Superficial or missing reflection

---

## Getting Help

### 🤝 Resources

1. **Hugging Face Course Forums**: Each chapter has discussion sections for questions
2. **Course Discussion**: Use our class Discord/forums for peer collaboration
3. **Office Hours**: Bring specific technical questions to instructor office hours
4. **Documentation**: 
   - [Hugging Face Transformers Docs](https://huggingface.co/docs/transformers)
   - [Datasets Documentation](https://huggingface.co/docs/datasets)
   - [Tokenizers Documentation](https://huggingface.co/docs/tokenizers)

### 🚨 Technical Issues

**Common Issues & Solutions:**

- **GPU/Memory Issues in Colab**: Use smaller models or datasets, restart runtime, upgrade to Colab Pro if needed
- **Package Installation**: Follow the setup instructions in Chapter 0 of the HF course
- **Model Loading Errors**: Check your internet connection, try different model checkpoints
- **Authentication Issues**: Create a free Hugging Face account and use their tokens

### 📧 Getting Instructor Help

When asking for help, please provide:
1. Which chapter and section you're working on
2. Specific error messages (screenshots helpful)
3. What you've already tried
4. Your environment (Colab, local, etc.)

---

## Academic Integrity

### ✅ Encouraged Collaboration
- Discussing concepts and approaches with classmates
- Sharing resources and helpful links
- Asking for help debugging technical issues
- Working together to understand difficult concepts

### ❌ Not Permitted
- Copying completed notebooks from other students
- Sharing screenshots of your specific results with others
- Submitting work that is not your own
- Using AI tools to complete assignments without learning

### 🎯 Learning Goals
Remember: The goal is **your learning and skill development**. The Hugging Face course is expertly designed to build your understanding progressively. Take time to understand each concept rather than rushing through to completion.

---

## Submission Process

### Step 1: Repository Setup
1. **Fork the main course repository** (`MAI5201`)
2. **Clone your forked repository** locally
3. **Create a new branch**: `hw3-[your-name]` (e.g., `hw3-john-smith`)

### Step 2: File Organization
Create your submission folder structure:
```bash
cd hw/hw3/submissions/
mkdir [your-name]
cd [your-name]
# Create your folder structure as shown above
```

### Step 3: Complete Your Work
- Work through all required chapters (1-7, 11)
- Save completed notebooks in the appropriate folders
- Take screenshots and organize them properly
- Write your reflection README.md

### Step 4: Git Workflow
```bash
# Add your changes
git add hw/hw3/submissions/[your-name]/

# Commit with meaningful message
git commit -m "Add HW3 submission - Hugging Face Course completion"

# Push to your fork
git push origin hw3-[your-name]
```

### Step 5: Create Pull Request
1. **Go to the main course repository** on GitHub
2. **Click "New Pull Request"**
3. **Set the branch**: `[your-fork]:hw3-[your-name]` → `main:main`
4. **Add a detailed description** including:
   - Summary of chapters completed
   - Any challenges encountered
   - Key learnings from the experience
   - How this connects to course material

### 📧 Pull Request Template
Use this template for your PR description:

```markdown
## HW3 Submission: Hugging Face Course Completion

**Student**: [Your Name]
**Chapters Completed**: 1, 2, 3, 4, 5, 6, 7, 11
**Completion Date**: [Date]

### Summary
Brief overview of your experience with the Hugging Face course.

### Key Achievements
- [ ] Completed all required chapters
- [ ] All notebooks executed successfully  
- [ ] Screenshots captured for each chapter
- [ ] Personal reflection written

### Challenges Encountered
Describe any technical difficulties or conceptual challenges you faced.

### Course Connections
How does this practical experience connect to our MAI 5201 course material?

### File Structure
Confirm your submission includes:
- [ ] `notebooks/` folder with all completed chapters
- [ ] `screenshots/` folder with results documentation
- [ ] `README.md` with personal reflection
```

**Due Date**: October 28, 2025 at 11:59 PM (Guyana time)

---

**Good luck, and enjoy your journey into the world of Large Language Models! 🚀**

*This assignment will give you hands-on experience with the tools and techniques used by leading AI companies and research organizations worldwide. The skills you develop here will be directly applicable to your final course project and future NLP work.*