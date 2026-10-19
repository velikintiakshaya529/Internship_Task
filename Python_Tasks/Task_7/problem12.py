# Problem 12: Making Anagrams
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

s1 = input().strip()
s2 = input().strip()

count1 = Counter(s1)
count2 = Counter(s2)

deletions = 0

for ch in set(s1) | set(s2):
    deletions += abs(count1[ch] - count2[ch])

print(deletions)