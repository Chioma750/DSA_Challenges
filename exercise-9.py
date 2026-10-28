def first_duplicate(numbers):
    seen = []

    for num in numbers:
        if num in seen:
            return num
        else:
            seen.append(num)
    return None 

print(first_duplicate([4, 7, 2, 7, 5, 4]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([5, 5, 3]))
print(first_duplicate([]))