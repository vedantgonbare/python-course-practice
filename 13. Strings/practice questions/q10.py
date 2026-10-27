"""
Q102: Longest Word
Take a sentence as input. Print the longest word in it.
"""
def longest_word(sentence: str):
    words = sentence.split()
    print(words)
    long_count = 0
    long_word = ""
    for word in words:
        if len(word) > long_count:
            long_count = len(word)
            long_word = word
    print(long_word)


sentence = "Vedant is learning Python programming every single day"
longest_word(sentence)
