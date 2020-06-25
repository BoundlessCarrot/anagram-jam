import sympy as sym

def anagram(word1, word2):
    word1_total, word2_total = 1, 1

    for y in word1:
        word1_total *= sym.prime((ord(y) + 8) % 26)

    for z in word2:
        word2_total *= sym.prime((ord(z) + 8) % 26)

    if word1_total == word2_total:
        print("{} and {} are anagrams".format(word1.upper(), word2.upper()))
    else:
        print("{} and {} are not anagrams".format(word1.upper(), word2.upper()))

if __name__ == '__main__':
    word1, word2 = input('Input 1st word: '), input('Input 2nd word: ')

    anagram(word1.casefold(), word2.casefold())