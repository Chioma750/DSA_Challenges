def find_largest(numbers):
    if numbers == []:
        return None
    
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))