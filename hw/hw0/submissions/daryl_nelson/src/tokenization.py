"""
MAI 5201 - Homework 0: Tokenization
Part 2: Text tokenization and normalization

Student Name: [Your Name Here]
Student ID: [Your ID Here]
Date: [Date]

Instructions:
- Implement the tokenization and text processing functions below
- Test your solutions using: python autograder.py
- Run specific questions with: python autograder.py -q q8 (for individual questions)
- Do not modify function signatures or import additional libraries
"""

import re
import unicodedata
from typing import List, Tuple


def whitespace_tokenize(text: str) -> List[str]:
    """
    Basic whitespace tokenization.
    
    Simply splits on any whitespace characters.
    
    Args:
        text (str): Input text to tokenize
    
    Returns:
        List[str]: List of tokens split on whitespace
    
    Examples:
        >>> whitespace_tokenize("Hello world")
        ['Hello', 'world']
        >>> whitespace_tokenize("  Hello   world  ")
        ['Hello', 'world']
    """
    return text.strip().split()


def punctuation_tokenize(text: str) -> List[str]:
    """
    Tokenize text splitting on punctuation.
    
    Separates punctuation from words as individual tokens.
    
    Args:
        text (str): Input text to tokenize
    
    Returns:
        List[str]: List of tokens with punctuation separated
    
    Examples:
        >>> punctuation_tokenize("Hello, world!")
        ['Hello', ',', 'world', '!']
        >>> punctuation_tokenize("It's working.")
        ['It', "'", 's', 'working', '.']
    """
    return re.findall(r"\w+|[^\w\s]", text)


def sentence_tokenize(text: str) -> List[str]:
    """
    Split text into sentences.
    
    Handles sentence boundaries while preserving abbreviations.
    
    Args:
        text (str): Input text to split into sentences
    
    Returns:
        List[str]: List of sentences
    
    Examples:
        >>> sentence_tokenize("Hello world. How are you?")
        ['Hello world.', 'How are you?']
        >>> sentence_tokenize("Dr. Smith went to U.S.A. yesterday.")
        ['Dr. Smith went to U.S.A. yesterday.']
    """
    abbreviations = r"(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|U\.S\.A|U\.K|etc)"
    pattern = rf"(?<=[.!?])\s+(?=[A-Z])"

    sentences = re.split(pattern, text)

    merged = []
    for s in sentences:
        if merged and re.fullmatch(abbreviations + r"\.", merged[-1].split()[-1]):
            merged[-1] += " " + s
        else:
            merged.append(s)

    return [s.strip() for s in merged if s.strip()]


def advanced_tokenize(text: str) -> List[str]:
    """
    Advanced tokenization handling contractions, hyphenated words, and URLs.
    
    Special handling for:
    - Contractions (can't -> ca + n't)
    - Hyphenated words (twenty-first stays together)
    - URLs (stay together)
    - Email addresses (stay together)
    """
    url_pattern = r'https?://\S+|www\.\S+|[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/\S*)?'
    token_pattern = re.compile(
        f"{url_pattern}|[a-zA-Z]+(?:-[a-zA-Z]+)*|n't|'[a-z]+|[^\w\s]",
        re.IGNORECASE
    )

    tokens = token_pattern.findall(text)

    output = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]

        # Fix for "can't" style: if token is 'can' followed by "'t", merge as 'ca' + "n't"
        if i + 1 < len(tokens):
            next_tok = tokens[i + 1]
            if tok.lower() == "can" and next_tok.lower() == "'t":
                output.append("ca")
                output.append("n't")
                i += 2
                continue
            # Also handle other cases like "don" + "'t" -> "don" + "'t" (keep separate)

        # Handle contractions like "n't", "'s", "'m", "'ll", "'re", "'ve", "'d"
        if re.fullmatch(r"n't|'[a-z]+", tok, re.IGNORECASE):
            output.append(tok.lower())
            i += 1
            continue

        # Otherwise just add token as is
        output.append(tok)
        i += 1

    # Post-processing for hyphenated contractions like "don't-care":
    final_tokens = []
    for t in output:
        if "-" in t and ("'" in t or "’" in t):
            # e.g. "don't-care" -> ['don', "'t", '-', 'care']
            parts = t.split("-")
            for idx, p in enumerate(parts):
                if p.lower().endswith("n't") and "'" not in p:
                    final_tokens.append(p[:-3])
                    final_tokens.append("n't")
                else:
                    final_tokens.append(p)
                if idx < len(parts) - 1:
                    final_tokens.append('-')
        else:
            final_tokens.append(t)

    return final_tokens


def normalize_text(text: str) -> str:
    """
    Basic text normalization.
    
    Normalize text by:
    - Converting to lowercase
    - Removing basic accents/diacritics (using Unicode normalization)
    - Removing excessive punctuation (multiple consecutive !!! or ??? or ...)
    - Normalizing whitespace (multiple spaces/tabs/newlines to single space)
    
    Args:
        text (str): Input text to normalize
    
    Returns:
        str: Normalized text
        
    Examples:
        >>> normalize_text("THE CAFÉ serves COFFEE!!!")
        'the cafe serves coffee'
        >>> normalize_text("  Hello   World  ")
        'hello world'
        >>> normalize_text("résumé review???")
        'resume review'
    """
    # TODO: Implement basic text normalization
    # Hints:
    # 1. Convert to lowercase: text.lower()
    # 2. Remove accents using unicodedata.normalize('NFD', text) 
    #    then filter out characters with category 'Mn'
    # 3. Remove excessive punctuation with regex:
    #    - r'[!]{2,}' for multiple exclamations
    #    - r'[?]{2,}' for multiple questions
    #    - r'[.]{3,}' for ellipses (3+ dots)
    # 4. Normalize whitespace: r'\s+' -> ' ' and strip()

    text = text.casefold()

    text = ''.join(
        ch for ch in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(ch)
    )

    text = re.sub(r'[^\w\s]', '', text)

    text = re.sub(r'\s+', ' ', text).strip()

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


def edit_distance(str1: str, str2: str) -> int:
    """
    Compute the edit distance (Levenshtein distance) between two strings.
    
    Uses dynamic programming to find minimum number of operations
    (insertions, deletions, substitutions) to transform str1 into str2.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
    
    Returns:
        int: Minimum edit distance between the strings
        
    Examples:
        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("hello", "hello")
        0
    """
    # TODO: Implement edit distance using dynamic programming
    # Hints:
    # 1. Create a 2D DP table of size (len(str1)+1) x (len(str2)+1)
    # 2. Initialize first row and column with increasing values
    # 3. Fill table using recurrence relation:
    #    - If characters match: dp[i][j] = dp[i-1][j-1]
    #    - Else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    # 4. Return dp[m][n] where m, n are string lengths
    
    return 0  # TODO: Replace with your implementation


def find_closest_word(word: str, candidates: List[str]) -> str:
    """
    Find the closest word from a list of candidates using edit distance.
    
    Returns the candidate with the minimum edit distance to the input word.
    
    Args:
        word (str): Target word to find matches for
        candidates (List[str]): List of candidate words
    
    Returns:
        str: The candidate word with minimum edit distance
        
    Examples:
        >>> find_closest_word("teh", ["the", "tea", "ten"])
        'the'
        >>> find_closest_word("speling", ["spelling", "speaking", "special"])
        'spelling'
    """
    # TODO: Implement closest word finder using edit_distance function
    # Hints:
    # 1. Handle empty candidates list
    # 2. Calculate edit distance to each candidate
    # 3. Return candidate with minimum distance
    # 4. In case of ties, return the first one found
    
    if not candidates:
        return ""
    
    return ""  # TODO: Replace with your implementation


# Q11: BPE Algorithm Implementation

class BPETokenizer:
    """
    Byte Pair Encoding (BPE) Tokenizer implementation.
    
    This class implements the BPE algorithm used in modern NLP models.
    Students need to implement the core methods below.
    """
    
    def __init__(self, num_merges=1000):
        """
        Initialize the BPE tokenizer.
        
        Args:
            num_merges (int): Maximum number of merge operations to perform
        """
        self.num_merges = num_merges
        self.merges = []  # List of (token1, token2) merge operations
        self.vocab = set()  # Set of all tokens in vocabulary
        self.word_splits = {}  # Cache for word tokenizations
    
    def train(self, corpus):
        """
        Train the BPE model on a corpus of text.
        
        Args:
            corpus (List[str]): List of strings to train on
            
        Example:
            corpus = ["hello world", "hello there", "world peace"]
            bpe.train(corpus)
        """
        # TODO: Implement BPE training algorithm
        # 1. Initialize vocabulary with individual characters
        # 2. Count frequency of all adjacent character pairs
        # 3. Merge the most frequent pair
        # 4. Repeat until num_merges is reached
        pass
    
    def _get_word_tokens(self, word):
        """
        Convert a word into initial character tokens.
        
        Args:
            word (str): Input word
            
        Returns:
            List[str]: List of character tokens with end-of-word marker
            
        Example:
            _get_word_tokens("hello") -> ["h", "e", "l", "l", "o", "</w>"]
        """
        # TODO: Implement character-level tokenization
        # Add </w> marker to indicate end of word
        pass
    
    def _get_pairs(self, word_tokens):
        """
        Get all adjacent pairs from a list of tokens.
        
        Args:
            word_tokens (List[str]): List of tokens
            
        Returns:
            Set[Tuple[str, str]]: Set of adjacent token pairs
            
        Example:
            _get_pairs(["h", "e", "l", "l", "o"]) -> {("h", "e"), ("e", "l"), ("l", "l"), ("l", "o")}
        """
        # TODO: Extract all adjacent pairs from token list
        pass
    
    def _merge_vocab(self, pair, word_freq):
        """
        Merge a specific pair in the vocabulary.
        
        Args:
            pair (Tuple[str, str]): Pair of tokens to merge
            word_freq (Dict[str, int]): Word frequency dictionary
            
        Returns:
            Dict[str, int]: Updated word frequency dictionary
            
        Example:
            If pair = ("l", "l") and we have "h e l l o", 
            it becomes "h e ll o"
        """
        # TODO: Merge the specified pair in all words
        # Update the word_freq dictionary with merged tokens
        pass
    
    def tokenize(self, text):
        """
        Tokenize text using the trained BPE model.
        
        Args:
            text (str): Input text to tokenize
            
        Returns:
            List[str]: List of BPE tokens
            
        Example:
            tokenize("hello world") -> ["hell", "o", "w", "or", "ld"]
        """
        # TODO: Apply learned merges to tokenize new text
        # 1. Split text into words
        # 2. Apply BPE merges to each word
        # 3. Return flattened list of tokens
        pass
    
    def get_vocabulary(self):
        """
        Get the current vocabulary.
        
        Returns:
            Set[str]: Set of all tokens in vocabulary
        """
        return self.vocab.copy()
    
    def get_merges(self):
        """
        Get the list of merge operations performed during training.
        
        Returns:
            List[Tuple[str, str]]: List of merge operations in order
        """
        return self.merges.copy()


# Q12: Enhanced Edit Distance Applications
def levenshtein_distance(s1, s2):
    """
    Calculate the Levenshtein (edit) distance between two strings.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
    
    Returns:
        int: Minimum number of single-character edits required
        
    Examples:
        >>> levenshtein_distance("kitten", "sitting")
        3
        >>> levenshtein_distance("saturday", "sunday")
        3
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    previous_row = list(range(len(s1) + 1))
    for i2, c2 in enumerate(s2, 1):
        current_row = [i2]
        for i1, c1 in enumerate(s1, 1):
            insert_cost = previous_row[i1] + 1
            delete_cost = current_row[i1 - 1] + 1
            substitute_cost = previous_row[i1 - 1] + (c1 != c2)
            current_row.append(min(insert_cost, delete_cost, substitute_cost))
        previous_row = current_row

    return previous_row[-1]


def spell_check(word, candidates):
    """
    Find the best spelling correction from a list of candidates.
    
    Args:
        word (str): Misspelled word
        candidates (List[str]): List of potential corrections
    
    Returns:
        str: Best candidate with minimum edit distance
        
    Examples:
        >>> spell_check("recieve", ["receive", "deceive", "relieve"])
        'receive'
        >>> spell_check("teh", ["the", "tea", "ten"])
        'the'
    """
    # TODO: Implement spell checking using levenshtein_distance
    # Hints:
    # 1. Handle empty candidates
    # 2. Calculate distance to each candidate
    # 3. Return candidate with minimum distance
    
    if not candidates:
        return word

    best_word = min(candidates, key=lambda cand: levenshtein_distance(word, cand))
    return best_word


def name_matching(query, candidates):
    """
    Find the best matching name from a list of candidates.
    Useful for matching names with different spellings or transliterations.
    
    Args:
        query (str): Name to match
        candidates (List[str]): List of potential name matches
    
    Returns:
        str: Best matching candidate name
        
    Examples:
        >>> name_matching("Jon Smith", ["John Smith", "Jane Smith", "Jon Snow"])
        'John Smith'
        >>> name_matching("MacDonald", ["McDonald", "MacDonald", "Donald"])
        'MacDonald'
    """
    # TODO: Implement name matching using levenshtein_distance
    # Hints:
    # 1. Handle empty candidates
    # 2. Use case-insensitive comparison
    # 3. Return candidate with minimum edit distance
    
    if not candidates:
        return query

    query_lower = query.lower()
    best_candidate = min(candidates, key=lambda cand: levenshtein_distance(query_lower, cand.lower()))
    return best_candidate
