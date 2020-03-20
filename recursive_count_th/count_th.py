'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

'''


def count_th(word):
    # set up a counter to keep track of how many occurances of "th" happen.
    count = 0
    print("before statement",count)
    #have to set up base case
    # if the length of string is 1 or 0, then its impossible to have combination "th". Return 0.
    if len(word) <= 1:
        return 0
    else:
        # if word starts with th (1st and 2nd els)
        if word[0:2] == 'th':
            count += 1
            print("after func",count)
        return count + count_th(word[1:])


