from collections import defaultdict

def group_anagrams(words):
    anagram=defaultdict(list)
    for word in words:
        key=hash_word(word)
        anagram[key].append(word)
    return list(anagram.values())

def hash_word(word):
    count=[0]*26
    for i in word:
        count[ord(i)-ord('a')]+=1
    return tuple(count)


words=input().split()
anagram_sets=[]
anagram_sets.append(group_anagrams(words))
for i in anagram_sets:
    print(i)