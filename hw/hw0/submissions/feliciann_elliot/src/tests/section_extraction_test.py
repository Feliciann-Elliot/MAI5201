import regex_exercises

section_test_cases = [
    # Basic markdown headers
    ("# Introduction\nContent here", ["Introduction"]),
    ("## Background\nMore content", ["Background"]),
    ("### Details\nDetailed content", ["Details"]),
    ("#### Subsection\nSubsection content", ["Subsection"]),
    ("##### Minor Section\nMinor content", ["Minor Section"]),
    ("###### Smallest\nSmallest content", ["Smallest"]),
    
    # Multiple headers
    ("# Main Title\n## Subsection\n### Details", ["Main Title", "Subsection", "Details"]),
    ("## Chapter 1\n### Section 1.1\n### Section 1.2", ["Chapter 1", "Section 1.1", "Section 1.2"]),
    ("# Introduction\n## Methods\n## Results\n## Conclusion", 
     ["Introduction", "Methods", "Results", "Conclusion"]),
    
    # Headers with numbers
    ("## 1. Introduction", ["1. Introduction"]),
    ("### 2.1 Background", ["2.1 Background"]),
    ("#### 3.2.1 Methodology", ["3.2.1 Methodology"]),
    ("## Chapter 1: Getting Started", ["Chapter 1: Getting Started"]),
    ("### Section 2.3: Advanced Topics", ["Section 2.3: Advanced Topics"]),
    
    # Headers with special characters
    ("# Introduction & Overview", ["Introduction & Overview"]),
    ("## Methods - Part I", ["Methods - Part I"]),
    ("### Results (Preliminary)", ["Results (Preliminary)"]),
    ("#### Discussion [Draft]", ["Discussion [Draft]"]),
    ("##### Conclusion: Final Thoughts", ["Conclusion: Final Thoughts"]),
    
    # Academic paper structure
    ("# Abstract\n## Introduction\n## Literature Review\n## Methodology\n## Results\n## Discussion\n## Conclusion", 
     ["Abstract", "Introduction", "Literature Review", "Methodology", "Results", "Discussion", "Conclusion"]),
    
    # Technical documentation
    ("# API Documentation\n## Authentication\n## Endpoints\n### GET /users\n### POST /users\n## Error Handling", 
     ["API Documentation", "Authentication", "Endpoints", "GET /users", "POST /users", "Error Handling"]),
    
    # Mixed levels
    ("# Part I\n## Chapter 1\n### 1.1 Overview\n### 1.2 Details\n## Chapter 2\n# Part II", 
     ["Part I", "Chapter 1", "1.1 Overview", "1.2 Details", "Chapter 2", "Part II"]),
    
    # Headers with content between
    ("# Introduction\nThis is intro content\n## Background\nBackground info\n### History\nHistorical context", 
     ["Introduction", "Background", "History"]),
    
    # No headers
    ("Just regular text without any headers", []),
    ("Plain content with no markdown formatting", []),
    ("Text with # but not at start of line", []),
    
    # Edge cases
    ("#NoSpace", ["NoSpace"]),
    ("# ", []),  # Empty header
    ("####### Too many hashes", []),  # Invalid markdown
    ("Not a header # in middle", []),
    ("# Valid Header\n### Another Valid Header", ["Valid Header", "Another Valid Header"]),
]

def run_test_cases(test_cases):
    passed = 0
    failed = 0
    for i, (input_str, expected_output) in enumerate(test_cases):
        actual_output = regex_exercises.extract_sections(input_str)
        if actual_output == expected_output:
            print(f"Test Case {i+1}: Passed")
            passed += 1
        else:
            print(f"Test Case {i+1}: Failed")
            print(f"Input: {input_str}")
            print(f"Expected Output: {expected_output}")
            print(f"Actual Output: {actual_output}")
            print()
            failed += 1
    print(f"Passed: {passed} / {len(test_cases)}")
    print(f"Failed: {failed} / {len(test_cases)}")

run_test_cases(section_test_cases)