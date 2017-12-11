def search_for_vowels(word:str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))