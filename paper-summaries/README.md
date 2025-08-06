# Paper Summaries - MAI 5201

This directory contains student submissions for research paper summary assignments. Each assignment requires students to critically analyze assigned papers and submit their summaries via GitHub Pull Request.

## Assignment Overview

An important aspect of doing cutting-edge AI engineering and problem solving is being able to read papers. Particularly now more than ever, developments in the science are required to envision solutions to engineering challenges in AI.

Students will read assigned research papers and submit critical summaries addressing specific analytical questions. This process develops critical reading skills, encourages engagement with current research, and builds professional Git/GitHub workflow experience.

## Submission Process

### Step 1: Repository Setup
1. Fork the main course repository (`MAI5201`)
2. Clone your forked repository locally
3. Create a new branch: `paper-summary-[assignment-number]-[your-name]`

### Step 2: File Creation
Create your submission file in the appropriate directory:
```
paper-summaries/
├── assignment-1/
│   ├── student1-name.md
│   ├── student2-name.md
│   └── student3-name.md
└── assignment-2/
    ├── student1-name.md
    ├── student2-name.md
    └── student3-name.md
```

### Step 3: Summary Requirements
Each summary file must contain:

**Header Information:**
- Your full name and student ID
- Assignment number and date
- Paper citation in APA format
- Word count (target: 200-300 words)

**Summary Content (3 paragraphs):**
1. **What is most interesting in the paper?**
   - Key innovations and contributions
   - Historical or technical significance
   - Novel approaches or insights

2. **What could the paper have done better?**
   - Methodological limitations
   - Writing clarity issues
   - Missing considerations or analyses

3. **What questions do you have from reading the paper?**
   - Technical questions about implementation
   - Theoretical questions about approaches
   - Follow-up research directions

### Step 4: Pull Request Submission
1. Commit changes with meaningful message: `Add [Paper Title] summary - [Your Name]`
2. Push branch to your forked repository
3. Create Pull Request to main repository with:
   - **Title**: `Paper Summary [#]: [Paper Title] - [Your Name]`
   - **Description**: Brief overview of your main insights
   - **Reviewers**: Assign Dr. Clarke

### Step 5: Review and Discussion
- Instructor will review and provide feedback via PR comments
- Summaries will be discussed during class sessions
- PRs will be merged after review completion

## Assessment Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Content Quality** | 60% | Depth of analysis, critical thinking, understanding of paper |
| **Writing Clarity** | 20% | Clear expression, proper grammar, organization |
| **Git/GitHub Usage** | 15% | Proper branching, commits, PR format |
| **Timeliness** | 5% | Submitted by deadline |

## Technical Requirements

- **Format**: Markdown (.md) file with proper formatting
- **Length**: 200-300 words total
- **Style**: Professional tone and academic writing
- **Citations**: Include at least one direct quote with page number
- **Originality**: Must be your own analysis (no plagiarism)

## Git Workflow Quick Reference

```bash
# 1. Fork the repository on GitHub (use the fork button)

# 2. Clone your fork
git clone https://github.com/[your-username]/MAI5201.git
cd MAI5201

# 3. Create a new branch
git checkout -b paper-summary-1-[your-name]

# 4. Create your summary file
# paper-summaries/assignment-1/[your-name].md

# 5. Add and commit your work
git add paper-summaries/assignment-1/[your-name].md
git commit -m "Add ELIZA paper summary - [Your Name]"

# 6. Push to your fork
git push origin paper-summary-1-[your-name]

# 7. Create Pull Request on GitHub
# Go to your fork on GitHub and click "New Pull Request"
```

## Current Assignments

### Assignment 1: ELIZA (1966)
- **Paper**: "ELIZA—A Computer Program For the Study of Natural Language Communication Between Man and Machine" by Joseph Weizenbaum
- **URL**: https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf
- **Due Date**: July 29, 2025 @ 11:59 PM (GYD)
- **Submission Directory**: `paper-summaries/assignment-1/`

### Assignment 2: Neural Machine Translation with Subword Units (2016)
- **Paper**: "Neural Machine Translation of Rare Words with Subword Units" by Rico Sennrich, Barry Haddow, Alexandra Birch
- **URL**: https://aclanthology.org/P16-1162.pdf
- **Due Date**: August 6, 2025 @ 11:59 PM (GYD)
- **Submission Directory**: `paper-summaries/assignment-2/`

### Assignment 3: Class-Based n-gram Models (1992)
- **Paper**: "Class-Based n-gram Models of Natural Language" by Peter F. Brown, Peter V. deSouza, Robert L. Mercer, Vincent J. Della Pietra, Jenifer C. Lai
- **URL**: https://aclanthology.org/J92-4003.pdf
- **Due Date**: August 12, 2025 @ 11:59 PM (GYD)
- **Submission Directory**: `paper-summaries/assignment-3/`

---

*For questions about assignments or technical issues with Git/GitHub, please email Dr. Clarke at christopher.clarke@uog.edu.gy or create an issue in the course repository.*
