
# ===========================================================================================

# Exercise 10.1. Write a function called nested_sum that takes a nested list of integers and add up
# the elements from all of the nested lists.




def nested_sum(nested_list):
    total = 0
    for sublist in nested_list:
        for num in sublist:
            total += num
        return total   
    
print(nested_sum([[1, 2], [3, 4], [5]]))


# =============================================================================================



def nested_max(nested_list):
    max_value = None
    for sublist in nested_list:
        for num in sublist:
            if max_value is None or num > max_value:
                max_value = num
    return max_value

print(nested_max([[1, 2], [10, 3], [5]]))


# =================================================================================================================


# Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes
# a nested list of strings and returns a new nested list with all strings capitalized.

def capitalize_nested(nested_list):
    result = []
    for sublist in nested_list:
        new_sublist = []
        for word in sublist:
            new_sublist.append(word.capitalize())
        result.append(new_sublist)
    return result

data = [["hello", "world"], ["python", "code"]]
print(capitalize_nested(data))



# ======================================================================================================

# Exercise 10.4 write a function called middle that takes a list and returns a new list that contains 
# all but the first and last elements.so middle([1, 2, 3, 4]) should return[2, 3].


def middle(lst):
    return lst [1 : -1]

print(middle([1, 2, 3, 4]))


# ==========================================================================================================

# Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None.

def chop(lst):
    del lst[0]
    del lst[-1]

numbers = [1, 2, 3, 4]
chop (numbers)
print(numbers)


# ===========================================================================================================


# Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
# the elements of the list can be compared with the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should re-
# turn False.

def is_sorted(lst):
    for i in range (len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


# =====================================

def is_sorted(lst):
    return lst == sorted(lst)

# ====================================================================================

# Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("listen", "silent")) # True
print(is_anagram("hello", "world")) # False
print(is_anagram("Dormitory", "Dirtyroom")) # True

# ====================================================================================================


# Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
# list with only the unique elements from the original. Hint: they don’t have to be in the same order.

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))
