# Problem 7: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        middle = alphabet[size - i - 1:size]
        line = "-".join(left + middle)
        lines.append(line.center(4 * size - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


n = int(input())
print_rangoli(n)