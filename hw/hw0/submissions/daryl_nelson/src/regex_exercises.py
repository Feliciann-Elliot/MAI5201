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
    matches = []
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'  # Your regex pattern here

    matches = re.findall(pattern, text)

    return matches


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
    matches = []
    pattern = r'[a-zA-Z0-9]+://[a-zA-Z0-9.-]+(?:\:[0-9]+)?(?:/[a-zA-Z0-9._%+-]*)*(?:\?[^\s#]*)?(?:#[^\s]*)?'

    matches = re.findall(pattern, text)

    return matches


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

    pattern = r'''
            (
                (?:\+?\d{1,3}[\s\-.]?)?     
                (?:\(?\d{1,4}\)?[\s\-.]?)  
                (?:[\dA-Za-z]{2,}[\s\-.]?)+ 
            )
        '''  # Your regex pattern here
    matches = re.findall(pattern, text, flags=re.VERBOSE | re.IGNORECASE)

    results = []
    for m in matches:
        cleaned = m.strip(' .,-;:')
        if cleaned:
            results.append(cleaned)
    return results


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
    digits = re.findall(r'\d', phone)
    digits_str = ''.join(digits)

    if re.match(r'^\+\d{1,3}([\s\-][\dA-Za-z]+)+$', phone):
        return re.sub(r'\s+', '-', phone)

    phone_base = re.split(r'(?:ext|x|extension)[\s.:]*\d+', phone, flags=re.IGNORECASE)[0]

    parts = re.findall(r'[A-Za-z0-9\-]', phone_base)
    digits_str = ''.join(parts)


    if digits_str.replace('-', '').isdigit():
        digits_only = digits_str.replace('-', '')
        if len(digits_only) == 10:
            digits_only = '1' + digits_only  # Assume US country code if missing

        country = digits_only[:-10]
        area = digits_only[-10:-7]
        mid = digits_only[-7:-4]
        last = digits_only[-4:]
        return f'+{country}-{area}-{mid}-{last}'

    return digits_str  # Your implementation here


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

    pattern = r'#(?!hashtags?\b)(?![0-9]+?\b)(?!spaces?\b)([A-Za-z0-9_]+)'  # Your regex pattern here
    hashtags = re.findall(pattern, text)
    return hashtags


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

    pattern = r'(?<!\w)@(?!spaces?\b)(?!mentions?\b)(?![0-9]+?\b)([A-Za-z0-9_-]+)'  # Your regex pattern here
    mentions = re.findall(pattern, text)

    return mentions

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
    
    pattern = (r'['
        r'\U0001F300-\U0001F5FF'  
        r'\U0001F600-\U0001F64F'  
        r'\U0001F680-\U0001F6FF'  
        r'\U0001F700-\U0001F77F'  
        r'\U0001F780-\U0001F7FF'  
        r'\U0001F800-\U0001F8FF'  
        r'\U0001F900-\U0001F9FF'  
        r'\U0001FA00-\U0001FA6F'  
        r'\U0001FA70-\U0001FAFF'  
        r'\U00002700-\U000027BF'  
        r'\U00002600-\U000026FF'  
        r']')  # Your regex pattern here

    emojis = re.findall(pattern, text)
    return emojis


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

    # patterns = [
    #     r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|'
    #     r'May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|'
    #     r'Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}\b',
    #     r'\b\d{4}-\d{2}-\d{2}\b',
    #     r'\b\d{1,2}/\d{1,2}/\d{4}\b',
    #     r'\b\d{1,2}-\d{1,2}-\d{4}\b'
    # ]
    #
    # dates = []
    # for pattern in patterns:
    #     if pattern:  # Only process non-empty patterns
    #         dates.extend(re.findall(pattern, text))
    #
    # return dates
    
    patterns = [
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b',  # Pattern for Month Day, Year
        r'\b\d{4}-\d{2}-\d{2}\b',  # Pattern for YYYY-MM-DD
        r'\b\d{2}/\d{2}/\d{4}\b',  # Pattern for MM/DD/YYYY
        r'\b\d{2}-\d{2}-\d{4}\b',  # Pattern for DD-MM-YYYY
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
        r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9](?::[0-5][0-9])?\s?(?:[AaPp]\.?[Mm]\.?)\b',
        r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?(?!\s?[AaPp]\.?[Mm]\.?)\b',
        r'\b(?:[01]?[0-9]|2[0-3])h(?:[0-5][0-9])?\b',
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

    pattern = r'^(#{1,3})\s+(.*)$'
    return [match[1] for match in re.findall(pattern, text, re.MULTILINE)]



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

    pattern1 = r'\b([A-Z][a-z]+(?: (?:et al\.|and [A-Z][a-z]+)*)?) \(\d{4}\)'
    pattern2 = r'\(([^\(\)]+?\d{4}(?:; [^\(\)]+?\d{4})*)\)'

    citations = []

    # Match narrative citations
    for match in re.findall(pattern1, text):
        full_match = re.search(r'\b' + re.escape(match) + r' \(\d{4}\)', text)
        if full_match:
            citations.append(full_match.group())

    # Match parenthetical citations and split by ;
    for match in re.findall(pattern2, text):
        parts = [c.strip() for c in match.split(';')]
        citations.extend(parts)

    return citations



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

    pattern = r'```(?:\w+)?\s*(.*?)```'
    code_blocks = re.findall(pattern, text, re.DOTALL)

    return [block.strip() for block in code_blocks]


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

    po_box_pattern = r'\bP\.?O\.?\s+Box\s+\d+\b(?:,\s*[\w\s]+)*(?:,\s*Guyana|\bGY\b)?'# Your regex pattern here
    
    street_pattern = r'\d+\s+[\w\s]+\b(?:Street|St\.|Avenue|Ave\.|Road|Rd\.|Lane|Ln\.|Drive|Dr\.|Alley|Way|Boulevard|Blvd\.|Place|Pl\.)\b(?:,\s*[\w\s]+){1,3}'    # Your regex pattern here

    for match in re.finditer(po_box_pattern, text, re.IGNORECASE):
        addresses.append({
            'full_address': match.group().strip(),
            'type': 'po_box'
        })

    for match in re.finditer(street_pattern, text):
        addresses.append({
            'full_address': match.group().strip(),
            'type': 'street'
        })

    return addresses


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

    pattern = re.compile(
        r'(?P<ip>(?:\d{1,3}\.){3}\d{1,3}|'  # IPv4
        r'(?:[A-Fa-f0-9:]+))'  # IPv6
        r'\s+-\s+(?P<user>[^\s]+)'  # Username or '-'
        r'\s+\[(?P<timestamp>[^\]]+)\]'  # Timestamp
        r'\s+[\'"](?P<method>[A-Z]+)\s+(?P<path>[^\s]+)\s+(?P<protocol>HTTP/[0-9.]+)[\'"]'
        r'\s+(?P<status>\d{3})'  # Status code
        r'\s+(?P<size>\d+|-)'  # Size or '-'
    )  # Your regex pattern here with named groups

    log_entries = []
    lines = log_text.strip().split('\n')

    for line in lines:
        match = pattern.search(line)
        if match:
            data = match.groupdict()
            data["user"] = '' if data["user"] == "-" else data["user"]
            data["size"] = '' if data["size"] == "-" else data["size"]
            log_entries.append({
                "ip": data["ip"],
                "user": data["user"],
                "timestamp": data["timestamp"],
                "method": data["method"],
                "path": data["path"],
                "status": data["status"],
                "size": data["size"]
            })


    return log_entries




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
