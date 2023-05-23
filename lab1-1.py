# 14. Write a function to find the list of words that are longer than n from a given list of words.
def find_long_words(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

# 15. Write a function that takes two lists and returns True if they have at least one common member.
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# 16. Write a function to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations. Go to the editor
def find_triplets(arr1, arr2, arr3, target):
    for num1 in arr1:
        for num2 in arr2:
            for num3 in arr3:
                if num1 + num2 + num3 == target:
                    print(num1, num2, num3)

# 17. Write a function to get n-th Fibonaci number.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# 18. Write a function to get all sub-list of a list, the sub-list must have at least 2 elements.
def get_all_sublists(lst):
    sublists = [[]]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j+1]
            if len(sublist) > 1:
                sublists.append(sublist)
    return sublists

# 19. Write a function to find the intersections and differences of 2 lists.
def find_intersection_difference(list1, list2):
    intersection = []
    difference = []
    for elem in list1:
        if elem in list2:
            intersection.append(elem)
        else:
            difference.append(elem)
    for elem in list2:
        if elem not in list1:
            difference.append(elem)
    return intersection, difference

# 10. Write a function that takes a list of words and returns the length of the longest one.
def longest_word_length(word_list):
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length


def sort_tuples_by_last_element2(tuples):
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            if tuples[i][-1] > tuples[j][-1]:
                tuples[i], tuples[j] = tuples[j], tuples[i]
    return tuples


def concatenate_dicts(dicts_list):
    result = {}
    for d in dicts_list:
        for k, v in d.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result
