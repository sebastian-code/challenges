import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input(f"Make a word using this letters {draw}: ").upper()
    # while not _validation(word, draw):
    #     word = input(f'Invalid word. Using only this letters {draw}:')
    _validation(word, draw)
    return word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    if word not in get_possible_dict_words(draw):
        raise ValueError(f"{word.lower()} is not a valid word.")


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum([LETTER_SCORES.get(letter, 0) for letter in word.upper()])


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [word for word in _get_permutations_draw(draw) if word.lower() in DICTIONARY]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return [
        "".join(word)
        for n in range(1, NUM_LETTERS + 1)
        for word in itertools.permutations(draw, n)
    ]


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    word = input_word(draw)
    score = calc_word_value(word)
    print(f"Value given to: {word} (value: {score})")
    possible_words = get_possible_dict_words(draw)
    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print(f"Optimal word possible: {max_word} (value: {max_word_score})")
    game_score = score / max_word_score * 100
    print("You scored: {:.1f}".format(game_score))


if __name__ == "__main__":
    main()
