'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set up counter
    counter = 0 
    if len(word) <= 1:
        return 0
    if word[0] + word[1] == 'th':
        counter +=1
    
    return counter + count_th(word[1:])
    