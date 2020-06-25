import sympy as sym

def anagram(word1, word2):
    if len(word1) != len(word2):
        return "{} and {} are not anagrams".format(word1.upper(), word2.upper())

    word1_total, word2_total = 1, 1

    for y, z in zip(word1, word2):
        word1_total *= sym.prime((ord(y) + 8) % 26)
        word2_total *= sym.prime((ord(z) + 8) % 26)

    if word1_total == word2_total:
        return "{} and {} are anagrams".format(word1.upper(), word2.upper())
    else:
        return "{} and {} are not anagrams".format(word1.upper(), word2.upper())

if __name__ == '__main__':
    word1, word2 = input('Input 1st word: '), input('Input 2nd word: ')

    print(anagram(word1.casefold(), word2.casefold()))