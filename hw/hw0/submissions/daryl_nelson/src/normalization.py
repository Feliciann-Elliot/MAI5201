"""
MAI 5201 - Homework 0: Text Normalization
Part 2: Text preprocessing and normalization functions

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement text normalization functions
- These functions support the tokenization exercises
- Test your solutions using the autograder
"""

import re
import unicodedata
from typing import List, Optional


def normalize_text(text: str) -> str:
    """
    Comprehensive text normalization function.
    
    This function should:
    1. Convert to lowercase
    2. Remove accents/diacritics
    3. Normalize whitespace
    4. Remove or normalize punctuation
    
    Args:
        text (str): Input text to normalize
    
    Returns:
        str: Normalized text
    
    Examples:
        >>> normalize_text("The café in São Paulo serves EXCELLENT coffee!!!")
        'the cafe in sao paulo serves excellent coffee'
        
        >>> normalize_text("  Multiple   spaces   and\t\ttabs  ")
        'multiple spaces and tabs'
    """
    # TODO: Implement comprehensive text normalization
    # Step 1: Convert to lowercase
    
    # Step 2: Remove accents and diacritics
    
    # Step 3: Normalize whitespace
    
    # Step 4: Remove excessive punctuation
    
    return text


def remove_accents(text: str) -> str:
    """
    Remove accents and diacritics from text.
    
    Args:
        text (str): Text with potential accents
    
    Returns:
        str: Text with accents removed
    
    Examples:
        >>> remove_accents("café")
        'cafe'
        >>> remove_accents("naïve")
        'naive'
        >>> remove_accents("résumé")
        'resume'
    """
    # TODO: Implement accent removal using Unicode normalization
    # Hint: Use unicodedata.normalize() and unicodedata.category()
    return text


def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in text (spaces, tabs, newlines).
    
    Args:
        text (str): Text with irregular whitespace
    
    Returns:
        str: Text with normalized whitespace
    
    Examples:
        >>> normalize_whitespace("hello    world")
        'hello world'
        >>> normalize_whitespace("line1\n\n\nline2")
        'line1 line2'
    """
    # TODO: Implement whitespace normalization
    # Replace multiple spaces, tabs, newlines with single spaces
    return text


def normalize_punctuation(text: str) -> str:
    """
    Normalize punctuation in text.
    
    Args:
        text (str): Text with irregular punctuation
    
    Returns:
        str: Text with normalized punctuation
    
    Examples:
        >>> normalize_punctuation("hello!!!")
        'hello!'
        >>> normalize_punctuation("really???")
        'really?'
    """
    # TODO: Implement punctuation normalization
    # Reduce repeated punctuation to single instances
    return text


def case_fold(text: str) -> str:
    """
    Advanced case folding that handles special Unicode cases.
    
    This is more sophisticated than simple .lower() as it handles
    special cases like German ß, Turkish İ/ı, etc.
    
    Args:
        text (str): Text to case fold
    
    Returns:
        str: Case-folded text
    
    Examples:
        >>> case_fold("HELLO WORLD")
        'hello world'
        >>> case_fold("İstanbul")  # Turkish capital İ
        'i̇stanbul'
    """
    # TODO: Implement case folding using Unicode standards
    # Hint: Use str.casefold() which is more aggressive than .lower()
    return text


def normalize_numbers(text: str) -> str:
    """
    Normalize number representations in text.
    
    Args:
        text (str): Text containing numbers
    
    Returns:
        str: Text with normalized numbers
    
    Examples:
        >>> normalize_numbers("I have 1,000 dollars")
        'I have 1000 dollars'
        >>> normalize_numbers("Price: $19.99")
        'Price: 19.99'
    """
    # TODO: Implement number normalization
    # Remove commas from numbers, handle currency symbols, etc.
    return text


def expand_contractions(text: str) -> str:
    """
    Expand common English contractions.
    
    Args:
        text (str): Text containing contractions
    
    Returns:
        str: Text with expanded contractions
    
    Examples:
        >>> expand_contractions("I can't believe it's working!")
        "I cannot believe it is working!"
        >>> expand_contractions("We'll see you tomorrow")
        "We will see you tomorrow"
    """
    # TODO: Implement contraction expansion
    # Create a dictionary of common contractions and their expansions
    
    contractions_dict = {
        "can't": "cannot",
        "won't": "will not",
        "n't": " not",
        "'ll": " will",
        "'re": " are",
        "'ve": " have",
        "'m": " am",
        "'d": " would",
        "it's": "it is",
        "that's": "that is",
        # Add more contractions as needed
    }
    
    # TODO: Apply the contractions dictionary to the text
    return text


def remove_special_characters(text: str, keep_alphanumeric: bool = True, keep_spaces: bool = True) -> str:
    """
    Remove special characters from text.
    
    Args:
        text (str): Input text
        keep_alphanumeric (bool): Whether to keep alphanumeric characters
        keep_spaces (bool): Whether to keep spaces
    
    Returns:
        str: Text with special characters removed
    
    Examples:
        >>> remove_special_characters("Hello, World! @#$")
        'Hello World'
        >>> remove_special_characters("user@domain.com", keep_alphanumeric=True, keep_spaces=False)
        'userdomaincom'
    """
    # TODO: Implement special character removal
    return text
