# Problem 10: CamelCase
# Link: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

words = 1 if s else 0

for ch in s:
    if ch.isupper():
        words += 1

print(words)