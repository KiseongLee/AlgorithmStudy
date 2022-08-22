import collections


strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = collections.defaultdict(list)
for word in strs:
    print(word)
    print(sorted(word))
    anagrams[''.join(sorted(word))].append(word)

print(anagrams.values())
print(list(anagrams.values()))