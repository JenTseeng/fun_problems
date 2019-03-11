
def is_balanced_recursive(to_check, in_recursion=False):
    """Recursive solution for checking for balanced opening/closing chars"""

    lookup_dict = {')':'(', '}':'{', ']':'[', '>':'<'}
    open_chars = set(['(', '{', '[', '<'])
    
    
    # remove all chars that are not open/closing chars on first run
    if not in_recursion:
        char_list = []
        for char in to_check:
            if char in lookup_dict or char in open_chars:
                char_list.append(char)
        to_check = char_list
        

        # return false if 1 or no open/closing chars found
        if len(to_check)<2:
            return False


    while to_check:

        # open char with enough chars to close
        if to_check[0] in open_chars and len(to_check)>=2:
            x = is_balanced_recursive(to_check[1:],True)

            # return false for mismatched chars
            if lookup_dict[x[0]] != to_check[0]:
                return False

            # continue loop for matching open/close chars
            else:
                to_check = x[1:]
                
        # closed char only valid in recursion
        elif to_check[0] in lookup_dict and in_recursion:
            return to_check

        else:
            return False

    # all open chars have been closed
    return True


assert is_balanced_recursive('}') == False
assert is_balanced_recursive('[') == False
assert is_balanced_recursive('sklfdjdsj{(<>)}}') == False
assert is_balanced_recursive('({[]})') == True
assert is_balanced_recursive('askjfsdljf') == False