"""
MAI 5201 - Homework 0: Regular Expressions
Part 1: Pattern Matching and Text Extraction

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement the functions below using regular expressions
- Run the autograder with: python autograder.py -q q1 (for specific questions)
- Do not modify function signatures or import additional libraries
"""

import re
from typing import List, Optional


def extract_emails(text: str) -> List[str]:
    """
    Extract all email addresses from the given text.
    
    Args:
        text (str): Input text that may contain email addresses
    
    Returns:
        List[str]: List of email addresses found in the text
    
    Examples:
        >>> extract_emails("Contact us at info@university.edu or admin@school.org")
        ['info@university.edu', 'admin@school.org']
        
        >>> extract_emails("My email is john.doe+newsletter@gmail.com")
        ['john.doe+newsletter@gmail.com']
    """
    # TODO: Implement email extraction using regex
    # Hint: Consider various email formats including:
    # - Basic format: user@domain.com
    # - With dots and underscores: first.last_name@domain.co.uk
    # - With plus signs: user+tag@domain.com
    # - Various domain extensions: .com, .edu, .org, .co.uk, etc.
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace the empty pattern above with your implementation
    # For now, return empty list until implemented
    return []


def extract_urls(text: str) -> List[str]:
    """
    Extract all URLs from the given text.
    
    Args:
        text (str): Input text that may contain URLs
    
    Returns:
        List[str]: List of URLs found in the text
    
    Examples:
        >>> extract_urls("Visit https://www.uog.edu.gy or http://example.com for more info")
        ['https://www.uog.edu.gy', 'http://example.com']
        
        >>> extract_urls("Check out ftp://files.example.com/data.txt")
        ['ftp://files.example.com/data.txt']
    """
    # TODO: Implement URL extraction using regex
    # Hint: Consider various URL formats:
    # - HTTP/HTTPS: https://www.example.com
    # - FTP: ftp://files.example.com
    # - With paths: https://example.com/path/to/page
    # - With query parameters: https://example.com/search?q=nlp
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_phone_numbers(text: str) -> List[str]:
    """
    Extract all phone numbers from the given text.
    
    Args:
        text (str): Input text that may contain phone numbers
    
    Returns:
        List[str]: List of phone numbers found in the text
    
    Examples:
        >>> extract_phone_numbers("Call (592) 123-4567 or 592.123.4567")
        ['(592) 123-4567', '592.123.4567']
        
        >>> extract_phone_numbers("International: +1-800-555-0123")
        ['+1-800-555-0123']
    """
    # TODO: Implement phone number extraction using regex
    # Hint: Consider various phone number formats:
    # - (XXX) XXX-XXXX
    # - XXX.XXX.XXXX
    # - XXX-XXX-XXXX
    # - +X-XXX-XXX-XXXX (international)
    # - +XXXXXXXXXX (international without separators)
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def normalize_phone_number(phone: str) -> str:
    """
    Normalize a phone number to the format +XXX-XXX-XXXX.
    
    Args:
        phone (str): Phone number in any format
    
    Returns:
        str: Normalized phone number
    
    Examples:
        >>> normalize_phone_number("(592) 123-4567")
        '+592-123-4567'
        
        >>> normalize_phone_number("592.123.4567")
        '+592-123-4567'
    """
    # TODO: Implement phone number normalization
    # Hint: 
    # 1. Extract digits using regex
    # 2. Format as +XXX-XXX-XXXX
    
    # Remove all non-digit characters
    # digits = re.findall(r'\d', phone)
    # digits_str = ''.join(digits)
    
    # TODO: Format the digits as +XXX-XXX-XXXX
    # Handle cases where country code might be missing
    
    return ''  # Your implementation here


def extract_hashtags(text: str) -> List[str]:
    """
    Extract hashtags from social media text.
    
    Args:
        text (str): Social media text that may contain hashtags
    
    Returns:
        List[str]: List of hashtags (without the # symbol)
    
    Examples:
        >>> extract_hashtags("Great day! #university #education #nlp")
        ['university', 'education', 'nlp']
        
        >>> extract_hashtags("Learning #MachineLearning and #NLP_basics")
        ['MachineLearning', 'NLP_basics']
    """
    # TODO: Implement hashtag extraction using regex
    # Hint: Hashtags start with # and can contain letters, numbers, and underscores
    # Return the hashtag text without the # symbol
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_mentions(text: str) -> List[str]:
    """
    Extract user mentions from social media text.
    
    Args:
        text (str): Social media text that may contain mentions
    
    Returns:
        List[str]: List of mentions (without the @ symbol)
    
    Examples:
        >>> extract_mentions("Thanks @UofG and @DrClarke for the great lecture!")
        ['UofG', 'DrClarke']
        
        >>> extract_mentions("Shoutout to @user_123 and @another-user")
        ['user_123', 'another-user']
    """
    # TODO: Implement mention extraction using regex
    # Hint: Mentions start with @ and can contain letters, numbers, underscores, and hyphens
    # Return the mention text without the @ symbol
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_emojis(text: str) -> List[str]:
    """
    Extract emojis from text.
    
    Args:
        text (str): Text that may contain emojis
    
    Returns:
        List[str]: List of emojis found in the text
    
    Examples:
        >>> extract_emojis("Great day! 🎓 Looking forward to graduation! 🎉")
        ['🎓', '🎉']
        
        >>> extract_emojis("Weather is nice ☀️ and I'm happy 😊")
        ['☀️', '😊']
    """
    # TODO: Implement emoji extraction using regex
    # Hint: Emojis are Unicode characters in specific ranges
    # You can use Unicode ranges or a simplified pattern for common emojis
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_dates(text: str) -> List[str]:
    """
    Extract dates in various formats from text.
    
    Args:
        text (str): Text that may contain dates
    
    Returns:
        List[str]: List of dates found in the text
    
    Examples:
        >>> extract_dates("The meeting is on July 25, 2025 and the deadline is 2025-07-30")
        ['July 25, 2025', '2025-07-30']
        
        >>> extract_dates("Important dates: 12/25/2025 and 25-12-2025")
        ['12/25/2025', '25-12-2025']
    """
    # TODO: Implement date extraction using regex
    # Hint: Consider various date formats:
    # - July 25, 2025 (Month Day, Year)
    # - 2025-07-25 (YYYY-MM-DD)
    # - 12/25/2025 (MM/DD/YYYY)
    # - 25-12-2025 (DD-MM-YYYY)
    
    patterns = [
        r'',  # Pattern for Month Day, Year
        r'',  # Pattern for YYYY-MM-DD
        r'',  # Pattern for MM/DD/YYYY
        r'',  # Pattern for DD-MM-YYYY
    ]
    
    dates = []
    for pattern in patterns:
        if pattern:  # Only process non-empty patterns
            dates.extend(re.findall(pattern, text))
    
    return dates


def extract_times(text: str) -> List[str]:
    """
    Extract times in various formats from text.
    
    Args:
        text (str): Text that may contain times
    
    Returns:
        List[str]: List of times found in the text
    
    Examples:
        >>> extract_times("Meeting at 3:30 PM and conference call at 14:30:00")
        ['3:30 PM', '14:30:00']
        
        >>> extract_times("Event starts at 9:00am and ends at 5:30 p.m.")
        ['9:00am', '5:30 p.m.']
    """
    # TODO: Implement time extraction using regex
    # Hint: Consider various time formats:
    # - 3:30 PM / 3:30 AM
    # - 14:30:00 (24-hour format with seconds)
    # - 9:00am / 5:30p.m. (various AM/PM formats)
    
    patterns = [
        r'',  # Pattern for 12-hour format with AM/PM
        r'',  # Pattern for 24-hour format
        r'',  # Pattern for compact AM/PM format
    ]
    
    times = []
    for pattern in patterns:
        if pattern:  # Only process non-empty patterns
            times.extend(re.findall(pattern, text))
    
    return times


def extract_sections(text: str) -> List[str]:
    """
    Extract section headers from a document.
    
    Args:
        text (str): Document text with markdown-style headers
    
    Returns:
        List[str]: List of section headers (without the # symbols)
    
    Examples:
        >>> doc = "# Introduction\\n## 1.1 Background\\n### Details"
        >>> extract_sections(doc)
        ['Introduction', '1.1 Background', 'Details']
    """
    # TODO: Implement section header extraction using regex
    # Hint: Markdown headers start with one or more # symbols
    # Return the header text without the # symbols and leading/trailing whitespace
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_citations(text: str) -> List[str]:
    """
    Extract academic citations from text.
    
    Args:
        text (str): Academic text that may contain citations
    
    Returns:
        List[str]: List of citations found in the text
    
    Examples:
        >>> text = "According to Smith et al. (2023) and Jones (2022), this is important."
        >>> extract_citations(text)
        ['Smith et al. (2023)', 'Jones (2022)']
    """
    # TODO: Implement citation extraction using regex
    # Hint: Look for patterns like "Author (Year)" or "Author et al. (Year)"
    # Consider different citation formats:
    # - Smith (2023)
    # - Smith et al. (2023)
    # - Smith and Jones (2023)
    # - (Smith, 2023)
    # - Multiple citations separated by semicolons
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


def extract_code_blocks(text: str) -> List[str]:
    """
    Extract code blocks from markdown text.
    
    Args:
        text (str): Markdown text that may contain code blocks
    
    Returns:
        List[str]: List of code content (without the ``` markers)
    
    Examples:
        >>> text = "Here's some code:\\n```python\\nprint('Hello')\\n```"
        >>> extract_code_blocks(text)
        ["print('Hello')"]
    """
    # TODO: Implement code block extraction using regex
    # Hint: Markdown code blocks are surrounded by triple backticks ```
    # Use re.DOTALL flag to match across multiple lines
    # Return the code content without the ``` markers and language identifier
    
    pattern = r''  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    return []


# Additional utility functions for testing
def validate_email(email: str) -> bool:
    """
    Validate if a string is a properly formatted email address.
    
    Args:
        email (str): String to validate
    
    Returns:
        bool: True if valid email, False otherwise
    """
    # TODO: Implement email validation
    # This is a more strict validation than extraction
    # pattern = r''  # Your regex pattern here
    # return bool(re.fullmatch(pattern, email))
    return False  # TODO: Implement validation


def validate_url(url: str) -> bool:
    """
    Validate if a string is a properly formatted URL.
    
    Args:
        url (str): String to validate
    
    Returns:
        bool: True if valid URL, False otherwise
    """
    # TODO: Implement URL validation
    # pattern = r''  # Your regex pattern here
    # return bool(re.fullmatch(pattern, url))
    return False  # TODO: Implement validation


def extract_addresses(text: str) -> List[dict]:
    """
    Extract addresses from text.
    Should handle:
    - Street addresses: "123 Main Street", "456 Oak Avenue"
    - P.O. Boxes: "P.O. Box 123", "PO Box 456"
    - Complete addresses with city, state/region, postal code
    
    Args:
        text (str): The input text to search
        
    Returns:
        List[dict]: List of dictionaries with address components
        
    Examples:
        >>> text = "Send mail to 123 Main Street, Georgetown, Guyana or P.O. Box 456"
        >>> extract_addresses(text)
        [{'full_address': '123 Main Street, Georgetown, Guyana', 'type': 'street'}, 
         {'full_address': 'P.O. Box 456', 'type': 'po_box'}]
    """
    # TODO: Implement address extraction using regex
    # Hint: Consider patterns for:
    # - Street addresses: number + street name + street type (St, Ave, Rd, etc.)
    # - P.O. Boxes: "P.O. Box" or "PO Box" followed by number
    # - City, state/country combinations
    
    addresses = []
    
    # Pattern for P.O. Box addresses
    # po_box_pattern = r''  # Your regex pattern here
    
    # Pattern for street addresses  
    # street_pattern = r''  # Your regex pattern here
    
    # TODO: Find P.O. Box addresses
    # TODO: Find street addresses
    # TODO: Return list of dictionaries with address info
    
    return []  # TODO: Implement address extraction


def parse_log_files(log_text: str) -> List[dict]:
    """
    Extract structured information from server log files.
    Parse entries like:
    "192.168.1.100 - admin [25/Jul/2025:10:30:45 +0000] 'GET /api/users HTTP/1.1' 200 1234"
    
    Extract:
    - IP address
    - Username (if present)
    - Timestamp
    - HTTP method and path
    - Status code
    - Response size
    
    Args:
        log_text (str): Raw log file content
        
    Returns:
        List[dict]: List of dictionaries with parsed log entry components
        
    Examples:
        >>> log = "192.168.1.100 - admin [25/Jul/2025:10:30:45 +0000] 'GET /api/users HTTP/1.1' 200 1234"
        >>> parse_log_files(log)
        [{'ip': '192.168.1.100', 'user': 'admin', 'timestamp': '25/Jul/2025:10:30:45 +0000', 
          'method': 'GET', 'path': '/api/users', 'status': '200', 'size': '1234'}]
    """
    # TODO: Implement log file parsing using regex
    # Hint: Apache/Nginx log format is typically:
    # IP - USER [TIMESTAMP] "METHOD PATH PROTOCOL" STATUS SIZE
    # Use named groups for easier extraction
    
    # pattern = r''  # Your regex pattern here with named groups
    
    log_entries = []
    lines = log_text.strip().split('\n')
    
    for line in lines:
        if line.strip():  # Skip empty lines
            # TODO: Parse each line and extract components
            pass
    
    return []  # TODO: Implement log parsing


if __name__ == "__main__":
    # Test your functions here
    sample_text = """
    Contact us at info@university.edu or visit https://www.uog.edu.gy for more information.
    You can also call us at (592) 123-4567 or send a message to @UofG on social media.
    Great day! #university #education 🎓 
    Meeting scheduled for July 25, 2025 at 3:30 PM.
    Our office is located at 123 Main Street, Georgetown, Guyana or P.O. Box 456.
    """
    
    print("Testing regex functions:")
    print("Emails:", extract_emails(sample_text))
    print("URLs:", extract_urls(sample_text))
    print("Phone numbers:", extract_phone_numbers(sample_text))
    print("Hashtags:", extract_hashtags(sample_text))
    print("Mentions:", extract_mentions(sample_text))
    print("Emojis:", extract_emojis(sample_text))
    print("Dates:", extract_dates(sample_text))
    print("Times:", extract_times(sample_text))
    print("Addresses:", extract_addresses(sample_text))
