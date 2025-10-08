from decorators import *

@show_calls
def min_ops_to_make_palindrome(phrase):
    clean = (combine(phrase)).lower()
    if clean == clean[::-1]:
        return 0
    else:
        if clean[:-1] == clean[:-1][::-1]:
            return 1
        elif clean[1:] == clean[1:][::-1]:
            return 1
        else:
            return min_ops_to_make_palindrome(clean[1:])

def combine(phrase):
    if not phrase:
        return ""
    else:
        if phrase[0] != " ":
            return phrase[0] + combine(phrase[1:])
        else:
            return combine(phrase[1:])

print(combine('A man a plan a canal Panama'))

print(min_ops_to_make_palindrome('madam'))
print(min_ops_to_make_palindrome('Webew'))
print(min_ops_to_make_palindrome('Web'))
print(min_ops_to_make_palindrome('Race Car'))
print(min_ops_to_make_palindrome('a  adam a'))
print(min_ops_to_make_palindrome('A man a plan a canal Panama'))
print(min_ops_to_make_palindrome('aaaaaaaaab'))