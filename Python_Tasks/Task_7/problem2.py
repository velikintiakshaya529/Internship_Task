# Problem 2: The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_numbers = list(map(int, input().split()))

room_numbers.sort()

for i in range(len(room_numbers)):
    if i == 0:
        if room_numbers[i] != room_numbers[i + 1]:
            print(room_numbers[i])
            break
    elif i == len(room_numbers) - 1:
        if room_numbers[i] != room_numbers[i - 1]:
            print(room_numbers[i])
            break
    elif room_numbers[i] != room_numbers[i - 1] and room_numbers[i] != room_numbers[i + 1]:
        print(room_numbers[i])
        break
