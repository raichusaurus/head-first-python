def search_for_vowels(phrase:str) -> set:
    """Return any vowels in a supplied phrase."""
    vowels = set('aeiou')
    return search_for_letters(phrase, vowels)


def search_for_letters(phrase:str, letters:str) -> set:
    """Return any supplied letters found from the supplied phrase."""
    return set(letters).intersection(set(phrase))