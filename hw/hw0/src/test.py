import regex_exercises

# Test Case 1: Basic sections (should work)
document1 = """
# Introduction
This is the introduction section.

## 1.1 Background
Some background information.

## 1.2 Motivation
Some motivation details.

# Methods
Research methods here.
"""

# Test Case 2: Sections with extra spacing
document2 = """
#  Introduction With Spaces  
This is the introduction section.

##   1.1 Background Info   
Some background information.
"""

# Test Case 3: Sections with special characters
document3 = """
# Introduction & Overview
This is the introduction section.

## 1.1 Background/Context
Some background information.

## 1.2 Goals & Objectives
Research goals here.
"""

# Test Case 4: Code blocks and edge cases
document4 = """
# Introduction
This is the introduction.

```python
# This is a comment in code, not a section
print("Hello")
"""

print(regex_exercises.extract_sections(document1))
print(regex_exercises.extract_sections(document2))
print(regex_exercises.extract_sections(document3))
print(regex_exercises.extract_sections(document4))