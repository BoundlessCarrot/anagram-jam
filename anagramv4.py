def sieve(n):
    initlist = list(range(2, n+1))
    for x in range(2, n+1):
        for y in range(x, n+1, x):
            if x != y:
                try:
                    initlist.remove(y)
                except ValueError:
                    continue
    
    return initlist

def anagram(word1, word2):
    if len(word1) != len(word2):
        return "{} and {} are not anagrams".format(word1.upper(), word2.upper())

    primelist = sieve(102)
    
    word1_total, word2_total = 1, 1

    for a, b in zip(word1, word2):
        word1_total *= primelist[(ord(a) + 8) % 26]
        word2_total *= primelist[(ord(b) + 8) % 26]

    if word1_total == word2_total:
        return "{} and {} are anagrams".format(word1.upper(), word2.upper())
    else:
        return "{} and {} are not anagrams".format(word1.upper(), word2.upper())

def main():
    word1, word2 = input('Input 1st word: '), input('Input 2nd word: ')
    print(anagram(word1.casefold(), word2.casefold()))

if __name__ == '__main__':
    main()