# Problem 3: Mars Exploration
# Link: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
message = "SOS" * (len(s) // 3)

count = 0
for i in range(len(s)):
    if s[i] != message[i]:
        count += 1

print(count)