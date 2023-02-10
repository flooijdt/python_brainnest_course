def anagrams(lst):
    d = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in d:
            d[sorted_word].append(word)
            print(d)
        else:
            d[sorted_word] = [word]
    return [set(v) for v in d.values() if len(v) > 1]

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(anagrams(words))
