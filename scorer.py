"""
Given a SolveState object, finds the 
highest scoring word and returns the score of that word.
"""

letter_to_points = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 2,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10,
}


def calculate_score(word):
    """Given a word, calculates the score for that word.

    Parameters
    ----------
    word : str
        The word to compute the score for.

    Returns
    -------
    int
        Score of the word.
    """
    return sum(letter_to_points[letter] for letter in word)


def get_highest_score_word(solver):
    """Given a list of word position pairs, returns the word 
    with the highest score along with the positions of each 
    letter of that word.

    Parameters
    ----------
    solver : SolveState
        scrabble solver object.

    Returns
    -------
    tuple
        The word (str) and list of (r, c) positions of each letter of that word.
    """
    words_and_positions = solver.find_all_options()

    if words_and_positions == []:
        return None

    final_word = ''
    final_positions = []
    highest_score = 0

    for word, positions in words_and_positions:
        score = calculate_score(word)
        if score > highest_score:
            final_word = word
            final_positions = positions
            highest_score = score
    
    return final_word, final_positions, highest_score