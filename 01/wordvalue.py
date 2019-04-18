from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        full_list = file.read().splitlines()

    return full_list



def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[e] for e in word.upper()])


def max_word_value(word=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    result = 0
    line = ""
    for e in word:
        try:
            new_result = calc_word_value(e)

        except Exception:
            continue

        if new_result > result:
            result = new_result
            line = e

    return line

if __name__ == "__main__":
    pass  # run unittests to validate
