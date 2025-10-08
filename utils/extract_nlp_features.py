"""
Linguistic Feature Extraction Functions for NLP Analysis

This module contains functions to extract various linguistic features from text,
particularly useful for analyzing language patterns in dementia research.
"""

import nltk
from nltk.tokenize import word_tokenize
from functools import lru_cache
import string

# Download required NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('averaged_perceptron_tagger_eng', quiet=True)


# Helper utilities for efficient token processing
ALPHA = set(string.ascii_lowercase)


def _clean_tokens(text):
    """Lowercase, tokenize, keep only purely alphabetic tokens."""
    tokens = [t.lower() for t in word_tokenize(text)]
    return [t for t in tokens if t.isalpha()]


@lru_cache(maxsize=2048)
def _pos_tags(text):
    """Cache POS tags for efficiency."""
    toks = _clean_tokens(text)
    return nltk.pos_tag(toks) if toks else []


# ==================== Linguistic Feature Functions ====================


def nouns_freq_in_text(text):
    """Return noun token ratio: proportion of noun POS tokens among cleaned tokens.
    
    Noun tags counted: NN, NNS, NNP, NNPS.
    Returns 0.0 if no lexical tokens present.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        float: Ratio of noun tokens to total tokens (0.0 to 1.0)
    """
    tags = _pos_tags(text)
    if not tags:
        return 0.0
    noun_tags = {"NN", "NNS", "NNP", "NNPS"}
    noun_count = sum(1 for _, tag in tags if tag in noun_tags)
    return noun_count / len(tags)


def word_used_once_frequency(text):
    """Hapax legomena ratio: proportion of token types occurring exactly once among cleaned tokens.
    
    Uses lowercase alphabetic tokens via _clean_tokens.
    Returns 0.0 if no valid tokens.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        float: Ratio of hapax legomena to total tokens (0.0 to 1.0)
    """
    tokens = _clean_tokens(text)
    if not tokens:
        return 0.0
    freq = nltk.FreqDist(tokens)
    hapax_count = sum(1 for c in freq.values() if c == 1)
    return hapax_count / len(tokens)


def word_used_once_or_twice_frequency(text):
    """Low-frequency token ratio: proportion of tokens whose type frequency ≤ 2 among cleaned tokens.
    
    Uses lowercase alphabetic tokens via _clean_tokens.
    Returns 0.0 if no valid tokens.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        float: Ratio of low-frequency tokens to total tokens (0.0 to 1.0)
    """
    tokens = _clean_tokens(text)
    if not tokens:
        return 0.0
    freq = nltk.FreqDist(tokens)
    leq2_count = sum(1 for c in freq.values() if c <= 2)
    return leq2_count / len(tokens)


def brunet_index(text, alpha=-0.165):
    """Calculate the Brunet index for lexical richness.
    
    The Brunet index measures vocabulary richness using the formula:
    W = N^(V^alpha) where N is token count, V is type count, alpha is a constant.
    
    Args:
        text (str): Input text to analyze
        alpha (float): Constant parameter (default: -0.165)
        
    Returns:
        float: Brunet index value
    """
    tokens = _clean_tokens(text)
    if not tokens:
        return 0.0
    
    word_freq = nltk.FreqDist(tokens)
    unique_words = len(word_freq)
    tokens_count = len(tokens)
    
    if unique_words == 0 or tokens_count == 0:
        return 0.0
    
    return tokens_count ** (unique_words ** alpha)


def token_type_ratio(text):
    """Type-Token Ratio (TTR) over cleaned lowercase alphabetic tokens.
    
    TTR is the ratio of unique words (types) to total words (tokens).
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        float: Type-Token Ratio (0.0 to 1.0)
    """
    tokens = _clean_tokens(text)
    N = len(tokens)
    if N == 0:
        return 0.0
    return len(set(tokens)) / N


def adposition_frequency(text, include_to: bool = True):
    """Adposition ratio: proportion of adposition POS tags among cleaned tokens.

    Counts Penn Treebank tag 'IN' (prepositions/subordinating conjunctions) and, by default,
    'TO' (the infinitival/particle 'to') when include_to is True.
    Uses cached POS tagging over cleaned alphabetic lowercase tokens.
    Returns 0.0 if no lexical tokens are present.
    
    Args:
        text (str): Input text to analyze
        include_to (bool): Whether to include 'TO' tag (default: True)
        
    Returns:
        float: Ratio of adposition tokens to total tokens (0.0 to 1.0)
    """
    tokens = _clean_tokens(text)
    tags = _pos_tags(text)
    if not tags:
        return 0.0
    adp_tags = {"IN"}
    if include_to:
        adp_tags.add("TO")
    adp_count = sum(1 for _, tag in tags if tag in adp_tags)
    return adp_count / len(tokens)


def uni_and_bi_grams_repetitions(text):
    """Calculate the number of unique unigrams and bigrams in the text.
    
    Measures vocabulary diversity by counting unique unigrams plus unique bigrams.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        int: Sum of unique unigrams and unique bigrams
    """
    tokens = word_tokenize(text)
    if not tokens:
        return 0
    unigrams = nltk.FreqDist(tokens)
    bigrams = nltk.FreqDist(nltk.bigrams(tokens))
    return len(unigrams) + len(bigrams)


def word_freq_subtl(text, corpus_data):
    """Calculate the frequency of words in the text based on SUBTLEXus data.
    
    Computes weighted average of SUBTLEX word frequencies.
    
    Args:
        text (str): Input text to analyze
        corpus_data (pd.DataFrame): DataFrame with 'Word' and 'SUBTLWF' columns
        
    Returns:
        float: Mean weighted SUBTLEX frequency
    """
    if corpus_data is None:
        return 0.0

    tokens = _clean_tokens(text)
    if not tokens:
        return 0.0

    word_freq = nltk.FreqDist(tokens)
    total_freq = sum(word_freq.values())

    subtl_freq = 0
    for word, freq in word_freq.items():
        matching_rows = corpus_data[corpus_data['Word'] == word]
        if not matching_rows.empty:
            subtl_value = matching_rows['SUBTLWF'].values[0]
            subtl_freq += freq * subtl_value

    return subtl_freq / len(tokens) if total_freq > 0 else 0.0


def word_freq_zipf(text, corpus_data):
    """Calculate the frequency of words in the text based on Zipf data.
    
    Computes weighted average of Zipf word frequencies.
    
    Args:
        text (str): Input text to analyze
        corpus_data (pd.DataFrame): DataFrame with 'Word' and 'Zipf-value' columns
        
    Returns:
        float: Mean weighted Zipf frequency
    """
    if corpus_data is None:
        return 0.0

    tokens = _clean_tokens(text)
    if not tokens:
        return 0.0

    word_freq = nltk.FreqDist(tokens)
    total_freq = sum(word_freq.values())

    zipf_freq = 0
    for word, freq in word_freq.items():
        matching_rows = corpus_data[corpus_data['Word'] == word]
        if not matching_rows.empty:
            zipf_value = matching_rows['Zipf-value'].values[0]
            zipf_freq += freq * zipf_value

    return zipf_freq / total_freq if total_freq > 0 else 0.0


# ==================== Export All Functions ====================

__all__ = [
    'nouns_freq_in_text',
    'word_used_once_frequency',
    'word_used_once_or_twice_frequency',
    'brunet_index',
    'token_type_ratio',
    'adposition_frequency',
    'uni_and_bi_grams_repetitions',
    'word_freq_subtl',
    'word_freq_zipf',
]
