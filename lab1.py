# 1. Write a function to sum all the odd numbers in a list.
def sum_odd_numbers(numbers):
    odd_sum = 0
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

# 2. Write a function to find all prime numbers in a list.
def find_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# 3. Write a function to get the largest number from a list.
def get_largest_number(numbers):
    largest = None
    for num in numbers:
        if largest is None or num > largest:
            largest = num
    return largest

# 4. Write a function to get the smallest number from a list.
def get_smallest_number(numbers):
    """
    This function takes a list of numbers as input and returns the smallest number in the list.
    """
    smallest = None
    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
    return smallest

# 5. Write a function program to count the number of characters occurrences in a string.
def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# 6. Write a function to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sort_tuples_by_last_element(tuples):
    def get_last_element(t):
        return t[-1]
    
    sorted_tuples = sorted(tuples, key=get_last_element)
    return sorted_tuples

def sort_tuples_by_last_element2(tuples):
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            if tuples[i][-1] > tuples[j][-1]:
                tuples[i], tuples[j] = tuples[j], tuples[i]
    return tuples

# 7. Write a function to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def replace_first_char_occurrences(string):
    first_char = string[0]
    new_string = first_char
    
    for i in range(1, len(string)):
        if string[i] == first_char:
            new_string += '$'
        else:
            new_string += string[i]
    
    return new_string

# 8. Write a function to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_first_two_chars(str1, str2):
    # swap the first two characters of str1 and str2
    str1_swapped = str2[:2] + str1[2:]
    str2_swapped = str1[:2] + str2[2:]
    
    # concatenate the two modified strings with a space between them
    result = str1_swapped + ' ' + str2_swapped
    
    return result

# 9. Write a function to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
def add_ing_or_ly(s):
    if len(s) < 3:  # if the string length is less than 3, leave it unchanged
        return s
    
    if s[-3:] == 'ing':  # if the string already ends with 'ing', add 'ly' instead
        return s + 'ly'
    
    return s + 'ing'  # otherwise, add 'ing' at the end

# 10. Write a function that takes a list of words and returns the length of the longest one.
def longest_word_length(word_list):
    max_length = 0  # initialize the maximum length to 0
    
    for word in word_list:
        if len(word) > max_length:  # if the length of the current word is greater than the current maximum, update the maximum
            max_length = len(word)
    
    return max_length

# 11. Write a function to concatenate following dictionaries to create a new one.
def concatenate_dicts(dicts_list):
    result = {}
    for d in dicts_list:
        for k, v in d.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result

dic1={1:10, 2:20}
dic2={2:30, 4:40}
dic3={5:50, 4:60}
dict_list = [dic1,dic2, dic3]
print(dict_list)
print(concatenate_dicts(dict_list))

# 13. Write a function to remove duplicates from a list.
def remove_duplicates(lst):
    result = []
    for element in lst:
        if element not in result:
            result.append(element)
    return result

# 14. Write a function to find the list of words that are longer than n from a given list of words.
def find_long_words(words, n):
    """
    This function takes a list of words and a length 'n' as input and returns a list of all words in the input list
    that are longer than 'n'.
    """
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

source = [1, 2 , 3, 4]
print(get_all_sublists(source))

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

a = [1, 2, 3]
b = [2, 4, 5]
intersections = [2]
differences = [1, 3, 4, 5]
print(find_intersection_difference(a, b))