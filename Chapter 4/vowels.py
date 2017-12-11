def search_for_vowels(phrase:str) -> set:
    """Return any vowels in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))