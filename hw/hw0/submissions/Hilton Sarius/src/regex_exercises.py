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
    
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'    # Your regex pattern here
    found_emails = re.findall(pattern, text)
    return found_emails

    #pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Your regex pattern here
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
    
    pattern = r'[a-zA-Z][a-zA-Z0-9+.-]*://[^\s\'",)>\]};]+'  # Your regex pattern
    matched_urls  = re.findall(pattern, text)
    return matched_urls 
    #pattern = r''  # Your regex pattern here
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
    
 
    # Define regex patterns for different phone number formats
    intl_pattern = r'\+\d{1,3}(?:[\s.-]\d{1,4}){2,6}'  # International format
    branded_pattern = r'(?:1-)?\d{3}(?:-[A-Za-z0-9]{2,}){1,3}'  # Vanity numbers

    # Local formats
    local_variants = [
        r'\(\d{3}\)\s*\d{3}-\d{4}',      # (123) 456-7890
        r'\d{3}[.-]\d{3}[.-]\d{4}',      # 123.456.7890 or 123-456-7890
        r'\d{3}\s\d{3}\s\d{4}',          # 123 456 7890
    ]

    # Merge all patterns
    all_patterns = [intl_pattern, branded_pattern] + local_variants
    full_regex = '|'.join(all_patterns)

    # Search for matches
    results = re.findall(full_regex, text)

    # Clean and return results
    return [num.strip() for num in results if num]
    #pattern = r''  # Your regex pattern here
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
    


    cleaned = phone.strip()

    # Remove common extension formats
    cleaned = re.sub(r'\b(?:x|ext|extension)\s*\d+\b', '', cleaned, flags=re.IGNORECASE)

    # Handle vanity numbers (e.g., 1-800-FLOWERS)
    if re.search(r'[A-Za-z]', cleaned):
        if re.fullmatch(r'\d{3}-\w+', cleaned):
            return f'+1-{cleaned}'
        elif re.fullmatch(r'1-\d{3}-\w+', cleaned):
            return f'+{cleaned.lstrip("+")}'
        return cleaned

    # Extract digits only
    digits_only = ''.join(re.findall(r'\d', cleaned))

    # Format for Guyana numbers
    if digits_only.startswith('592') and len(digits_only) == 10:
        return f'+592-{digits_only[3:6]}-{digits_only[6:]}'

    # Break into number-like groups
    number_parts = re.findall(r'\+?\d+', cleaned)

    if not number_parts:
        return cleaned

    # US/Canada 11-digit format
    if len(digits_only) == 11 and digits_only.startswith('1'):
        return f'+1-{digits_only[1:4]}-{digits_only[4:7]}-{digits_only[7:]}'

    # Default to US/Canada if 10 digits and no country code
    if len(digits_only) == 10 and not any(part.startswith('+') for part in number_parts):
        return f'+1-{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}'

    # Reconstruct normalized format
    formatted = []
    for idx, segment in enumerate(number_parts):
        formatted.append(segment if idx == 0 and segment.startswith('+') else segment)

    final = '-'.join(formatted)

    return final if final != phone else phone
    #return ''  # Your implementation here


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
    
    pattern = r'(?<!\w)#([A-Za-z0-9_]+)\b'
    hashtags = re.findall(pattern, text)

    exceptions = {'hashtag', 'hashtags', 'tag', 'tags', 'spaces'}
    return [tag for tag in hashtags if re.search(r'[A-Za-z]', tag) and tag.lower() not in exceptions]

    #pattern = r''  # Your regex pattern here
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
    
    pattern = r'(?<!\w)@([A-Za-z0-9_-]+)'  # Your regex pattern here
    mentions = re.findall(pattern, text)
    exceptions = {'mention', 'mentions', 'spaces'}
    return [mention for mention in mentions if re.search(r'[A-Za-z]', mention) and mention.lower() not in exceptions]   
    #pattern = r''  # Your regex pattern here
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

    pattern = (
        r'(?:[\U0001F1E6-\U0001F1FF]{2})'
        r'|['
        r'\U0001F300-\U0001F9FF'
        r'\U0001F0CF'
        r'\U0001F600-\U0001F64F'
        r'\U0001F680-\U0001F6FF'
        r'\u2600-\u26FF'
        r'\u2700-\u27BF'
        r'\u231A-\u231B'
        r'\u23E9-\u23EF'
        r'\u23F0-\u23F3'
        r'\u23F8-\u23FA'
        r'\u25AA-\u25AB'
        r'\u25B6'
        r'\u25C0'
        r'\u25FB-\u25FE'
        r'\u2605'
        r'\u2606'
        r'\u2614'
        r'\u2615'
        r'\u261D'
        r'\u2640'
        r'\u2642'
        r'\u2648-\u2653'
        r'\u267F'
        r'\u2693'
        r'\u26A1'
        r'\u26AA'
        r'\u26AB'
        r'\u26BD'
        r'\u26BE'
        r'\u26C4'
        r'\u26C5'
        r'\u26CE'
        r'\u26D4'
        r'\u26EA'
        r'\u26F2'
        r'\u26F3'
        r'\u26F5'
        r'\u26FA'
        r'\u26FD'
        r'\u2705'
        r'\u270A-\u270B'
        r'\u2728'
        r'\u274C'
        r'\u274E'
        r'\u2753-\u2755'
        r'\u2757'
        r'\u2795-\u2797'
        r'\u27B0'
        r'\u27BF'
        r'\u2B1B-\u2B1C'
        r'\u2B50'
        r'\u2B55'
        r'\u2328'
        r'\u2194-\u2199'
        r'\u21A9-\u21AA'
        r'\u2B05-\u2B07'
        r'\uFFFD'
        r']'
        r'[\U0001F3FB-\U0001F3FF\uFE0F\u200D\u2640\u2642]*'
    )
    #pattern = r'[\U0001F300-\U0001F9FF\U0001F0CF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF\u231A-\u231B\u23E9-\u23EF\u23F0-\u23F3\u23F8-\u23FA\u25AA-\u25AB\u25B6\u25C0\u25FB-\u25FE\u2605\u2606\u2614\u2615\u261D\u2640\u2642\u2648-\u2653\u267F\u2693\u26A1\u26AA\u26AB\u26BD\u26BE\u26C4\u26C5\u26CE\u26D4\u26EA\u26F2\u26F3\u26F5\u26FA\u26FD\u2705\u270A-\u270B\u2728\u274C\u274E\u2753-\u2755\u2757\u2795-\u2797\u27B0\u27BF\u2B1B-\u2B1C\u2B50\u2B55\u2328\u2194-\u2199\u21A9-\u21AA\U0001F1E6-\U0001F1FF][\U0001F3FB-\U0001F3FF\uFE0F\u200D\u2640\u2642]*'  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    emojis = re.findall(pattern, text)
    return emojis   
    #pattern = r''  # Your regex pattern here
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
r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{2,4}',  # Pattern for Month Day, Year (including abbreviations and ordinals, 2-4 digit years)
    r'\d{4}-\d{2}-\d{2}',  # Pattern for YYYY-MM-DD
    r'\d{1,2}/\d{1,2}/\d{4}',  # Pattern for MM/DD/YYYY
    r'\d{1,2}-\d{1,2}-\d{4}',  # Pattern for DD-MM-YYYY
    r'\d{1,2}\.\d{2}\.\d{4}',  # Pattern for DD.MM.YYYY
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

    # Match HH:MM:SS 24-hour format
    r'\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b',

    # Match 12-hour format with AM/PM 
    r'\b(?:1[0-2]|0?[1-9]):[0-5]\d\s*(?:[Aa][Mm]|[Pp][Mm]|[Aa]\.?[Mm]\.?|[Pp]\.?[Mm]\.?)\.?',

    # Match HH:MM 24-hour with colon — prevent HH:MM:SS & AM/PM
    r'\b(?:[01]\d|2[0-3]):[0-5]\d\b(?!\s*(?::[0-5]\d|[AaPp][Mm]|[AaPp]\.?[Mm]\.?))',

    # Match H:MM format (single digit hours) — prevent HH:MM:SS & AM/PM
    r'\b[0-9]:[0-5]\d\b(?!\s*(?::[0-5]\d|[AaPp][Mm]|[AaPp]\.?[Mm]\.?))',

    # Match HH.MM 24-hour with dot
    r'\b(?:[01]\d|2[0-3])\.[0-5]\d\b',

    # Match HhMM format
    r'\b(?:[01]?\d)h[0-5]\d\b',

    # Match HH:MMh format
    r'\b(?:[01]\d|2[0-3]):[0-5]\d\s*h\b',
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

    to_ignore = re.sub(r'^\s*[\s\S]*?(?:^\s*\s*$|$(?![\r\n]))', '', text, flags=re.MULTILINE)

    remove_inline = re.sub(r'[^]*`', '', to_ignore)  # Remove inline code blocks

    pattern = r'^(?!#{7,})(#{1,6})\s*(.+?)\s*$'
    sections = [
        match[1].strip()
        for match in re.findall(pattern, remove_inline, flags=re.MULTILINE)
        if match[1].strip()  # Ensure header text is not empty
    ]
    return sections   
    #pattern = r''  # Your regex pattern here
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

    pattern = r'''
            # ---- Narrative citations: Author (2023), Author et al. (2022, p. 5) ----
            (?:
                (?:[A-Z][a-z]+|[A-Z]{2,})                        # First word: last name or acronym
                (?:\s(?:and|et\ al\.|of|the|[A-Z][a-z]+))*       # Additional words
            )
            \s*
            \(
                \d{4}                                            # Year
                (?:,\s*p{1,2}\.?\s*\d+(?:[-–]\d+)?)?             # Optional page numbers
            \)

            |

            # ---- Parenthetical citations: (Author, 2023), (Author et al., 2022; Author, 2020) ----
            (?<=\()
            (?:
                (?:[A-Z][a-z]+|[A-Z]{2,})
                (?:\s(?:and|et\ al\.|of|the|[A-Z][a-z]+))*
            )
            ,\s*
            \d{4}
            (?:,\s*p{1,2}\.?\s*\d+(?:[-–]\d+)?)?
            (?=\))
        '''

    # Step 1: Match narrative and simple parenthetical citations
    raw_matches = re.findall(pattern, text, re.VERBOSE)

    # Step 2: Extract grouped citations from inside parentheses (e.g. (Author, 2023; Author et al., 2022))
    parenthetical_blocks = re.findall(r'\(([^()]+)\)', text)
    parenthetical_citations = []

    inner_citation_pattern = re.compile(r'''
            ^
            (?:
                (?:[A-Z][a-z]+|[A-Z]{2,})
                (?:\s(?:and|et\ al\.|of|the|[A-Z][a-z]+))*
            )
            ,\s*
            \d{4}
            (?:,\s*p{1,2}\.?\s*\d+(?:[-–]\d+)?)?
            $
        ''', re.VERBOSE)

    for block in parenthetical_blocks:
        parts = [p.strip() for p in block.split(';')]
        for part in parts:
            if inner_citation_pattern.fullmatch(part):
                parenthetical_citations.append(part)

    # Step 3: Clean narrative matches to remove any leading text like "See Jones (2022)"
    citation_cleaner = re.compile(r'''
        (?:
            (?:[A-Z][a-z]+|[A-Z]{2,})
            (?:\s(?:and|et\ al\.|of|the|[A-Z][a-z]+))*
        )
        \s*
        \(
            \d{4}
            (?:,\s*p{1,2}\.?\s*\d+(?:[-–]\d+)?)?
        \)
    ''', re.VERBOSE)

    cleaned_narrative_citations = []
    for match in raw_matches:
        cleaned = citation_cleaner.search(match)
        if cleaned:
            cleaned_narrative_citations.append(cleaned.group(0))
        else:
            cleaned_narrative_citations.append(match)

    # Step 4: Combine and deduplicate
    citations = list(set(cleaned_narrative_citations + parenthetical_citations))
    return citations    
    #pattern = r''  # Your regex pattern here
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
    
    pattern = r'(?:[a-zA-Z]*)\n?([\s\S]*?)\n?'  # Your regex pattern here
    # TODO: Replace empty pattern with your implementation
    code_blocks = re.findall(pattern, text)
    return code_blocks
    #pattern = r''  # Your regex pattern here
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
    po_box_pattern = r'\b(P\.?\s*O\.?\s+Box\s+\d+(?:,\s*[A-Za-z\s]+)?)'  # Your regex pattern here
    
    # Pattern for street addresses  
    street_pattern = r'\b(\d+\s+[A-Za-z\s]+(?:Street|Avenue|Road|Drive|Lane|Boulevard|Circle|St|Ave|Rd|Dr|Ln|Blvd|Cir)\.?(?:,\s*(?:Suite|Unit|Apt)\s*[A-Za-z0-9]+)?(?:,\s*[A-Za-z\s]+)+)'  # Your regex pattern here
    
    # TODO: Find P.O. Box addresses
    # TODO: Find street addresses
    # TODO: Return list of dictionaries with address info
    # Find P.O. Box addresses
    po_box_matches = re.findall(po_box_pattern, text)
    for match in po_box_matches:
        addresses.append({
            'full_address': match,
            'type': 'po_box'
        })

    # Find street addresses
    street_matches = re.findall(street_pattern, text)
    for match in street_matches:
        addresses.append({
            'full_address': match,
            'type': 'street'
        })
    
    return addresses  # TODO: Implement address extraction

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
    
    pattern = r'^(?P<ip>\S+)\s+-\s+(?P<user>\S+)\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>\w+)\s+(?P<path>[^"\s]+)[^"]*"\s+(?P<status>\d{3})\s+(?P<size>\d+)'  # Your regex pattern here with named groups
    
    log_entries = []
    lines = log_text.strip().split('\n')
    
    for line in lines:
        if line.strip():  # Skip empty lines
            match = re.match(pattern, line.strip())
            if match:
                entry = {
                    'ip': match.group('ip'),
                    'user': match.group('user'),
                    'timestamp': match.group('timestamp'),
                    'method': match.group('method'),
                    'path': match.group('path'),
                    'status': match.group('status'),
                    'size': match.group('size')
                }
                log_entries.append(entry)
            # TODO: Parse each line and extract components
            pass
                
    return log_entries  # TODO: Implement log parsing

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
