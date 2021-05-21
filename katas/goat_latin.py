"""LeetCode Goat Lating Kata
From: https://leetcode.com/problems/goat-latin/"""

VOWELS = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']


def to_goat_latin(sentence):
    """A sentence sentence is given, composed of words separated by spaces.
    Each word consists of lowercase and uppercase letters only.
    We would like to convert the sentence to "Goat Latin"
    (a made-up language similar to Pig Latin)."""

    words_in_goat_latin = []
    for index, word in enumerate(sentence.split(' '), start=1):
        if word[0] in VOWELS:
            word_in_goat_latin = word + 'ma'
        else:
            word_in_goat_latin = word[1:] + word[0] + 'ma'

        words_in_goat_latin.append(word_in_goat_latin + ('a' * index))

    return ' '.join(words_in_goat_latin)
