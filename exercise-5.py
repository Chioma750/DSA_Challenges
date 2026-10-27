def count_occurrences(numbers, target):
    counter = 0

    for num in numbers:
        if num == target:
            counter += 1
    return counter

print(count_occurrences( numbers = [2, 5, 2, 8, 2], target = 2))
print(count_occurrences( numbers = [1, 4, 7], target = 10))