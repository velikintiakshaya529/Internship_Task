# Problem 6: Pangrams
# Link: https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()
letters = set()

for ch in s:
    if ch.isalpha():
        letters.add(ch)

print("pangram" if len(letters) == 26 else "not pangram")