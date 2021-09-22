""" CIS 192 Python Programming
    Do not distribute. Collaboration is NOT permitted.
"""

from collections import defaultdict


def all_factors(n):
    """ Return the set of factors of n (including 1 and n).
    You may assume n is a positive integer. Do this in one line for extra credit.

    Example:
    >>> all_factors(24)
    {1, 2, 3, 4, 6, 8, 12, 24}
    >>> all_factors(5)
    {1, 5}
    """
    factors = set()
    for i in range(1, n + 1):
      if n % i == 0:
        factors.add(i)
    return factors



def get_student_avg(gradebook_dict, student):
    """ Given a dictionary where each key-value pair is of the form: (student_name, [scores]),
    return the average score of the given student. If the given student does not exist, return -1

    Example:
    >>> get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "Sally")
    90.0
    >>> get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "John")
    -1
    """
    #first take care of edge case: if the student does not exist
    if student not in gradebook_dict:
      #return -1
      return -1
    #otherwise, if the student is in the dictionary
    #create result score variable
    result_score = 0
    #iterate over the list at this key
    for score in gradebook_dict[student]:
      #add each value to the result score variable
      result_score += score
    #divide the result score variable by the number of items in the list at that key
    result_score /= len(gradebook_dict[student])
    #return result score variable
    return result_score


def every_other(seq):
    """ Returns a new sequence containing every other element of the input sequence, starting with
    the first. If the input sequence is empty, a new empty sequence of the same type should be
    returned.

    Example: every_other("abcde")
    "ace"
    """
    #edge case: if the input sequence is empty
    if len(seq) == 0:
      #return new empty sequence of the same type
      return seq[0:0]
    #otherwise create new sequence containing every other element of the input sequence
    new_every_other_string = seq[::2]
    # return this new sequence
    return new_every_other_string


def all_but_last(seq):
    """ Returns a new sequence containing all but the last element of the input sequence.
    If the input sequence is empty, a new empty sequence of the same type should be returned.

    Example:
    >>> all_but_last("abcde")
    "abcd"
    """
    #edge case: if the input sequence is empty
    if len(seq) == 0:
      #return new empty sequence of the same type
      return seq[0:0]
    #otherwise create a new sequence containing all but the last element of the input sequence
    new_sequence_containing_all_but_last = seq[:len(seq) - 1]
    #return this new sequence
    return new_sequence_containing_all_but_last


def substrings(seq):
    """ Returns a set of all the substrings of s.
    Recall we can compute a substring using s[i:j] where 0 <= i, j < len(s).

    Example:
    >>> substrings("abc")
    {"", "a", "ab", "abc", "b", "bc", "c"}
    """
    #create a set called all_substrings
    all_substrings = set()
    #add the empty string to this set
    all_substrings.add("")
    #create var for seq length
    length = len(seq)
    #iterate over the string starting at the first element
    for i in range(length):
      #iterate over the string starting at the index one greater than the previous loop
      for j in range(i, length):
        #create temp substring from [i:j]
        substring = seq[i:j + 1]
        #if the substring is not in the set
        if substring not in all_substrings:
          #add the substring to the set
          all_substrings.add(substring)
    #return the all_substrings
    return all_substrings


def many_any(lst, k):
    """ Returns True if at least k elements of lst are True;
    otherwise False. Do this in one line for extra credit.
    Hint: use a list comprehension.

    Example:
    >>> many_any([True, True, False, True], 3)
    True
    >>> many_any([True, True, False, False], 3)
    False
    """
    #create result var for number of trues
    number_of_trues = 0
    #calculate the number of trues in the list: iterate over the list
    for currEl in lst:
      # breakpoint()
      #if the current element is a true
      if currEl == True:
        #increase number of trues by one
        number_of_trues += 1
    #if the number of trues is equal to k
    if number_of_trues >= k:
      #return True
      return True
    #return False
    return False



def alphabet_construct(seq, alphabet):
    """ Returns True if string s can be constructed from the set of length-1 strings
    alphabet and False otherwise.

    Example:
    >>> alphabet_construct("hello", {"a", "b", "h", "e", "l", "o"})
    True
    >>> alphabet_construct("hello", {"a", "b", "h", "e", "o"})
    False
    """
    #basically are the letters that make up the word in the set - first iterate over the string
    for char in seq:
      #if the current char is not in the set
      if char not in alphabet:
        #return False
        return False
    #return true
    return True


def common_chars(seq, k):
    """ Returns the set of characters that appear more than k times in
    the input string, along with their number of occurrences.

    Example:
    >>> common_chars("cat in a hat", 2)
    {("a", 3), (" ", 3)}
    """
    #instantiate a default dictionary
    tempDictionary = defaultdict(int)
    #iterate over the string
    for char in seq:
      #add nums to the occurrences of each letter as they are encountered
      tempDictionary[char] += 1
    #create final set var
    final_set = set()
    #iterate over the dictionary
    for key in tempDictionary:
      #if the current item has an occurrence val greater than k
      if tempDictionary[key] > k:
        #add it to the final set
        final_set.add((key, tempDictionary[key]))
    #return the final dictionary
    return final_set





def dict_to_tuple_list(my_dict):
    """ Given a dictionary where each k-v pair is of the form (x, [y]), convert the dictionary
    into a list of tuples.

    Example:
    >>> dict_to_tuple_list({'x': [1, 2, 3], 'y':[4, 5, 6]})
    [(x, 1), (x, 2), (x, 3), (y, 4), (y, 5), (y, 6)]
    """
    #create a list
    dict_to_list = list()
    #iterate over the dictionary keys
    for key in my_dict:
      #iterate over the list of nums in the val position
      for current_num in my_dict[key]:
        #instantiate a new tuple that is (key, current num)
        new_pair = (key, current_num)
        #add this new tuple to the list
        dict_to_list.append(new_pair)
    #return the list
    return dict_to_list


"You're done! Wahoo!"


# print(all_factors(24)) #{1, 2, 3, 4, 6, 8, 12, 24}
# print(all_factors(5))

# print(get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "Sally")) #90.0
# print(get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "John")) #-1

# print(every_other("abcde")) #"ace"

# print(all_but_last("abcde")) #"abcd"

# print(substrings("abc")) #{"", "a", "ab", "abc", "b", "bc", "c"}

# print(many_any([True, True, False, True], 3)) #True
# print(many_any([True, True, False, False], 3)) #False

# print(alphabet_construct("hello", {"a", "b", "h", "e", "l", "o"})) #True
# print(alphabet_construct("hello", {"a", "b", "h", "e", "o"})) #False

# print(common_chars("cat in a hat", 2)) #{("a", 3), (" ", 3)}

# print(dict_to_tuple_list({'x': [1, 2, 3], 'y':[4, 5, 6]})) #[(x, 1), (x, 2), (x, 3), (y, 4), (y, 5), (y, 6)]