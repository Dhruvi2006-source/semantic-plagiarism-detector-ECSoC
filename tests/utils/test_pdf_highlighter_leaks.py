import pytest
from src.utils.pdf_highlighter import highlight_pdf_matches, get_word_ngrams

def test_get_word_ngrams():
    """
    Assert that get_word_ngrams correctly splits a phrase into 6-word overlapping windows.
    """
    phrase = "This is a very long phrase that has more than six words"
    ngrams = get_word_ngrams(phrase, n=6)
    
    assert len(ngrams) == 7
    assert ngrams[0] == "This is a very long phrase"
    assert ngrams[1] == "is a very long phrase that"
    assert ngrams[-1] == "has more than six words"

def test_pdf_highlighter_ngrams():
    """
    Verify that highlight_pdf_matches executes successfully when n-gram highlighting is applied.
    """
    with open("tests/fixtures/clean.pdf", "rb") as f:
        pdf_bytes = f.read()

    # Test highlighting with sliding windows
    phrase = "Plagiarism detection is a critical educational challenge in modern classrooms."
    res = highlight_pdf_matches(pdf_bytes, [phrase])
    assert isinstance(res, bytes)
    assert len(res) > 0
