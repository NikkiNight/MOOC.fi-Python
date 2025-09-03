"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named all_the_longest, which takes a list of strings as its argument.
The function should return a new list containing the longest string in the original list.
If more than one are equally long, the function should return all of the longest strings.
"""

# Write your solution here
def all_the_longest(my_list):

    max_len = max(len(word) for word in my_list) # Cycle through all words to find the max length
    longest_list = []

    for word in my_list:
        if len(word) == max_len:
            longest_list.append(word)

    return longest_list

if __name__ == "__main__":

    my_list = ["first", "second", "fouth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

    my_list = ["Alan", "Grace", "Steve", "Kim", "Susan"]
    result = all_the_longest(my_list)
    print(result) # ['Grace', 'Steve', 'Susan']
