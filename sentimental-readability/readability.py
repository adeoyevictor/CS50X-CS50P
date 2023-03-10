from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = calc_index(letters, words, sentences)
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


def calc_index(letters, words, sentences):
    L = (letters * 100) / words
    S = (sentences * 100) / words
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


def count_letters(s):
    letters = 0
    for i in s:
        if i.isalpha():
            letters += 1
    return letters
    

def count_words(s):
    words = 1
    for i in s:
        if i == ' ':
            words += 1
    return words


def count_sentences(s):
    sentences = 0
    for i in s:
        if (i == '.' or i == '?' or i == '!'):
            sentences += 1
    return sentences


main()