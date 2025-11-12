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

import re, regex
import unicodedata
from typing import List, Tuple
import nltk
from nltk.tokenize import TweetTokenizer
from collections import defaultdict, Counter

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

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
    # TODO: Implement basic whitespace tokenization
    # Hint: Use the string split() method
    return text.split()


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
    # TODO: Implement punctuation tokenization
    # Hints:
    # 1. Use regex to separate words from punctuation
    # 2. Consider contractions (they should be split)
    # 3. Pattern ideas: \w+ for words, [^\w\s] for punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    return tokens


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
    # TODO: Implement sentence tokenization
    # Hints:
    # 1. Split on sentence-ending punctuation (.!?)
    # 2. Handle abbreviations like "Dr.", "U.S.A."
    # 3. Preserve punctuation at end of sentences
    sentences = regex.split(r'(?<!\b(?:[A-Z][a-z]*\.|[A-Z]\.)+|(?:Dr|Mr|Mrs|Ms|Prof|Sr|Jr|vs|etc|Inc|Ltd|Co|Corp|St|Ave|Rd)\.)(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return [text.strip()] if text.strip() else []
    return sentences


def advanced_tokenize(text: str) -> List[str]:
    """
    Advanced tokenization handling contractions, hyphenated words, and URLs.
    
    Special handling for:
    - Contractions (can't -> ca + n't)
    - Hyphenated words (twenty-first stays together)
    - URLs (stay together)
    - Email addresses (stay together)
    """
    # TODO: Implement advanced tokenization
    # Hints:
    # 1. Preserve URLs and email addresses as single tokens
    # 2. Handle contractions by splitting them appropriately
    # 3. Keep hyphenated words together
    # 4. Split on punctuation otherwise

        # Step 1: Protect URLs and emails
    protected_pattern = r'https?://\S+|www\.\S+|bit\.ly/\S+|\S+@\S+\.\S+'
    protected_tokens = re.findall(protected_pattern, text)
    placeholder_map = {}
    
    # Replace protected tokens with placeholders
    modified_text = text
    for i, token in enumerate(protected_tokens):
        placeholder = f"__PROTECTED_{i}__"
        placeholder_map[placeholder] = token
        modified_text = modified_text.replace(token, placeholder, 1)
    
    # Step 2: Use TweetTokenizer (handles contractions well)
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(modified_text)
    
    # Step 3: Post-process to match expected format
    final_tokens = []
    
    for token in tokens:
        # Handle special case for "can't" → "ca" "n't"
        if token.lower() == "can't":
            final_tokens.extend(["ca", "n't"])
        elif token.startswith("__PROTECTED_"):
            # Restore protected tokens
            final_tokens.append(placeholder_map[token])
        else:
            final_tokens.append(token)
    
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
    
    text = text.lower()
    
    # Step 2: Remove accents and diacritics using Unicode normalization
    # NFD decomposes characters, then we remove combining marks (Mn category)
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    
    # Step 3: Remove excessive punctuation
    # Remove 2 or more consecutive exclamation marks
    text = re.sub(r'[!]{2,}', '', text)
    # Remove 2 or more consecutive question marks
    text = re.sub(r'[?]{2,}', '', text)
    # Remove 3 or more consecutive dots (ellipses)
    text = re.sub(r'[.]{3,}', '', text)
    
    # Step 4: Remove remaining punctuation (except spaces)
    # Keep only alphanumeric characters and spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Step 5: Normalize whitespace - collapse multiple spaces and strip
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
    
    m, n = len(str1), len(str2)

    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                           dp[i][j - 1] + 1,    # Insertion
                           dp[i - 1][j - 1] + cost)

    return dp[m][n]  # TODO: Replace with your implementation


def load_dictionary(filepath):
    """
    Load dictionary from file, skipping first 4 lines.
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            # Skip first 4 lines, get words from line 5 onwards
            words = []
            for i, line in enumerate(lines):
                if i >= 4:  # Skip first 4 lines
                    word = line.strip().lower()
                    if word:  # Skip empty lines
                        words.append(word)
            return words
    except FileNotFoundError:
        print(f"Dictionary file {filepath} not found")
        return []

load_dictionary('data/english_words.txt')  # Load dictionary if needed

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
    
    min_distance = float('inf')
    closest_word = candidates[0]

    for candidate in candidates:
        distance = edit_distance(word, candidate)
        if distance < min_distance:
            min_distance = distance
            closest_word = candidate

    return closest_word  # TODO: Replace with your implementation


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
        # Initialize vocabulary with individual characters
        self.vocab = set()
        
        # Pre-tokenize corpus into words and count frequencies
        word_freq = defaultdict(int)
        for text in corpus:
            # Simple word tokenization (you might want to use a more sophisticated one)
            words = text.split()
            for word in words:
                word_freq[word] += 1
                # Add characters to vocabulary
                for char in word:
                    self.vocab.add(char)
        
        # Add end-of-word marker to vocabulary
        self.vocab.add('</w>')
        
        # Convert words to initial token sequences
        word_tokens = {}
        for word in word_freq:
            word_tokens[word] = self._get_word_tokens(word)
        
        # Perform BPE merges
        for i in range(self.num_merges):
            # Count all adjacent pairs
            pair_counts = defaultdict(int)
            
            for word, tokens in word_tokens.items():
                freq = word_freq[word]
                pairs = self._get_pairs(tokens)
                for pair in pairs:
                    pair_counts[pair] += freq
            
            # Stop if no pairs found
            if not pair_counts:
                break
                
            # Find the most frequent pair
            best_pair = max(pair_counts, key=pair_counts.get)
            
            # If the best pair occurs only once, stop merging
            if pair_counts[best_pair] < 2:
                break
            
            # Add the new merged token to vocabulary
            new_token = ''.join(best_pair)
            self.vocab.add(new_token)
            
            # Record the merge operation
            self.merges.append(best_pair)
            
            # Apply the merge to all words
            word_tokens = self._merge_vocab(best_pair, word_tokens, word_freq)
    
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
        return list(word) + ['</w>']
    
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
        pairs = set()
        for i in range(len(word_tokens) - 1):
            pairs.add((word_tokens[i], word_tokens[i + 1]))
        return pairs
    
    def _merge_vocab(self, pair, word_tokens, word_freq):
        """
        Merge a specific pair in the vocabulary.
        
        Args:
            pair (Tuple[str, str]): Pair of tokens to merge
            word_tokens (Dict[str, List[str]]): Dictionary mapping words to their token lists
            word_freq (Dict[str, int]): Word frequency dictionary
            
        Returns:
            Dict[str, List[str]]: Updated word tokens dictionary
        """
        first, second = pair
        new_token = first + second
        
        updated_word_tokens = {}
        
        for word, tokens in word_tokens.items():
            # Apply merges to this word's tokens
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == first and tokens[i + 1] == second:
                    # Merge the pair
                    new_tokens.append(new_token)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            updated_word_tokens[word] = new_tokens
            
        return updated_word_tokens
    
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
        # Split text into words
        words = text.split()
        all_tokens = []
        
        for word in words:
            # Start with character-level tokenization
            tokens = self._get_word_tokens(word)[:-1]  # Remove </w> for processing
            tokens.append('</w>')
            
            # Apply all learned merges in order
            for merge_pair in self.merges:
                first, second = merge_pair
                new_tokens = []
                i = 0
                while i < len(tokens):
                    if i < len(tokens) - 1 and tokens[i] == first and tokens[i + 1] == second:
                        # Merge the pair
                        merged_token = first + second
                        new_tokens.append(merged_token)
                        i += 2
                    else:
                        new_tokens.append(tokens[i])
                        i += 1
                tokens = new_tokens
            
            # Remove </w> marker from final tokens
            if tokens and tokens[-1] == '</w>':
                tokens = tokens[:-1]
            
            all_tokens.extend(tokens)
        
        return all_tokens
    
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
    # TODO: Implement Levenshtein distance algorithm
    # This should be the same as edit_distance but with a different name
    # Use the same dynamic programming approach
    
    m, n = len(s1), len(s2)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1, # Deletion
                dp[i][j - 1] + 1, # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
                )    

    return dp[m][n]  # TODO: Replace with your implementation


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

    
    return find_closest_word(word, candidates)  # TODO: Replace with your implementation


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
    
    min_distance = float('inf')
    best_match = query

    query_lower = query.lower()

    for candidate in candidates:
        candidate_lower = candidate.lower()
        distance = levenshtein_distance(query_lower, candidate_lower)

        if distance < min_distance:
            min_distance = distance
            best_match = candidate

    return best_match  # TODO: Replace with your implementation
