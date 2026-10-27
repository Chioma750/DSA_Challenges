def count_even(numbers):
    counter = 0

    for num in numbers:
        if num % 2 == 0:
            counter += 1

    return counter

print(count_even( [1, 2, 3, 4, 6]))
print(count_even([1, 3, 5, 7]))