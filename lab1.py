class ListFunctions:
    """
    Class containing functions that operate on lists.
    """

    def __init__(self, numbers):
        self.numbers = numbers

    def sum_odd_numbers(self):
        odd_sum = 0
        for num in self.numbers:
            if num % 2 != 0:
                odd_sum += num
        return odd_sum

    def find_prime_numbers(self):
        primes = []
        for num in self.numbers:
            if num > 1:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
        return primes

    def get_largest_number(self):
        largest = None
        for num in self.numbers:
            if largest is None or num > largest:
                largest = num
        return largest

    def get_smallest_number(self):
        smallest = None
        for num in self.numbers:
            if smallest is None or num < smallest:
                smallest = num
        return smallest

    def remove_duplicates(self):
        result = []
        for element in self.numbers:
            if element not in result:
                result.append(element)
        return result



class StringFunctions:
    """
    Class containing functions that operate on strings.
    """
    def __init__(self, string):
        self.string = string

    def count_characters(self):
        counts = {}
        for char in self.string:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts

    def replace_first_char_occurrences(self):
        first_char = self.string[0]
        new_string = first_char

        for i in range(1, len(self.string)):
            if self.string[i] == first_char:
                new_string += '$'
            else:
                new_string += self.string[i]

        return new_string

    def swap_first_two_chars(self, str2):
        # swap the first two characters of str1 and str2
        str1_swapped = str2[:2] + self.string[2:]
        str2_swapped = self.string[:2] + str2[2:]

        result = str1_swapped + ' ' + str2_swapped
        return result

    def add_ing_or_ly(self):
        if len(self.s) < 3:
            return self.s
        if self.s[-3:] == 'ing':
            return self.s + 'ly'
        return self.s + 'ing'


class DictFunctions:
    """
    Class containing functions that operate on dictionaries.
    """
    def __init__(self, dict):
        self.dict = dict

    def sort_dict_by_value_descending(self):
        sorted_dict = dict(
            sorted(self.dict.items(), key=lambda x: x[1], reverse=True))
        return sorted_dict

    def sort_dict_by_value_ascending(self):
        sorted_dict = dict(sorted(self.dict.items(), key=lambda x: x[1]))
        return sorted_dict


list1 = ListFunctions([1,2,3])
print(list1.get_largest_number())
