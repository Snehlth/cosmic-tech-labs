from collections import defaultdict

def group_anagrams(words):
    anagram=defaultdict(list)               # Dictionary to store anagram groups
    for word in words:
        key=hash_word(word)                 # Generate a key for the word
        anagram[key].append(word)           # Add the word to the corresponding anagram group
    return list(anagram.values())           # Return the anagram groups as a list

def hash_word(word):
    count=[0]*26                            # Frequency count of each letter in the word
    for i in word:
        count[ord(i)-ord('a')]+=1           # Increment the count for each letter
    return tuple(count)                     # Return a tuple as the key because it is immutable and hashable



words=input().split()                       # Take input from the user
anagram_sets=[]                             # Call the function to group the anagrams
anagram_sets.append(group_anagrams(words))  # Print the resulting anagram sets
for i in anagram_sets:
    print(i)
