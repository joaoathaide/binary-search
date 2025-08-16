def binary_search(list, item):
    init = 0
    high = len(list) - 1

    while(init <= high):
        center = (init + high) // 2
        guess = list[center]

        if (guess == item):
            return center
        elif (guess < item):
            init = center + 1
        else:
            high = center - 1

    return None


list = [0, 1, 2, 3, 4, 5, 6, 14, 18, 30, 54]
item = 18

result = binary_search(list, item)
print(result)