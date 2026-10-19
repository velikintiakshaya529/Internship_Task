# Problem 17: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = ""

        while len(result) < len(s):
            result += str(current)
            current += 1

        if result == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    separateNumbers(input().strip())