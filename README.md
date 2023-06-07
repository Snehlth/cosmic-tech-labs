GROUPING ANAGRAMS :

Anagrams are words that have the same characters but in a different order.
for example if the words are: ["cat", "dog", "tac", "god", "act"]
then the anagram sets are: [["cat", "tac", "act"], ["dog", "god"]].
this is the python code for grouping the anagrams

1)first defaultdict class is imported from collections module

2)The function group_anagrams takes a list of words as input.

3)It creates a defaultdict called anagram to store the anagram groups
 every anagram group has different key.

4)The function iterates over each word in the list.

5)For each word, it generates a key using the hash_word function.
the hashword calculates the frequency of each letter in the word.thus the key is generated.the hashword function returns the key as a tuple because it is immutable and it is hashable.

6)then the word is appended to the anagram dictionary using the key.

7)After iterating all the words,the function returns anagram groups as list of lists.it only returns the values in the dictionary.the values are nothing but the required sets of anagrams.

8)In the hash_word function, a list called count is created.it stores the count of each letter in the word.
The function iterates over each character in the word.
the index is calculated by (ASCII value of the current character - the ASCII value character 'a').
The count for that letter is then incremented in the index we got.

9)Finally, the hash_word function returns a tuple representing the count of each letter in the word, which will be used as the key for grouping anagrams.

10)thus the anagrams sets are finally printed.

* the time complexity is O(n * m)

* space complexity for the dictionary is O(n*m)

  where n is the number of words given in the list and m is the length of the list.
